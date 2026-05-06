# Amis Table/CRUD 组件完整指南

## 目录
- [基础表格 (Table)](#基础表格-table)
- [CRUD 组件](#crud-组件)
- [列配置详解](#列配置详解)
- [搜索与筛选](#搜索与筛选)
- [分页配置](#分页配置)
- [行内编辑](#行内编辑)
- [操作按钮](#操作按钮)

---

## 基础表格 (Table)

### 基础用法

```json
{
  "type": "page",
  "body": {
    "type": "table",
    "columns": [
      { "name": "name", "label": "姓名" },
      { "name": "age", "label": "年龄" },
      { "name": "email", "label": "邮箱" }
    ],
    "data": {
      "items": [
        { "name": "张三", "age": 25, "email": "zhang@example.com" },
        { "name": "李四", "age": 30, "email": "li@example.com" }
      ]
    }
  }
}
```

### Table 完整配置

```json
{
  "type": "table",
  "name": "myTable",
  "dataSource": "/api/list",
  "columns": [],
  // 表格样式
  "className": "table-striped table-hover",
  "trClassName": "tr-${index % 2 === 0 ? 'bg-light' : ''}",
  // 行选择
  "selectable": true,
  "multiple": true,
  "primaryField": "id",
  // 配置列
  "columnsTogglable": true,
  "headerHeight": 40,
  "rowHeight": 40,
  // 加载状态
  "loading": false,
  // 无数据提示
  "placeholder": "暂无数据",
  "showHeader": true,
  // 虚拟滚动（大数据量）
  "virtualized": true,
  "itemHeight": 40
}
```

---

## CRUD 组件

CRUD 是 Table 的增强，集成了增删改查、分页、筛选等完整功能。

### 基础 CRUD

```json
{
  "type": "crud",
  "name": "userCrud",
  "api": "/api/users",
  "columns": [
    { "name": "id", "label": "ID" },
    { "name": "name", "label": "用户名" },
    { "name": "email", "label": "邮箱" }
  ]
}
```

### CRUD 完整配置

```json
{
  "type": "crud",
  "name": "userCrud",
  // 数据获取 API
  "api": "/api/users",
  // 新增 API
  "createApi": "post:/api/users",
  // 更新 API
  "updateApi": "put:/api/users/${id}",
  // 删除 API
  "deleteApi": "delete:/api/users/${id}",
  // 批量删除 API
  "bulkDeleteApi": "post:/api/users/batch-delete",
  // 快速保存 API
  "quickSaveApi": "post:/api/users/batch-edit",
  // 快速编辑 API
  "quickEditApi": "put:/api/users/${id}",
  // 工具栏配置
  "headerToolbar": ["bulkActions", "filter-toggler", "columns-toggler"],
  "footerToolbar": ["pagination", "statistics"],
  // 筛选器配置
  "filter": {
    "title": "搜索条件",
    "body": [
      { "type": "input-text", "name": "keywords", "label": "关键字" }
    ],
    "actions": [
      { "type": "reset", "label": "重置" },
      { "type": "submit", "label": "搜索", "level": "primary" }
    ]
  },
  "columns": []
}
```

### API 响应格式

Amis 期望的 API 响应格式：

```json
{
  "status": 0,
  "msg": "ok",
  "data": {
    "items": [...],
    "total": 100
  }
}
```

**关键字段说明**：
- `status`: 0 表示成功，其他值表示失败
- `msg`: 状态消息
- `data.items`: 数据列表
- `data.total`: 总记录数（用于分页）

---

## 列配置详解

### 基础列类型

```json
{
  "columns": [
    // 文本列
    { "name": "name", "label": "用户名" },
    
    // 数字列
    { "name": "age", "label": "年龄", "type": "number", "format": "YYO" },
    
    // 图片列
    { "name": "avatar", "label": "头像", "type": "image", "imageClassName": "rounded w-36" },
    
    // 日期列
    { "name": "createdAt", "label": "创建时间", "type": "date", "format": "YYYY-MM-DD" },
    
    // 日期时间列
    { 
      "name": "updatedAt", 
      "label": "更新时间", 
      "type": "datetime", 
      "format": "YYYY-MM-DD HH:mm:ss" 
    },
    
    // 链接列
    { 
      "name": "blog", 
      "label": "博客", 
      "type": "link", 
      "href": "${blog}", 
      "blank": true 
    }
  ]
}
```

### 映射列 (Mapping)

用于状态展示：

```json
{
  "name": "status",
  "label": "状态",
  "type": "mapping",
  "map": {
    "0": "<span class='text-muted'>禁用</span>",
    "1": "<span class='text-success'>启用</span>",
    "2": "<span class='text-warning'>待审核</span>"
  },
  "placeholder": "-"
}
```

### 操作列 (Operation)

```json
{
  "type": "operation",
  "label": "操作",
  "width": 200,
  "buttons": [
    {
      "type": "button",
      "label": "查看",
      "actionType": "dialog",
      "dialog": {
        "title": "详情",
        "body": { "type": "tpl", "tpl": "详细内容..." }
      }
    },
    {
      "type": "button",
      "label": "编辑",
      "actionType": "drawer",
      "drawer": {
        "title": "编辑",
        "body": { "type": "form", "api": "put:/api/item/${id}", "body": [] }
      }
    },
    {
      "type": "button",
      "label": "删除",
      "actionType": "ajax",
      "api": "delete:/api/item/${id}",
      "confirmText": "确定删除？",
      "level": "danger"
    }
  ]
}
```

### 拖拽排序列

```json
{
  "name": "sort",
  "label": "排序",
  "type": "draggable"
}
```

### 复选框列

```json
{
  "name": "selected",
  "label": "选择",
  "type": "checkbox",
  "value": false
}
```

### 列宽与对齐

```json
{
  "name": "name",
  "label": "姓名",
  "width": 150,
  "align": "left",
  "fixed": "left"  // 固定列：left, right, none
}
```

### 可排序列

```json
{
  "name": "createdAt",
  "label": "创建时间",
  "sortable": true,
  "sorted": "desc"  // asc, desc, initial
}
```

### 可搜索列

```json
{
  "name": "name",
  "label": "姓名",
  "searchable": true,
  "searchable": {
    "type": "input-text",
    "placeholder": "搜索姓名"
  }
}
```

---

## 搜索与筛选

### 简单筛选器

```json
{
  "filter": {
    "title": "筛选条件",
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
          { "label": "全部", "value": "" },
          { "label": "启用", "value": "active" },
          { "label": "禁用", "value": "inactive" }
        ]
      },
      {
        "type": "date-range",
        "name": "dateRange",
        "label": "时间范围"
      }
    ],
    "actions": [
      { "type": "reset", "label": "重置" },
      { "type": "submit", "label": "搜索", "level": "primary" }
    ]
  }
}
```

### 高级筛选器（折叠面板）

```json
{
  "filter": {
    "title": "搜索条件",
    "mode": "normal",
    "body": [
      { "type": "input-text", "name": "keywords", "label": "关键字" },
      { "type": "select", "name": "category", "label": "分类" }
    ],
    "actions": [
      { "type": "reset", "label": "重置" },
      { "type": "submit", "label": "搜索", "level": "primary" }
    ]
  },
  "filterDefaultVisible": false
}
```

### 工具栏快捷筛选

```json
{
  "headerToolbar": [
    {
      "type": "tpl",
      "tpl": "状态：",
      "className": "m-r-xs"
    },
    {
      "type": "dropdown-button",
      "label": "全部",
      "buttons": [
        { "type": "button", "label": "全部", "onClick": "..." },
        { "type": "button", "label": "启用", "onClick": "..." },
        { "type": "button", "label": "禁用", "onClick": "..." }
      ]
    }
  ]
}
```

---

## 分页配置

### 基础分页

```json
{
  "footerToolbar": [
    "pagination"
  ]
}
```

### 分页详细配置

```json
{
  "pageField": "page",
  "perPageField": "pageSize",
  "perPage": 20,
  "pagePerPage": 50,
  "footerToolbar": [
    {
      "type": "pagination",
      "layout": "total, perPage, pager"
    }
  ]
}
```

### 分页位置

- `headerToolbar`: 顶部工具栏
- `footerToolbar`: 底部工具栏

### 分页组件配置

```json
{
  "type": "pagination",
  "layout": "total, perPage, pager, go",
  "totalLocation": "toolbar-left",
  "showPageInput": true,
  "maxButtons": 7
}
```

### 统计信息

```json
{
  "footerToolbar": [
    "statistics"
  ]
}
```

统计模板：

```json
{
  "type": "tpl",
  "tpl": "共 ${total} 条记录，当前显示 ${items|picker:length} 条"
}
```

---

## 行内编辑

### 快速编辑

```json
{
  "quickEditEnabled": true,
  "quickEditApi": "put:/api/item/${id}",
  "columns": [
    {
      "name": "name",
      "label": "名称",
      "quickEdit": {
        "type": "input-text",
        "required": true
      }
    },
    {
      "name": "price",
      "label": "价格",
      "quickEdit": {
        "type": "input-number",
        "min": 0,
        "precision": 2
      }
    }
  ]
}
```

### 快速编辑 + 表单

```json
{
  "name": "status",
  "label": "状态",
  "quickEdit": {
    "type": "select",
    "options": [
      { "label": "启用", "value": 1 },
      { "label": "禁用", "value": 0 }
    ]
  }
}
```

### 批量行内编辑

启用批量选择和快速保存：

```json
{
  "selectable": true,
  "multiple": true,
  "quickSaveApi": "post:/api/items/batch-edit",
  "quickEditEnabled": true,
  "columns": [
    {
      "name": "sort",
      "label": "排序",
      "quickEdit": {
        "type": "input-number"
      }
    }
  ]
}
```

---

## 操作按钮

### 按钮类型

```json
{
  "type": "operation",
  "label": "操作",
  "buttons": [
    // 普通按钮
    { "type": "button", "label": "查看", "actionType": "dialog" },
    
    // 图标按钮
    { "type": "button", "icon": "fa fa-eye", "actionType": "dialog" },
    
    // 文字按钮
    { "type": "button", "label": "删除", "level": "danger", "actionType": "ajax" },
    
    // 下拉菜单
    {
      "type": "dropdown-button",
      "label": "更多",
      "buttons": [
        { "type": "button", "label": "编辑" },
        { "type": "button", "label": "复制" },
        { "type": "button", "label": "删除", "level": "danger" }
      ]
    }
  ]
}
```

### 常用操作

#### 1. Dialog 弹窗

```json
{
  "type": "button",
  "label": "详情",
  "actionType": "dialog",
  "dialog": {
    "title": "用户详情",
    "size": "lg",
    "body": {
      "type": "form",
      "mode": "horizontal",
      "body": [
        { "type": "static", "name": "name", "label": "用户名" },
        { "type": "static", "name": "email", "label": "邮箱" }
      ]
    }
  }
}
```

#### 2. Drawer 抽屉

```json
{
  "type": "button",
  "label": "编辑",
  "actionType": "drawer",
  "drawer": {
    "title": "编辑用户",
    "position": "right",
    "size": "lg",
    "body": {
      "type": "form",
      "api": "put:/api/user/${id}",
      "body": [
        { "type": "input-text", "name": "name", "label": "用户名" },
        { "type": "input-email", "name": "email", "label": "邮箱" }
      ],
      "buttons": [
        { "type": "cancel", "label": "取消" },
        { "type": "submit", "label": "保存", "level": "primary" }
      ]
    }
  }
}
```

#### 3. Ajax 请求

```json
{
  "type": "button",
  "label": "删除",
  "actionType": "ajax",
  "api": "delete:/api/user/${id}",
  "confirmText": "确定删除该用户吗？此操作不可逆！",
  "level": "danger",
  // 成功后刷新表格
  "reload": "userCrud"
}
```

#### 4. 页面跳转

```json
{
  "type": "button",
  "label": "查看详情",
  "actionType": "link",
  "link": "/user/detail/${id}"
}
```

### 按钮权限控制

```json
{
  "type": "button",
  "label": "删除",
  "visibleOn": "data.role === 'admin'",
  "hiddenOn": "data.isDeleted"
}
```

---

## 完整示例

```json
{
  "type": "crud",
  "name": "userCrud",
  "api": "/api/users",
  "filter": {
    "title": "搜索条件",
    "body": [
      { "type": "input-text", "name": "keywords", "label": "关键字", "placeholder": "用户名/邮箱" },
      { "type": "select", "name": "status", "label": "状态", "options": [{"label": "全部", "value": ""}, {"label": "启用", "value": "active"}, {"label": "禁用", "value": "inactive"}] }
    ],
    "actions": [{"type": "reset", "label": "重置"}, {"type": "submit", "label": "搜索", "level": "primary"}]
  },
  "headerToolbar": [
    {"type": "button", "label": "新增用户", "icon": "fa fa-plus", "actionType": "dialog", "level": "primary", "dialog": {"title": "新增用户", "body": {"type": "form", "api": "post:/api/users", "body": [{"type": "input-text", "name": "name", "label": "用户名", "required": true}, {"type": "input-email", "name": "email", "label": "邮箱", "required": true}]}}}},
    "bulkActions",
    "filter-toggler",
    "columns-toggler"
  ],
  "footerToolbar": ["statistics", "pagination"],
  "columns": [
    {"type": "columns-toggler"},
    {"name": "id", "label": "ID", "width": 80, "sortable": true},
    {"name": "name", "label": "用户名", "width": 120, "sortable": true, "searchable": true},
    {"name": "email", "label": "邮箱", "searchable": true},
    {"name": "status", "label": "状态", "type": "mapping", "map": {"active": "<span class='text-success'>启用</span>", "inactive": "<span class='text-muted'>禁用</span>"}},
    {"name": "createdAt", "label": "创建时间", "type": "date", "format": "YYYY-MM-DD", "sortable": true},
    {"type": "operation", "label": "操作", "width": 200, "buttons": [{"type": "button", "label": "编辑", "actionType": "drawer", "drawer": {"title": "编辑用户", "body": {"type": "form", "api": "put:/api/users/${id}", "body": [{"type": "input-text", "name": "name", "label": "用户名", "required": true}]}}}, {"type": "button", "label": "删除", "actionType": "ajax", "api": "delete:/api/users/${id}", "confirmText": "确定删除？", "level": "danger"}]}]}
  ]
}
```
