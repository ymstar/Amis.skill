# Amis Form 组件完整指南

## 目录
- [基础表单](#基础表单)
- [表单配置](#表单配置)
- [输入组件](#输入组件)
- [级联选择](#级联选择)
- [表单验证](#表单验证)
- [Combo 组合输入](#combo-组合输入)
- [文件上传](#文件上传)
- [完整示例](#完整示例)

---

## 基础表单

### 最小示例

```json
{
  "type": "page",
  "body": {
    "type": "form",
    "api": "post:/api/submit",
    "body": [
      { "type": "input-text", "name": "username", "label": "用户名" },
      { "type": "input-email", "name": "email", "label": "邮箱" }
    ],
    "buttons": [
      { "type": "submit", "label": "提交", "level": "primary" }
    ]
  }
}
```

---

## 表单配置

### Form 组件属性

```json
{
  "type": "form",
  "name": "myForm",
  "mode": "normal",
  "title": "表单标题",
  "api": "post:/api/submit",
  "method": "post",
  // 提交后行为
  "redirect": "/success",
  "resetAfterSubmit": true,
  "showErrorMsg": true,
  "clearPersistDataAfterSubmit": true,
  // 表单值
  "values": {},
  "default": {},
  "data": {},
  // 布局
  "columnCount": 2,
  "labelWidth": 100,
  // 调试
  "debug": false
}
```

### mode 布局模式

| mode | 说明 |
|------|------|
| `normal` | 标准布局（标签在上） |
| `horizontal` | 水平布局（标签在左） |
| `inline` | 行内布局（全部在一行） |

```json
{
  "type": "form",
  "mode": "horizontal",
  "labelWidth": 120,
  "body": [
    { "type": "input-text", "name": "name", "label": "姓名" }
  ]
}
```

### 按钮配置

```json
{
  "type": "form",
  "body": [...],
  "buttons": [
    { "type": "reset", "label": "重置" },
    { "type": "submit", "label": "提交", "level": "primary" }
  ]
}
```

---

## 输入组件

### 文本输入

```json
{
  "type": "input-text",
  "name": "username",
  "label": "用户名",
  "placeholder": "请输入用户名",
  "required": true,
  "clearable": true,
  "trim": true,
  "maxLength": 50,
  "validations": {
    "minLength": 2,
    "maxLength": 20
  }
}
```

### 邮箱输入

```json
{
  "type": "input-email",
  "name": "email",
  "label": "邮箱",
  "required": true,
  "validations": {
    "isEmail": true
  }
}
```

### 密码输入

```json
{
  "type": "input-password",
  "name": "password",
  "label": "密码",
  "required": true,
  "validations": {
    "minLength": 6
  }
}
```

### 数字输入

```json
{
  "type": "input-number",
  "name": "price",
  "label": "价格",
  "value": 0,
  "min": 0,
  "max": 999999,
  "step": 0.01,
  "precision": 2,
  "prefix": "¥"
}
```

### 多行文本

```json
{
  "type": "textarea",
  "name": "description",
  "label": "描述",
  "placeholder": "请输入详细描述",
  "minRows": 3,
  "maxRows": 10,
  "trim": true
}
```

### 下拉选择 (Select)

```json
{
  "type": "select",
  "name": "country",
  "label": "国家",
  "placeholder": "请选择",
  "required": true,
  "options": [
    { "label": "中国", "value": "cn" },
    { "label": "美国", "value": "us" },
    { "label": "日本", "value": "jp" }
  ],
  "clearable": true,
  "searchable": true,
  "multiple": false
}
```

**多选模式**：

```json
{
  "type": "select",
  "name": "hobbies",
  "label": "爱好",
  "multiple": true,
  "options": [
    { "label": "阅读", "value": "reading" },
    { "label": "运动", "value": "sports" },
    { "label": "音乐", "value": "music" }
  ],
  "checkAll": true,
  "source": "/api/options/hobbies"
}
```

**动态数据源**：

```json
{
  "type": "select",
  "name": "category",
  "label": "分类",
  "source": {
    "method": "get",
    "url": "/api/categories"
  },
  "labelField": "name",
  "valueField": "id"
}
```

### 单选按钮 (Radios)

```json
{
  "type": "radios",
  "name": "gender",
  "label": "性别",
  "required": true,
  "options": [
    { "label": "男", "value": "male" },
    { "label": "女", "value": "female" }
  ],
  "inline": true
}
```

### 复选框 (Checkboxes)

```json
{
  "type": "checkboxes",
  "name": "interests",
  "label": "兴趣领域",
  "required": true,
  "options": [
    { "label": "前端开发", "value": "frontend" },
    { "label": "后端开发", "value": "backend" },
    { "label": "移动开发", "value": "mobile" },
    { "label": "数据分析", "value": "data" }
  ],
  "checkAll": true
}
```

### 开关 (Switch)

```json
{
  "type": "switch",
  "name": "isEnabled",
  "label": "启用",
  "value": true,
  "trueValue": true,
  "falseValue": false
}
```

### 日期选择

```json
{
  "type": "input-date",
  "name": "birthday",
  "label": "生日",
  "format": "YYYY-MM-DD",
  "value": "2024-01-01",
  "minDate": "1900-01-01",
  "maxDate": "today"
}
```

### 日期时间选择

```json
{
  "type": "input-datetime",
  "name": "startTime",
  "label": "开始时间",
  "format": "YYYY-MM-DD HH:mm:ss"
}
```

### 日期范围

```json
{
  "type": "date-range",
  "name": "dateRange",
  "label": "日期范围",
  "format": "YYYY-MM-DD",
  "ranges": ["today", "yesterday", "last7days", "last30days"]
}
```

### 时间选择

```json
{
  "type": "input-time",
  "name": "startTime",
  "label": "开始时间",
  "format": "HH:mm"
}
```

### 颜色选择

```json
{
  "type": "input-color",
  "name": "color",
  "label": "主题色",
  "value": "#1890ff"
}
```

### 评分

```json
{
  "type": "rating",
  "name": "rating",
  "label": "满意度",
  "value": 4,
  "max": 5
}
```

### 滑块

```json
{
  "type": "slider",
  "name": "price",
  "label": "价格区间",
  "value": 50,
  "min": 0,
  "max": 100,
  "step": 1,
  "showInput": true
}
```

### Tree 选择器

```json
{
  "type": "tree-select",
  "name": "category",
  "label": "分类",
  "options": [
    {
      "label": "研发部",
      "value": "dev",
      "children": [
        { "label": "前端组", "value": "frontend" },
        { "label": "后端组", "value": "backend" }
      ]
    },
    {
      "label": "市场部",
      "value": "marketing"
    }
  ],
  "multiple": true
}
```

---

## 级联选择

### Cascader 基本用法

```json
{
  "type": "cascader",
  "name": "region",
  "label": "所在地区",
  "placeholder": "请选择省市区",
  "options": [
    {
      "label": "北京市",
      "value": "beijing",
      "children": [
        { "label": "东城区", "value": "dongcheng" },
        { "label": "西城区", "value": "xicheng" }
      ]
    },
    {
      "label": "广东省",
      "value": "guangdong",
      "children": [
        { "label": "广州市", "value": "guangzhou" },
        { "label": "深圳市", "value": "shenzhen" }
      ]
    }
  ]
}
```

### 动态加载级联数据

```json
{
  "type": "cascader",
  "name": "category",
  "label": "商品分类",
  "source": {
    "method": "get",
    "url": "/api/categories/tree"
  },
  "value": "a/b/c",
  "delimiter": "/"
}
```

### 多级联动（独立选择器）

多个 Select 联动：

```json
{
  "type": "form",
  "body": [
    {
      "type": "select",
      "name": "province",
      "label": "省份",
      "source": "/api/regions/provinces",
      "onChange": "window.updateCity(this)"
    },
    {
      "type": "select",
      "name": "city",
      "label": "城市",
      "source": {
        "method": "get",
        "url": "/api/regions/cities",
        "data": { "province": "${province}" }
      }
    },
    {
      "type": "select",
      "name": "district",
      "label": "区县",
      "source": {
        "method": "get",
        "url": "/api/regions/districts",
        "data": { "city": "${city}" }
      }
    }
  ]
}
```

---

## 表单验证

### 内置验证规则

```json
{
  "type": "input-text",
  "name": "field",
  "validations": {
    "isRequired": true,
    "isEmail": true,
    "isUrl": true,
    "isPhoneNumber": true,
    "isZipCode": true,
    "minLength": 2,
    "maxLength": 20,
    "minimum": 0,
    "maximum": 100,
    "pattern": "^[a-zA-Z]+$"
  },
  "validationErrors": {
    "isRequired": "此字段必填",
    "isEmail": "请输入有效的邮箱地址",
    "minLength": "至少输入 ${minLength} 个字符"
  }
}
```

### 自定义验证规则

```json
{
  "type": "form",
  "rules": [
    {
      "name": "passwordMatch",
      "message": "两次输入的密码不一致",
      "rule": function(data) {
        return data.password === data.confirmPassword;
      }
    },
    {
      "name": "startBeforeEnd",
      "message": "开始时间必须早于结束时间",
      "rule": function(data) {
        return new Date(data.startTime) < new Date(data.endTime);
      }
    }
  ],
  "body": [
    { "type": "input-password", "name": "password", "label": "密码" },
    { "type": "input-password", "name": "confirmPassword", "label": "确认密码" },
    { "type": "input-datetime", "name": "startTime", "label": "开始时间" },
    { "type": "input-datetime", "name": "endTime", "label": "结束时间" }
  ]
}
```

### 异步验证

```json
{
  "type": "input-text",
  "name": "username",
  "label": "用户名",
  "validations": {
    "minLength": 3
  },
  "validity": {
    "url": "/api/check/username",
    "method": "post",
    "data": {
      "username": "${username}"
    }
  }
}
```

### 必填校验

```json
{
  "type": "input-text",
  "name": "title",
  "label": "标题",
  "required": true,
  "requiredOn": "data.type === 'article'"
}
```

---

## Combo 组合输入

### 基础组合

```json
{
  "type": "combo",
  "name": "contacts",
  "label": "联系人",
  "multiple": true,
  "addable": true,
  "editable": true,
  "items": [
    { "type": "input-text", "name": "name", "placeholder": "姓名" },
    { "type": "input-text", "name": "phone", "placeholder": "电话" }
  ]
}
```

### 表格形式组合

```json
{
  "type": "combo",
  "name": "members",
  "label": "团队成员",
  "multiple": true,
  "addable": true,
  "removable": true,
  "tabsMode": true,
  "items": [
    { "type": "input-text", "name": "name", "label": "姓名" },
    { "type": "select", "name": "role", "label": "角色", "options": [{"label": "组长", "value": "leader"}, {"label": "成员", "value": "member"}] },
    { "type": "input-email", "name": "email", "label": "邮箱" }
  ]
}
```

### 卡片形式组合

```json
{
  "type": "combo",
  "name": "products",
  "label": "商品列表",
  "multiple": true,
  "addable": true,
  "draggable": true,
  "type": "cards",
  "card": {
    "body": [
      { "type": "input-text", "name": "name", "label": "商品名称" },
      { "type": "input-number", "name": "price", "label": "价格" },
      { "type": "input-number", "name": "quantity", "label": "数量" }
    ]
  }
}
```

---

## 文件上传

### 图片上传

```json
{
  "type": "input-image",
  "name": "avatar",
  "label": "头像",
  "accept": ".jpg,.png,.gif",
  "maxSize": 5242880,
  "limit": 1,
  "receiver": {
    "method": "post",
    "url": "/api/upload"
  },
  "crop": true,
  "cropRate": 1
}
```

### 多图片上传

```json
{
  "type": "input-image",
  "name": "images",
  "label": "图片集",
  "multiple": true,
  "maxLength": 9,
  "limit": 9,
  "receiver": "/api/upload/multiple"
}
```

### 文件上传

```json
{
  "type": "input-file",
  "name": "document",
  "label": "上传文档",
  "accept": ".pdf,.doc,.docx,.xls,.xlsx",
  "maxSize": 10485760,
  "receiver": {
    "method": "post",
    "url": "/api/upload"
  }
}
```

### 拖拽上传

```json
{
  "type": "input-file",
  "name": "files",
  "label": "拖拽上传",
  "drag": true,
  "multiple": true,
  "receiver": "/api/upload"
}
```

### 上传 API 响应格式

```json
{
  "status": 0,
  "msg": "上传成功",
  "data": {
    "filename": "image.jpg",
    "url": "https://example.com/uploads/image.jpg"
  }
}
```

---

## 完整示例

```json
{
  "type": "page",
  "title": "用户注册",
  "body": {
    "type": "form",
    "mode": "horizontal",
    "api": "post:/api/register",
    "redirect": "/login",
    "body": [
      {
        "type": "input-text",
        "name": "username",
        "label": "用户名",
        "required": true,
        "validations": {
          "minLength": 3,
          "maxLength": 20
        },
        "placeholder": "3-20位字母、数字或下划线"
      },
      {
        "type": "input-email",
        "name": "email",
        "label": "邮箱",
        "required": true,
        "validations": {
          "isEmail": true
        }
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
        "type": "input-password",
        "name": "confirmPassword",
        "label": "确认密码",
        "required": true,
        "validations": {
          "equalsField": "password"
        },
        "validationErrors": {
          "equalsField": "两次输入的密码不一致"
        }
      },
      {
        "type": "select",
        "name": "gender",
        "label": "性别",
        "options": [
          { "label": "男", "value": "male" },
          { "label": "女", "value": "female" },
          { "label": "保密", "value": "secret" }
        ]
      },
      {
        "type": "input-date",
        "name": "birthday",
        "label": "生日"
      },
      {
        "type": "radios",
        "name": "agree",
        "label": "",
        "options": [
          { "label": "我已阅读并同意《用户协议》和《隐私政策》", "value": "yes" }
        ],
        "validations": {
          "isRequired": true
        }
      }
    ],
    "buttons": [
      { "type": "reset", "label": "重置" },
      { "type": "submit", "label": "注册", "level": "primary" }
    ]
  }
}
```
