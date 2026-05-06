# Amis API对接指南

## API配置基础

### 简单字符串配置

最基础的API配置，直接使用URL字符串：

```json
{
  "api": "/api/users"
}
```

Amis会自动识别HTTP方法：
- `GET` 请求：`/api/users`
- `POST` 请求：`post:/api/users`
- `PUT` 请求：`put:/api/users/1`
- `DELETE` 请求：`delete:/api/users/1`

### 完整对象配置

```json
{
  "api": {
    "method": "get",
    "url": "/api/users",
    "data": {
      "page": "${page}",
      "pageSize": "${pageSize}",
      "keyword": "${keyword}"
    },
    "headers": {
      "Authorization": "Bearer ${token}"
    },
    "dataType": "json"
  }
}
```

**关键属性说明**：

| 属性 | 类型 | 说明 |
|------|------|------|
| method | string | HTTP方法：get/post/put/delete/patch |
| url | string | 接口地址，支持变量替换 |
| data | object | 请求数据，值可以是表达式 |
| headers | object | 请求头 |
| dataType | string | 数据格式：json/form/form-data |
| cache | number | 缓存时间（毫秒） |
| sendOn | string | 发送条件表达式 |
| adaptor | string/function | 响应适配器 |
| requestAdaptor | string/function | 请求适配器 |

---

## 标准响应格式

Amis要求后端返回标准JSON格式：

### 成功响应

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

### 失败响应

```json
{
  "status": 422,
  "msg": "参数验证失败",
  "data": null
}
```

**状态码约定**：
- `status: 0` 或无status字段 → 成功
- `status: 非0` → 失败

---

## 兼容多种后端格式

### 全局适配器配置

```javascript
const env = {
  fetcher: async (api) => {
    const response = await fetch(api.url, {
      method: api.method,
      headers: {
        'Content-Type': 'application/json',
        ...api.headers
      },
      body: api.data ? JSON.stringify(api.data) : undefined
    });
    
    const result = await response.json();
    
    // 统一转换为 amis 格式
    return {
      status: result.code === 0 ? 0 : result.code,
      msg: result.message || result.msg,
      data: result.data || result.result
    };
  }
};

amis.embed('#root', schema, env);
```

### 单接口适配器

```json
{
  "api": {
    "url": "/api/legacy/users",
    "adaptor": "function(payload, response, api) { return { status: 0, msg: 'ok', data: payload.result }; }"
  }
}
```

---

## CRUD组件API配置

### 标准CRUD配置

```json
{
  "type": "crud",
  "api": {
    "method": "get",
    "url": "/api/users",
    "data": {
      "page": "${page}",
      "pageSize": "${perPage}",
      "sortField": "${orderBy}",
      "sortOrder": "${orderDir}"
    }
  },
  "quickSaveApi": {
    "method": "put",
    "url": "/api/users/${id}",
    "data": {
      "&": "$$"
    }
  },
  "quickSaveItemApi": {
    "method": "put",
    "url": "/api/users/${id}",
    "data": {
      "&": "$$"
    }
  }
}
```

### 分页参数配置

```json
{
  "type": "crud",
  "api": "/api/users",
  "pageField": "page",
  "perPageField": "pageSize",
  "columns": []
}
```

### 带筛选的CRUD

```json
{
  "type": "crud",
  "api": "/api/users",
  "filter": {
    "body": [
      {"type": "input-text", "name": "keyword", "label": "关键字"},
      {"type": "select", "name": "status", "label": "状态", "options": [...]}
    ],
    "actions": [
      {"type": "submit", "label": "搜索", "level": "primary"},
      {"type": "reset", "label": "重置"}
    ]
  }
}
```

---

## 数据映射（Data Mapping）

### 基本语法

- `${fieldName}` - 获取字段值
- `${object.nested}` - 获取嵌套字段
- `${array.0}` - 获取数组元素
- `$$` - 获取整行数据
- `&` - 整个数据域

### 数据映射示例

```json
{
  "api": {
    "url": "/api/users",
    "data": {
      "ids": "${selectedItems|pick:id|join:,}",
      "filter": "${filter|json}"
    }
  }
}
```

### responseData 数据映射

```json
{
  "api": {
    "url": "/api/users",
    "responseData": {
      "items": "${users}",
      "total": "${count}"
    }
  }
}
```

---

## 请求适配器（Request Adaptor）

### 基本用法

```json
{
  "api": {
    "method": "post",
    "url": "/api/users",
    "requestAdaptor": "function(api) { return { ...api, data: { user: api.data } }; }"
  }
}
```

### 完整示例

```json
{
  "api": {
    "method": "post",
    "url": "/api/complex-endpoint",
    "requestAdaptor": "function(api) { var data = api.data; return { ...api, data: { user: { name: data.name, email: data.email, meta: { createTime: new Date().toISOString() } } }, headers: { ...api.headers, 'X-Custom-Header': 'value' } }; }"
  }
}
```

---

## 响应适配器（Response Adaptor）

### 适配老旧系统

```json
{
  "api": {
    "url": "/api/legacy/users",
    "adaptor": "function(payload, response, api) { if (payload.code === 200) { return { status: 0, msg: payload.message, data: payload.result }; } return { status: payload.code, msg: payload.message, data: null }; }"
  }
}
```

### 重组数据结构

```json
{
  "api": {
    "url": "/api/raw-data",
    "adaptor": "function(payload, response, api) { var items = payload.data.list || []; return { status: 0, msg: 'ok', data: { items: items.map(function(item) { return { id: item.ID, name: item.UserName, email: item.Email }; }), total: payload.data.totalCount } }; }"
  }
}
```

