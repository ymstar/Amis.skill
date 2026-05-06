# Amis 主题定制完整指南

## 目录
- [内置主题](#内置主题)
- [主题切换](#主题切换)
- [自定义主题色](#自定义主题色)
- [自定义 CSS](#自定义-css)
- [暗黑模式](#暗黑模式)
- [响应式配置](#响应式配置)
- [主题应用场景](#主题应用场景)

---

## 内置主题

Amis 提供三种内置主题：

| 主题 | 主题名 | 特点 | 适用场景 |
|------|--------|------|----------|
| C XD | `cxd` | 默认蓝色主题，功能完善 | 通用后台系统 |
| Ant Design | `antd` | 接近 Ant Design 风格 | 企业级应用 |
| Classic | `classic` | 经典简洁风格 | 老系统迁移 |

### 引入主题

```html
<!-- CDN 引入 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/antd.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/classic.css" rel="stylesheet">

<!-- 企业主题包 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cool.css" rel="stylesheet">
```

### 主题对比效果

**C XD 主题**：
```json
{
  "type": "page",
  "themeCss": {},
  "body": {
    "type": "button",
    "label": "主要按钮",
    "level": "primary"
  }
}
```

---

## 主题切换

### 静态主题配置

```html
<!DOCTYPE html>
<html>
<head>
  <!-- 选择一个主题 -->
  <link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/antd.css" rel="stylesheet">
</head>
<body>
  <div id="root"></div>
</body>
</html>
```

### 动态主题切换

```javascript
// 切换主题函数
function switchTheme(themeName) {
  // 移除旧主题
  const oldLink = document.getElementById('amis-theme');
  if (oldLink) {
    oldLink.remove();
  }
  
  // 添加新主题
  const link = document.createElement('link');
  link.id = 'amis-theme';
  link.rel = 'stylesheet';
  link.href = `https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/${themeName}.css`;
  document.head.appendChild(link);
  
  // 重新渲染页面
  renderApp();
}

// 使用
switchTheme('antd');  // 切换到 Ant Design 主题
switchTheme('cxd');   // 切换到 CXD 主题
switchTheme('classic'); // 切换到经典主题
```

### 基于配置的主题

```json
{
  "type": "page",
  "theme": "antd",
  "body": {}
}
```

---

## 自定义主题色

### 方式一：CSS 变量覆盖

```html
<style>
  :root {
    /* 主色调 */
    --primary: #1890ff;           /* 主色 */
    --primary-hover: #40a9ff;     /* 主色悬停 */
    --primary-active: #096dd9;    /* 主色激活 */
    
    /* 成功色 */
    --success: #52c41a;
    --success-hover: #73d13d;
    
    /* 警告色 */
    --warning: #faad14;
    --warning-hover: #ffc53d;
    
    /* 错误色 */
    --danger: #ff4d4f;
    --danger-hover: #ff7875;
    
    /* 文字颜色 */
    --text-color: #262626;
    --text-color-secondary: #8c8c8c;
    
    /* 边框颜色 */
    --border-color: #d9d9d9;
    
    /* 背景颜色 */
    --bg-color: #ffffff;
    --bg-color-secondary: #fafafa;
  }
</style>
```

### 方式二：通过 themeCss 配置

```json
{
  "type": "page",
  "themeCss": {
    "className": {
      "base": {
        "--color-primary": "#1890ff"
      }
    }
  },
  "body": {}
}
```

### 方式三：预设主题变量

```json
{
  "type": "page",
  "style": {
    "--color-brand-1": "#e6f7ff",
    "--color-brand-2": "#bae7ff",
    "--color-brand-3": "#91d5ff",
    "--color-brand-4": "#69c0ff",
    "--color-brand-5": "#40a9ff",
    "--color-brand-6": "#1890ff",
    "--color-brand-7": "#096dd9",
    "--color-brand-8": "#0050b3",
    "--color-brand-9": "#003a8c",
    "--color-brand-10": "#002766"
  },
  "body": {}
}
```

---

## 自定义 CSS

### 基础自定义

```json
{
  "type": "page",
  "css": {
    ".page-title": {
      "font-size": "24px",
      "font-weight": "bold",
      "color": "#333",
      "margin-bottom": "20px"
    },
    ".custom-card": {
      "border-radius": "12px",
      "box-shadow": "0 2px 12px rgba(0,0,0,0.1)"
    }
  },
  "body": {
    "type": "tpl",
    "tpl": "<h1 class='page-title'>自定义样式</h1>"
  }
}
```

### 全局 CSS 类

```json
{
  "type": "page",
  "className": "my-custom-page",
  "css": {
    "body": {
      "padding": "24px"
    }
  },
  "body": {}
}
```

### 组件级别自定义

```json
{
  "type": "button",
  "label": "自定义按钮",
  "className": "my-custom-button",
  "style": {
    "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "color": "#fff",
    "border-radius": "20px",
    "padding": "8px 24px"
  }
}
```

### 卡片样式

```json
{
  "type": "card",
  "className": "gradient-card",
  "header": {
    "title": "渐变卡片",
    "className": "gradient-header"
  },
  "css": {
    ".gradient-card": {
      "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
      "border-radius": "16px",
      "overflow": "hidden"
    },
    ".gradient-header": {
      "background": "transparent",
      "color": "#fff",
      "border-bottom": "none"
    }
  }
}
```

---

## 暗黑模式

### 方式一：使用 dark 主题

```html
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">
<!-- 可选：暗色变体 -->
<link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" data-theme="dark" rel="stylesheet">
```

### 方式二：系统跟随

```html
<!DOCTYPE html>
<html>
<head>
  <link id="theme-link" href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">
  <script>
    // 监听系统主题变化
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    function handleThemeChange(e) {
      const link = document.getElementById('theme-link');
      link.href = e.matches 
        ? 'https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css'
        : 'https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css';
    }
    mediaQuery.addEventListener('change', handleThemeChange);
  </script>
</head>
</html>
```

### 方式三：手动切换

```javascript
// 暗黑模式配置
const darkMode = {
  '--bg-color': '#141414',
  '--bg-color-secondary': '#1f1f1f',
  '--text-color': '#e8e8e8',
  '--text-color-secondary': '#a6a6a6',
  '--border-color': '#303030',
  '--primary': '#177ddc',
  '--primary-hover': '#4098ff',
  '--success': '#49aa19',
  '--warning': '#d89614',
  '--danger': '#dc4446'
};

function enableDarkMode() {
  const root = document.documentElement;
  Object.entries(darkMode).forEach(([key, value]) => {
    root.style.setProperty(key, value);
  });
}

function disableDarkMode() {
  const root = document.documentElement;
  root.style.removeProperty('--bg-color');
  // ... 移除其他自定义属性
}
```

### 方式四：基于 amis 配置

```json
{
  "type": "page",
  "data": {
    "isDarkMode": false
  },
  "body": [
    {
      "type": "button",
      "label": "切换主题",
      "onClick": "window.toggleDarkMode()"
    }
  ],
  "css": {
    "body": {
      "background-color": "${isDarkMode ? '#141414' : '#f5f6fa'}",
      "color": "${isDarkMode ? '#e8e8e8' : '#262626'}"
    }
  }
}
```

---

## 响应式配置

### 栅格断点

| 断点 | 宽度 | 说明 |
|------|------|------|
| `xs` | < 768px | 手机 |
| `sm` | ≥ 768px | 平板 |
| `md` | ≥ 992px | 小屏电脑 |
| `lg` | ≥ 1200px | 大屏电脑 |
| `xl` | ≥ 1600px | 超大屏 |

### 响应式布局

```json
{
  "type": "grid",
  "columns": [
    {
      "xs": 12,    // 手机：占满
      "sm": 12,    // 平板：占满
      "md": 8,     // 电脑：占 2/3
      "lg": 8,     // 大屏：占 2/3
      "body": { "type": "crud", "api": "/api/data" }
    },
    {
      "xs": 12,
      "sm": 12,
      "md": 4,
      "lg": 4,
      "body": { "type": "panel", "title": "侧边栏" }
    }
  ]
}
```

### 响应式隐藏

```json
{
  "type": "flex",
  "justify": "space-between",
  "items": [
    {
      "type": "tpl",
      "tpl": "仅电脑可见",
      "className": "hidden-xs hidden-sm"
    },
    {
      "type": "button",
      "label": "移动端按钮",
      "visibleOn": "matchMedia('(max-width: 768px)').matches"
    }
  ]
}
```

### 响应式表单

```json
{
  "type": "form",
  "mode": "${window.innerWidth < 768 ? 'normal' : 'horizontal'}",
  "labelWidth": "${window.innerWidth < 768 ? 'auto' : 120}",
  "body": []
}
```

### 响应式图表

```json
{
  "type": "chart",
  "height": "${window.innerWidth < 768 ? 250 : 400}",
  "config": {}
}
```

---

## 主题应用场景

### 场景一：多租户主题

```javascript
// 根据租户切换主题
function applyTenantTheme(tenantId) {
  const themes = {
    'tenant-a': { primary: '#1890ff', name: 'cxd' },
    'tenant-b': { primary: '#52c41a', name: 'cxd' },
    'tenant-c': { primary: '#722ed1', name: 'antd' }
  };
  
  const theme = themes[tenantId] || themes['tenant-a'];
  document.documentElement.style.setProperty('--primary', theme.primary);
}

// 使用
applyTenantTheme('tenant-b');
```

### 场景二：品牌定制

```json
{
  "type": "page",
  "brandName": "企业名称",
  "logo": "/images/logo.png",
  "css": {
    "body": {
      "--primary": "${brandColor}",
      "--primary-hover": "${brandColorHover}",
      "--primary-active": "${brandColorActive}"
    }
  },
  "body": {}
}
```

### 场景三：主题预览

```json
{
  "type": "page",
  "toolbar": [
    {
      "type": "dropdown-button",
      "label": "切换主题",
      "buttons": [
        {
          "type": "button",
          "label": "蓝色主题",
          "onClick": "window.setTheme('cxd')"
        },
        {
          "type": "button",
          "label": "绿色主题",
          "onClick": "window.setTheme('green')"
        },
        {
          "type": "button",
          "label": "紫色主题",
          "onClick": "window.setTheme('purple')"
        }
      ]
    }
  ],
  "body": {}
}
```

### 场景四：时间主题

```javascript
// 根据时间切换主题
function applyTimeBasedTheme() {
  const hour = new Date().getHours();
  
  if (hour >= 6 && hour < 18) {
    // 白天：浅色主题
    document.body.classList.remove('dark-mode');
  } else {
    // 夜晚：暗黑模式
    document.body.classList.add('dark-mode');
  }
}

// 页面加载时执行
applyTimeBasedTheme();

// 每小时检查一次
setInterval(applyTimeBasedTheme, 3600000);
```

---

## 完整示例

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Amis 主题定制示例</title>
  
  <!-- 引入默认主题 -->
  <link id="theme-link" href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/cxd.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/helper.css" rel="stylesheet">
  
  <style>
    /* 自定义样式 */
    :root {
      --custom-primary: #1890ff;
    }
    
    body.dark-mode {
      --bg-color: #141414;
      --bg-color-secondary: #1f1f1f;
      --text-color: #e8e8e8;
      --border-color: #303030;
    }
    
    .theme-switcher {
      position: fixed;
      top: 20px;
      right: 20px;
      z-index: 1000;
    }
  </style>
</head>
<body>
  <div class="theme-switcher">
    <button onclick="switchTheme('cxd')">默认蓝</button>
    <button onclick="switchTheme('antd')">AntD</button>
    <button onclick="switchTheme('classic')">经典</button>
    <button onclick="toggleDarkMode()">切换暗色</button>
  </div>
  
  <div id="root"></div>
  
  <script src="https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/sdk.js"></script>
  <script>
    // 主题切换
    function switchTheme(theme) {
      const link = document.getElementById('theme-link');
      link.href = `https://cdn.jsdelivr.net/npm/amis@6.13.0/lib/themes/${theme}.css`;
      renderApp();
    }
    
    // 暗色模式
    function toggleDarkMode() {
      document.body.classList.toggle('dark-mode');
    }
    
    const schema = {
      type: 'page',
      title: '主题定制示例',
      body: [
        {
          type: 'flex',
          justify: 'space-around',
          items: [
            {
              type: 'card',
              header: { title: '统计卡片 1' },
              body: '内容区域'
            },
            {
              type: 'card',
              header: { title: '统计卡片 2' },
              body: '内容区域'
            },
            {
              type: 'card',
              header: { title: '统计卡片 3' },
              body: '内容区域'
            }
          ]
        },
        {
          type: 'form',
          mode: 'horizontal',
          body: [
            { type: 'input-text', name: 'name', label: '用户名' },
            { type: 'input-email', name: 'email', label: '邮箱' },
            { type: 'select', name: 'role', label: '角色', options: [
              { label: '管理员', value: 'admin' },
              { label: '用户', value: 'user' }
            ]}
          ],
          buttons: [
            { type: 'submit', label: '提交', level: 'primary' }
          ]
        }
      ]
    };
    
    function renderApp() {
      amisRequire('amis/embed').embed('#root', schema);
    }
    
    renderApp();
  </script>
</body>
</html>
```
