# PlotTheme

**PlotTheme** 是一个用于管理和应用自定义 Matplotlib 绘图风格的基础设施库。

它提供了一套灵活的 API 来定义、注册和应用绘图主题，旨在帮助科研人员和开发者轻松维护一致的图表风格。

## 核心功能

- **主题定义 (Theme Definition)**: 将 Matplotlib 的 `rcParams` 和颜色循环 (Color Cycle) 封装在一个 `Theme` 对象中。
- **主题注册 (Registry)**: 集中管理多个主题，支持运行时动态注册。
- **一键应用**: 通过简单的 API 切换全局绘图风格。
- **预设风格**: 内置了 "clean_modern" 等出版级风格。

## 安装

```bash
pip install .
```

## 使用指南

### 1. 使用内置风格 (Clean Modern 风格)

```python
import matplotlib.pyplot as plt
import plottheme
import numpy as np

# 1. 加载 Clean Modern 风格
plottheme.load_theme("clean_modern")

# 2. 绘图
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 5))
line1, = ax.plot(x, y1, label='Sine')
line2, = ax.plot(x, y2, label='Cosine')

# 3. 使用辅助函数添加行内标注 (Line Annotation)
plottheme.label_line(ax, line1, "Sine Wave", x=8)
plottheme.label_line(ax, line2, "Cosine Wave", x=2)

ax.set_title("Trigonometric Functions", loc='left')
plt.show()
```

### 2. 定义和注册自定义主题

你可以通过代码动态注册一个主题：

```python
import plottheme

# 定义主题参数
my_rc_params = {
    "font.family": "sans-serif",
    "axes.titlesize": 18,
    "axes.labelsize": 14,
    "lines.linewidth": 2.5
}

# 定义配色方案 (可选)
my_palette = ["#E63946", "#F1FAEE", "#A8DADC", "#457B9D", "#1D3557"]

# 注册主题
plottheme.register_theme("my_custom_style", my_rc_params, palette=my_palette)

# 应用
plottheme.load_theme("my_custom_style")
```

## API 参考

- `plottheme.load_theme(name)`: 应用指定名称的主题。
- `plottheme.register_theme(name, rc_params, palette)`: 注册新主题。
- `plottheme.list_themes()`: 列出所有可用主题。
- `plottheme.label_line(ax, line, label, ...)`: 在折线上添加彩色文本标注。
