# Professional Plot Manager

A professional plotting manager that provides a clean, object-oriented interface for creating and managing matplotlib plots. This manager simplifies the creation of multi-subplot figures while providing extensive customization options through configuration files.

## Features

- Easy creation and management of multi-subplot figures
- Configurable styling through external configuration files
- Automatic backend detection and compatibility with both Qt5 and TkAgg
- Support for various plot types:
  - Regular plots
  - Semi-log plots (x and y)
  - Log-log plots
- Interactive zoom controls
- Customizable titles, labels, and fonts
- Figure size management for both display and output
- Line tracking and access capabilities

## Configuration

The plot manager uses `.ini` configuration files to control various aspects of the plots:

- Text properties (fonts, sizes)
- Line styles and colors
- Axis properties
- Background settings

Example configuration structure:
```ini
[text]
xlabels.font = Arial
xlabels.fontsize = 12
title.font = Arial
title.fontsize = 14

[lines]
color_sequence = blue, red, green
linestyle_sequence = solid, dashed, dotted

[axes]
background_color = 1.0, 1.0, 1.0
```

## Usage Example

```python
from plot_manager import PlotManager
import numpy as np

# Create a plot manager with 2 rows and 2 columns
plot_manager = PlotManager(rows=2, cols=2)

# Generate some example data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot in first subplot
plot_manager.set_active_subplot(0, 0)
plot_manager.plot(x, y1, legend='sin(x)')
plot_manager.set_subplot_title('Sine Wave')

# Plot in second subplot
plot_manager.set_active_subplot(0, 1)
plot_manager.plot(x, y2, legend='cos(x)')
plot_manager.set_subplot_title('Cosine Wave')

# Customize the view
plot_manager.zoom_x(0, 5)  # Zoom x-axis
plot_manager.set_figure_title('Trigonometric Functions')

# Save the figure
plot_manager.save_figure('trig_functions.png', dpi=300)
```

## Installation

Clone this repository and ensure you have the required dependencies:

```bash
pip install -r requirements.txt
```

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contributing

[N/A]
