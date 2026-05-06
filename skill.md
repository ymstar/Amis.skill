# Amis低代码页面生成 Skill

## 版本信息

**当前版本：v1.1**（2025年5月更新）

### v1.1 更新内容
- 🆕 **新增3个可直接运行的HTML Demo**，双击即可预览
- 🆕 **补全三大组件完整文档**：Table、Form、Chart 指南
- 🆕 **新增联动指南**：字段显隐、值联动、条件渲染
- 🆕 **新增主题定制指南**：主题切换、暗黑模式、响应式

## 概述

Amis（Another Modular Interface Solution）是百度开源的前端低代码框架，通过 JSON 配置即可生成各种复杂的后台管理页面。当前最新稳定版本：**6.13.0**（2025年1月发布）。

**核心特点**：
- JSON 配置驱动，无需编写前端代码
- 100+ 内置组件，覆盖常用业务场景
- 支持数据绑定、联动、验证
- 内置 ECharts 图表集成
- 支持主题定制和国际化

**官方文档**：https://aisuda.bce.baidu.com/amis/zh-CN/docs/index
**在线编辑器**：https://aisuda.bce.baidu.com/amis-editor/

---

## 🎯 Demo 快速入口

> **推荐从 Demo 开始学习**，每个 Demo 都是完整可运行的页面，双击 HTML 文件即可在浏览器中预览。

| Demo | 文件路径 | 功能说明 |
|------|----------|----------|
| **CRUD 管理页** | `demos/crud-demo.html` | 用户列表 + 增删改查、搜索、分页、批量操作 |
| **数据仪表盘** | `demos/dashboard-demo.html` | 统计卡片、ECharts图表（折线/柱状/饼图）、数据表格 |
| **复杂表单** | `demos/form-demo.html` | 表单验证、级联选择、文件上传、Combo组合输入 |

### 使用方式
1. 找到 `demos/` 目录下的 HTML 文件
2. 双击文件在浏览器中打开
3. 查看源码中的 `schema` 配置作为学习参考

---

## 快速开始

### 基础页面结构

```json
{
  "type": "page",
  "title": "页面标题",
  "subTitle": "副标题",
  "body": {
    "type": "tpl",
    "tpl": "页面内容"
  }
}
```

### 快速渲染示例

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Amis Demo</title>
  <link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">
</head>
<body>
  <div id="root"></div>
  <script src="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/sdk.js"></script>
  <script>
    const amis = amisRequire('amis/embed');
    const schema = {
      "type": "page",
      "title": "Hello Amis",
      "body": "欢迎使用 Amis 低代码框架"
    };
    amis.embed('#root', schema);
  </script>
