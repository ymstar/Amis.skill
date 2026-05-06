#!/usr/bin/env python3
"""
Amis Schema 验证脚本
检查 JSON Schema 格式合法性、必要字段、常见错误
退出码：0=通过，1=有错误
"""

import json
import sys
import re
from typing import List, Dict, Any, Tuple

# 必需包含 type 字段的组件
REQUIRED_TYPE_COMPONENTS = [
    'page', 'crud', 'form', 'table', 'card', 'cards', 'list',
    'flex', 'grid', 'hbox', 'vbox', 'wrapper', 'panel', 'tabs', 'collapse'
]

# 容器类组件（可以包含 body/items/columns 等子元素）
CONTAINER_COMPONENTS = [
    'page', 'crud', 'form', 'dialog', 'drawer', 'panel', 'tabs',
    'flex', 'grid', 'hbox', 'vbox', 'wrapper', 'container',
    'service', 'card', 'cards', 'list', 'wizard', 'steps'
]

# 子元素字段名
CHILDREN_FIELDS = ['body', 'items', 'columns', 'tabs', 'steps', 'controls', 'buttons', 'headerToolbar', 'footerToolbar']


class SchemaValidator:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.schema: Dict[str, Any] = {}
    
    def validate(self, schema: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """验证 Schema，返回 (是否通过, 错误列表, 警告列表)"""
        self.schema = schema
        self.errors = []
        self.warnings = []
        
        # 1. 检查是否为有效字典
        if not isinstance(schema, dict):
            self.errors.append("Schema 必须是 JSON 对象")
            return False, self.errors, self.warnings
        
        # 2. 检查必需字段
        self._check_required_fields(schema)
        
        # 3. 检查 type 字段
        self._check_type_field(schema)
        
        # 4. 检查 API 格式
        self._check_api_format(schema)
        
        # 5. 检查组件嵌套
        self._check_component_nesting(schema)
        
        # 6. 检查表达式语法
        self._check_expressions(schema)
        
        # 7. 检查常见错误
        self._check_common_errors(schema)
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _check_required_fields(self, obj: Dict[str, Any], path: str = ""):
        """检查必需字段"""
        if 'type' in obj:
            comp_type = obj.get('type', '')
            
            # Page 组件应该有 body
            if comp_type == 'page' and 'body' not in obj and 'aside' not in obj:
                self.warnings.append(f"{path}: Page 组件建议包含 body 或 aside 内容")
            
            # CRUD 组件应该有 columns
            if comp_type == 'crud' and 'columns' not in obj:
                self.warnings.append(f"{path}: CRUD 组件建议包含 columns 列配置")
            
            # Form 组件应该有 body 或 controls
            if comp_type == 'form' and 'body' not in obj and 'controls' not in obj:
                self.warnings.append(f"{path}: Form 组件建议包含 body 或 controls")
    
    def _check_type_field(self, obj: Dict[str, Any], path: str = ""):
        """检查 type 字段"""
        if 'type' not in obj:
            # 如果没有 type，检查是否有 body 等内容
            has_children = any(field in obj for field in CHILDREN_FIELDS)
            if has_children and not path:  # 根级别没有 type
                self.errors.append(f"{path}: 缺少 type 字段")
        else:
            comp_type = obj.get('type', '')
            # 检查 type 是否为有效字符串
            if not isinstance(comp_type, str):
                self.errors.append(f"{path}: type 必须是字符串")
            elif not comp_type:
                self.errors.append(f"{path}: type 不能为空")
    
    def _check_api_format(self, obj: Dict[str, Any], path: str = ""):
        """检查 API 配置格式"""
        for key in ['api', 'initApi', 'schemaApi', 'source', 'receiver']:
            if key in obj:
                api = obj[key]
                
                if isinstance(api, dict):
                    # 检查 method
                    if 'method' in api:
                        method = api['method'].lower()
                        if method not in ['get', 'post', 'put', 'delete', 'patch', 'ajax']:
                            self.errors.append(f"{path}.{key}: method '{method}' 不是有效的 HTTP 方法")
                    
                    # 检查 url
                    if 'url' in api and not isinstance(api['url'], str):
                        self.errors.append(f"{path}.{key}.url: url 必须是字符串")
                
                elif isinstance(api, str):
                    # 检查是否以 http:// 或 https:// 或 / 开头
                    if api and not (api.startswith('/') or api.startswith('http')):
                        # 检查是否是简写格式，如 "get:/api/xxx"
                        if not re.match(r'^(get|post|put|delete|patch):', api):
                            self.warnings.append(f"{path}.{key}: API URL 建议以 / 开头")
    
    def _check_component_nesting(self, obj: Dict[str, Any], path: str = ""):
        """检查组件嵌套"""
        if not isinstance(obj, dict):
            return
        
        comp_type = obj.get('type', '')
        
        # 遍历所有子元素字段
        for field in CHILDREN_FIELDS:
            if field in obj:
                children = obj[field]
                current_path = f"{path}.{field}" if path else field
                
                if isinstance(children, dict):
                    self._check_component_nesting(children, current_path)
                elif isinstance(children, list):
                    for i, child in enumerate(children):
                        child_path = f"{current_path}[{i}]"
                        if isinstance(child, dict):
                            # 检查必需 type
                            if 'type' not in child:
                                # 某些场景下可以没有 type
                                has_content = any(f in child for f in CHILDREN_FIELDS)
                                if not has_content:
                                    self.warnings.append(f"{child_path}: 子元素缺少 type 字段")
                            self._check_component_nesting(child, child_path)
                        elif isinstance(child, str):
                            # 字符串是允许的，会被当作 tpl 处理
                            pass
                        elif child is not None:
                            self.warnings.append(f"{child_path}: 子元素应该是对象或字符串")
    
    def _check_expressions(self, obj: Dict[str, Any], path: str = ""):
        """检查表达式语法"""
        # 需要检查表达式的字段
        expression_fields = ['visibleOn', 'hiddenOn', 'disabledOn', 'staticOn', 
                            'source', 'data', 'tpl', 'body']
        
        for key, value in obj.items():
            if key in expression_fields and isinstance(value, str):
                current_path = f"{path}.{key}" if path else key
                
                # 检查 ${} 语法
                matches = re.findall(r'\$\{([^}]+)\}', value)
                for expr in matches:
                    # 检查是否有明显的语法错误
                    if expr.count('(') != expr.count(')'):
                        self.errors.append(f"{current_path}: 表达式 '{expr}' 括号不匹配")
                    
                    # 检查是否有未闭合的引号
                    single_quotes = expr.count("'")
                    double_quotes = expr.count('"')
                    if single_quotes % 2 != 0:
                        self.errors.append(f"{current_path}: 表达式 '{expr}' 单引号不匹配")
                    if double_quotes % 2 != 0:
                        self.errors.append(f"{current_path}: 表达式 '{expr}' 双引号不匹配")
    
    def _check_common_errors(self, obj: Dict[str, Any], path: str = ""):
        """检查常见错误"""
        if not isinstance(obj, dict):
            return
        
        # 1. 检查空字符串 type
        if obj.get('type') == '':
            self.errors.append(f"{path}: type 不能为空字符串")
        
        # 2. 检查重复的 name
        if 'name' in obj:
            name = obj['name']
            if not isinstance(name, str):
                self.errors.append(f"{path}.name: name 必须是字符串")
        
        # 3. 检查 JSON 语法
        # （实际上这里的 JSON 已经被解析过了，所以主要检查对象结构）
        
        # 4. 检查 options 格式
        if 'options' in obj:
            options = obj['options']
            if isinstance(options, list):
                for i, opt in enumerate(options):
                    if isinstance(opt, dict):
                        if 'label' not in opt and 'value' not in opt:
                            self.warnings.append(f"{path}.options[{i}]: 选项对象建议包含 label 和 value")
        
        # 5. 检查 columns 格式
        if 'columns' in obj and isinstance(obj['columns'], list):
            for i, col in enumerate(obj['columns']):
                if isinstance(col, dict):
                    col_path = f"{path}.columns[{i}]"
                    if 'label' not in col and 'name' not in col:
                        self.warnings.append(f"{col_path}: 列配置建议包含 label 或 name")
        
        # 递归检查子元素
        for field in CHILDREN_FIELDS:
            if field in obj:
                children = obj[field]
                current_path = f"{path}.{field}" if path else field
                
                if isinstance(children, list):
                    for i, child in enumerate(children):
                        if isinstance(child, dict):
                            self._check_common_errors(child, f"{current_path}[{i}]")
                elif isinstance(children, dict):
                    self._check_common_errors(children, current_path)


def print_result(is_valid: bool, errors: List[str], warnings: List[str], verbose: bool = True):
    """打印验证结果"""
    if verbose:
        print("=" * 60)
        print("Amis Schema 验证结果")
        print("=" * 60)
        
        if is_valid:
            print("✅ 验证通过")
        else:
            print("❌ 验证失败")
        
        if errors:
            print(f"\n错误 ({len(errors)}):")
            for i, error in enumerate(errors, 1):
                print(f"  {i}. {error}")
        
        if warnings:
            print(f"\n警告 ({len(warnings)}):")
            for i, warning in enumerate(warnings, 1):
                print(f"  {i}. {warning}")
        
        if is_valid and not warnings:
            print("\n🎉 Schema 格式正确，可以正常使用！")
    
    return is_valid


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python amis-validator.py <schema.json> [--quiet]")
        print("\n示例:")
        print("  python amis-validator.py schema.json")
        print("  cat schema.json | python amis-validator.py -")
        sys.exit(1)
    
    # 读取 Schema 文件
    file_path = sys.argv[1]
    verbose = '--quiet' not in sys.argv
    
    try:
        if file_path == '-':
            # 从标准输入读取
            content = sys.stdin.read()
            schema = json.loads(content)
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
    except FileNotFoundError:
        if verbose:
            print(f"❌ 错误: 文件 '{file_path}' 不存在")
        sys.exit(1)
    except json.JSONDecodeError as e:
        if verbose:
            print(f"❌ 错误: JSON 解析失败 - {e}")
        sys.exit(1)
    except Exception as e:
        if verbose:
            print(f"❌ 错误: {e}")
        sys.exit(1)
    
    # 验证 Schema
    validator = SchemaValidator()
    is_valid, errors, warnings = validator.validate(schema)
    
    # 打印结果
    print_result(is_valid, errors, warnings, verbose)
    
    # 返回退出码
    return 0 if is_valid else 1


if __name__ == '__main__':
    sys.exit(main())
