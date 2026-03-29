# -*- coding: utf-8 -*-
"""
仪表 - Instruments
==================

温度/压力/流量/分析仪表绘制
"""

from matplotlib.patches import Circle
from ..core.colors import INSTRUMENT_COLORS


class Instrument:
    """
    仪表基类（圆形+符号）
    
    Args:
        x, y: 仪表中心坐标
        tag: 位号（如 'TIC-101'）
        inst_type: 仪表类型
        size: 尺寸
    """
    
    # 仪表类型对应的符号（显示在圆内）
    TYPE_SYMBOLS = {
        'TI': 'TI',
        'TE': 'TE', 
        'TIC': 'TIC',
        'TICL': 'TIC',  # 带本地显示
        'PI': 'PI',
        'PE': 'PE',
        'PIC': 'PIC',
        'FI': 'FI',
        'FE': 'FE',
        'FIC': 'FIC',
        'PT': 'PT',
        'PS': 'PS',
        'PSH': 'PSH',
        'PSL': 'PSL',
        'AE': 'AE',
        'AI': 'AI',
        'default': 'IN',
    }
    
    def __init__(self, x, y, tag='', inst_type='default', size=0.25):
        self.x = x
        self.y = y
        self.tag = tag
        self.inst_type = inst_type
        self.size = size
        
    def draw(self, ax):
        """绘制仪表"""
        colors = INSTRUMENT_COLORS['default']
        
        # 圆形仪表
        circle = Circle((self.x, self.y), self.size/2,
                       facecolor=colors['facecolor'],
                       edgecolor=colors['edgecolor'],
                       linewidth=1.2,
                       zorder=6)
        ax.add_patch(circle)
        
        # 仪表符号
        symbol = self.TYPE_SYMBOLS.get(self.inst_type, self.inst_type[:2])
        ax.text(self.x, self.y,
               symbol, ha='center', va='center',
               fontsize=5, fontweight='bold',
               color=colors['label_color'], zorder=7)
        
        # 位号标签（在下方）
        if self.tag:
            ax.text(self.x, self.y - self.size/2 - 0.1,
                   self.tag, ha='center', va='top',
                   fontsize=6, color=colors['label_color'], zorder=7)
                   
    def get_connection_points(self):
        """获取连接点"""
        return {
            'top': (self.x, self.y + self.size/2),
            'bottom': (self.x, self.y - self.size/2),
            'left': (self.x - self.size/2, self.y),
            'right': (self.x + self.size/2, self.y),
        }


# ===================== 便捷子类 =====================

class TIC(Instrument):
    """温度指示控制器"""
    def __init__(self, x, y, tag='TIC-101', size=0.25):
        super().__init__(x, y, tag, 'TIC', size)


class PIC(Instrument):
    """压力指示控制器"""
    def __init__(self, x, y, tag='PIC-101', size=0.25):
        super().__init__(x, y, tag, 'PIC', size)


class FIC(Instrument):
    """流量指示控制器"""
    def __init__(self, x, y, tag='FIC-101', size=0.25):
        super().__init__(x, y, tag, 'FIC', size)


class TE(Instrument):
    """温度传感器"""
    def __init__(self, x, y, tag='TE-101', size=0.22):
        super().__init__(x, y, tag, 'TE', size)


class PE(Instrument):
    """压力传感器"""
    def __init__(self, x, y, tag='PE-101', size=0.22):
        super().__init__(x, y, tag, 'PE', size)


class FE(Instrument):
    """流量元件"""
    def __init__(self, x, y, tag='FE-101', size=0.22):
        super().__init__(x, y, tag, 'FE', size)


class PSH(Instrument):
    """压力开关（高报）"""
    def __init__(self, x, y, tag='PSH-101', size=0.22):
        super().__init__(x, y, tag, 'PSH', size)


class PSL(Instrument):
    """压力开关（低报）"""
    def __init__(self, x, y, tag='PSL-101', size=0.22):
        super().__init__(x, y, tag, 'PSL', size)


class AE(Instrument):
    """在线分析仪"""
    def __init__(self, x, y, tag='AE-101', size=0.28):
        super().__init__(x, y, tag, 'AE', size)