</body>
</html>
```

---

## 页面基础结构模板

### 完整 Page 组件结构

```json
{
  "type": "page",
  "title": "页面标题",
  "subTitle": "副标题",
  "remark": "页面提示信息",
  "className": "特殊样式类名",
  "initApi": "/api/page/init",
  "initFetchOn": "表达式条件",
  "body": [
    "内容区域，可以是字符串或组件数组"
  ],
  "aside": [
    "侧边栏内容"
  ],
  "toolbar": [
    "工具栏内容"
  ],
  "regions": ["body", "aside", "toolbar"]
}
```

### 数据初始化

```json
{
  "type": "page",
  "data": {
    "userName": "张三",
    "userId": 1,
    "isVip": true
  },
  "body": {
    "type": "tpl",
    "tpl": "欢迎 ${userName}，您的ID是 ${userId}"
  }
}
```

---

## 组件分类速查

| 分类 | 组件类型 | 用途 |
|------|----------|------|
| 页面 | page | 页面根容器 |
| 布局 | flex, grid, hbox, vbox, wrapper, panel, tabs, collapse | 页面结构布局 |
| 容器 | container, card, cards, list | 内容容器 |
| 表单 | form, input-text, input-number, select, radio, checkbox, switch, date, input-file | 数据收集 |
| 表格 | table, crud | 数据展示与操作 |
| 展示 | mapping, tpl, json, markdown, chart | 数据渲染 |
| 反馈 | dialog, drawer, toast, alert | 用户交互 |
| 数据 | service, dataSource | 数据加载 |

---

## 常用页面模板

### CRUD 管理页

```json
{
  "type": "page",
  "title": "用户管理",
  "body": {
    "type": "crud",
    "api": "/api/users",
    "filter": {
      "title": "搜索条件",
      "body": [
        {
          "type": "input-text",
          "name": "keywords",
          "label": "关键字",
          "placeholder": "输入用户名或邮箱"
        },
        {
          "type": "select",
          "name": "status",
          "label": "状态",
          "options": [
            {"label": "全部", "value": ""},
            {"label": "启用", "value": "active"},
            {"label": "禁用", "value": "inactive"}
          ]
        }
      ],
      "actions": [
        {"type": "reset", "label": "重置"},
        {"type": "submit", "label": "搜索", "level": "primary"}
      ]
    },
    "columns": [
      {
        "name": "id",
        "label": "ID",
        "width": 80
      },
      {
        "name": "name",
        "label": "用户名"
      },
      {
        "name": "email",
        "label": "邮箱"
      },
      {
        "name": "status",
        "label": "状态",
        "type": "mapping",
        "map": {
          "active": "<span class='label label-success'>启用</span>",
          "inactive": "<span class='label label-default'>禁用</span>"
        }
      },
      {
        "name": "createdAt",
        "label": "创建时间",
        "type": "date",
        "format": "YYYY-MM-DD"
      },
      {
        "type": "operation",
        "label": "操作",
        "buttons": [
          {
            "type": "button",
            "label": "编辑",
            "actionType": "drawer",
            "drawer": {
              "title": "编辑用户",
              "body": {
                "type": "form",
                "api": "put:/api/users/${id}",
                "body": [
                  {"type": "input-text", "name": "name", "label": "用户名", "required": true},
                  {"type": "input-email", "name": "email", "label": "邮箱", "required": true}
                ]
              }
            }
          },
          {
            "type": "button",
            "label": "删除",
            "actionType": "ajax",
            "api": "delete:/api/users/${id}",
            "confirmText": "确定删除该用户？"
          }
        ]
      }
    ],
    "bulkActions": [
      {
        "type": "button",
        "label": "批量删除",
        "actionType": "ajax",
        "api": "post:/api/users/batch-delete",
        "confirmText": "确定删除选中的 ${count} 条记录？"
      }
    ],
    "headerToolbar": ["bulkActions", "filter-toggler", "columns-toggler"],
    "footerToolbar": ["statistics", "pagination"]
  }
}
```

### 表单提交页

```json
{
  "type": "page",
  "title": "新增用户",
  "body": {
    "type": "form",
    "api": "post:/api/users",
    "redirect": "/users",
    "body": [
      {
        "type": "input-text",
        "name": "username",
        "label": "用户名",
        "required": true,
        "validations": {
          "minLength": 3,
          "maxLength": 20
        }
      },
      {
        "type": "input-email",
        "name": "email",
        "label": "邮箱",
        "required": true
      },
      {
        "type": "input-password",
        "name": "password",
        "label": "密码",
        "required": true,
        "validations": {
          "minLength": 6
        }
      },
      {
        "type": "select",
        "name": "department",
        "label": "部门",
        "options": [
          {"label": "技术部", "value": "tech"},
          {"label": "市场部", "value": "marketing"},
          {"label": "运营部", "value": "operation"}
        ]
      },
      {
        "type": "radios",
        "name": "gender",
        "label": "性别",
        "options": [
          {"label": "男", "value": "male"},
          {"label": "女", "value": "female"}
        ]
      },
      {
        "type": "checkboxes",
        "name": "hobbies",
        "label": "爱好",
        "options": [
          {"label": "阅读", "value": "reading"},
          {"label": "运动", "value": "sports"},
          {"label": "音乐", "value": "music"}
        ]
      },
      {
        "type": "switch",
        "name": "isActive",
        "label": "启用账号"
      },
      {
        "type": "input-file",
        "name": "avatar",
        "label": "头像",
        "accept": ".jpg,.png",
        "maxSize": 2097152
      },
      {
        "type": "textarea",
        "name": "remark",
        "label": "备注",
        "rows": 3
      }
    ],
    "buttons": [
      {"type": "reset", "label": "重置"},
      {"type": "submit", "label": "提交", "level": "primary"}
    ]
  }
}
```

### 数据看板页

```json
{
  "type": "page",
  "title": "数据看板",
  "body": [
    {
      "type": "flex",
      "justify": "space-around",
      "items": [
        {
          "type": "card",
          "header": {"title": "总用户数"},
          "body": "${totalUsers}"
        },
        {
          "type": "card",
          "header": {"title": "活跃用户"},
          "body": "${activeUsers}"
        },
        {
          "type": "card",
          "header": {"title": "总订单数"},
          "body": "${totalOrders}"
        },
        {
          "type": "card",
          "header": {"title": "总销售额"},
          "body": "¥${totalSales|number}"
        }
      ]
    },
    {
      "type": "grid",
      "columns": [
        {
          "md": 8,
          "body": {
            "type": "chart",
            "config": {
              "title": {"text": "月度销售额趋势"},
              "xAxis": {"type": "category", "data": ["1月", "2月", "3月", "4月"]},
              "yAxis": {"type": "value"},
              "series": [{"data": [120, 200, 150, 180]}]
            }
          }
        },
        {
          "md": 4,
          "body": {
            "type": "crud",
            "api": "/api/recent-orders",
            "columns": [
              {"name": "orderNo", "label": "订单号"},
              {"name": "amount", "label": "金额"}
            ]
          }
        }
      ]
    }
  ]
}
```

### 详情展示页

```json
{
  "type": "page",
  "title": "用户详情",
  "toolbar": [
    {
      "type": "button",
      "label": "返回列表",
      "actionType": "link",
      "link": "/users"
    },
    {
      "type": "button",
      "label": "编辑",
      "actionType": "drawer",
      "drawer": {
        "title": "编辑用户",
        "body": {
          "type": "form",
          "api": "put:/api/users/${id}",
          "body": [
            {"type": "input-text", "name": "name", "label": "用户名"},
            {"type": "input-email", "name": "email", "label": "邮箱"}
          ]
        }
      }
    }
  ],
  "body": {
    "type": "detail",
    "api": "/api/users/${id}",
    "mode": "horizontal",
    "columns": [
      {
        "name": "name",
        "label": "用户名"
      },
      {
        "name": "email",
        "label": "邮箱"
      },
      {
        "name": "department",
        "label": "部门"
      },
      {
        "name": "createdAt",
        "label": "创建时间",
        "type": "date",
        "format": "YYYY-MM-DD HH:mm"
      }
    ]
  }
}
```

### 登录注册页

```json
{
  "type": "page",
  "body": {
    "type": "flex",
    "justify": "center",
    "alignItems": "middle",
    "style": {"minHeight": "100vh"},
    "items": [
      {
        "type": "card",
        "className": "w-lg",
        "body": {
          "type": "tabs",
          "tabs": [
            {
              "title": "登录",
              "body": {
                "type": "form",
                "api": "post:/api/login",
                "redirect": "/dashboard",
                "body": [
                  {"type": "input-text", "name": "username", "label": "用户名", "required": true},
                  {"type": "input-password", "name": "password", "label": "密码", "required": true}
                ],
                "buttons": [
                  {"type": "submit", "label": "登录", "level": "primary"}
                ]
              }
            },
            {
              "title": "注册",
              "body": {
                "type": "form",
                "api": "post:/api/register",
                "redirect": "/login",
                "body": [
                  {"type": "input-text", "name": "username", "label": "用户名", "required": true},
                  {"type": "input-email", "name": "email", "label": "邮箱", "required": true},
                  {"type": "input-password", "name": "password", "label": "密码", "required": true}
                ],
                "buttons": [
                  {"type": "submit", "label": "注册", "level": "primary"}
                ]
              }
            }
          ]
        }
      }
    ]
  }
}
```

### 向导页（分步表单）

```json
{
  "type": "page",
  "title": "新建项目",
  "body": {
    "type": "wizard",
    "api": "post:/api/projects",
    "steps": [
      {
        "title": "基本信息",
        "body": {
          "type": "form",
          "body": [
            {"type": "input-text", "name": "name", "label": "项目名称", "required": true},
            {"type": "textarea", "name": "description", "label": "项目描述"}
          ]
        }
      },
      {
        "title": "配置设置",
        "body": {
          "type": "form",
          "body": [
            {"type": "select", "name": "type", "label": "项目类型", "options": [
              {"label": "Web应用", "value": "web"},
              {"label": "移动应用", "value": "mobile"}
            ]},
            {"type": "switch", "name": "isPublic", "label": "公开项目"}
          ]
        }
      },
      {
        "title": "完成",
        "body": {
          "type": "tpl",
          "tpl": "项目创建完成！"
        }
      }
    ]
  }
}
```

---

## 预览方案

### 在线编辑器预览

1. 访问 https://aisuda.bce.baidu.com/amis-editor/
2. 点击「新建页面」或「导入 JSON」
3. 粘贴 Schema 配置
4. 实时预览效果

### 本地预览

```html
<!DOCTYPE html>
<html>
<head>
  <link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">
