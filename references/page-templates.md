# Amis 页面模板参考

## CRUD 管理页模板

### 标准用户管理页

```json
{
  "type": "page",
  "title": "用户管理",
  "subTitle": "管理系统用户",
  "body": {
    "type": "crud",
    "api": "/api/users",
    "syncLocation": false,
    "filter": {
      "title": "搜索条件",
      "body": [
        {
          "type": "input-text",
          "name": "keywords",
          "label": "关键字",
          "placeholder": "用户名/邮箱/手机号",
          "clearable": true
        },
        {
          "type": "select",
          "name": "status",
          "label": "状态",
          "placeholder": "全部",
          "options": [
            {"label": "启用", "value": "active"},
            {"label": "禁用", "value": "inactive"}
          ]
        },
        {
          "type": "input-date-range",
          "name": "createdAt",
          "label": "创建时间",
          "format": "YYYY-MM-DD"
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
        "width": 80,
        "sortable": true
      },
      {
        "name": "avatar",
        "label": "头像",
        "type": "image",
        "width": 60,
        "popOver": {
          "title": "查看大图",
          "body": "<img src='${avatar}' style='max-width:200px'/>"
        }
      },
      {
        "name": "username",
        "label": "用户名",
        "sortable": true,
        "searchable": true
      },
      {
        "name": "email",
        "label": "邮箱",
        "searchable": true
      },
      {
        "name": "phone",
        "label": "手机号"
      },
      {
        "name": "department",
        "label": "部门"
      },
      {
        "name": "role",
        "label": "角色",
        "type": "mapping",
        "map": {
          "admin": "<span class='label label-danger'>管理员</span>",
          "user": "<span class='label label-info'>普通用户</span>",
          "*": "${role}"
        }
      },
      {
        "name": "status",
        "label": "状态",
        "type": "switch",
        "trueValue": "active",
        "falseValue": "inactive",
        "quickEdit": {
          "type": "select",
          "options": [
            {"label": "启用", "value": "active"},
            {"label": "禁用", "value": "inactive"}
          ]
        }
      },
      {
        "name": "createdAt",
        "label": "创建时间",
        "type": "date",
        "format": "YYYY-MM-DD HH:mm",
        "sortable": true
      },
      {
        "type": "operation",
        "label": "操作",
        "width": 180,
        "buttons": [
          {
            "type": "button",
            "label": "编辑",
            "icon": "fa fa-pencil",
            "actionType": "drawer",
            "drawer": {
              "title": "编辑用户",
              "size": "md",
              "body": {
                "type": "form",
                "api": "put:/api/users/${id}",
                "body": [
                  {"type": "input-text", "name": "username", "label": "用户名", "required": true},
                  {"type": "input-email", "name": "email", "label": "邮箱", "required": true},
                  {"type": "input-text", "name": "phone", "label": "手机号"},
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
                    "type": "select",
                    "name": "role",
                    "label": "角色",
                    "options": [
                      {"label": "管理员", "value": "admin"},
                      {"label": "普通用户", "value": "user"}
                    ]
                  }
                ]
              },
              "actions": [
                {"type": "button", "label": "取消"},
                {"type": "submit", "label": "提交", "level": "primary"}
              ]
            }
          },
          {
            "type": "button",
            "label": "删除",
            "icon": "fa fa-trash",
            "level": "danger",
            "actionType": "ajax",
            "api": "delete:/api/users/${id}",
            "confirmText": "确定删除用户 ${username}？删除后无法恢复！"
          }
        ]
      }
    ],
    "bulkActions": [
      {
        "type": "button",
        "label": "批量启用",
        "actionType": "ajax",
        "api": "post:/api/users/batch-enable",
        "confirmText": "确定启用选中的 ${count} 个用户？"
      },
      {
        "type": "button",
        "label": "批量禁用",
        "level": "warning",
        "actionType": "ajax",
        "api": "post:/api/users/batch-disable",
        "confirmText": "确定禁用选中的 ${count} 个用户？"
      },
      {
        "type": "button",
        "label": "批量删除",
        "level": "danger",
        "actionType": "ajax",
        "api": "post:/api/users/batch-delete",
        "confirmText": "确定删除选中的 ${count} 个用户？删除后无法恢复！"
      }
    ],
    "headerToolbar": [
      {
        "type": "button",
        "label": "新增用户",
        "icon": "fa fa-plus",
        "level": "primary",
        "actionType": "dialog",
        "dialog": {
          "title": "新增用户",
          "size": "md",
          "body": {
            "type": "form",
            "api": "post:/api/users",
            "body": [
              {"type": "input-text", "name": "username", "label": "用户名", "required": true},
              {"type": "input-email", "name": "email", "label": "邮箱", "required": true},
              {"type": "input-password", "name": "password", "label": "密码", "required": true},
              {"type": "input-text", "name": "phone", "label": "手机号"},
              {
                "type": "select",
                "name": "department",
                "label": "部门",
                "options": [
                  {"label": "技术部", "value": "tech"},
                  {"label": "市场部", "value": "marketing"},
                  {"label": "运营部", "value": "operation"}
                ]
              }
            ]
          },
          "actions": [
            {"type": "button", "label": "取消"},
            {"type": "submit", "label": "提交", "level": "primary"}
          ]
        }
      },
      "bulkActions",
      "filter-toggler",
      "columns-toggler",
      {
        "type": "tpl",
        "tpl": "共 ${count} 条数据"
      }
    ],
    "footerToolbar": ["statistics", "switch-per-page", "pagination"]
  }
}
```

