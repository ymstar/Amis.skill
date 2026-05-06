<div align="center">

# 🏗️ Amis.skill

**百度Amis低代码框架的Agent技能包 — JSON驱动页面生成**

覆盖100+组件 · 3个可运行Demo · 完整组件指南 · API对接方案

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Amis](https://img.shields.io/badge/Amis-6.13.0-brightgreen.svg)
![Demo](https://img.shields.io/badge/Demo-3个可运行示例-orange.svg)
[![npx compatible](https://img.shields.io/badge/npx-skills--compatible-green)](https://skills.sh/)

</div>

---

## 🚀 快速安装

### 方式一：通过 npx skills 安装（推荐）

```bash
# 查看技能详情
npx skills add ymstar/Amis.skill --list

# 安装到当前项目
npx skills add ymstar/Amis.skill

# 全局安装（所有AI助手共用）
npx skills add ymstar/Amis.skill -g -y
```

✅ 支持：**Claude Code、Cursor、Windsurf、Codex、OpenCode** 等

### 方式二：手动安装

```bash
# 克隆到 Claude Code 技能目录
git clone https://github.com/ymstar/Amis.skill.git ~/.claude/skills/amis-skill
```

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
- ⚡ **npx兼容** — 一条命令安装到所有AI编程助手

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
| 📝 复杂表单 | 级联选择 + 文件上传 + 表单验证 + 富文本 | 双击 `demos/form-demo.html` |

---

## 📁 目录结构

```
Amis.skill/
├── SKILL.md                    # 技能说明（npx识别必备）
├── demos/                      # 可运行示例
│   ├── crud-demo.html
│   ├── dashboard-demo.html
│   └── form-demo.html
├── references/                 # 参考文档
│   ├── amis-quickstart.md
│   ├── component-guide.md
│   ├── schema-reference.md
│   └── api-integration.md
├── scripts/                    # 工具脚本
│   └── validate_schema.py
└── README.md                   # 本文件
```

---

## 💡 使用方法

安装后，Agent会自动加载此技能。你可以这样使用：

> "用Amis生成一个订单管理后台，包含搜索、表格、新增编辑"
>
> "做一个数据仪表盘，显示销售额趋势和用户分布饼图"
>
> "生成一个企业注册表单，包含省市区级联选择和附件上传"

---

## 🔗 相关链接

- **Amis官方文档**：https://aisuda.bce.baidu.com/amis/zh-CN/docs/index
- **Skills CLI**：https://github.com/vercel-labs/skills
- **技能市场**：https://skills.sh/

---

## 📄 License

MIT License