</head>
<body>
  <div id="root"></div>
  <script src="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/sdk.js"></script>
  <script>
    const schema = { /* 你的 Schema 配置 */ };
    amisRequire('amis/embed').embed('#root', schema);
  </script>
</body>
</html>
```

### 使用 Node.js 预览

```bash
npm install amis@6.13.0
```

```javascript
const { getSchema, render } = require('amis');

const schema = { /* 你的 Schema */ };
const html = render(schema);
console.log(html);
```

---

## API 配置指南

### 简单字符串配置

```json
{
  "api": "/api/users"
}
```

### 完整对象配置

```json
{
  "api": {
    "method": "get",
    "url": "/api/users",
    "data": {
      "page": "${page}",
      "pageSize": "${pageSize}"
    },
    "headers": {
      "Authorization": "Bearer ${token}"
    },
    "adaptor": "function(payload) { return payload; }"
  }
}
```

### 标准响应格式

```json
{
  "status": 0,
  "msg": "success",
  "data": {
    "items": [],
    "total": 100
  }
}
```

---

## 数据绑定表达式

- `${fieldName}` - 获取字段值
- `${object.nested.field}` - 获取嵌套字段
- `${array.0}` - 获取数组元素
- `${field | filter}` - 使用过滤器
- `&` - 整个数据域

### 内置过滤器

- `| raw` - 不转义 HTML
- `| json` - JSON 序列化
- `| date` - 格式化日期
- `| number` - 格式化数字
- `| truncate` - 截断字符串

---

## 组件组合最佳实践

### 布局组合

```json
{
  "type": "page",
  "body": {
    "type": "grid",
    "columns": [
      {
        "md": 8,
        "body": { "type": "crud", "api": "/api/list" }
      },
      {
        "md": 4,
        "body": { "type": "panel", "title": "快捷操作", "body": "..." }
      }
    ]
  }
}
```

### 表单组合

```json
{
  "type": "form",
  "body": [
    {
      "type": "fieldSet",
      "title": "基本信息",
      "body": [
        {"type": "input-text", "name": "name", "label": "姓名"},
        {"type": "input-email", "name": "email", "label": "邮箱"}
      ]
    },
    {
      "type": "fieldSet",
      "title": "详细信息",
      "body": [
        {"type": "input-text", "name": "company", "label": "公司"},
        {"type": "input-text", "name": "position", "label": "职位"}
      ]
    }
  ]
}
```

---

## 事件与动作

### 常用 actionType

| actionType | 说明 |
|------------|------|
| `ajax` | 发送 AJAX 请求 |
| `dialog` | 打开弹窗 |
| `drawer` | 打开抽屉 |
| `link` | 页面跳转 |
| `reload` | 刷新组件 |
| `reset` | 重置表单 |
| `submit` | 提交表单 |
| `copy` | 复制到剪贴板 |

### 按钮配置

```json
{
  "type": "button",
  "label": "保存",
  "level": "primary",
  "actionType": "ajax",
  "api": "post:/api/save",
  "confirmText": "确定要保存吗？",
  "onSuccess": {
    "actionType": "toast",
    "msg": "保存成功！"
  }
}
```

---

## 常见问题

### Q: 如何处理跨域请求？
A: 配置代理或在服务端设置 CORS 头。

### Q: 如何实现条件显示？
A: 使用 `visibleOn` 或 `hiddenOn` 属性：
```json
{
  "type": "input-text",
  "name": "vipField",
  "visibleOn": "this.isVip === true"
}
```

### Q: 如何动态加载选项？
A: 使用 `source` 属性：
```json
{
  "type": "select",
  "name": "city",
  "source": "/api/cities"
}
```

---

## 相关文档

### 📚 组件完整指南
- [表格组件指南](./references/table-guide.md) - Table/CRUD、列配置、搜索筛选、分页、行内编辑
- [表单组件指南](./references/form-guide.md) - Form、各种输入组件、验证规则、文件上传
- [图表组件指南](./references/chart-guide.md) - ECharts集成、常用图表类型、数据绑定
- [字段联动指南](./references/linkage-guide.md) - 显隐联动、值联动、条件渲染、数据转换
- [主题定制指南](./references/theme-guide.md) - 主题切换、自定义样式、暗黑模式、响应式

### 🔧 其他参考
- [组件参考手册](./references/components.md)
- [页面模板](./references/page-templates.md)
- [API对接指南](./references/api-integration.md)
- [样式定制指南](./references/styling-guide.md)
