# Amis 组件参考手册

## 布局类组件

### Flex 弹性布局

**用途**：使用 CSS Flexbox 实现灵活的弹性布局。

**Schema 模板**：
```json
{
  "type": "flex",
  "direction": "row",
  "justify": "flex-start",
  "alignItems": "stretch",
  "className": "",
  "style": {},
  "items": [
    { "type": "tpl", "tpl": "子项1" },
    { "type": "tpl", "tpl": "子项2" }
  ]
}
```

**关键属性**：
| 属性 | 说明 | 可选值 |
|------|------|--------|
| direction | 主轴方向 | `row`(默认), `column` |
| justify | 主轴对齐 | `flex-start`, `center`, `flex-end`, `space-between`, `space-around` |
| alignItems | 交叉轴对齐 | `stretch`(默认), `flex-start`, `center`, `flex-end`, `baseline` |
| flex | 份数 | 数字，如 `1`, `2` |
| items | 子元素 | 组件数组 |

**示例**：等分布局
```json
{
  "type": "flex",
  "justify": "space-around",
  "items": [
    { "flex": 1, "body": { "type": "card", "header": {"title": "卡片1"} } },
    { "flex": 1, "body": { "type": "card", "header": {"title": "卡片2"} } },
    { "flex": 1, "body": { "type": "card", "header": {"title": "卡片3"} } }
  ]
}
```

---

### Grid 栅格布局

**用途**：使用 12 列栅格系统实现响应式布局。

