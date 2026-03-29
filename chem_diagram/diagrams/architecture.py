# -*- coding: utf-8 -*-
"""
系统架构图生成器
================

数字孪生/物联网系统架构图
"""

from matplotlib.patches import FancyBboxPatch
from ..core.canvas import ChemicalCanvas
from ..core.colors import COLORS


class ArchitectureGenerator:
    """
    系统架构图生成器
    
    适用于：
    - 数字孪生系统架构
    - 物联网架构
    - 云边端架构
    - 软件系统架构
    
    Usage:
        gen = ArchitectureGenerator()
        gen.set_title("数字孪生系统架构")
        gen.add_layer("设备层", ["温度传感器", "PLC", "边缘网关"])
        gen.add_layer("边缘计算层", ["ESP32", "Edge Agent"])
        gen.add_layer("云平台层", ["MQTT", "AI Model", "数字孪生"])
        gen.render().save('arch.png')
    """
    
    # 默认层颜色
    LAYER_COLORS = [
        '#E8F5E9',  # 绿
        '#E3F2FD',  # 蓝
        '#F3E5F5',  # 紫
        '#FFF8E1',  # 黄
        '#E8F5E9',  # 绿
    ]
    
    def __init__(self, figsize=(14, 10), dpi=150):
        self.canvas = ChemicalCanvas(figsize=figsize, dpi=dpi)
        self.layers = []
        self.layer_height = 1.8
        self.layer_width = 12
        self.start_x = 1
        self.start_y = 8
        
    def set_title(self, title, subtitle=''):
        """设置标题"""
        self.canvas.set_title(title, subtitle)
        return self
        
    def add_layer(self, name, components, color=None):
        """
        添加架构层
        
        Args:
            name: 层名称（如 '设备层'）
            components: 组件列表（如 ['温度传感器', 'PLC']）
            color: 层颜色（可选）
        """
        layer_idx = len(self.layers)
        layer_color = color or self.LAYER_COLORS[layer_idx % len(self.LAYER_COLORS)]
        
        y = self.start_y - layer_idx * self.layer_height
        x = self.start_x
        
        # 层框
        rect = FancyBboxPatch(
            (x, y - self.layer_height + 0.3),
            self.layer_width,
            self.layer_height - 0.4,
            boxstyle="round,pad=0.05",
            facecolor=layer_color,
            edgecolor='#455A64',
            linewidth=2,
            zorder=3
        )
        self.canvas.ax.add_patch(rect)
        
        # 层名称
        self.canvas.add_text(
            x + 0.3, y - 0.5,
            name,
            fontsize=14,  # 10 * dpi / 100
            color='#333333',
            bold=True
        )
        
        # 组件
        comp_x = x + 0.5
        comp_width = 2.2
        comp_height = 0.8
        comp_y = y - self.layer_height + 0.6
        
        for comp in components:
            # 组件框
            comp_rect = FancyBboxPatch(
                (comp_x, comp_y),
                comp_width, comp_height,
                boxstyle="round,pad=0.03",
                facecolor='white',
                edgecolor='#455A64',
                linewidth=1,
                zorder=4
            )
            self.canvas.ax.add_patch(comp_rect)
            
            # 组件文字
            self.canvas.add_text(
                comp_x + comp_width/2,
                comp_y + comp_height/2,
                comp,
                fontsize=9,
                color='#333333'
            )
            
            comp_x += comp_width + 0.2
            
        # 层间连接箭头
        if layer_idx > 0:
            prev_y = self.start_y - (layer_idx - 1) * self.layer_height
            arrow_x = x + self.layer_width / 2
            
            # 双向箭头
            self.canvas.draw_arrow(
                arrow_x, prev_y - self.layer_height + 0.4,
                arrow_x, y + 0.3,
                color='#455A64',
                lw=2,
                style='<->'
            )
            
        self.layers.append({
            'name': name,
            'components': components,
            'color': layer_color
        })
        return self
        
    def render(self):
        """渲染并返回canvas"""
        return self.canvas
        
    def save(self, path):
        """保存图片"""
        return self.canvas.save(path)


# ===================== 便捷函数 =====================

def draw_architecture(title, layers, output='arch_output.png'):
    """
    快速绘制系统架构图
    
    Args:
        title: 图表标题
        layers: 层列表 [{
            'name': '设备层',
            'components': ['传感器', 'PLC']
        }]
        output: 输出路径
    
    Returns:
        ArchitectureGenerator实例
    """
    gen = ArchitectureGenerator()
    gen.set_title(title)
    
    for layer in layers:
        gen.add_layer(layer['name'], layer.get('components', []))
        
    gen.save(output)
    return gen