---

## 表单提交页模板

### 用户注册表单

```json
{
  "type": "page",
  "title": "用户注册",
  "body": {
    "type": "card",
    "className": "w-xxl",
    "body": {
      "type": "form",
      "mode": "horizontal",
      "api": "post:/api/register",
      "redirect": "/login",
      "messages": {
        "success": "注册成功！正在跳转登录页..."
      },
      "body": [
        {
          "type": "divider",
          "label": "账号信息"
        },
        {
          "name": "username",
          "type": "input-text",
          "label": "用户名",
          "required": true,
          "validations": {
            "minLength": 3,
            "maxLength": 20,
            "matchRegexp": "/^[a-zA-Z0-9_]+$/"
          },
          "validationErrors": {
            "minLength": "用户名至少3个字符",
            "maxLength": "用户名最多20个字符",
            "matchRegexp": "用户名只能包含字母、数字和下划线"
          },
          "placeholder": "3-20个字符，支持字母、数字和下划线"
        },
        {
          "name": "email",
          "type": "input-email",
          "label": "邮箱",
          "required": true,
          "placeholder": "请输入邮箱地址"
        },
        {
          "name": "password",
          "type": "input-password",
          "label": "密码",
          "required": true,
          "validations": {
            "minLength": 6,
            "maxLength": 20
          },
          "validationErrors": {
            "minLength": "密码至少6个字符",
            "maxLength": "密码最多20个字符"
          },
          "placeholder": "6-20个字符"
        },
        {
          "name": "confirmPassword",
          "type": "input-password",
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
          "name": "phone",
          "type": "input-text",
          "label": "手机号",
          "validations": {
            "isPhoneNumber": true
          },
          "placeholder": "请输入手机号"
        },
        {
          "type": "divider",
          "label": "基本信息"
        },
        {
          "name": "realName",
          "type": "input-text",
          "label": "真实姓名",
          "placeholder": "请输入真实姓名"
        },
        {
          "name": "gender",
          "type": "radios",
          "label": "性别",
          "options": [
            {"label": "男", "value": "male"},
            {"label": "女", "value": "female"},
            {"label": "保密", "value": "secret"}
          ],
          "value": "secret"
        },
        {
          "name": "birthday",
          "type": "input-date",
          "label": "出生日期",
          "maxDate": "${now}"
        },
        {
          "name": "department",
          "type": "select",
          "label": "部门",
          "options": [
            {"label": "请选择部门", "value": ""},
            {"label": "技术部", "value": "tech"},
            {"label": "市场部", "value": "marketing"},
            {"label": "运营部", "value": "operation"},
            {"label": "人事部", "value": "hr"}
          ]
        },
        {
          "name": "hobbies",
          "type": "checkboxes",
          "label": "兴趣爱好",
          "options": [
            {"label": "阅读", "value": "reading"},
            {"label": "运动", "value": "sports"},
            {"label": "音乐", "value": "music"},
            {"label": "旅行", "value": "travel"},
            {"label": "摄影", "value": "photo"}
          ]
        },
        {
          "name": "intro",
          "type": "textarea",
          "label": "个人简介",
          "placeholder": "简单介绍一下自己...",
          "rows": 4,
          "maxLength": 500
        },
        {
          "type": "divider",
          "label": "文件上传"
        },
        {
          "name": "avatar",
          "type": "input-image",
          "label": "头像",
          "accept": ".jpg,.png,.jpeg",
          "maxSize": 2097152,
          "crop": true,
          "cropRatio": "1:1",
          "receiver": "/api/upload"
        },
        {
          "name": "agreement",
          "type": "checkboxes",
          "label": "协议",
          "options": [
            {"label": "我已阅读并同意", "value": "agreed"}
          ],
          "required": true,
          "validationErrors": {
            "isRequired": "请勾选用户协议"
          }
        }
      ],
      "buttons": [
        {"type": "reset", "label": "重置"},
        {"type": "submit", "label": "立即注册", "level": "primary"}
      ]
    }
  }
}
```

