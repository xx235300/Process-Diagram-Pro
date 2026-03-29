# Process Diagram Pro

[English](./README.md) | [简体中文](https://github.com/xx235300/process-diagram-pro/blob/main/README_ZH.md)

**Professional PFD/P&ID Diagram Generator for Chemical Engineering**

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)]()
[![License](https://img.shields.io/badge/license-MIT-orange.svg)]()

---

## Disclaimer

**Disclaimer**:
This project is 99% AI-generated. The AI's owner has no programming background. Please evaluate the project's feasibility before use.


## Overview

Process Diagram Pro is a Python-based professional diagram generation tool for chemical/pharmaceutical/food process industries, featuring:

- ✅ **PFD** (Process Flow Diagram)
- ✅ **P&ID** (Piping & Instrumentation Diagram)  
- ✅ **System Architecture Diagram**
- ✅ **Data Flow Diagram**

## Features

- 🌡️ **Temperature-based color mapping** (Blue → Green → Orange → Red)
- 🔤 **Chinese font support** (Automatic fallback)
- 🎨 **Industry-standard color scheme**
- ⚙️ **Professional equipment symbols** (Tank, Reactor, Valve, Instrument)
- 🔗 **Control loop connections** (Signal lines)

## Installation

```bash
# Clone the repository
git clone https://github.com/xx235300/process-diagram-pro.git
cd process-diagram-pro

# Install dependencies
pip install matplotlib pillow numpy
```

## Quick Start

### Generate PFD

```python
from chem_diagram_v3 import PFDGenerator

gen = PFDGenerator()
gen.set_title("Maleic Anhydride Hydrogenation")
gen.add_equipment({
    'type': 'tank',
    'x': 1, 'y': 3,
    'tag': 'T-101',
    'name': 'Maleic Anhydride Tank'
})
gen.add_equipment({
    'type': 'reactor',
    'x': 5, 'y': 3,
    'tag': 'R-01',
    'name': 'Fixed Bed Reactor',
    'temp': 140,
    'pressure': 4.0
})
gen.add_flow({'from': 'T-101', 'to': 'R-01', 'label': 'MA + H₂', 'temp': 60})
gen.save('pfd_output.png')
```

### Generate P&ID

```python
from chem_diagram_v3 import PIDGenerator

gen = PIDGenerator()
gen.set_title("P&ID with Control Loops & ESD")
gen.add_equipment({'type': 'reactor', 'x': 6, 'y': 3, 'tag': 'R-01', 'name': 'Reactor', 'temp': 140})
gen.add_valve({'type': 'esd', 'x': 3, 'y': 3, 'tag': 'XV-101'})
gen.add_instrument({'type': 'TIC', 'x': 6, 'y': 5, 'tag': 'TIC-101'})
gen.add_signal({'from': 'TE-101', 'to': 'TIC-101'})
gen.save('pid_output.png')
```

### Generate Architecture Diagram

```python
from chem_diagram_v3 import ArchitectureGenerator

gen = ArchitectureGenerator()
gen.set_title("Digital Twin System Architecture")
gen.add_layer("Device Layer", ["Temperature Sensor", "PLC", "Edge Gateway"])
gen.add_layer("Edge Computing", ["ESP32", "Edge Agent"])
gen.add_layer("Cloud Platform", ["MQTT", "AI Model"])
gen.add_layer("Application", ["HMI Dashboard", "Alarm System"])
gen.save('arch_output.png')
```

## API Reference

### Equipment Types

| Type | Class | Description |
|------|-------|-------------|
| `'tank'` | Tank | Storage tank |
| `'reactor'` | Reactor | Fixed bed reactor |
| `'heat_exchanger'` | HeatExchanger | Heat exchanger / Preheater |
| `'separator'` | Separator | Gas-liquid separator |

### Valve Types

| Type | Class | Description |
|------|-------|-------------|
| `'control'` | ControlValve | Control valve (kite shape) |
| `'esd'` | ESDValve | Emergency shutdown valve (pentagon) |
| `'safety'` | SafetyValve | Safety valve (circle) |

### Instrument Types

| Type | Class | Description |
|------|-------|-------------|
| `'TIC'` | TIC | Temperature Indicator Controller |
| `'PIC'` | PIC | Pressure Indicator Controller |
| `'FIC'` | FIC | Flow Indicator Controller |
| `'TE'` | TE | Temperature Element |
| `'PE'` | PE | Pressure Element |
| `'FE'` | FE | Flow Element |

## Color Scheme

| Equipment | Color Code | Application |
|-----------|------------|------------|
| 🟦 Tank | `#E8F4FD` | Light blue |
| 🟧 Heat Exchanger | `#FFF3E0` | Light orange |
| 🟥 Reactor | `#FDE8E8` | Light red |
| 🟩 Separator | `#E8F5E9` | Light green |
| 🟪 Pump | `#F3E5F5` | Light purple |

### Temperature Gradient

```
0°C   → #0033FF (Deep blue)
40°C  → #00FFCC (Cyan)
80°C  → #FF6600 (Orange)
120°C → #FF0000 (Red)
```

## Directory Structure

```
chem_diagram_v3/
├── __init__.py
├── core/
│   ├── canvas.py        # Drawing canvas
│   └── colors.py        # Color system
├── devices/
│   ├── base.py          # Device base class
│   ├── tanks.py         # Tank
│   ├── reactors.py       # Reactor
│   ├── heat_exchangers.py # Heat exchanger
│   ├── valves.py         # Valves
│   └── instruments.py    # Instruments
├── pipelines/
│   └── pipe.py          # Pipe / Signal line
├── diagrams/
│   ├── pfd.py          # PFD generator
│   ├── pid.py          # P&ID generator
│   └── architecture.py # Architecture generator
└── fonts/
    └── loader.py       # Font loader
```

## Examples

See the `examples/` directory for complete examples:
- `example_pfd.py` - PFD generation
- `example_pid.py` - P&ID generation  
- `example_architecture.py` - Architecture diagram

## FAQ

**Q: Chinese characters show as boxes?**

A: The tool automatically searches for available Chinese fonts on your system. If issues persist, install Source Han Sans or Alibaba PuHuiTi font.

**Q: Can I generate engineering-level P&ID?**

A: This tool generates professional-looking PFD/P&ID for proposals and presentations. It cannot replace AutoCAD/SmartPlant for engineering drawings.

---

I have no coding experience, what should I do if an error occurs during use?
Just send the cloud document link to the AI and let it troubleshoot and find a solution on its own.

**Skill Usage Documentation**: [使用指南飞书云文档链接](https://my.feishu.cn/wiki/XPOVwSB8CivVPkkdFBgcZaCunIf)

## Disclaimer

**Disclaimer**:
This project is 99% AI-generated. The AI's owner has no programming background. Please evaluate the project's feasibility before use.

## License

MIT License

## Reference

- [matplotlib](https://matplotlib.org/)
- [Pillow](https://pillow.readthedocs.io/)
- [P&ID Design Standards](https://en.wikipedia.org/wiki/Piping_and_instrumentation_diagram)
