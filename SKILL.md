---
name: amis-low-code
description: 使用 Amis 低代码框架快速生成管理后台页面、数据仪表盘和复杂表单。支持 CRUD 表格、图表、表单验证和自定义组件。
---

# Amis 低代码页面生成

使用百度开源的 Amis 低代码框架，快速构建专业级管理后台页面。

## 何时使用

- 需要快速搭建 CRUD 管理后台
- 需要数据可视化仪表盘
- 需要复杂表单（级联选择、动态字段、验证规则）
- 不想从零写 React/Vue 前端代码
- 需要快速验证产品原型

## 核心能力

### 1. CRUD 管理页面
自动生成完整的增删改查表格，包含：
- 搜索过滤器（关键字、分类、状态）
- 数据表格（排序、分页、批量操作）
- 新增/编辑弹窗表单
- 行内编辑、详情查看
- 自定义操作按钮

**快速开始**：
```html
<!-- 复制 demos/crud-demo.html 到项目 -->
<!-- 双击即可在浏览器运行 -->
```

### 2. 数据仪表盘
生成包含统计卡片和图表的监控面板：
- 统计数字卡片（带趋势标记）
- 折线图/柱状图/饼图
- 数据表格和最近操作记录
- 响应式布局适配

**快速开始**：
```html
<!-- 复制 demos/dashboard-demo.html 到项目 -->
```

### 3. 复杂表单
企业级表单能力：
- 表单验证（必填、格式、自定义规则）
- 级联选择器（省市区三级联动）
- 动态表单字段
- 文件上传（支持裁剪、预览）
- 富文本编辑器

**快速开始**：
```html
<!-- 复制 demos/form-demo.html 到项目 -->
```

## 使用流程

### 步骤 1：选择模板
从三个预设模板中选择：
- `crud-demo.html` - 管理后台表格
- `dashboard-demo.html` - 数据仪表盘
- `form-demo.html` - 复杂表单

### 步骤 2：修改数据
编辑 HTML 文件中的 Mock 数据：
```javascript
// 替换为你的真实数据
const mockData = [
  { id: 1, name: '项目A', status: 'active' },
  // ...
];
```

### 步骤 3：配置 Schema
调整 Amis Schema 配置：
```javascript
const schema = {
  type: 'page',
  title: '你的页面标题',
  body: [
    // 配置组件
  ]
};
```

### 步骤 4：运行
直接用浏览器打开 HTML 文件即可运行，无需构建工具。

## 常用组件配置

### 表格列配置
```javascript
columns: [
  { name: 'id', label: 'ID', sortable: true },
  { name: 'avatar', label: '头像', type: 'image' },
  { name: 'name', label: '名称', searchable: true },
  {
    type: 'operation',
    label: '操作',
    buttons: [
      { label: '编辑', actionType: 'dialog' },
      { label: '删除', actionType: 'ajax' }
    ]
  }
]
```

### 表单字段配置
```javascript
body: [
  { type: 'input-text', name: 'username', label: '用户名', required: true },
  { type: 'input-email', name: 'email', label: '邮箱' },
  { type: 'select', name: 'role', label: '角色', options: [...] },
  { type: 'switch', name: 'status', label: '启用状态' }
]
```

### 图表配置
```javascript
{
  type: 'chart',
  config: {
    xAxis: { data: categories },
    series: [{
      type: 'line',
      data: values,
      smooth: true,
      areaStyle: { color: 'rgba(24,144,255,0.3)' }
    }]
  }
}
```

## 目录结构

```
amis-low-code/
├── SKILL.md                    # 本技能说明
├── demos/
│   ├── crud-demo.html         # CRUD 管理后台模板
│   ├── dashboard-demo.html    # 数据仪表盘模板
│   └── form-demo.html         # 复杂表单模板
└── references/
    ├── amis-quickstart.md     # Amis 快速入门
    ├── component-guide.md     # 组件使用指南
    ├── schema-reference.md    # Schema 完整参考
    └── api-integration.md     # 后端 API 对接指南
```

## 技术栈

- **Amis** - 百度开源低代码框架
- **ECharts** - 数据可视化图表库
- **纯 HTML/JS** - 无构建依赖，双击即运行
- **CDN 引入** - 所有资源来自 jsdelivr

## 最佳实践

1. **从模板开始**：不要从零写，复制 demo 后修改
2. **渐进式改造**：先跑通静态数据，再对接真实 API
3. **善用官方文档**：https://aisuda.bce.baidu.com/amis/zh-CN/components/index
4. **Theme 定制**：修改 CSS 变量即可定制品牌色
5. **组件复用**：把常用表单字段提取为模板

## 进阶场景

查看 `references/` 目录下的文档：
- **字段联动** - 表单字段间的依赖和动态显示
- **主题定制** - 修改全局配色和样式
- **API 对接** - 对接真实后端接口
- **自定义组件** - 扩展 Amis 组件库

## 常见问题

**Q: 为什么 demo 打不开？**
A: 检查网络连接，Amis SDK 从 CDN 加载，需要联网。

**Q: 如何对接后端 API？**
A: 替换 adaptor 函数中的 mock 逻辑，改为真实 fetch 请求。参考 `references/api-integration.md`。

**Q: 可以在 Vue/React 项目中使用吗？**
A: 可以，Amis 提供了 React/Vue 封装组件，参考官方文档。

**Q: 表单验证失败怎么办？**
A: 检查 rules 配置，确保字段 name 与 schema 一致。
