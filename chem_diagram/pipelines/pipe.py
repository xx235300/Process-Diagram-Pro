# -*- coding: utf-8 -*-
"""
管道模块 - Pipelines
==================

管道，流向箭头、信号线绘制
"""

import numpy as np
from matplotlib.patches import FancyArrowPatch
from ..core.colors import PIPELINE_COLORS


class Pipe:
    """
    管道
    
    绘制带箭头和标注的物料管道
    
    Args:
        start: 起点坐标 (x, y)
        end: 终点坐标 (x, y)
        label: 物料标注
        color: 颜色
        linewidth: 线宽
        arrow: 是否带箭头
    """
    
    def __init__(self, start, end, label='', color=None, 
                 linewidth=2.0, arrow=True):
        self.start = start
        self.end = end
        self.label = label
        self.color = color or PIPELINE_COLORS['process']['color']
        self.linewidth = linewidth
        self.arrow = arrow
        
    def draw(self, ax):
        """绘制管道"""
        x1, y1 = self.start
        x2, y2 = self.end
        
        if self.arrow:
            # 带箭头的管道
            ax.annotate('',
                      xy=(x2, y2), xytext=(x1, y1),
                      arrowprops=dict(
                          arrowstyle='->',
                          color=self.color,
                          lw=self.linewidth,
                          connectionstyle='arc3,rad=0'
                      ),
                      zorder=2)
        else:
            # 直线管道
            ax.plot([x1, x2], [y1, y2],
                  color=self.color,
                  linewidth=self.linewidth,
                  zorder=2)
                  
        # 物料标注
        if self.label:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            
            # 标注框
            ax.text(mid_x, mid_y + 0.15,
                   self.label,
                   ha='center', va='bottom',
                   fontsize=7, color=self.color,
                   fontweight='bold',
                   bbox=dict(
                       boxstyle='round,pad=0.15',
                       facecolor='white',
                       edgecolor=self.color,
                       linewidth=0.8,
                       alpha=0.9
                   ),
                   zorder=8)


class FlowArrow:
    """
    物流流向箭头
    
    带物料信息和参数的流向箭头
    
    Args:
        start: 起点
        end: 终点
        label: 物料名称
        temp: 温度
        pressure: 压力
        flow_rate: 流量
    """
    
    def __init__(self, start, end, label='', temp=None, 
                 pressure=None, flow_rate=None):
        self.start = start
        self.end = end
        self.label = label
        self.temp = temp
        self.pressure = pressure
        self.flow_rate = flow_rate
        
    def draw(self, ax):
        """绘制流向箭头"""
        x1, y1 = self.start
        x2, y2 = self.end
        
        # 计算方向并稍微缩短以便箭头清晰
        dx, dy = x2 - x1, y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        if length > 0:
            # 缩短5%避免箭头和设备重叠
            x2_s, y2_s = x1 + dx * 0.95, y1 + dy * 0.95
        else:
            x2_s, y2_s = x2, y2
        
        # 箭头
        ax.annotate('',
                  xy=(x2_s, y2_s), xytext=(x1, y1),
                  arrowprops=dict(
                      arrowstyle='->',
                      color='#1565C0',
                      lw=1.8,
                      connectionstyle='arc3,rad=0'
                  ),
                  zorder=2)
        
        # 标注信息
        if self.label or self.temp or self.pressure:
            mid_x = (x1 + x2_s) / 2
            mid_y = (y1 + y2_s) / 2
            
            # 构建标注文字
            lines = []
            if self.label:
                lines.append(self.label)
            if self.temp:
                lines.append(f'{self.temp}°C')
            if self.pressure:
                lines.append(f'{self.pressure}MPa')
            if self.flow_rate:
                lines.append(self.flow_rate)
            
            text = '\n'.join(lines)
            
            ax.text(mid_x, mid_y + 0.15,
                   text,
                   ha='center', va='bottom',
                   fontsize=6.5, color='#1565C0',
                   fontweight='bold',
                   bbox=dict(
                       boxstyle='round,pad=0.12',
                       facecolor='white',
                       edgecolor='#1565C0',
                       linewidth=0.8,
                       alpha=0.9
                   ),
                   zorder=8)


class SignalLine:
    """
    信号线（虚线）
    
    仪表到控制器的信号连接
    
    Args:
        start: 起点坐标
        end: 终点坐标
        line_type: 信号类型
    """
    
    def __init__(self, start, end, line_type='analog'):
        self.start = start
        self.end = end
        self.line_type = line_type
        
    def draw(self, ax):
        """绘制信号线"""
        x1, y1 = self.start
        x2, y2 = self.end
        
        color = PIPELINE_COLORS['signal']['color']
        
        # 虚线
        ax.plot([x1, x2], [y1, y2],
              color=color,
              linewidth=1.0,
              linestyle='--',
              zorder=2)