**Schema 模板**：
```json
{
  "type": "grid",
  "columns": [
    { "md": 6, "body": "左侧内容" },
    { "md": 6, "body": "右侧内容" }
  ]
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| columns | 列配置数组 |
| columns[x].md | PC 端占比 (1-12) |
| columns[x].lg | 大屏幕占比 |
| columns[x].sm | 平板占比 |
| columns[x].xs | 手机占比 |

**示例**：左侧 2/3，右侧 1/3
```json
{
  "type": "grid",
  "columns": [
    { "md": 8, "body": { "type": "crud", "api": "/api/list" } },
    { "md": 4, "body": { "type": "panel", "title": "统计", "body": "..." } }
  ]
}
```

---

### HBox 水平布局

**用途**：Form 内部水平排列表单项。

**Schema 模板**：
```json
{
  "type": "hbox",
  "columns": [
    { "columnClassName": "w-sm", "controls": [...] },
    { "columnClassName": "w-sm", "controls": [...] }
  ]
}
```

---

### VBox 垂直布局

**用途**：垂直方向排列内容。

**Schema 模板**：
```json
{
  "type": "vbox",
  "rows": [
    { "height": 100, "body": "第一行" },
    { "flex": 1, "body": "第二行（自动填充）" }
  ]
}
```

---

### Wrapper 容器

**用途**：简单的内容包裹容器，支持尺寸预设。

**Schema 模板**：
```json
{
  "type": "wrapper",
  "className": "wrapper--sm",
  "body": "内容"
}
```

**常用尺寸**：`wrapper--xs`, `wrapper--sm`, `wrapper--md`, `wrapper--lg`, `wrapper--xl`

---

### Panel 面板

**用途**：带标题、边框的分组容器。

**Schema 模板**：
```json
{
  "type": "panel",
  "title": "面板标题",
  "subTitle": "副标题",
  "headerClassName": "",
  "body": "面板内容",
  "footer": "底部内容",
  "actions": [
    { "type": "button", "label": "确定" }
  ]
}
```

---

### Tabs 选项卡

**用途**：多内容区域切换展示。

**Schema 模板**：
```json
{
  "type": "tabs",
  "tabs": [
    { "title": "标签1", "body": { "type": "tpl", "tpl": "内容1" } },
    { "title": "标签2", "body": { "type": "tpl", "tpl": "内容2" } }
  ],
  "mode": "vertical"
}
```

**关键属性**：
| 属性 | 说明 | 可选值 |
|------|------|--------|
| tabs | 选项卡数组 | - |
| mode | 排列方式 | `horizontal`(默认), `vertical`, `tiled` |
| source | 动态数据源 | API 地址 |

---

### Collapse 折叠器

**用途**：可折叠的内容区域，支持手风琴模式。

**Schema 模板**：
```json
{
  "type": "collapse",
  "header": "点击展开",
  "body": "折叠内容",
  "collapsed": false,
  "accordion": true
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| header | 折叠触发器标题 |
| body | 折叠内容 |
| collapsed | 默认是否折叠 |
| accordion | 是否手风琴模式 |

---

## 容器类组件

### Page 页面

**用途**：页面根容器，所有页面的入口。

**Schema 模板**：
```json
{
  "type": "page",
  "title": "页面标题",
  "subTitle": "副标题",
  "remark": "提示信息",
  "initApi": "/api/init",
  "body": [],
  "aside": [],
  "toolbar": []
}
```

---

### Container 容器

**用途**：通用内容容器。

**Schema 模板**：
```json
{
  "type": "container",
  "className": "",
  "style": {},
  "body": "内容"
}
```

---

### Chart 图表容器

**用途**：ECharts 图表容器。

**Schema 模板**：
```json
{
  "type": "chart",
  "config": {
    "title": {"text": "图表标题"},
    "xAxis": {"type": "category", "data": ["一月", "二月"]},
    "yAxis": {"type": "value"},
    "series": [{"name": "销量", "type": "line", "data": [120, 200]}]
  },
  "source": "/api/chart-data"
}
```

---

### IFrame

**用途**：嵌入外部网页。

**Schema 模板**：
```json
{
  "type": "iframe",
  "src": "https://example.com",
  "height": 400
}
```

---

## 表单类组件

### Form 表单

**用途**：数据收集和提交。

**Schema 模板**：
```json
{
  "type": "form",
  "mode": "normal",
  "api": "post:/api/submit",
  "redirect": "/success",
  "body": [
    {"type": "input-text", "name": "name", "label": "姓名", "required": true}
  ],
  "buttons": [
    {"type": "reset", "label": "重置"},
    {"type": "submit", "label": "提交", "level": "primary"}
  ]
}
```

**关键属性**：
| 属性 | 说明 | 可选值 |
|------|------|--------|
| mode | 表单模式 | `normal`, `horizontal`, `inline` |
| api | 提交接口 | - |
| body | 表单项 | 数组 |
| rules | 表单级验证规则 | - |

---

### InputText 文本框

**Schema 模板**：
```json
{
  "type": "input-text",
  "name": "username",
  "label": "用户名",
  "placeholder": "请输入用户名",
  "required": true,
  "validations": {
    "minLength": 3,
    "maxLength": 20
  }
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| name | 字段名 |
| label | 标签 |
| placeholder | 占位符 |
| required | 是否必填 |
| clearable | 是否可清空 |
| resetValue | 重置值 |

---

### InputNumber 数字框

**Schema 模板**：
```json
{
  "type": "input-number",
  "name": "age",
  "label": "年龄",
  "min": 0,
  "max": 150,
  "step": 1,
  "precision": 0
}
```

---

### Select 下拉选择

**Schema 模板**：
```json
{
  "type": "select",
  "name": "city",
  "label": "城市",
  "options": [
    {"label": "北京", "value": "bj"},
    {"label": "上海", "value": "sh"},
    {"label": "广州", "value": "gz"}
  ],
  "source": "/api/cities",
  "multiple": false,
  "searchable": true
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| options | 静态选项 |
| source | 动态数据源 |
| multiple | 是否多选 |
| searchable | 是否可搜索 |
| labelField | 选项标签字段 |
| valueField | 选项值字段 |

---

### Radio 单选

**Schema 模板**：
```json
{
  "type": "radios",
  "name": "gender",
  "label": "性别",
  "options": [
    {"label": "男", "value": "male"},
    {"label": "女", "value": "female"}
  ],
  "inline": true
}
```

---

### Checkbox 复选

**Schema 模板**：
```json
{
  "type": "checkboxes",
  "name": "hobbies",
  "label": "爱好",
  "options": [
    {"label": "阅读", "value": "reading"},
    {"label": "运动", "value": "sports"},
    {"label": "音乐", "value": "music"}
  ],
  "inline": true
}
```

---

### Switch 开关

**Schema 模板**：
```json
{
  "type": "switch",
  "name": "isActive",
  "label": "启用状态",
  "onText": "开",
  "offText": "关"
}
```

---

### DatePicker 日期选择

**Schema 模板**：
```json
{
  "type": "input-date",
  "name": "birthday",
  "label": "出生日期",
  "format": "YYYY-MM-DD",
  "inputFormat": "YYYY-MM-DD"
}
```

**日期范围**：
```json
{
  "type": "input-date-range",
  "name": "dateRange",
  "label": "日期范围",
  "format": "YYYY-MM-DD",
  "ranges": ["today", "yesterday", "lastWeek", "lastMonth"]
}
```

---

### InputFile 文件上传

**Schema 模板**：
```json
{
  "type": "input-file",
  "name": "attachment",
  "label": "附件",
  "accept": ".jpg,.png,.pdf",
  "maxSize": 5242880,
  "multiple": false,
  "draggable": true
}
```

---

### InputImage 图片上传

**Schema 模板**：
```json
{
  "type": "input-image",
  "name": "avatar",
  "label": "头像",
  "accept": ".jpg,.png",
  "maxSize": 2097152,
  "multiple": false,
  "crop": true,
  "cropRatio": "1:1"
}
```

---

### InputRichText 富文本

**Schema 模板**：
```json
{
  "type": "input-rich-text",
  "name": "content",
  "label": "内容",
  "options": {
    "menus": ["bold", "italic", "underline"]
  }
}
```

---

### InputTable 表格编辑

**Schema 模板**：
```json
{
  "type": "input-table",
  "name": "items",
  "label": "明细",
  "columns": [
    {"name": "name", "label": "名称", "type": "input-text"},
    {"name": "quantity", "label": "数量", "type": "input-number"},
    {"name": "price", "label": "单价", "type": "input-number"}
  ],
  "addable": true,
  "editable": true,
  "removable": true
}
```

---

### Combo 组合输入

**Schema 模板**：
```json
{
  "type": "combo",
  "name": "contacts",
  "label": "联系人",
  "multiple": true,
  "items": [
    {"type": "input-text", "name": "name", "placeholder": "姓名"},
    {"type": "input-text", "name": "phone", "placeholder": "电话"}
  ],
  "addable": true,
  "removable": true
}
```

---

### FieldSet 字段集

**Schema 模板**：
```json
{
  "type": "fieldSet",
  "title": "基本信息",
  "collapsable": true,
  "collapsed": false,
  "body": [
    {"type": "input-text", "name": "name", "label": "姓名"},
    {"type": "input-email", "name": "email", "label": "邮箱"}
  ]
}
```

---

### InputGroup 输入组合

**Schema 模板**：
```json
{
  "type": "input-group",
  "name": "phone",
  "label": "电话号码",
  "body": [
    {"type": "select", "name": "prefix", "options": [{"label": "+86", "value": "86"}], "style": {"width": "80px"}},
    {"type": "input-text", "name": "number", "placeholder": "手机号"}
  ]
}
```

---

## 展示类组件

### Table 表格

**Schema 模板**：
```json
{
  "type": "table",
  "data": {"items": []},
  "columns": [
    {"name": "id", "label": "ID"},
    {"name": "name", "label": "名称"},
    {"type": "operation", "label": "操作", "buttons": []}
  ]
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| columns | 列配置 |
| columns[x].name | 数据字段名 |
| columns[x].label | 列标题 |
| columns[x].type | 列类型 |
| columns[x].sortable | 是否可排序 |
| columns[x].searchable | 是否可搜索 |

---

### CRUD 增删改查

**Schema 模板**：
```json
{
  "type": "crud",
  "api": "/api/list",
  "filter": {
    "body": [],
    "actions": []
  },
  "columns": [],
  "bulkActions": [],
  "headerToolbar": ["bulkActions", "filter-toggler", "pagination"],
  "footerToolbar": ["statistics", "pagination"]
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| api | 数据接口 |
| filter | 筛选器 |
| columns | 表格列 |
| bulkActions | 批量操作 |
| quickSaveApi | 快速保存接口 |
| headerToolbar | 顶部工具栏 |
| footerToolbar | 底部工具栏 |

---

### Cards 卡片列表

**Schema 模板**：
```json
{
  "type": "cards",
  "source": "${items}",
  "card": {
    "header": {"title": "${title}", "subTitle": "${subTitle}"},
    "body": "${description}",
    "media": {"type": "image", "src": "${image}"}
  }
}
```

---

### List 列表

**Schema 模板**：
```json
{
  "type": "list",
  "source": "${items}",
  "listItem": {
    "title": "${title}",
    "subTitle": "${createTime}",
    "description": "${description}",
    "actions": []
  }
}
```

---

### Detail 详情

**Schema 模板**：
```json
{
  "type": "detail",
  "api": "/api/detail/${id}",
  "mode": "horizontal",
  "columns": [
    {"name": "name", "label": "姓名"},
    {"name": "email", "label": "邮箱"}
  ]
}
```

---

### Log 日志

**Schema 模板**：
```json
{
  "type": "log",
  "source": "/api/logs",
  "height": 400,
  "autoScroll": true
}
```

---

### Json 展示

**Schema 模板**：
```json
{
  "type": "json",
  "value": {"key": "value"},
  "source": "/api/json-data"
}
```

---

### Markdown 渲染

**Schema 模板**：
```json
{
  "type": "markdown",
  "value": "# 标题\n\n内容",
  "source": "/api/markdown-content"
}
```

---

## 反馈类组件

### Dialog 对话框

**Schema 模板**：
```json
{
  "type": "dialog",
  "title": "对话框标题",
  "body": "内容",
  "size": "md",
  "actions": [
    {"type": "button", "label": "取消"},
    {"type": "button", "label": "确定", "level": "primary", "actionType": "confirm"}
  ]
}
```

**常用尺寸**：`xs`, `sm`, `md`, `lg`, `xl`, `full`

---

### Drawer 抽屉

**Schema 模板**：
```json
{
  "type": "drawer",
  "title": "抽屉标题",
  "position": "right",
  "size": "md",
  "body": "内容"
}
```

**位置**：`left`, `right`, `top`, `bottom`

---

### Toast 提示

**Schema 模板**：
```json
{
  "type": "toast",
  "content": "提示内容",
  "level": "success",
  "position": "top-center"
}
```

**级别**：`info`, `success`, `warning`, `error`

---

### Alert 警告

**Schema 模板**：
```json
{
  "type": "alert",
  "level": "info",
  "title": "提示",
  "body": "提示内容",
  "showClose": true
}
```

---

## 数据类组件

### Service 数据容器

**用途**：用于加载和展示远程数据。

**Schema 模板**：
```json
{
  "type": "service",
  "api": "/api/data",
  "schemaApi": "/api/schema",
  "body": {
    "type": "tpl",
    "tpl": "数据：${data}"
  }
}
```

**关键属性**：
| 属性 | 说明 |
|------|------|
| api | 数据接口 |
| schemaApi | Schema 接口 |
| initApi | 初始化接口 |
| body | 内容 |
| data | 初始数据 |

---

### DataSource 数据源

**用途**：封装 API 数据源配置。

**Schema 模板**：
```json
{
  "type": "dataSource",
  "name": "users",
  "api": "/api/users",
  "value": []
}
```

---

## 其他常用组件

### Button 按钮

**Schema 模板**：
```json
{
  "type": "button",
  "label": "按钮文字",
  "level": "default",
  "actionType": "ajax",
  "api": "post:/api/action",
  "icon": "fa fa-plus",
  "disabled": false
}
```

**级别**：`default`, `primary`, `danger`, `info`, `success`, `warning`

---

### Icon 图标

**Schema 模板**：
```json
{
  "type": "icon",
  "icon": "fa fa-home"
}
```

---

### Tpl 模板

**Schema 模板**：
```json
{
  "type": "tpl",
  "tpl": "Hello ${name}",
  "html": false
}
```

---

### Mapping 映射

**Schema 模板**：
```json
{
  "type": "mapping",
  "name": "status",
  "map": {
    "0": "<span class='text-success'>正常</span>",
    "1": "<span class='text-danger'>禁用</span>",
    "*": "未知状态"
  }
}
```

---

### Progress 进度条

**Schema 模板**：
```json
{
  "type": "progress",
  "name": "progress",
  "value": 75,
  "map": {
    "0": "危险",
    "75": "进行中",
    "100": "完成"
  }
}
```

---

### Avatar 头像

**Schema 模板**：
```json
{
  "type": "avatar",
  "src": "${avatarUrl}",
  "size": "lg",
  "name": "${name}"
}
```
