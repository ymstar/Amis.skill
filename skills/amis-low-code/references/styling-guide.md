# Amis 样式定制指南

## 主题系统

### 内置主题

Amis 提供了多个内置主题：

```html
<!-- 默认蓝色主题 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">

<!-- 侧边栏深色主题 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/akan.css" rel="stylesheet">

<!-- 经典灰色主题 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/classic.css" rel="stylesheet">

<!-- 干练深蓝主题 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/antd.css" rel="stylesheet">
```

### 主题切换

```javascript
// 方式1：直接引入主题CSS
import 'amis/lib/themes/cxd.css';

// 方式2：运行时切换
const theme = 'cxd'; // cxd, akan, classic, antd
amisRequire('amis').theme = theme;
```

---

## CSS类名覆盖

### 常用类名

| 类名 | 说明 |
|------|------|
| `b-d-inline-block` | 行内块元素 |
| `b-d-flex` | Flex布局 |
| `b-m-0` | 清除外边距 |
| `b-p-0` | 清除内边距 |
| `b-w-full` | 100%宽度 |
| `b-h-full` | 100%高度 |
| `text-center` | 居中文字 |
| `text-right` | 右对齐文字 |
| `text-primary` | 主色调文字 |
| `text-success` | 成功色文字 |
| `text-danger` | 危险色文字 |
| `text-warning` | 警告色文字 |
| `bg-primary` | 主色调背景 |
| `bg-success` | 成功色背景 |
| `bg-danger` | 危险色背景 |

### 尺寸类名

| 类名 | 说明 |
|------|------|
| `w-xs` | 极小宽度 |
| `w-sm` | 小宽度 |
| `w-md` | 中等宽度 |
| `w-lg` | 大宽度 |
| `w-xl` | 极大宽度 |
| `w-px-300` | 固定300px |
| `w-px-500` | 固定500px |

### 间距类名

| 类名 | 说明 |
|------|------|
| `m-t-sm` | 上边距 |
| `m-b-sm` | 下边距 |
| `m-l-sm` | 左边距 |
| `m-r-sm` | 右边距 |
| `p-t-sm` | 上内边距 |
| `p-b-sm` | 下内边距 |
| `p-l-sm` | 左内边距 |
| `p-r-sm` | 右内边距 |

### 颜色类名

| 类名 | 说明 |
|------|------|
| `label-default` | 默认灰色 |
| `label-primary` | 主色蓝色 |
| `label-success` | 成功绿色 |
| `label-info` | 信息蓝色 |
| `label-warning` | 警告橙色 |
| `label-danger` | 危险红色 |

---

## 行内样式配置

### 直接使用style属性

```json
{
  "type": "container",
  "style": {
    "padding": "20px",
    "background": "#f5f5f5",
    "borderRadius": "8px"
  },
  "body": "内容"
}
```

### 响应式样式

```json
{
  "type": "div",
  "style": {
    "width": "100%",
    "@md": {
      "width": "50%"
    },
    "@lg": {
      "width": "33.33%"
    }
  }
}
```

---

## 响应式设计

### 断点说明

| 断点 | 说明 | 屏幕宽度 |
|------|------|----------|
| xs | 极小屏幕 | < 768px |
| sm | 小屏幕 | 768px - 992px |
| md | 中等屏幕 | 992px - 1200px |
| lg | 大屏幕 | > 1200px |

### Grid响应式

```json
{
  "type": "grid",
  "columns": [
    {
      "xs": 24,
      "sm": 12,
      "md": 8,
      "lg": 6,
      "body": "响应式列"
    }
  ]
}
```

### Flex响应式

```json
{
  "type": "flex",
  "items": [
    {
      "xs": 24,
      "md": 12,
      "lg": 8,
      "body": "响应式项"
    }
  ]
}
```

---

## 常见UI定制场景

### 卡片样式

```json
{
  "type": "card",
  "className": "border-0 shadow",
  "headerClassName": "bg-primary text-white",
  "bodyClassName": "p-20"
}
```

### 表格样式

```json
{
  "type": "crud",
  "className": "table-hover",
  "columns": [
    {
      "name": "name",
      "label": "姓名",
      "className": "font-bold",
      "style": {
        "color": "#333"
      }
    }
  ]
}
```

### 表单样式

```json
{
  "type": "form",
  "mode": "horizontal",
  "className": "form-horizontal",
  "body": [
    {
      "type": "input-text",
      "name": "name",
      "label": "姓名",
      "labelClassName": "text-right font-bold",
      "inputClassName": "border-primary"
    }
  ]
}
```

### 按钮样式

