# Amis Chart 组件完整指南

## 目录
- [基础图表](#基础图表)
- [ECharts 配置](#echarts-配置)
- [常用图表类型](#常用图表类型)
- [数据源绑定](#数据源绑定)
- [实时数据刷新](#实时数据刷新)
- [响应式配置](#响应式配置)
- [图表交互](#图表交互)
- [完整示例](#完整示例)

---

## 基础图表

### 最小示例

```json
{
  "type": "page",
  "body": {
    "type": "chart",
    "config": {
      "title": { "text": "销售趋势" },
      "xAxis": { "type": "category", "data": ["周一", "周二", "周三", "周四", "周五"] },
      "yAxis": { "type": "value" },
      "series": [{ "data": [120, 200, 150, 80, 70] }]
    }
  }
}
```

### Chart 组件属性

```json
{
  "type": "chart",
  "name": "salesChart",
  "title": "销售数据",
  "config": {},
  // 数据源（可选）
  "dataSource": "/api/chart/data",
  // 图表类型映射（可选）
  "chartType": "line",
  // 高度
  "height": 400,
  // 转换函数
  "dataFilter": function(data) { return data.items; },
  // 加载状态
  "loading": false,
  // 占位文字
  "placeholder": "暂无数据"
}
```

---

## ECharts 配置

Amis 底层使用 ECharts，所有 ECharts 配置都通过 `config` 属性传入。

### config 基础结构

```json
{
  "type": "chart",
  "config": {
    // 标题
    "title": {
      "text": "主标题",
      "subtext": "副标题",
      "left": "center",
      "textStyle": { "color": "#333", "fontSize": 18 }
    },
    // 提示框
    "tooltip": {
      "trigger": "axis",
      "axisPointer": { "type": "cross" }
    },
    // 图例
    "legend": {
      "data": ["销量", "访问量"],
      "bottom": 0
    },
    // 工具栏
    "toolbox": {
      "feature": {
        "saveAsImage": {},
        "dataZoom": { "yAxisIndex": "none" },
        "magicType": { "type": ["line", "bar"] }
      }
    },
    // 网格
    "grid": {
      "left": "3%",
      "right": "4%",
      "bottom": "3%",
      "top": "10%",
      "containLabel": true
    },
    // X 轴
    "xAxis": {},
    // Y 轴
    "yAxis": {},
    // 系列
    "series": []
  }
}
```

---

## 常用图表类型

### 1. 折线图

```json
{
  "type": "chart",
  "config": {
    "title": { "text": "月度销售趋势" },
    "tooltip": { "trigger": "axis" },
    "legend": { "data": ["销售额", "订单量"], "bottom": 0 },
    "grid": { "left": "3%", "right": "4%", "bottom": "12%", "top": "10%", "containLabel": true },
    "xAxis": {
      "type": "category",
      "boundaryGap": false,
      "data": ["1月", "2月", "3月", "4月", "5月", "6月", "7月"]
    },
    "yAxis": [
      { "type": "value", "name": "销售额(万)", "axisLabel": { "formatter": "{value} 万" } },
      { "type": "value", "name": "订单量", "axisLabel": { "formatter": "{value}" } }
    ],
    "series": [
      {
        "name": "销售额",
        "type": "line",
        "smooth": true,
        "data": [120, 95, 160, 180, 210, 195, 220],
        "itemStyle": { "color": "#1890ff" },
        "areaStyle": {
          "color": {
            "type": "linear", "x": 0, "y": 0, "x2": 0, "y2": 1,
            "colorStops": [
              { "offset": 0, "color": "rgba(24,144,255,0.3)" },
              { "offset": 1, "color": "rgba(24,144,255,0.05)" }
            ]
          }
        }
      },
      {
        "name": "订单量",
        "type": "line",
        "smooth": true,
        "yAxisIndex": 1,
        "data": [450, 380, 520, 580, 650, 620, 700],
        "itemStyle": { "color": "#52c41a" }
      }
    ]
  }
}
```

### 2. 柱状图

```json
{
  "type": "chart",
  "config": {
    "title": { "text": "各部门业绩对比" },
    "tooltip": { "trigger": "axis", "axisPointer": { "type": "shadow" } },
    "legend": { "data": ["Q1", "Q2", "Q3"], "bottom": 0 },
    "grid": { "left": "3%", "right": "4%", "bottom": "12%", "top": "10%", "containLabel": true },
    "xAxis": {
      "type": "category",
      "data": ["技术部", "市场部", "销售部", "运营部"]
    },
    "yAxis": { "type": "value", "name": "业绩(万)" },
    "series": [
      {
        "name": "Q1",
        "type": "bar",
        "data": [120, 200, 150, 80],
        "itemStyle": { "color": "#1890ff" }
      },
      {
        "name": "Q2",
        "type": "bar",
        "data": [180, 250, 200, 120],
        "itemStyle": { "color": "#52c41a" }
      },
      {
        "name": "Q3",
        "type": "bar",
        "data": [150, 180, 250, 150],
        "itemStyle": { "color": "#faad14" }
      }
    ]
  }
}
```

### 3. 饼图

```json
{
  "type": "chart",
  "config": {
    "title": { "text": "用户来源分布", "left": "center" },
    "tooltip": { "trigger": "item", "formatter": "{b}: {c} ({d}%)" },
    "legend": { "orient": "vertical", "right": "5%", "top": "center" },
    "series": [
      {
        "type": "pie",
        "radius": ["40%", "70%"],
        "center": ["40%", "50%"],
        "avoidLabelOverlap": false,
        "itemStyle": {
          "borderRadius": 6,
          "borderColor": "#fff",
          "borderWidth": 2
        },
        "label": { "show": false },
        "emphasis": {
          "label": { "show": true, "fontSize": 14, "fontWeight": "bold" }
        },
        "data": [
          { "value": 1048, "name": "搜索引擎", "itemStyle": { "color": "#1890ff" } },
          { "value": 735, "name": "直接访问", "itemStyle": { "color": "#52c41a" } },
          { "value": 580, "name": "邮件营销", "itemStyle": { "color": "#faad14" } },
          { "value": 484, "name": "联盟广告", "itemStyle": { "color": "#f5222d" } },
          { "value": 300, "name": "视频广告", "itemStyle": { "color": "#722ed1" } }
        ]
      }
    ]
  }
}
```

### 4. 环形图

```json
{
  "type": "chart",
  "config": {
    "series": [
      {
        "type": "pie",
        "radius": ["55%", "70%"],
        "center": ["50%", "50%"],
        "avoidLabelOverlap": false,
        "label": {
          "show": true,
          "position": "outside",
          "formatter": "{b}\n{d}%"
        },
        "data": [
          { "value": 335, "name": "直接访问" },
          { "value": 310, "name": "邮件营销" },
          { "value": 234, "name": "联盟广告" },
          { "value": 135, "name": "视频广告" },
          { "value": 1548, "name": "搜索引擎" }
        ]
      }
    ]
  }
}
```

### 5. 散点图

```json
{
  "type": "chart",
  "config": {
    "title": { "text": "身高体重分布" },
    "tooltip": { "trigger": "item" },
    "grid": { "left": "3%", "right": "4%", "bottom": "3%", "top": "10%", "containLabel": true },
    "xAxis": { "type": "value", "name": "身高(cm)", "min": 150, "max": 200 },
    "yAxis": { "type": "value", "name": "体重(kg)", "min": 40, "max": 100 },
    "series": [
      {
        "type": "scatter",
        "symbolSize": 10,
        "data": [
          [170, 65], [175, 72], [168, 58], [180, 80], [165, 55],
          [172, 68], [178, 75], [162, 52], [185, 88], [170, 62]
        ],
        "itemStyle": { "color": "#1890ff" }
      }
    ]
  }
}
```

### 6. 雷达图

```json
{
  "type": "chart",
  "config": {
    "title": { "text": "用户画像对比" },
    "tooltip": {},
    "legend": { "data": ["用户A", "用户B"], "bottom": 0 },
    "radar": {
      "indicator": [
        { "name": "销售", "max": 100 },
        { "name": "管理", "max": 100 },
        { "name": "技术", "max": 100 },
        { "name": "市场", "max": 100 },
        { "name": "客服", "max": 100 }
      ],
      "center": ["50%", "55%"],
      "radius": "60%"
    },
    "series": [
      {
        "type": "radar",
        "data": [
          {
            "value": [85, 70, 60, 80, 75],
            "name": "用户A",
            "areaStyle": { "color": "rgba(24,144,255,0.3)" },
            "lineStyle": { "color": "#1890ff" }
          },
          {
            "value": [70, 85, 90, 65, 80],
            "name": "用户B",
            "areaStyle": { "color": "rgba(82,196,26,0.3)" },
            "lineStyle": { "color": "#52c41a" }
          }
        ]
      }
    ]
  }
}
```

### 7. 漏斗图

```json
{
  "type": "chart",
  "config": {
    "title": { "text": "转化漏斗" },
    "tooltip": { "trigger": "item", "formatter": "{b}: {c}%" },
    "series": [
      {
        "type": "funnel",
        "left": "10%",
        "top": 60,
        "bottom": 60,
        "width": "80%",
        "minSize": "0%",
        "maxSize": "100%",
        "sort": "descending",
        "gap": 2,
        "label": { "show": true, "position": "inside" },
        "labelLine": { "show": false },
        "data": [
          { "value": 100, "name": "访问", "itemStyle": { "color": "#1890ff" } },
          { "value": 80, "name": "注册", "itemStyle": { "color": "#36cfc9" } },
          { "value": 60, "name": "活跃", "itemStyle": { "color": "#52c41a" } },
          { "value": 30, "name": "付费", "itemStyle": { "color": "#faad14" } },
          { "value": 10, "name": "复购", "itemStyle": { "color": "#f5222d" } }
        ]
      }
    ]
  }
}
```

---

## 数据源绑定

### 静态数据

```json
{
  "type": "chart",
  "data": {
    "items": [
      { "category": "1月", "value": 120 },
      { "category": "2月", "value": 150 },
      { "category": "3月", "value": 180 }
    ]
  },
  "config": {
    "xAxis": { "type": "category", "data": "${items|picker:category}" },
    "series": [{ "data": "${items|picker:value}" }]
  }
}
```

### 动态 API 数据

```json
{
  "type": "chart",
  "source": {
    "method": "get",
    "url": "/api/sales/data"
  },
  "config": {
    "xAxis": { "type": "category", "data": "${categories}" },
    "series": [{ "data": "${salesData}" }]
  }
}
```

### 数据映射转换

```json
{
  "type": "chart",
  "source": "/api/chart/data",
  "dataFilter": function(data) {
    return {
      categories: data.items.map(item => item.month),
      sales: data.items.map(item => item.sales),
      orders: data.items.map(item => item.orders)
    };
  },
  "config": {
    "xAxis": { "type": "category", "data": "${categories}" },
    "series": [
      { "name": "销售额", "data": "${sales}" },
      { "name": "订单量", "data": "${orders}" }
    ]
  }
}
```

---

## 实时数据刷新

### 自动刷新

```json
{
  "type": "chart",
  "source": {
    "method": "get",
    "url": "/api/realtime/data",
    "interval": 3000
  },
  "config": {}
}
```

### 手动刷新

```json
{
  "type": "page",
  "toolbar": [
    {
      "type": "button",
      "label": "刷新图表",
      "actionType": "reload",
      "target": "realtimeChart"
    }
  ],
  "body": {
    "type": "chart",
    "name": "realtimeChart",
    "source": "/api/realtime/data",
    "config": {}
  }
}
```

---

## 响应式配置

### 响应式宽度

```json
{
  "type": "chart",
  "config": {
    "responsive": true,
    "maintainAspectRatio": false
  }
}
```

### 暗色主题

```json
{
  "type": "chart",
  "config": {
    "backgroundColor": "transparent",
    "title": { "textStyle": { "color": "#fff" } },
    "legend": { "textStyle": { "color": "#fff" } },
    "xAxis": { "axisLine": { "lineStyle": { "color": "#fff" } } },
    "yAxis": { "axisLine": { "lineStyle": { "color": "#fff" } } }
  }
}
```

---

## 图表交互

### 点击事件

```json
{
  "type": "chart",
  "name": "myChart",
  "config": {},
  "onClick": function(data) {
    console.log("点击了:", data);
    // 跳转到详情页
    window.location.href = "/detail/" + data.dataIndex;
  }
}
```

### Tooltip 回调

```json
{
  "type": "chart",
  "config": {
    "tooltip": {
      "trigger": "axis",
      "formatter": function(params) {
        var result = params[0].axisValue + "<br/>";
        params.forEach(function(item) {
          result += item.marker + item.seriesName + ": " + item.value + "<br/>";
        });
        return result;
      }
    }
  }
}
```

---

## 完整示例

### Dashboard 组合图表

```json
{
  "type": "page",
  "title": "数据看板",
  "body": [
    {
      "type": "grid",
      "columns": [
        {
          "md": 8,
          "body": {
            "type": "panel",
            "title": "月度销售趋势",
            "body": {
              "type": "chart",
              "height": 350,
              "config": {
                "tooltip": { "trigger": "axis", "axisPointer": { "type": "cross" } },
                "legend": { "data": ["销售额", "订单量"], "bottom": 0 },
                "grid": { "left": "3%", "right": "4%", "bottom": "12%", "top": "8%", "containLabel": true },
                "xAxis": {
                  "type": "category",
                  "data": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
                },
                "yAxis": [
                  { "type": "value", "name": "销售额(万)" },
                  { "type": "value", "name": "订单量" }
                ],
                "series": [
                  {
                    "name": "销售额",
                    "type": "line",
                    "smooth": true,
                    "data": [120, 95, 160, 180, 210, 195, 220, 250, 280, 310, 350, 380],
                    "areaStyle": { "color": { "type": "linear", "x": 0, "y": 0, "x2": 0, "y2": 1, "colorStops": [{ "offset": 0, "color": "rgba(24,144,255,0.3)" }, { "offset": 1, "color": "rgba(24,144,255,0.05)" }] } }
                  },
                  {
                    "name": "订单量",
                    "type": "line",
                    "smooth": true,
                    "yAxisIndex": 1,
                    "data": [450, 380, 520, 580, 650, 620, 700, 780, 850, 920, 1050, 1150]
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
            "title": "订单状态分布",
            "body": {
              "type": "chart",
              "height": 350,
              "config": {
                "tooltip": { "trigger": "item", "formatter": "{b}: {c} ({d}%)" },
                "legend": { "orient": "vertical", "right": "5%", "top": "center" },
                "series": [
                  {
                    "type": "pie",
                    "radius": ["45%", "70%"],
                    "center": ["40%", "50%"],
                    "avoidLabelOverlap": false,
                    "itemStyle": { "borderRadius": 6, "borderColor": "#fff", "borderWidth": 2 },
                    "label": { "show": false },
                    "emphasis": { "label": { "show": true, "fontSize": 12, "fontWeight": "bold" } },
                    "data": [
                      { "value": 28500, "name": "已完成", "itemStyle": { "color": "#52c41a" } },
                      { "value": 4200, "name": "进行中", "itemStyle": { "color": "#1890ff" } },
                      { "value": 2100, "name": "已取消", "itemStyle": { "color": "#ff4d4f" } },
                      { "value": 1042, "name": "待支付", "itemStyle": { "color": "#faad14" } }
                    ]
                  }
                ]
              }
            }
          }
        }
      ]
    }
  ]
}
```
