import os
import pytest
import tempfile
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing

@pytest.fixture
def config_file():
    """Create a temporary config file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.ini', delete=False) as f:
        f.write("""[text]
xlabels.font = Arial
xlabels.fontsize = 12
title.font = Arial
title.fontsize = 14

[lines]
color_sequence = blue, red, green
linestyle_sequence = solid, dashed, dotted

[axes]
background_color = 1.0, 1.0, 1.0
""")
        f.flush()
        yield f.name
    os.unlink(f.name)

@pytest.fixture
def plot_manager(config_file):
    """Create a PlotManager instance for testing."""
    from src.plot_manager import PlotManager
    pm = PlotManager(2, 2, config_file)
    yield pm
    plt.close('all') 