---

## 数据看板页模板

### 销售数据仪表盘

```json
{
  "type": "page",
  "title": "销售数据看板",
  "subTitle": "实时监控销售数据",
  "initApi": {
    "method": "get",
    "url": "/api/dashboard/stats"
  },
  "body": [
    {
      "type": "flex",
      "justify": "space-around",
      "className": "mb-10",
      "items": [
        {
          "type": "card",
          "className": "text-center",
          "header": {"title": "今日销售额", "className": "bg-primary-light"},
          "body": {
            "type": "tpl",
            "tpl": "<span class='text-xxl text-primary font-bold'>¥${todaySales|number}</span>"
          }
        },
        {
          "type": "card",
          "className": "text-center",
          "header": {"title": "今日订单数", "className": "bg-success-light"},
          "body": {
            "type": "tpl",
            "tpl": "<span class='text-xxl text-success font-bold'>${todayOrders}</span>"
          }
        },
        {
          "type": "card",
          "className": "text-center",
          "header": {"title": "新增客户", "className": "bg-info-light"},
          "body": {
            "type": "tpl",
            "tpl": "<span class='text-xxl text-info font-bold'>${newCustomers}</span>"
          }
        },
        {
          "type": "card",
          "className": "text-center",
          "header": {"title": "客户总数", "className": "bg-warning-light"},
          "body": {
            "type": "tpl",
            "tpl": "<span class='text-xxl text-warning font-bold'>${totalCustomers}</span>"
          }
        }
      ]
    },
    {
      "type": "grid",
      "columns": [
        {
          "md": 8,
          "body": {
            "type": "panel",
            "title": "月度销售趋势",
            "headerClassName": "panel-primary",
            "body": {
              "type": "chart",
              "height": 350,
              "config": {
                "tooltip": {"trigger": "axis"},
                "legend": {"data": ["销售额", "订单数"]},
                "xAxis": {
                  "type": "category",
                  "data": ["1月", "2月", "3月", "4月", "5月", "6月"]
                },
                "yAxis": [
                  {"type": "value", "name": "销售额"},
                  {"type": "value", "name": "订单数"}
                ],
                "series": [
                  {
                    "name": "销售额",
                    "type": "bar",
                    "data": [8200, 9320, 9010, 12340, 18900, 21330]
                  },
                  {
                    "name": "订单数",
                    "type": "line",
                    "yAxisIndex": 1,
                    "data": [120, 200, 150, 80, 70, 110]
                  }
                ]
              }
            }
          }
        },
        {
          "md": 4,
          "body": {
            "type": "panel",
            "title": "销售占比",
            "headerClassName": "panel-success",
            "body": {
              "type": "chart",
              "height": 350,
              "config": {
                "tooltip": {"trigger": "item"},
                "legend": {"bottom": "0"},
                "series": [
                  {
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "avoidLabelOverlap": false,
                    "itemStyle": {"borderRadius": 10, "borderColor": "#fff", "borderWidth": 2},
                    "label": {"show": false},
                    "data": [
                      {"value": 1048, "name": "电子产品"},
                      {"value": 735, "name": "服装"},
                      {"value": 580, "name": "食品"},
                      {"value": 484, "name": "家居"},
                      {"value": 300, "name": "其他"}
                    ]
                  }
                ]
              }
            }
          }
        }
      ]
    },
    {
      "type": "grid",
      "columns": [
        {
          "md": 6,
          "body": {
            "type": "panel",
            "title": "热销商品 TOP 5",
            "headerClassName": "panel-warning",
            "body": {
              "type": "table",
              "api": "/api/dashboard/top-products",
              "columns": [
                {"name": "rank", "label": "排名", "width": 60},
                {"name": "name", "label": "商品名称"},
                {"name": "sales", "label": "销量", "type": "number"},
                {"name": "amount", "label": "销售额", "type": "number", "format": "¥${value}"}
              ]
            }
          }
        },
        {
          "md": 6,
          "body": {
            "type": "panel",
            "title": "最新订单",
            "headerClassName": "panel-info",
            "body": {
              "type": "crud",
              "api": "/api/dashboard/recent-orders",
              "columns": [
                {"name": "orderNo", "label": "订单号"},
                {"name": "customer", "label": "客户"},
                {"name": "amount", "label": "金额"},
                {
                  "name": "status",
                  "label": "状态",
                  "type": "mapping",
                  "map": {
                    "pending": "<span class='label label-warning'>待处理</span>",
                    "completed": "<span class='label label-success'>已完成</span>",
                    "cancelled": "<span class='label label-default'>已取消</span>"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  ]
}
```

