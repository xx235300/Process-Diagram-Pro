[English](./README.md) | [简体中文](https://github.com/xx235300/process-diagram-pro/blob/main/README_ZH.md)

# Process Diagram Pro

**Professional PFD/P&ID Diagram Generator for Chemical Engineering**

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)]()
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

- 🌡️ **Temperature-based color mapping** (Blue → Cyan → Orange → Red)
- 🔤 **Chinese font support** (Automatic fallback)
- 🎨 **Industry-standard color scheme**
- ⚙️ **Professional equipment symbols** (Tank, Reactor, Valve, Instrument)
- 🔗 **Control loop connections** (Signal lines - gray dashed)
- 🏗️ **Grid backgrounds** (Customizable styles)
- 🔌 **More valve types** (Hand valve, Check valve)

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
gen.add_valve({'type': 'control', 'x': 4.5, 'y': 3, 'tag': 'TV-101'})
gen.add_instrument({'type': 'TIC', 'x': 6, 'y': 5, 'tag': 'TIC-101'})
gen.add_signal({'from': 'TE-101', 'to': 'TIC-101'})  # Gray dashed line
gen.save('pid_output.png')
```

### Generate Architecture Diagram

```python
from chem_diagram_v3 import ArchitectureGenerator

gen = ArchitectureGenerator(show_grid=True, grid_style='light')
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
| `'reactor'` | Reactor | Fixed bed reactor (temperature-based color) |
| `'heat_exchanger'` | HeatExchanger | Heat exchanger / Preheater |
| `'separator'` | Separator | Gas-liquid separator |

### Valve Types

| Type | Class | Description |
|------|-------|-------------|
| `'control'` | ControlValve | Control valve (kite shape) |
| `'esd'` | ESDValve | Emergency shutdown valve (pentagon, red) |
| `'safety'` | SafetyValve | Safety valve (semicircle + triangle) |
| `'hand'` | HandValve | Manual valve (diamond) ⭐ NEW |
| `'check'` | CheckValve | Check valve (triangle) ⭐ NEW |

### Instrument Types

| Type | Class | Description |
|------|-------|-------------|
| `'TIC'` | TIC | Temperature Indicator Controller |
| `'PIC'` | PIC | Pressure Indicator Controller |
| `'FIC'` | FIC | Flow Indicator Controller |
| `'TE'` | TE | Temperature Element |
| `'PE'` | PE | Pressure Element |
| `'FE'` | FE | Flow Element |
| `'PSH'` | PSH | Pressure Switch (High) |
| `'PSL'` | PSL | Pressure Switch (Low) |
| `'AE'` | AE | Online Analyzer (hexagon) |

## Signal Lines (Enhanced)

Signal lines now use **gray dashed style** (industry standard):

```python
gen.add_signal({'from': 'TE-101', 'to': 'TIC-101'})
# Renders as: gray dashed line with direction markers
```

## Grid Backgrounds (NEW)

Architecture diagrams support configurable grid backgrounds:

```python
gen = ArchitectureGenerator(show_grid=True, grid_style='light')  # light, dark, colorful
```

## Directory Structure

```
chem_diagram_v3/
├── __init__.py
├── core/
│   ├── canvas.py        # Drawing canvas
│   └── colors.py        # Color system + temperature gradient
├── devices/
│   ├── base.py          # Device base class
│   ├── tanks.py         # Tank
│   ├── reactors.py      # Reactor (temperature color)
│   ├── heat_exchangers.py # Heat exchanger
│   ├── valves.py         # Valves (5 types)
│   └── instruments.py    # Instruments (9 types)
├── pipelines/
│   └── pipe.py          # Pipe, SignalLine (gray dashed), PipeElbow
├── diagrams/
│   ├── pfd.py          # PFD generator
│   ├── pid.py           # P&ID generator
│   └── architecture.py  # Architecture generator (grid support)
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

A: The tool automatically searches for available Chinese fonts. If issues persist, install Source Han Sans or Alibaba PuHuiTi font.

**Q: Can I generate engineering-level P&ID?**

A: This tool generates professional-looking PFD/P&ID for proposals and presentations. It cannot replace AutoCAD/SmartPlant for engineering drawings.

---

## Changelog

### v2.0.0 (2026-03-29)

**New Features:**
- ✨ **New valve types**: HandValve (diamond), CheckValve (triangle)
- ✨ **Enhanced instrument markers**: TIC/PIC/FIC use bold letters; PSH/PSL use triangle markers
- ✨ **Signal line color change**: Gray dashed lines (industry standard)
- ✨ **Background grids**: Architecture diagrams support configurable grid styles

**Improvements:**
- Valve symbols with enhanced borders and marker points
- Pipe arrow style optimization
- Instrument double-ring design
- Signal lines with direction markers

**Bug Fixes:**
- Fixed `grid()` matplotlib 3.10+ compatibility (`b=True` → `visible=True`)

**API Changes:**
```python
# Signal line color (old → new)
# Old: Purple #9C27B0
# New: Gray #757575

# Architecture diagram new parameters
gen = ArchitectureGenerator(show_grid=True, grid_style='light')
```

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
