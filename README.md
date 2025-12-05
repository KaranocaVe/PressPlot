# PressPlot

**PressPlot** (formerly PlotTheme) 是一个用于管理和应用自定义 Matplotlib 绘图风格的基础设施库。

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
import pressplot
import numpy as np

# 1. 加载 Clean Modern 风格
pressplot.load_theme("clean_modern")

# 2. 绘图
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 5))
line1, = ax.plot(x, y1, label='Sine')
line2, = ax.plot(x, y2, label='Cosine')

# 3. 使用辅助函数添加行内标注 (Line Annotation)
pressplot.label_line(ax, line1, "Sine Wave", x=8)
pressplot.label_line(ax, line2, "Cosine Wave", x=2)

ax.set_title("Trigonometric Functions", loc='left')
plt.show()
```

### 2. 定义和注册自定义主题

你可以通过代码动态注册一个主题：

```python
import pressplot

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
pressplot.register_theme("my_custom_style", my_rc_params, palette=my_palette)

# 应用
pressplot.load_theme("my_custom_style")
```

## API 参考

- `pressplot.load_theme(name)`: 应用指定名称的主题。
- `pressplot.register_theme(name, rc_params, palette)`: 注册新主题。
- `pressplot.list_themes()`: 列出所有可用主题。
- `pressplot.label_line(ax, line, label, ...)`: 在折线上添加彩色文本标注。
- `pressplot.add_border(input_path, output_path, ...)`: 为图片添加出版级边框。

## Gallery

以下是使用 PressPlot 复刻的经典图表案例：

### 1. Political & Social Issues

| Government Shutdown Blame | Support for Political Violence |
|:---:|:---:|
| ![Shutdown](reproduce_shutdown.png) | ![Political Violence](reproduce_political_violence.png) |

| Nobel Laureates | Passport Issuance |
|:---:|:---:|
| ![Nobel](reproduce_nobel.png) | ![Passport](reproduce_passport.png) |

### 2. Economics & Policy

| One Big Beautiful Bill Act | Manufacturing Output |
|:---:|:---:|
| ![Bill Act](reproduce_bill_act.png) | ![Manufacturing](reproduce_manufacturing.png) |

| Tariff Impact | Tech Stocks |
|:---:|:---:|
| ![Tariff](reproduce_tariff.png) | ![Tech](reproduce_tech.png) |

### 3. Maps & Demographics

| Greenland | World Map (Obesity Rates) |
|:---:|:---:|
| ![Greenland](reproduce_greenland.png) | ![Map](reproduce_map.png) |

| French Children Maths Performance | Drinking Habits |
|:---:|:---:|
| ![French Math](reproduce_french_math.png) | ![Drinking](reproduce_drinking.png) |

### 4. Social Media & Tech

| TikTok Usage | Bubble Chart Example |
|:---:|:---:|
| ![TikTok](reproduce_tiktok.png) | ![Bubble](reproduce_bubble.png) |

### 5. Basic Demos

| Scatter Plot | Theme Overview |
|:---:|:---:|
| ![Scatter](reproduce_scatter.png) | ![Theme](replicate_clean_modern_packaged.png) |