---

## 详情展示页模板

### 订单详情页

```json
{
  "type": "page",
  "title": "订单详情",
  "toolbar": [
    {
      "type": "button",
      "label": "返回列表",
      "icon": "fa fa-arrow-left",
      "actionType": "link",
      "link": "/orders"
    },
    {
      "type": "button",
      "label": "打印",
      "icon": "fa fa-print",
      "actionType": "url",
      "url": "/api/orders/${id}/print"
    },
    {
      "type": "button",
      "label": "编辑",
      "icon": "fa fa-edit",
      "level": "primary",
      "actionType": "drawer",
      "drawer": {
        "title": "编辑订单",
        "body": {
          "type": "form",
          "api": "put:/api/orders/${id}",
          "body": [
            {"type": "input-text", "name": "orderNo", "label": "订单号", "disabled": true},
            {
              "type": "select",
              "name": "status",
              "label": "订单状态",
              "options": [
                {"label": "待支付", "value": "pending"},
                {"label": "已支付", "value": "paid"},
                {"label": "已发货", "value": "shipped"},
                {"label": "已完成", "value": "completed"},
                {"label": "已取消", "value": "cancelled"}
              ]
            },
            {"type": "textarea", "name": "remark", "label": "备注"}
          ]
        }
      }
    }
  ],
  "body": [
    {
      "type": "panel",
      "title": "基本信息",
      "body": {
        "type": "detail",
        "api": "/api/orders/${id}",
        "mode": "horizontal",
        "columns": [
          [
            {"name": "orderNo", "label": "订单编号"},
            {"name": "status", "label": "订单状态", "type": "mapping", "map": {
              "pending": "<span class='label label-warning'>待支付</span>",
              "paid": "<span class='label label-info'>已支付</span>",
              "shipped": "<span class='label label-primary'>已发货</span>",
              "completed": "<span class='label label-success'>已完成</span>",
              "cancelled": "<span class='label label-default'>已取消</span>"
            }},
            {"name": "createdAt", "label": "下单时间", "type": "date", "format": "YYYY-MM-DD HH:mm:ss"}
          ],
          [
            {"name": "totalAmount", "label": "订单金额", "type": "tpl", "tpl": "¥${totalAmount|number}"},
            {"name": "payAmount", "label": "实付金额", "type": "tpl", "tpl": "¥${payAmount|number}"},
            {"name": "payMethod", "label": "支付方式"}
          ]
        ]
      }
    },
    {
      "type": "panel",
      "title": "客户信息",
      "body": {
        "type": "detail",
        "api": "/api/orders/${id}",
        "mode": "horizontal",
        "columns": [
          [
            {"name": "customerName", "label": "客户姓名"},
            {"name": "customerPhone", "label": "联系电话"},
            {"name": "customerEmail", "label": "邮箱"}
          ],
          [
            {"name": "shippingAddress", "label": "收货地址", "className": "w-xxl"},
            {"name": "remark", "label": "订单备注"}
          ]
        ]
      }
    },
    {
      "type": "panel",
      "title": "商品明细",
      "body": {
        "type": "table",
        "api": "/api/orders/${id}/items",
        "columns": [
          {"name": "productName", "label": "商品名称"},
          {"name": "sku", "label": "SKU"},
          {"name": "price", "label": "单价", "type": "tpl", "tpl": "¥${price|number}"},
          {"name": "quantity", "label": "数量"},
          {"name": "subtotal", "label": "小计", "type": "tpl", "tpl": "¥${subtotal|number}"}
        ]
      }
    },
    {
      "type": "panel",
      "title": "操作日志",
      "body": {
        "type": "service",
        "api": "/api/orders/${id}/logs",
        "body": {
          "type": "list",
          "source": "${items}",
          "listItem": {
            "title": "${action}",
            "subTitle": "${operator} 于 ${createdAt}",
            "description": "${detail}"
          }
        }
      }
    }
  ]
}
```

