# Process Diagram Pro

[[English](https://github.com/xx235300/process-diagram-pro/blob/main/README.md)] | 简体中文

**专业化工工艺图生成器**

[![版本](https://img.shields.io/badge/version-3.0.0-blue.svg)]()
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
- 🌡️ **温度颜色渐变**（蓝 → 绿 → 橙 → 红）
- 🔤 **中文字幕渲染**（自动字体适配）
- 🎨 **化工行业标准配色**
- ⚙️ **专业设备符号**（储罐/反应器/阀门/仪表）
- 🔗 **控制回路信号线连接**

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
gen.add_instrument({'type': 'TIC', 'x': 6, 'y': 5, 'tag': 'TIC-101'})
gen.add_signal({'from': 'TE-101', 'to': 'TIC-101'})
gen.save('pid_output.png')
```

### 生成系统架构图

```python
from chem_diagram_v3 import ArchitectureGenerator

gen = ArchitectureGenerator()
gen.set_title("数字孪生系统架构")
gen.add_layer("设备层", ["温度传感器", "PLC", "边缘网关"])
gen.add_layer("边缘计算层", ["ESP32", "Edge Agent"])
gen.add_layer("云平台层", ["MQTT", "AI模型"])
gen.add_layer("应用层", ["HMI监控面板", "报警系统"])
gen.save('arch_output.png')
```

## API 参考

### 设备类型

| type | 类 | 说明 |
|------|-----|------|
| `'tank'` | Tank | 储罐/原料罐 |
| `'reactor'` | Reactor | 反应器 |
| `'heat_exchanger'` | HeatExchanger | 换热器/预热器/冷凝器 |
| `'separator'` | Separator | 分离器 |

### 阀门类型

| type | 类 | 说明 |
|------|-----|------|
| `'control'` | ControlValve | 调节阀（风筝形） |
| `'esd'` | ESDValve | ESD紧急切断阀（五边形） |
| `'safety'` | SafetyValve | 安全阀（圆形） |

### 仪表类型

| type | 类 | 说明 |
|------|-----|------|
| `'TIC'` | TIC | 温度指示控制器 |
| `'PIC'` | PIC | 压力指示控制器 |
| `'FIC'` | FIC | 流量指示控制器 |
| `'TE'` | TE | 温度传感器 |
| `'PE'` | PE | 压力传感器 |
| `'FE'` | FE | 流量元件 |

## 颜色体系

| 设备 | 颜色代码 | 用途 |
|------|---------|------|
| 🟦 储罐 | `#E8F4FD` | 淡蓝 |
| 🟧 换热器 | `#FFF3E0` | 淡橙 |
| 🟥 反应器 | `#FDE8E8` | 淡红 |
| 🟩 分离器 | `#E8F5E9` | 淡绿 |
| 🟪 泵 | `#F3E5F5` | 淡紫 |

### 温度渐变

```
0°C   → #0033FF 深蓝
40°C  → #00FFCC 青绿
80°C  → #FF6600 橙色
120°C → #FF0000 红色
```

## 目录结构

```
chem_diagram_v3/
├── __init__.py
├── core/
│   ├── canvas.py        # 画布核心
│   └── colors.py        # 颜色体系
├── devices/
│   ├── base.py          # 设备基类
│   ├── tanks.py         # 储罐
│   ├── reactors.py      # 反应器
│   ├── heat_exchangers.py # 换热器
│   ├── valves.py        # 阀门
│   └── instruments.py   # 仪表
├── pipelines/
│   └── pipe.py          # 管道/信号线
├── diagrams/
│   ├── pfd.py          # PFD生成器
│   ├── pid.py          # P&ID生成器
│   └── architecture.py # 架构图生成器
└── fonts/
    └── loader.py       # 字体加载
```

## 示例

参考 `examples/` 目录下的完整示例：
- `example_pfd.py` - PFD图生成
- `example_pid.py` - P&ID图生成
- `example_architecture.py` - 架构图生成

## 常见问题

**问：中文显示为方块怎么办？**

答：工具会自动搜索系统中可用的中文字体。如果仍有问题，请安装思源黑体（Source Han Sans）或阿里巴巴普惠体。

**问：能生成工程级P&ID图吗？**

答：本工具可生成专业级别的P&ID图用于方案汇报和投标展示，但不能完全替代AutoCAD/SmartPlant等工程软件。

---

没有编程经验，使用过程中遇到错误怎么办？
把使用指南云文档链接发给AI，让它帮你排查和解决问题。

**使用指南云文档**：[使用指南飞书云文档链接](https://my.feishu.cn/wiki/XPOVwSB8CivVPkkdFBgcZaCunIf)

## 免责声明

**免责声明**：
本项目 99% 由 AI 自动生成，AI 所有者无任何编程背景。使用前请自行评估项目可行性。

## 许可

MIT License

## 参考

- [matplotlib](https://matplotlib.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [P&ID设计规范](https://en.wikipedia.org/wiki/Piping_and_instrumentation_diagram)
