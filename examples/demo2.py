import sys
from pathlib import Path
import platform
import os

parentDir = str(Path(__file__).parent.parent)
configDir = str(Path(parentDir) / 'config')

# Add parent directory to Python path
sys.path.append(parentDir)

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' if you prefer Qt
import matplotlib.pyplot as plt
from src.plot_manager import PlotManager

# Define output filename
output_filename = 'demo_plot.jpg'

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/5) * np.sin(x)
y4 = x**2 / 50

# Define config file path and verify it exists
confFile = 'plot_defaults.ini'
# confFile = 'plotConfigTesting.ini'
# confFile = '../config/plotConfigTesting.ini'
fullConfFile = Path(configDir) / confFile

if not fullConfFile.exists():
    raise FileNotFoundError(f"Configuration file not found: {fullConfFile}")

# Now use the verified config file path
pm = PlotManager(2, 2, str(fullConfFile))

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

# Link just x axes, y axes or both axes
pm.link_axes('x')       # valid arguments are 'x', 'y', 'xy'    

# Set overall figure title
pm.set_figure_title('Demo Plot')

# Adjust figure size
pm.set_figure_size(12, 8)

# Save the figure
pm.save_figure(output_filename, dpi=300, preview=False)


# Keep the plot window open
input("Press Enter to close...") 