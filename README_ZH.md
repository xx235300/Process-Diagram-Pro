[[English](https://github.com/xx235300/process-diagram-pro/blob/main/README.md)] | 简体中文

# Process Diagram Pro

**专业化工工艺图生成器**

[![版本](https://img.shields.io/badge/version-2.0.0-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)]()
[![许可](https://img.shields.io/badge/license-MIT-orange.svg)]()

---

## 免责声明

**免责声明**：
本项目 99% 由 AI 自动生成，AI 所有者无任何编程背景。使用前请自行评估项目可行性。

## 简介

Process Diagram Pro 是一个基于 Python 的专业化工工艺图生成工具，支持：

- ✅ **PFD 工艺流程图** (Process Flow Diagram)
- ✅ **P&ID 管道仪表流程图** (Piping & Instrumentation Diagram)
- ✅ **系统架构图** (System Architecture Diagram)
- ✅ **数据流图** (Data Flow Diagram)

专为**化工/制药/食品/水处理**等过程工业设计，支持：
- 🌡️ **温度颜色渐变**（蓝 → 青 → 橙 → 红）
- 🔤 **中文字幕渲染**（自动字体适配）
- 🎨 **化工行业标准配色**
- ⚙️ **专业设备符号**（储罐/反应器/阀门/仪表完整符号）
- 🔗 **控制回路**（信号线连接展示）
- 🏗️ **背景网格**（可配置样式）
- 🔌 **更多阀门类型**（手动阀、止回阀）

---

## 安装

```bash
# 克隆仓库
git clone https://github.com/xx235300/process-diagram-pro.git
cd process-diagram-pro

# 安装依赖
pip install matplotlib pillow numpy
```

## 快速开始

### 生成 PFD 图

```python
from chem_diagram_v3 import PFDGenerator

gen = PFDGenerator()
gen.set_title("顺酐加氢制丁二酸酐")
gen.add_equipment({
    'type': 'tank',
    'x': 1, 'y': 3,
    'tag': 'T-101',
    'name': '顺酐原料罐'
})
gen.add_equipment({
    'type': 'reactor',
    'x': 5, 'y': 3,
    'tag': 'R-01',
    'name': '固定床反应器',
    'temp': 140,
    'pressure': 4.0
})
gen.add_flow({'from': 'T-101', 'to': 'R-01', 'label': '顺酐 + H₂', 'temp': 60})
gen.save('pfd_output.png')
```

### 生成 P&ID 图

```python
from chem_diagram_v3 import PIDGenerator

gen = PIDGenerator()
gen.set_title("P&ID 带控制回路与ESD")
gen.add_equipment({'type': 'reactor', 'x': 6, 'y': 3, 'tag': 'R-01', 'name': '反应器', 'temp': 140})
gen.add_valve({'type': 'esd', 'x': 3, 'y': 3, 'tag': 'XV-101'})
gen.add_valve({'type': 'control', 'x': 4.5, 'y': 3, 'tag': 'TV-101'})
gen.add_instrument({'type': 'TIC', 'x': 6, 'y': 5, 'tag': 'TIC-101'})
gen.add_signal({'from': 'TE-101', 'to': 'TIC-101'})  # 灰色虚线
gen.save('pid_output.png')
```

### 生成系统架构图

```python
from chem_diagram_v3 import ArchitectureGenerator

gen = ArchitectureGenerator(show_grid=True, grid_style='light')
gen.set_title("数字孪生系统架构")
gen.add_layer("设备层", ["温度传感器", "PLC", "边缘网关"])
gen.add_layer("边缘计算层", ["ESP32", "边缘代理"])
gen.add_layer("云平台层", ["MQTT", "AI模型"])
gen.add_layer("应用层", ["HMI监控面板", "报警系统"])
gen.save('arch_output.png')
```

## API 参考

### 设备类型

| type | 类 | 说明 | 支持参数 |
|------|-----|------|---------|
| `'tank'` | Tank | 储罐/原料罐 | name, tag, note |
| `'reactor'` | Reactor | 反应器（温度变色） | name, tag, temp, pressure, catalyst |
| `'heat_exchanger'` | HeatExchanger | 换热器/预热器/冷凝器 | name, tag, note |
| `'separator'` | Separator | 气液分离器 | name, tag, note |

### 阀门类型

| type | 类 | 符号形状 | 说明 |
|------|-----|---------|------|
| `'control'` | ControlValve | 风筝形 | 气动调节阀 |
| `'esd'` | ESDValve | 五边形（红色） | 紧急切断阀 |
| `'safety'` | SafetyValve | 半圆+三角 | 安全阀 |
| `'hand'` | HandValve | 菱形 | 手动阀 ⭐ 新增 |
| `'check'` | CheckValve | 三角形 | 止回阀 ⭐ 新增 |

### 仪表类型

| type | 类 | 说明 | 典型用途 |
|------|-----|------|---------|
| `'TIC'` | TIC | 温度指示控制器 | 温度控制回路 |
| `'PIC'` | PIC | 压力指示控制器 | 压力控制回路 |
| `'FIC'` | FIC | 流量指示控制器 | 流量控制回路 |
| `'TE'` | TE | 温度传感器 | 温度检测 |
| `'PE'` | PE | 压力传感器 | 压力检测 |
| `'FE'` | FE | 流量元件 | 流量测量 |
| `'PSH'` | PSH | 压力开关（高报） | 高压报警 |
| `'PSL'` | PSL | 压力开关（低报） | 低压报警 |
| `'AE'` | AE | 在线分析仪 | 成分分析 |

---

## 信号线增强（v2.0 新增）

信号线现在使用**灰色虚线**（行业标准）：

```python
gen.add_signal({'from': 'TE-101', 'to': 'TIC-101'})
# 渲染为：灰色虚线 + 方向标记
```

## 背景网格（v2.0 新增）

架构图支持可配置的背景网格：

```python
gen = ArchitectureGenerator(show_grid=True, grid_style='light')  # light, dark, colorful
```

---

## 目录结构

```
chem_diagram_v3/
├── __init__.py
├── core/
│   ├── canvas.py        # 画布核心
│   └── colors.py        # 颜色体系 + 温度渐变
├── devices/
│   ├── base.py          # 设备基类
│   ├── tanks.py         # 储罐
│   ├── reactors.py      # 反应器（温度变色）
│   ├── heat_exchangers.py # 换热器
│   ├── valves.py        # 阀门（5种类型）
│   └── instruments.py    # 仪表（9种类型）
├── pipelines/
│   └── pipe.py          # 管道、信号线（灰色虚线）、弯头
├── diagrams/
│   ├── pfd.py          # PFD生成器
│   ├── pid.py           # P&ID生成器
│   └── architecture.py  # 架构图生成器（网格支持）
└── fonts/
    └── loader.py       # 字体加载
```

---

## 常见问题

**问：中文显示为方块？**

答：系统会自动搜索可用中文字体。如仍有问题，请安装思源黑体（Source Han Sans）或阿里巴巴普惠体。

**问：能替代AutoCAD吗？**

答：本工具生成专业级P&ID用于方案汇报和投标展示，不能完全替代工程软件。

---

## 更新日志

### v2.0.0 (2026-03-29)

**新增功能：**
- ✨ **新增阀门类型**：HandValve（手动阀）、CheckValve（止回阀）
- ✨ **增强仪表标记**：TIC/PIC/FIC 使用醒目字母；PSH/PSL 使用三角箭头标记
- ✨ **信号线颜色改进**：改用灰色虚线（符合化工行业标准）
- ✨ **背景网格**：架构图支持可配置背景网格（light/dark/colorful）

**改进：**
- 阀门符号增强边框和标记点
- 管道箭头样式优化
- 仪表圆形双环设计
- 信号线添加方向标记

**Bug 修复：**
- 修复 `grid()` 函数 matplotlib 3.10+ 兼容性问题（`b=True` → `visible=True`）

**API 变更：**
```python
# 信号线颜色（旧 → 新）
# 旧：紫色 #9C27B0
# 新：灰色 #757575

# 架构图新增参数
gen = ArchitectureGenerator(show_grid=True, grid_style='light')
```

---

## 使用指南

没有编程经验，使用过程中遇到错误怎么办？
把使用指南云文档链接发给AI，让它帮你排查和解决问题。

**使用指南云文档**：[使用指南飞书云文档链接](https://my.feishu.cn/wiki/XPOVwSB8CivVPkkdFBgcZaCunIf)

---

## 免责声明

**免责声明**：
本项目 99% 由 AI 自动生成，AI 所有者无任何编程背景。使用前请自行评估项目可行性。

---

## 参考

- [matplotlib](https://matplotlib.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [P&ID设计规范](https://en.wikipedia.org/wiki/Piping_and_instrumentation_diagram)