---

## 请求参数传递

### 表单提交参数

```json
{
  "type": "form",
  "api": {
    "method": "post",
    "url": "/api/users",
    "data": {
      "name": "${name}",
      "email": "${email}",
      "extra": "${extraData}"
    }
  }
}
```

### 批量操作参数

```json
{
  "bulkActions": [
    {
      "label": "批量删除",
      "actionType": "ajax",
      "api": {
        "method": "post",
        "url": "/api/users/batch-delete",
        "data": {
          "ids": "${selectedItems|pick:id}"
        }
      }
    }
  ]
}
```

---

## 联动刷新

### 刷新指定组件

```json
{
  "type": "form",
  "body": [
    {
      "type": "select",
      "name": "province",
      "label": "省份",
      "source": "/api/provinces",
      "onChange": {
        "actionType": "reload",
        "target": "city"
      }
    },
    {
      "type": "select",
      "name": "city",
      "label": "城市",
      "source": "/api/cities?provinceId=${province}"
    }
  ]
}
```

### 条件刷新

```json
{
  "type": "crud",
  "api": "/api/list",
  "reload": "list-component",
  "filter": {
    "body": [
      {
        "type": "select",
        "name": "category",
        "label": "分类",
        "options": [...],
        "onChange": {
          "actionType": "reload",
          "target": "list-component",
          "data": {
            "category": "${category}"
          }
        }
      }
    ]
  }
}
```

---

## 文件上传处理

### 基础配置

```json
{
  "type": "input-file",
  "name": "file",
  "label": "上传文件",
  "accept": ".jpg,.png,.pdf",
  "maxSize": 10485760,
  "receiver": {
    "method": "post",
    "url": "/api/upload",
    "adaptor": "function(payload, response, api) { return { status: 0, msg: 'ok', data: { value: payload.url, filename: payload.filename } }; }"
  }
}
```

### 图片上传带裁剪

```json
{
  "type": "input-image",
  "name": "avatar",
  "label": "头像",
  "crop": true,
  "cropRatio": "1:1",
  "receiver": {
    "method": "post",
    "url": "/api/upload/image"
  }
}
```

---

## 常见后端框架对接

### Spring Boot

后端返回格式：

```java
@RestController
public class UserController {
    
    @GetMapping("/api/users")
    public Map<String, Object> listUsers(Page page) {
        return Map.of(
            "status", 0,
            "msg", "success",
            "data", Map.of(
                "items", userService.list(page),
                "total", userService.count()
            )
        );
    }
    
    @PostMapping("/api/users")
    public Map<String, Object> createUser(@RequestBody User user) {
        userService.save(user);
        return Map.of("status", 0, "msg", "创建成功");
    }
}
```

### Express.js

```javascript
app.get('/api/users', (req, res) => {
  const { page = 1, pageSize = 10 } = req.query;
  
  res.json({
    status: 0,
    msg: 'success',
    data: {
      items: users.slice((page-1)*pageSize, page*pageSize),
      total: users.length
    }
  });
});

app.post('/api/users', (req, res) => {
  const user = { id: Date.now(), ...req.body };
  users.push(user);
  res.json({ status: 0, msg: '创建成功', data: user });
});
```

### Django

```python
from django.http import JsonResponse

def user_list(request):
    users = User.objects.all()
    return JsonResponse({
        'status': 0,
        'msg': 'success',
        'data': {
            'items': list(users.values()),
            'total': users.count()
        }
    })
```

---

## 认证与授权

### JWT Token

```json
{
  "api": {
    "url": "/api/users",
    "headers": {
      "Authorization": "Bearer ${token}"
    }
  }
}
```

### 带刷新令牌的配置

```javascript
const env = {
  fetcher: async (api) => {
    let token = localStorage.getItem('token');
    
    // 检查token是否过期
    if (isTokenExpired(token)) {
      const refreshToken = localStorage.getItem('refreshToken');
      const newToken = await refreshAccessToken(refreshToken);
      localStorage.setItem('token', newToken);
      token = newToken;
    }
    
    api.headers = api.headers || {};
    api.headers['Authorization'] = `Bearer ${token}`;
    
    return fetch(api.url, api).then(r => r.json());
  }
};
```

---

## 错误处理

### 全局错误处理

```javascript
const env = {
  fetcher: async (api) => {
    try {
      const response = await fetch(api.url, api);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }
      
      const data = await response.json();
      
      if (data.status !== 0) {
        throw new Error(data.msg || '请求失败');
      }
      
      return data;
    } catch (error) {
      return {
        status: 500,
        msg: error.message,
        data: null
      };
    }
  }
};
```

### 组件级错误处理

```json
{
  "type": "crud",
  "api": "/api/users",
  "onError": {
    "actionType": "toast",
    "level": "error",
    "msg": "${msg}"
  }
}
```

---

## 缓存策略

### 接口缓存

```json
{
  "api": {
    "url": "/api/config",
    "cache": 300000
  }
}
```

### 条件请求

```json
{
  "api": {
    "url": "/api/users",
    "sendOn": "this.shouldReload === true"
  }
}
```

---

## 最佳实践

1. **统一响应格式**：后端统一返回 `{status, msg, data}` 格式
2. **分页参数命名**：使用 `page` 和 `pageSize` 或 `page` 和 `perPage`
3. **使用适配器**：复杂接口使用适配器转换数据
4. **合理缓存**：静态数据设置缓存减少请求
5. **错误处理**：做好前后端的错误提示
6. **安全考虑**：敏感接口添加认证头
