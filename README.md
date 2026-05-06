<div align="center">

# 🏗️ Amis.skill

**百度Amis低代码框架的Agent技能包 — JSON驱动页面生成**

覆盖100+组件 · 3个可运行Demo · 完整组件指南 · API对接方案

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Amis](https://img.shields.io/badge/Amis-6.13.0-brightgreen.svg)
![Demo](https://img.shields.io/badge/Demo-3个可运行示例-orange.svg)

</div>

---

## 📖 项目简介

面向Agent的Amis低代码页面生成技能，帮助Agent通过JSON Schema快速生成后台管理页面。基于百度开源的Amis框架（v6.13.0），支持100+内置组件，覆盖常用业务场景。

### ✨ 核心价值

- 🎯 **JSON驱动** — 零前端代码，纯JSON配置生成页面
- 📦 **100+组件** — 表格、表单、图表、对话框等全覆盖
- 🖥️ **3个可运行Demo** — 双击HTML即可预览效果
- 📚 **完整指南** — 表格/表单/图表/联动/主题五大专题
- 🔧 **Schema验证** — Python脚本自动检查JSON配置
- 🔗 **API对接** — 后端数据交互完整方案

---

## 🌟 功能特性

### 组件覆盖

| 类别 | 组件 | 状态 |
|------|------|------|
| 📐 布局 | Flex/Grid/HBox/VBox/Panel/Tabs/Collapse | ✅ |
| 📦 容器 | Page/Container/Chart/IFrame | ✅ |
| 📝 表单 | Input/Select/Radio/Checkbox/Combo/FieldSet | ✅ |
| 📊 展示 | Table/CRUD/Cards/List/Detail | ✅ |
| 🔔 反馈 | Dialog/Drawer/Toast/Alert | ✅ |
| 📈 图表 | ECharts集成（折线/柱状/饼图等） | ✅ |

### 可运行Demo

| Demo | 说明 | 运行方式 |
|------|------|----------|
| 📋 CRUD管理页面 | 用户增删改查 + 搜索分页 + 批量操作 | 双击 `demos/crud-demo.html` |
| 📊 数据仪表盘 | 统计卡片 + ECharts图表 + 数据表格联动 | 双击 `demos/dashboard-demo.html` |
| 📝 复杂表单 | 验证 + 级联选择 + 文件上传 | 双击 `demos/form-demo.html` |

---

## 🚀 快速开始

### 方式一：运行Demo
```bash
# 克隆项目
git clone https://github.com/ymstar/Amis.skill.git
cd Amis.skill

# 双击打开Demo（无需后端，内置Mock数据）
open demos/crud-demo.html
open demos/dashboard-demo.html
open demos/form-demo.html
```

### 方式二：在Agent中使用
将skill.md和references目录加载到Agent的工作目录，Agent即可根据JSON Schema生成Amis页面。

### 方式三：Schema验证
```bash
# 验证你的Amis JSON配置
python3 scripts/amis-validator.py your-schema.json
```

---

## 📂 文档目录

| 文件 | 说明 |
|------|------|
| `skill.md` | 技能主文档（总览） |
| `demos/crud-demo.html` | CRUD管理页面Demo |
| `demos/dashboard-demo.html` | 数据仪表盘Demo |
| `demos/form-demo.html` | 复杂表单Demo |
| `references/table-guide.md` | 表格/CRUD完整指南 |
| `references/form-guide.md` | 表单完整指南 |
| `references/chart-guide.md` | 图表完整指南 |
| `references/linkage-guide.md` | 字段联动与条件渲染指南 |
| `references/theme-guide.md` | 主题定制完整指南 |
| `references/components.md` | 组件参考手册 |
| `references/page-templates.md` | 页面模板集合 |
| `references/api-integration.md` | API对接指南 |
| `references/styling-guide.md` | 样式定制指南 |
| `scripts/amis-validator.py` | Schema验证脚本 |

---

## 🧩 版本历史

### v1.1 (2026-05-06)
- ✨ 新增3个可直接运行的HTML Demo
- ✨ 新增表格/表单/图表三大组件完整指南
- ✨ 新增字段联动与条件渲染指南
- ✨ 新增主题定制完整指南

### v1.0 (2026-04-30)
- 🎉 初始版本发布
- 100+组件参考手册
- 6个页面模板
- API对接指南
- Schema验证脚本

---

## 🌐 虾评Skill

本技能已发布在虾评Skill平台：
👉 [Amis低代码页面生成 - 虾评Skill](https://xiaping.coze.site/skill/fcdc726b-e5e4-4cc2-814f-f5c5cc7e16e0)

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

---

<div align="center">

**JSON驱动，零代码生成页面** ✨

</div>
