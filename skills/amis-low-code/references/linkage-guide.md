# Amis 字段联动完整指南

## 目录
- [联动基础](#联动基础)
- [字段显隐联动](#字段显隐联动)
- [字段值联动](#字段值联动)
- [下拉选项动态加载](#下拉选项动态加载)
- [表单值联动计算](#表单值联动计算)
- [级联选择联动](#级联选择联动)
- [条件渲染](#条件渲染)
- [数据映射与转换](#数据映射与转换)

---

## 联动基础

### visibleOn / hiddenOn

控制字段是否显示：

```json
{
  "type": "form",
  "body": [
    {
      "type": "switch",
      "name": "isCompany",
      "label": "企业用户",
      "value": false
    },
    {
      "type": "input-text",
      "name": "companyName",
      "label": "公司名称",
      "visibleOn": "data.isCompany === true"
    }
  ]
}
```

### 常用表达式

| 表达式 | 说明 |
|--------|------|
| `data.field === 'value'` | 等于 |
| `data.field !== ''` | 不为空 |
| `data.field > 0` | 大于 |
| `data.count > data.limit` | 比较两个字段 |
| `data.items.length > 0` | 数组长度 |
| `data.field && data.field2` | 且 |
| `data.field || data.field2` | 或 |
| `!data.field` | 取反 |

---

## 字段显隐联动

### 简单显隐

```json
{
  "type": "form",
  "body": [
    {
      "type": "radios",
      "name": "accountType",
      "label": "账户类型",
      "options": [
        { "label": "个人", "value": "personal" },
        { "label": "企业", "value": "company" }
      ],
      "value": "personal"
    },
    {
      "type": "input-text",
      "name": "idCard",
      "label": "身份证号",
      "visibleOn": "data.accountType === 'personal'"
    },
    {
      "type": "input-text",
      "name": "businessLicense",
      "label": "营业执照",
      "visibleOn": "data.accountType === 'company'"
    }
  ]
}
```

### 多条件显隐

```json
{
  "type": "form",
  "body": [
    {
      "type": "radios",
      "name": "paymentMethod",
      "label": "支付方式",
      "options": [
        { "label": "微信支付", "value": "wechat" },
        { "label": "支付宝", "value": "alipay" },
        { "label": "银行卡", "value": "bankcard" }
      ]
    },
    {
      "type": "input-text",
      "name": "wechatAccount",
      "label": "微信号",
      "visibleOn": "data.paymentMethod === 'wechat'"
    },
    {
      "type": "input-text",
      "name": "alipayAccount",
      "label": "支付宝账号",
      "visibleOn": "data.paymentMethod === 'alipay'"
    },
    {
      "type": "input-text",
      "name": "bankCardNumber",
      "label": "银行卡号",
      "visibleOn": "data.paymentMethod === 'bankcard'"
    }
  ]
}
```

### 切换显示

```json
{
  "type": "form",
  "body": [
    {
      "type": "switch",
      "name": "enableDiscount",
      "label": "启用优惠",
      "value": false
    },
    {
      "type": "select",
      "name": "discountType",
      "label": "优惠类型",
      "options": [
        { "label": "折扣", "value": "percent" },
        { "label": "立减", "value": "amount" }
      ],
      "visibleOn": "data.enableDiscount === true"
    },
    {
      "type": "input-number",
      "name": "discountPercent",
      "label": "折扣比例",
      "suffix": "%",
      "visibleOn": "data.enableDiscount === true && data.discountType === 'percent'"
    },
    {
      "type": "input-number",
      "name": "discountAmount",
      "label": "立减金额",
      "prefix": "¥",
      "visibleOn": "data.enableDiscount === true && data.discountType === 'amount'"
    }
  ]
}
```

---

## 字段值联动

### 自动填充值

```json
{
  "type": "form",
  "body": [
    {
      "type": "input-text",
      "name": "username",
      "label": "用户名",
      "required": true
    },
    {
      "type": "input-email",
      "name": "email",
      "label": "邮箱",
      "required": true
    },
    {
      "type": "input-text",
      "name": "displayName",
      "label": "显示名称",
      "value": "${username}",
      "description": "默认与用户名一致，可自行修改"
    }
  ]
}
```

### 根据选择填充数据

```json
{
  "type": "form",
  "body": [
    {
      "type": "select",
      "name": "product",
      "label": "选择商品",
      "options": [
        { "label": "iPhone 15", "value": "iphone15", "price: 5999, stock: 100 },
        { "label": "MacBook Pro", "value": "macbook", "price: 14999, stock: 50 },
        { "label": "AirPods Pro", "value": "airpods", "price: 1899, stock: 200 }
      ]
    },
    {
      "type": "input-number",
      "name": "price",
      "label": "单价",
      "value": "${product.price}",
      "disabled": true
    },
    {
      "type": "input-number",
      "name": "stock",
      "label": "库存",
      "value": "${product.stock}",
      "disabled": true
    }
  ]
}
```

### 价格自动计算

```json
{
  "type": "form",
  "body": [
    {
      "type": "input-number",
      "name": "quantity",
      "label": "数量",
      "value": 1,
      "min": 1
    },
    {
      "type": "input-number",
      "name": "unitPrice",
      "label": "单价",
      "value": 100,
      "min": 0
    },
    {
      "type": "input-number",
      "name": "discount",
      "label": "折扣",
      "value": 0,
      "suffix": "%",
      "min": 0,
      "max": 100
    },
    {
      "type": "input-number",
      "name": "totalPrice",
      "label": "总价",
      "value": "${unitPrice * quantity * (1 - discount / 100)}",
      "disabled": true
    }
  ]
}
```

---

## 下拉选项动态加载

### 根据选择加载选项

```json
{
  "type": "form",
  "body": [
    {
      "type": "select",
      "name": "province",
      "label": "省份",
      "source": {
        "method": "get",
        "url": "/api/regions/provinces"
      },
      "valueField": "id",
      "labelField": "name"
    },
    {
      "type": "select",
      "name": "city",
      "label": "城市",
      "source": {
        "method": "get",
        "url": "/api/regions/cities",
        "data": {
          "provinceId": "${province}"
        }
      },
      "visibleOn": "data.province"
    },
    {
      "type": "select",
      "name": "district",
      "label": "区县",
      "source": {
        "method": "get",
        "url": "/api/regions/districts",
        "data": {
          "cityId": "${city}"
        }
      },
      "visibleOn": "data.city"
    }
  ]
}
```

### 联动清空

当上级选择变化时，自动清空下级值：

```json
{
  "type": "form",
  "body": [
    {
      "type": "select",
      "name": "category1",
      "label": "一级分类",
      "options": [
        { "label": "电子产品", "value": "electronics" },
        { "label": "服装", "value": "clothing" }
      ],
      "onChange": "reset:category2,category3"
    },
    {
      "type": "select",
      "name": "category2",
      "label": "二级分类",
      "source": {
        "method": "get",
        "url": "/api/categories/sub",
        "data": { "parentId": "${category1}" }
      },
      "visibleOn": "data.category1"
    },
    {
      "type": "select",
      "name": "category3",
      "label": "三级分类",
      "source": {
        "method": "get",
        "url": "/api/categories/sub",
        "data": { "parentId": "${category2}" }
      },
      "visibleOn": "data.category2"
    }
  ]
}
```

### 动态过滤选项

```json
{
  "type": "form",
  "body": [
    {
      "type": "select",
      "name": "brand",
      "label": "品牌",
      "options": [
        { "label": "苹果", "value": "apple", "category: "electronics" },
        { "label": "三星", "value": "samsung", "category: "electronics" },
        { "label": "华为", "value": "huawei", "category: "electronics" },
        { "label": "耐克", "value": "nike", "category: "clothing" },
        { "label": "阿迪达斯", "value": "adidas", "category: "clothing" }
      ]
    },
    {
      "type": "select",
      "name": "product",
      "label": "商品",
      "source": {
        "method": "get",
        "url": "/api/products",
        "data": {
          "brand": "${brand}"
        }
      },
      "visibleOn": "data.brand"
    }
  ]
}
```

---

## 表单值联动计算

### 简单计算

```json
{
  "type": "form",
  "body": [
    {
      "type": "input-number",
      "name": "length",
      "label": "长度(cm)"
    },
    {
      "type": "input-number",
      "name": "width",
      "label": "宽度(cm)"
    },
    {
      "type": "input-number",
      "name": "height",
      "label": "高度(cm)"
    },
    {
      "type": "input-number",
      "name": "volume",
      "label": "体积",
      "value": "${length * width * height}",
      "disabled": true,
      "suffix": "cm³"
    }
  ]
}
```

### 复杂业务计算

```json
{
  "type": "form",
  "body": [
    {
      "type": "input-number",
      "name": "orderAmount",
      "label": "订单金额",
      "prefix": "¥",
      "value": 1000
    },
    {
      "type": "switch",
      "name": "isVip",
      "label": "VIP会员"
    },
    {
      "type": "select",
      "name": "coupon",
      "label": "使用优惠券",
      "options": [
        { "label": "无优惠券", "value": "none" },
        { "label": "9折券", "value": "percent10", "discount": 0.1 },
        { "label": "减50券", "value": "reduce50", "discount": 50 }
      ]
    },
    {
      "type": "input-number",
      "name": "discountAmount",
      "label": "优惠金额",
      "value": "${coupon === 'reduce50' ? 50 : (coupon !== 'none' ? orderAmount * 0.1 : 0)}",
      "disabled": true,
      "prefix": "¥"
    },
    {
      "type": "input-number",
      "name": "vipDiscount",
      "label": "会员折扣",
      "value": "${isVip ? orderAmount * 0.05 : 0}",
      "disabled": true,
      "prefix": "¥"
    },
    {
      "type": "divider"
    },
    {
      "type": "input-number",
      "name": "finalAmount",
      "label": "应付金额",
      "value": "${orderAmount - discountAmount - vipDiscount}",
      "disabled": true,
      "prefix": "¥"
    }
  ]
}
```

### 时间计算

```json
{
  "type": "form",
  "body": [
    {
      "type": "input-datetime",
      "name": "startTime",
      "label": "开始时间"
    },
    {
      "type": "input-datetime",
      "name": "endTime",
      "label": "结束时间"
    },
    {
      "type": "static",
      "name": "duration",
      "label": "持续时长",
      "tpl": "${Math.round((new Date(endTime) - new Date(startTime)) / 86400000)} 天"
    }
  ]
}
```

---

## 级联选择联动

### 基本级联

```json
{
  "type": "form",
  "body": [
    {
      "type": "cascader",
      "name": "location",
      "label": "所在地区",
      "options": [
        {
          "label": "北京",
          "value": "beijing",
          "children": [
            { "label": "东城区", "value": "dongcheng" },
            { "label": "西城区", "value": "xicheng" }
          ]
        },
        {
          "label": "广东",
          "value": "guangdong",
          "children": [
            {
              "label": "广州",
              "value": "guangzhou",
              "children": [
                { "label": "天河区", "value": "tianhe" },
                { "label": "越秀区", "value": "yuexiu" }
              ]
            }
          ]
        }
      ],
      "joinValues": true,
      "delimiter": "/"
    }
  ]
}
```

### 动态级联数据

```json
{
  "type": "cascader",
  "name": "categoryTree",
  "label": "商品分类",
  "source": {
    "method": "get",
    "url": "/api/categories/tree"
  },
  "value": "a/b/c",
  "joinValues": true,
  "delimiter": "/"
}
```

---

## 条件渲染

### 根据数据值显示不同组件

```json
{
  "type": "form",
  "body": [
    {
      "type": "radios",
      "name": "reportType",
      "label": "报告类型",
      "options": [
        { "label": "日报", "value": "daily" },
        { "label": "周报", "value": "weekly" },
        { "label": "月报", "value": "monthly" }
      ],
      "value": "daily"
    },
    {
      "type": "input-date",
      "name": "reportDate",
      "label": "报告日期",
      "visibleOn": "data.reportType === 'daily'"
    },
    {
      "type": "select",
      "name": "reportWeek",
      "label": "报告周次",
      "options": [
        { "label": "第1周", "value": 1 },
        { "label": "第2周", "value": 2 },
        { "label": "第3周", "value": 3 },
        { "label": "第4周", "value": 4 }
      ],
      "visibleOn": "data.reportType === 'weekly'"
    },
    {
      "type": "select",
      "name": "reportMonth",
      "label": "报告月份",
      "options": [
        { "label": "1月", "value": 1 },
        { "label": "2月", "value": 2 },
        { "label": "3月", "value": 3 },
        { "label": "4月", "value": 4 },
        { "label": "5月", "value": 5 },
        { "label": "6月", "value": 6 },
        { "label": "7月", "value": 7 },
        { "label": "8月", "value": 8 },
        { "label": "9月", "value": 9 },
        { "label": "10月", "value": 10 },
        { "label": "11月", "value": 11 },
        { "label": "12月", "value": 12 }
      ],
      "visibleOn": "data.reportType === 'monthly'"
    }
  ]
}
```

### 根据角色权限显示

```json
{
  "type": "form",
  "body": [
    {
      "type": "input-text",
      "name": "title",
      "label": "标题",
      "required": true
    },
    {
      "type": "textarea",
      "name": "content",
      "label": "内容",
      "required": true
    },
    {
      "type": "switch",
      "name": "isTop",
      "label": "置顶",
      "visibleOn": "data.userRole === 'admin' || data.userRole === 'editor'"
    },
    {
      "type": "switch",
      "name": "isHidden",
      "label": "隐藏",
      "visibleOn": "data.userRole === 'admin'"
    },
    {
      "type": "select",
      "name": "category",
      "label": "分类",
      "visibleOn": "data.userRole === 'admin'"
    }
  ]
}
```

### 动态表单内容

```json
{
  "type": "page",
  "initApi": "/api/form/config",
  "body": {
    "type": "form",
    "api": "post:/api/submit",
    "body": {
      "type": "service",
      "source": "${fields}",
      "body": {
        "type": "input-text",
        "name": "${item.name}",
        "label": "${item.label}",
        "required": "${item.required}",
        "visibleOn": "${item.visible}"
      }
    }
  }
}
```

---

## 数据映射与转换

### API 数据转换

```json
{
  "type": "crud",
  "api": {
    "method": "get",
    "url": "/api/users",
    "adaptor": function(payload, response, api) {
      // 转换后端数据格式
      return {
        status: 0,
        msg: 'ok',
        data: {
          total: payload.totalCount,
          items: payload.list.map(function(item) {
            return {
              id: item.userId,
              name: item.userName,
              email: item.contactEmail,
              status: item.isActive ? 'active' : 'inactive'
            };
          })
        }
      };
    }
  },
  "columns": []
}
```

### 数据过滤器

```json
{
  "type": "crud",
  "api": "/api/users",
  "dataFilter": function(data) {
    // 处理返回数据
    if (data.items) {
      data.items = data.items.map(function(item) {
        item.displayName = item.lastName + item.firstName;
        item.fullAddress = [item.province, item.city, item.district].join('');
        return item;
      });
    }
    return data;
  }
}
```

### 前端数据交互

```json
{
  "type": "form",
  "api": "post:/api/order",
  "body": [
    { "type": "input-text", "name": "productId", "label": "商品ID" },
    { "type": "input-number", "name": "quantity", "label": "数量" }
  ],
  "onFinish": function(e) {
    var formData = e.data;
    // 可以在提交前做额外处理
    console.log('提交数据:', formData);
    // 或者跳转到其他页面
    window.location.href = '/order/success?id=' + formData.id;
  }
}
```

---

## 完整联动示例

```json
{
  "type": "page",
  "title": "订单申请",
  "body": {
    "type": "form",
    "mode": "horizontal",
    "api": "post:/api/order",
    "body": [
      {
        "type": "radios",
        "name": "orderType",
        "label": "订单类型",
        "options": [
          { "label": "标准订单", "value": "standard" },
          { "label": "定制订单", "value": "custom" },
          { "label": "批量订单", "value": "bulk" }
        ],
        "value": "standard"
      },
      {
        "type": "select",
        "name": "product",
        "label": "选择产品",
        "source": "/api/products",
        "required": true
      },
      {
        "type": "grid",
        "columns": [
          {
            "md": 6,
            "body": [
              {
                "type": "input-number",
                "name": "quantity",
                "label": "数量",
                "value": 1,
                "min": 1
              },
              {
                "type": "input-number",
                "name": "unitPrice",
                "label": "单价",
                "value": "${product.price}",
                "disabled": true
              }
            ]
          },
          {
            "md": 6,
            "body": [
              {
                "type": "input-number",
                "name": "discount",
                "label": "折扣率",
                "suffix": "%",
                "value": 0,
                "max": 100,
                "visibleOn": "data.orderType === 'standard'"
              },
              {
                "type": "input-text",
                "name": "customRequirement",
                "label": "定制要求",
                "visibleOn": "data.orderType === 'custom'"
              },
              {
                "type": "input-number",
                "name": "minQuantity",
                "label": "最小起订量",
                "visibleOn": "data.orderType === 'bulk'"
              }
            ]
          }
        ]
      },
      {
        "type": "divider"
      },
      {
        "type": "static",
        "name": "totalPrice",
        "label": "订单金额",
        "tpl": "<strong class='text-danger'>¥ ${(unitPrice * quantity * (1 - discount / 100)).toFixed(2)}</strong>"
      },
      {
        "type": "textarea",
        "name": "remark",
        "label": "备注"
      }
    ],
    "buttons": [
      { "type": "submit", "label": "提交订单", "level": "primary" }
    ]
  }
}
```