---

## 登录注册页模板

### 统一登录注册页

```json
{
  "type": "page",
  "body": {
    "type": "flex",
    "justify": "center",
    "alignItems": "middle",
    "style": {"minHeight": "100vh", "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"},
    "items": [
      {
        "type": "card",
        "className": "w-px-700",
        "style": {"box-shadow": "0 25px 50px -12px rgba(0, 0, 0, 0.25)"},
        "body": {
          "type": "tabs",
          "tabs": [
            {
              "title": "账号登录",
              "body": {
                "type": "form",
                "api": "post:/api/login",
                "redirect": "/dashboard",
                "className": "p-20",
                "body": [
                  {
                    "type": "input-text",
                    "name": "username",
                    "label": "用户名/邮箱",
                    "required": true,
                    "placeholder": "请输入用户名或邮箱",
                    "clearable": true,
                    "validations": {
                      "minLength": 2
                    }
                  },
                  {
                    "type": "input-password",
                    "name": "password",
                    "label": "密码",
                    "required": true,
                    "placeholder": "请输入密码",
                    "revealPassword": true
                  },
                  {
                    "type": "checkbox",
                    "name": "remember",
                    "label": "",
                    "option": "记住我"
                  },
                  {
                    "name": "captcha",
                    "type": "input-text",
                    "label": "验证码",
                    "required": true,
                    "placeholder": "请输入验证码"
                  }
                ],
                "buttons": [
                  {"type": "submit", "label": "登录", "level": "primary", "actionType": "submit", "className": "w-full"}
                ]
              }
            },
            {
              "title": "手机快捷登录",
              "body": {
                "type": "form",
                "api": "post:/api/login/sms",
                "className": "p-20",
                "body": [
                  {
                    "type": "input-text",
                    "name": "phone",
                    "label": "手机号",
                    "required": true,
                    "placeholder": "请输入手机号"
                  },
                  {
                    "type": "input-group",
                    "name": "code",
                    "label": "验证码",
                    "body": [
                      {
                        "type": "input-text",
                        "name": "code",
                        "placeholder": "请输入验证码",
                        "required": true
                      },
                      {
                        "type": "button",
                        "label": "获取验证码",
                        "level": "default",
                        "actionType": "ajax",
                        "api": "post:/api/sms/send"
                      }
                    ]
                  }
                ],
                "buttons": [
                  {"type": "submit", "label": "登录", "level": "primary", "actionType": "submit", "className": "w-full"}
                ]
              }
            },
            {
              "title": "注册账号",
              "body": {
                "type": "form",
                "api": "post:/api/register",
                "redirect": "/login",
                "className": "p-20",
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
                    "type": "input-text",
                    "name": "phone",
                    "label": "手机号",
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
                    "type": "input-password",
                    "name": "confirmPassword",
                    "label": "确认密码",
                    "required": true,
                    "validations": {
                      "equalsField": "password"
                    }
                  }
                ],
                "buttons": [
                  {"type": "submit", "label": "注册", "level": "primary", "actionType": "submit", "className": "w-full"}
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

---

## 向导页模板

### 分步表单向导

```json
{
  "type": "page",
  "title": "新建项目",
  "body": {
    "type": "wizard",
    "api": "post:/api/projects",
    "redirect": "/projects",
    "steps": [
      {
        "title": "基本信息",
        "description": "填写项目基本信息",
        "body": {
          "type": "form",
          "mode": "horizontal",
          "body": [
            {
              "name": "name",
              "type": "input-text",
              "label": "项目名称",
              "required": true,
              "placeholder": "请输入项目名称"
            },
            {
              "name": "code",
              "type": "input-text",
              "label": "项目代码",
              "required": true,
              "placeholder": "请输入项目代码，用于标识",
              "validations": {
                "matchRegexp": "/^[a-z][a-z0-9_]*$/"
              },
              "validationErrors": {
                "matchRegexp": "代码只能包含小写字母、数字和下划线"
              }
            },
            {
              "name": "description",
              "type": "textarea",
              "label": "项目描述",
              "placeholder": "请输入项目描述",
              "rows": 4
            },
            {
              "name": "type",
              "type": "select",
              "label": "项目类型",
              "required": true,
              "options": [
                {"label": "Web应用", "value": "web"},
                {"label": "移动应用", "value": "mobile"},
                {"label": "桌面应用", "value": "desktop"},
                {"label": "其他", "value": "other"}
              ]
            }
          ]
        }
      },
      {
        "title": "团队配置",
        "description": "配置项目团队成员",
        "body": {
          "type": "form",
          "mode": "horizontal",
          "body": [
            {
              "name": "owner",
              "type": "select",
              "label": "项目负责人",
              "required": true,
              "source": "/api/users",
              "labelField": "name",
              "valueField": "id"
            },
            {
              "name": "members",
              "type": "combo",
              "label": "团队成员",
              "multiple": true,
              "items": [
                {
                  "type": "select",
                  "name": "userId",
                  "placeholder": "选择成员",
                  "source": "/api/users",
                  "labelField": "name",
                  "valueField": "id"
                },
                {
                  "type": "select",
                  "name": "role",
                  "placeholder": "选择角色",
                  "options": [
                    {"label": "管理员", "value": "admin"},
                    {"label": "开发者", "value": "developer"},
                    {"label": "测试", "value": "tester"},
                    {"label": "观察者", "value": "viewer"}
                  ]
                }
              ],
              "addable": true,
              "removable": true
            }
          ]
        }
      },
      {
        "title": "功能配置",
        "description": "配置项目功能选项",
        "body": {
          "type": "form",
          "mode": "horizontal",
          "body": [
            {
              "name": "visibility",
              "type": "radios",
              "label": "可见性",
              "options": [
                {"label": "公开", "value": "public"},
                {"label": "私有", "value": "private"},
                {"label": "团队内", "value": "team"}
              ],
              "value": "private"
            },
            {
              "name": "features",
              "type": "checkboxes",
              "label": "启用功能",
              "options": [
                {"label": "Wiki文档", "value": "wiki"},
                {"label": "问题跟踪", "value": "issues"},
                {"label": "CI/CD", "value": "cicd"},
                {"label": "代码审查", "value": "review"}
              ]
            },
            {
              "name": "isPublic",
              "type": "switch",
              "label": "允许公开访问"
            },
            {
              "name": "autoArchive",
              "type": "switch",
              "label": "自动归档"
            }
          ]
        }
      },
      {
        "title": "完成",
        "description": "确认并创建项目",
        "body": {
          "type": "service",
          "schemaApi": "get:/api/projects/preview"
        }
      }
    ]
  }
}
```

---

## 空状态模板

```json
{
  "type": "page",
  "title": "暂无数据",
  "body": {
    "type": "empty",
    "image": "${avatar || '/amis/static/empty.svg'}",
    "description": "暂无相关数据",
    "actions": [
      {
        "type": "button",
        "label": "刷新页面",
        "actionType": "reload",
        "target": "page"
      },
      {
        "type": "button",
        "label": "新增数据",
        "level": "primary",
        "actionType": "dialog",
        "dialog": {
          "title": "新增",
          "body": {
            "type": "form",
            "api": "post:/api/data",
            "body": []
          }
        }
      }
    ]
  }
}
```