```json
{
  "type": "button",
  "label": "自定义按钮",
  "level": "default",
  "className": "custom-btn",
  "size": "sm"
}
```

---

## 自定义CSS

### 全局样式覆盖

```html
<style>
  /* 覆盖主题色 */
  :root {
    --primary: #1890ff;
  }
  
  /* 自定义按钮样式 */
  .custom-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
    border-radius: 20px;
  }
  
  /* 自定义表格样式 */
  .amis-grid .th,
  .amis-grid .td {
    padding: 12px 16px;
  }
</style>
```

### 组件级别覆盖

```json
{
  "type": "page",
  "body": {
    "type": "crud",
    "className": "custom-crud",
    "style": {
      "--header-bg": "#f8f9fa"
    }
  }
}
```

---

## CSS变量

### 可覆盖的变量

```css
:root {
  /* 主题色 */
  --primary: #3b82f6;
  --primary-hover: #2563eb;
  --primary-light: #dbeafe;
  
  /* 文字颜色 */
  --text-color: #374151;
  --text-color-secondary: #6b7280;
  
  /* 边框颜色 */
  --border-color: #e5e7eb;
  
  /* 背景色 */
  --bg-color: #ffffff;
  --bg-gray: #f9fafb;
  
  /* 圆角 */
  --border-radius: 6px;
  
  /* 阴影 */
  --box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
  
  /* 间距 */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
}
```

---

## 动画效果

### 过渡动画

```json
{
  "type": "container",
  "className": "transition-all duration-300",
  "body": "内容"
}
```

### 动画类名

| 类名 | 说明 |
|------|------|
| `invisible` | 不可见 |
| `infinite` | 无限循环 |
| `fade-in` | 淡入 |
| `fade-out` | 淡出 |
| `zoom-in` | 放大 |
| `spin` | 旋转 |

### 自定义动画

```css
@keyframes slideIn {
  from {
    transform: translateY(-20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.slide-in {
  animation: slideIn 0.3s ease-out;
}
```

---

## 深色模式

### 基础配置

```html
<html data-theme="dark">
  <link href="amis-dark.css" rel="stylesheet">
</html>
```

### 手动切换

```javascript
document.documentElement.setAttribute('data-theme', 'dark');
document.documentElement.setAttribute('data-theme', 'light');
```

### CSS变量方式

```css
[data-theme="dark"] {
  --bg-color: #1f2937;
  --text-color: #f3f4f6;
  --border-color: #374151;
}
```

---

## 阴影效果

### 预设阴影

| 类名 | 说明 |
|------|------|
| `shadow-sm` | 小阴影 |
| `shadow` | 默认阴影 |
| `shadow-md` | 中等阴影 |
| `shadow-lg` | 大阴影 |
| `shadow-xl` | 极大阴影 |

### 自定义阴影

```css
.custom-shadow {
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 
              0 4px 6px -4px rgb(0 0 0 / 0.1);
}
```

---

## 边框样式

### 边框类名

| 类名 | 说明 |
|------|------|
| `border` | 全边框 |
| `border-top` | 上边框 |
| `border-bottom` | 下边框 |
| `border-left` | 左边框 |
| `border-right` | 右边框 |
| `border-0` | 无边框 |

### 边框颜色

```json
{
  "type": "card",
  "className": "border border-primary"
}
```

---

## Flex布局辅助类

### 方向

| 类名 | 说明 |
|------|------|
| `flex-row` | 水平方向 |
| `flex-col` | 垂直方向 |

### 主轴对齐

| 类名 | 说明 |
|------|------|
| `justify-start` | 左对齐 |
| `justify-center` | 居中 |
| `justify-end` | 右对齐 |
| `justify-between` | 两端对齐 |
| `justify-around` | 环绕对齐 |

### 交叉轴对齐

| 类名 | 说明 |
|------|------|
| `items-start` | 顶部对齐 |
| `items-center` | 居中对齐 |
| `items-end` | 底部对齐 |
| `items-stretch` | 拉伸对齐 |

### Flex份数

| 类名 | 说明 |
|------|------|
| `flex-1` | 占1份 |
| `flex-none` | 不参与flex |
| `flex-auto` | 自动大小 |

---

## 最佳实践

1. **优先使用类名**：能用内置类名解决的问题，不使用自定义CSS
2. **保持一致性**：自定义样式时保持与系统风格一致
3. **响应式优先**：移动端设计先行，考虑PC端增强
4. **主题变量**：优先使用CSS变量，便于主题切换
5. **避免深度选择器**：尽量不用 `!important` 和深度选择器
6. **组件隔离**：自定义样式添加命名空间避免污染
