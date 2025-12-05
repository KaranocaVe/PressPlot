import os
import sys

import matplotlib.pyplot as plt

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    plottheme.load_theme("clean_modern")

    # Colors
    blue_color = "#5B84C4"  # Soft blue
    red_color = "#F48B82"  # Soft red/salmon
    text_blue = "#2C5AA0"  # Darker blue for text
    text_red = "#D92E27"  # Darker red for text
    bg_color = "#F1F0EA"

    fig, ax = plt.subplots(figsize=(12, 7))

    # --- Data Setup ---

    # Savings (Blue) - Going Up and Right (Stacked)
    # Cumulative width must reach 2.3
    # We simulate the steps by plotting horizontal bars with increasing 'left' offset
    savings_widths = [0.1, 0.2, 0.4, 0.6, 1.0]  # Total 2.3
    # Check sum
    total_savings = sum(savings_widths)

    # Costs (Red) - Going Down and Right
    # Cumulative width must reach 5.6
    costs_widths = [4.5, 0.4, 0.3, 0.2, 0.2]  # Total 5.6
    total_costs = sum(costs_widths)

    # --- Plotting ---

    # 1. Savings (Blue)
    # Start from some Y base, go UP
    # X starts from cumulative sum
    y_base_savings = 1.0
    current_x = 0
    bar_height = 1.0

    for i, w in enumerate(savings_widths):
        # To match the "Staircase" look:
        # Each new bar starts where the previous one ended (in X)
        # And is one step higher (in Y)
        # BUT, the image shows them as "blocks" filling the space?
        # Actually, looking at the image:
        # It looks like a staircase.
        # Step 1 (bottom): x=0 to 0.1, y=1
        # Step 2: x=0.1 to 0.3, y=2
        # ...
        # Step 5 (top): x=1.3 to 2.3, y=5

        # Wait, looking at the image, the blocks extend to the left?
        # No, the "skyline" is the step. The blocks are solid.
        # Let's assume simple horizontal bars.

        y_pos = y_base_savings + i * bar_height
        ax.barh(y_pos, w, left=current_x, height=bar_height,
                color=blue_color, edgecolor=blue_color, align='edge')

        current_x += w

    # 2. Costs (Red)
    # Start from Y base (below savings), go DOWN
    # X starts from 0 (or continues? Image shows it starts from left)
    # Image: Red bar starts at far left (x=0).
    y_base_costs = 0.0  # The top of the red section (gap between blue and red)
    current_x_red = 0

    for i, w in enumerate(costs_widths):
        # Step 1 (Top): x=0 to 4.5, y=0 (going down to -1)
        # Step 2: x=4.5 to 4.9, y=-1 (going down to -2)

        y_pos = y_base_costs - (i + 1) * bar_height
        ax.barh(y_pos, w, left=current_x_red, height=bar_height,
                color=red_color, edgecolor=red_color, align='edge')

        current_x_red += w

    # --- Vertical Line ---
    # At x = 2.3 (Total Savings)
    ax.axvline(x=total_savings, color='black', linewidth=2, zorder=10)

    # --- Arrows ---
    # Blue Arrow: On the top blue bar (last one), pointing Left
    # Top blue bar is at index 4: y = 1 + 4 = 5. Range [5, 6].
    # It spans x=[1.3, 2.3].
    # Arrow should be at the right end, pointing left?
    # Image: Arrow is inside the bar, near the right edge, pointing left.
    top_blue_y = y_base_savings + (len(savings_widths) - 1) * bar_height + 0.5 * bar_height
    top_blue_right_x = total_savings

    ax.annotate('', xy=(top_blue_right_x - 0.5, top_blue_y), xytext=(top_blue_right_x - 0.1, top_blue_y),
                arrowprops=dict(arrowstyle='->', color=text_blue, lw=2))
    # Wait, '->' points to xy. If we want pointing Left:
    # xy is the tip. xytext is the tail.
    # Tip should be Left.
    # So xy=(left), xytext=(right).
    ax.annotate('', xy=(top_blue_right_x - 0.4, top_blue_y), xytext=(top_blue_right_x - 0.1, top_blue_y),
                arrowprops=dict(arrowstyle='->', color=text_blue, lw=2))

    # Red Arrow: On the top red bar (first one), pointing Right
    # Top red bar is index 0: y = 0 - 1 = -1. Range [-1, 0]. Center -0.5.
    # It spans x=[0, 4.5].
    # Arrow is at the left side?
    # Image: Arrow is at the far left, pointing right.
    top_red_y = y_base_costs - 0.5 * bar_height

    ax.annotate('', xy=(0.4, top_red_y), xytext=(0.1, top_red_y),
                arrowprops=dict(arrowstyle='->', color=text_red, lw=2))

    # --- Labels ---
    # "Savings $2.3trn"
    # Placed below the top blue bars, to the left of the vertical line.
    # Center visually in the blue area's "gap"?
    # Actually, the text is in the whitespace.
    ax.text(total_savings - 0.2, y_base_savings + 2.5 * bar_height,
            "Savings\n$2.3trn",
            color=text_blue, fontsize=24, fontweight='bold', ha='right', va='center')

    # "Costs $5.6trn"
    # Placed below the main red bar, near the steps?
    # Or at the end?
    # Image: "Costs" is near the drop-off steps.
    ax.text(total_costs - 0.2, y_base_costs - 3.5 * bar_height,
            "Costs\n$5.6trn",
            color=text_red, fontsize=24, fontweight='bold', ha='right', va='center')

    # --- Axes Styling ---
    ax.set_xlim(0, 6.5)
    ax.set_ylim(-6, 7)

    # Grid
    ax.grid(axis='x', color='#d4d4d4', linewidth=1.5)
    ax.grid(axis='y', visible=False)

    # Remove Spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Remove Ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Title
    # fig.text coordinates
    fig.text(0.5, 0.92, "One Big Beautiful Bill Act",
             ha='center', va='top', fontsize=26, fontweight='bold', color='black')

    # Save
    output_file = "reproduce_bill_act.png"
    plottheme.save_clean_modern_style(fig, output_file)
    print(f"Saved {output_file}")


if __name__ == "__main__":
    main()
