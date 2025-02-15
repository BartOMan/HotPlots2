import pytest
import numpy as np
import matplotlib.pyplot as plt
from src.plot_manager import PlotManager

class TestPlotManager:
    def test_initialization(self, plot_manager):
        """Test basic initialization of PlotManager."""
        assert plot_manager.rows == 2
        assert plot_manager.cols == 2
        assert plot_manager.axes.shape == (2, 2)
        assert not plot_manager.is_window_closed()

    def test_active_subplot(self, plot_manager):
        """Test setting and getting active subplot."""
        plot_manager.set_active_subplot(1, 1)
        row, col = plot_manager.get_active_subplot()
        assert (row, col) == (1, 1)

        with pytest.raises(ValueError):
            plot_manager.set_active_subplot(2, 2)  # Out of bounds

    def test_plotting(self, plot_manager):
        """Test basic plotting functionality."""
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        plot_manager.plot(x, y, legend="sin(x)")
        assert plot_manager.getNumLines() == 1
        
        line = plot_manager.getLine(1)
        np.testing.assert_array_almost_equal(line.get_xdata(), x)
        np.testing.assert_array_almost_equal(line.get_ydata(), y)

    def test_log_plots(self, plot_manager):
        """Test logarithmic plotting functions."""
        x = np.logspace(0, 2, 100)
        y = x**2

        # Test semilogx
        plot_manager.set_active_subplot(0, 0)
        plot_manager.semilogx(x, y, legend="semilogx")
        assert plot_manager.getNumLines() == 1

        # Test semilogy
        plot_manager.set_active_subplot(0, 1)
        plot_manager.semilogy(x, y, legend="semilogy")
        assert plot_manager.getNumLines() == 1

        # Test loglog
        plot_manager.set_active_subplot(1, 0)
        plot_manager.loglog(x, y, legend="loglog")
        assert plot_manager.getNumLines() == 1

    def test_zoom_functions(self, plot_manager):
        """Test zooming functionality."""
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        plot_manager.plot(x, y)
        
        # Test x zoom
        plot_manager.zoom_x(2, 8)
        xlim = plot_manager.axes[0, 0].get_xlim()
        assert xlim[0] == pytest.approx(2)
        assert xlim[1] == pytest.approx(8)
        
        # Test y zoom
        plot_manager.zoom_y(-0.5, 0.5)
        ylim = plot_manager.axes[0, 0].get_ylim()
        assert ylim[0] == pytest.approx(-0.5)
        assert ylim[1] == pytest.approx(0.5)

    def test_titles(self, plot_manager):
        """Test setting titles."""
        plot_manager.set_subplot_title("Subplot Title")
        assert plot_manager.axes[0, 0].get_title() == "Subplot Title"

        plot_manager.set_figure_title("Figure Title")
        assert plot_manager.figure.texts[0].get_text() == "Figure Title"

    def test_figure_size(self, plot_manager):
        """Test figure size manipulation."""
        plot_manager.set_figure_size(8, 6)
        size = plot_manager.figure.get_size_inches()
        assert size[0] == pytest.approx(8)
        assert size[1] == pytest.approx(6)

    def test_save_figure(self, plot_manager, tmp_path):
        """Test figure saving functionality."""
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plot_manager.plot(x, y)
        
        # Save to a temporary file
        save_path = tmp_path / "test_plot.png"
        plot_manager.save_figure(str(save_path))
        assert save_path.exists()

    def test_line_management(self, plot_manager):
        """Test line management functions."""
        x = np.linspace(0, 10, 100)
        
        # Add multiple lines
        plot_manager.plot(x, np.sin(x), legend="sin")
        plot_manager.plot(x, np.cos(x), legend="cos")
        
        assert plot_manager.getNumLines() == 2
        
        with pytest.raises(ValueError):
            plot_manager.getLine(3)  # Non-existent line 