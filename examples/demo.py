import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from src.plot_manager import PlotManager

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/5) * np.sin(x)
y4 = x**2 / 50

# Create plot manager with 2x2 subplots
pm = PlotManager(2, 2)

# Plot in first subplot
pm.set_active_subplot(0, 0)
pm.plot(x, y1, legend='sin(x)', color='blue')
pm.plot(x, y2, legend='cos(x)', color='red')
pm.set_subplot_title('Trigonometric Functions')

# Plot in second subplot
pm.set_active_subplot(0, 1)
pm.semilogy(x, y4, legend='x^2', color='green')
pm.set_subplot_title('Quadratic Function')

# Plot in third subplot
pm.set_active_subplot(1, 0)
pm.plot(x, y3, legend='Damped Sine', color='purple')
pm.set_subplot_title('Damped Sine Wave')

# Set overall figure title
pm.set_figure_title('Demo Plot')

# Adjust figure size
pm.set_figure_size(12, 8)

# Save the figure
pm.save_figure('demo_plot.png', dpi=300)

# Keep the plot window open
input("Press Enter to close...") 