import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.backends.backend_qt5agg import FigureCanvasQT5Agg
import configparser
import os

class PlotManager:
    """A professional plotting manager class that simplifies matplotlib usage."""
    
    figure: Figure
    axes: np.ndarray
    rows: int
    cols: int
    config: configparser.ConfigParser
    
    def __init__(self, rows, cols, config_file=None):
        """
        Initialize the plot manager.
        
        Args:
            rows (int): Number of subplot rows
            cols (int): Number of subplot columns
            config_file (str, optional): Path to configuration file
        """
        self._check_backend()
        
        # Initialize figure and subplots
        self.figure = plt.figure()
        self.axes = np.array([[plt.subplot(rows, cols, i * cols + j + 1) 
                             for j in range(cols)] for i in range(rows)])
        self.rows = rows
        self.cols = cols
        
        # Track active subplot
        self._active_row = 0
        self._active_col = 0
        
        # Load configuration
        self.config = self._load_config(config_file)
        self._apply_config()
        
        # Connect to window close event
        self.figure.canvas.mpl_connect('close_event', self._on_close)
        self._window_closed = False
        
        # Initialize storage for lines in each subplot
        self._lines = [[[] for _ in range(cols)] for _ in range(rows)]
    
    def _check_backend(self):
        """Verify that we're using a supported backend."""
        backend = plt.get_backend()
        supported_backends = ['TkAgg', 'Qt5Agg', 'Qt6Agg']  # Add more as needed
        if backend not in supported_backends:
            raise ValueError(f"Unsupported backend: {backend}. Please use one of: {supported_backends}")
    
    def _load_config(self, config_file):
        """Load configuration from file."""
        if config_file is None:
            config_file = os.path.join(os.path.dirname(__file__), 
                                     '../config/plot_defaults.ini')
        
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    
    def _apply_config(self):
        """Apply configuration settings to the plot."""
        # Apply text settings
        font = self.config.get('text', 'xlabels.font')
        fontsize = self.config.getint('text', 'xlabels.fontsize')
        
        for ax_row in self.axes:
            for ax in ax_row:
                ax.tick_params(labelsize=fontsize)
                ax.set_xlabel('X Label', fontname=font, fontsize=fontsize)
                ax.set_ylabel('Y Label', fontname=font, fontsize=fontsize)
    
    def set_active_subplot(self, row, col):
        """Set the active subplot."""
        if row >= self.rows or col >= self.cols:
            raise ValueError(f"Invalid subplot indices: ({row}, {col})")
        self._active_row = row
        self._active_col = col
        plt.sca(self.axes[row, col])
    
    def get_active_subplot(self):
        """Get the current active subplot indices."""
        return self._active_row, self._active_col
    
    def plot(self, x, y, legend=None, **kwargs):
        """Plot data on the active subplot."""
        x = np.asarray(x)
        y = np.asarray(y)
        
        ax = self.axes[self._active_row, self._active_col]
        line = ax.plot(x, y, **kwargs)[0]
        
        if legend:
            line.set_label(legend)
            ax.legend()
        
        # Store the line
        self._lines[self._active_row][self._active_col].append(line)
        self.figure.canvas.draw()
    
    def semilogx(self, x, y, legend=None, **kwargs):
        """Create a semilog plot (log x-axis)."""
        x = np.asarray(x)
        y = np.asarray(y)
        
        ax = self.axes[self._active_row, self._active_col]
        line = ax.semilogx(x, y, **kwargs)[0]
        
        if legend:
            line.set_label(legend)
            ax.legend()
        
        # Store the line
        self._lines[self._active_row][self._active_col].append(line)
        self.figure.canvas.draw()
    
    def semilogy(self, x, y, legend=None, **kwargs):
        """Create a semilog plot (log y-axis)."""
        x = np.asarray(x)
        y = np.asarray(y)
        
        ax = self.axes[self._active_row, self._active_col]
        line = ax.semilogy(x, y, **kwargs)[0]
        
        if legend:
            line.set_label(legend)
            ax.legend()
        
        # Store the line
        self._lines[self._active_row][self._active_col].append(line)
        self.figure.canvas.draw()
    
    def loglog(self, x, y, legend=None, **kwargs):
        """Create a log-log plot."""
        x = np.asarray(x)
        y = np.asarray(y)
        
        ax = self.axes[self._active_row, self._active_col]
        line = ax.loglog(x, y, **kwargs)[0]
        
        if legend:
            line.set_label(legend)
            ax.legend()
        
        # Store the line
        self._lines[self._active_row][self._active_col].append(line)
        self.figure.canvas.draw()
    
    def zoom_x(self, xmin, xmax, autozoomy=False):
        """Set x-axis limits on active subplot.
        
        Args:
            xmin (float): Minimum x-axis value
            xmax (float): Maximum x-axis value
            autozoomy (bool): If True, automatically adjust y-axis limits to show
                            all data points within the new x-range
        """
        ax = self.axes[self._active_row, self._active_col]
        ax.set_xlim(xmin, xmax)
        
        if autozoomy:
            lines = ax.get_lines()
            if lines:
                ymin_list = []
                ymax_list = []
                for line in lines:
                    xdata = line.get_xdata()
                    ydata = line.get_ydata()
                    # Find indices of points within x range
                    mask = (xdata >= xmin) & (xdata <= xmax)
                    if any(mask):  # Only include if there are points in range
                        ymin_list.append(ydata[mask].min())
                        ymax_list.append(ydata[mask].max())
                
                if ymin_list and ymax_list:  # If we found any valid points
                    self.zoom_y(min(ymin_list), max(ymax_list))
                    return
        
        self.figure.canvas.draw()
    
    def zoom_y(self, ymin=None, ymax=None):
        """Set y-axis limits on active subplot."""
        ax = self.axes[self._active_row, self._active_col]
        if ymin is None or ymax is None:
            # Auto-zoom to visible lines
            lines = ax.get_lines()
            if not lines:
                return
            
            ymin_data = min(line.get_ydata().min() for line in lines)
            ymax_data = max(line.get_ydata().max() for line in lines)
            
            if ymin is None:
                ymin = ymin_data
            if ymax is None:
                ymax = ymax_data
        
        ax.set_ylim(ymin, ymax)
        self.figure.canvas.draw()
    
    def set_figure_size(self, width, height):
        """Set the displayed figure size in inches."""
        self.figure.set_size_inches(width, height)
        self.figure.canvas.draw()
    
    def set_output_size(self, width, height):
        """Set the output figure size for saving."""
        self._output_size = (width, height)
    
    def set_subplot_title(self, title, pad=None):
        """Set title for the active subplot.
        
        Args:
            title (str): Title text. Use '\n' for line breaks
            pad (float, optional): Spacing between the title and the plot
        """
        font = self.config.get('text', 'title.font')
        fontsize = self.config.getint('text', 'title.fontsize')
        self.axes[self._active_row, self._active_col].set_title(
            title, fontname=font, fontsize=fontsize)
        self.figure.canvas.draw()
    
    def set_figure_title(self, title):
        """Set title for the entire figure."""
        font = self.config.get('text', 'title.font')
        fontsize = self.config.getint('text', 'title.fontsize')
        self.figure.suptitle(title, fontname=font, fontsize=fontsize)
        self.figure.canvas.draw()
    
    def save_figure(self, filename, filetypes=None, dpi=300):
        """Save the figure to a file.
        
        Args:
            filename (str): Path where the figure should be saved
            filetypes (list, optional): List of allowed file extensions. If None, 
                matplotlib's default formats are used
            dpi (int, optional): Resolution in dots per inch. Defaults to 300
        
        Raises:
            RuntimeError: If attempting to save after the figure window has been closed
        """
        if self._window_closed:
            raise RuntimeError("Cannot save: figure window has been closed")
        
        if hasattr(self, '_output_size'):
            orig_size = self.figure.get_size_inches()
            self.figure.set_size_inches(*self._output_size)
        
        self.figure.savefig(filename, dpi=dpi)
        
        if hasattr(self, '_output_size'):
            self.figure.set_size_inches(*orig_size)
    
    def _on_close(self, event):
        """Handle window close event."""
        self._window_closed = True
    
    def is_window_closed(self):
        """Check if the figure window has been closed."""
        return self._window_closed

    def getNumLines(self):
        """Return the number of lines in the active subplot."""
        return len(self._lines[self._active_row][self._active_col])

    def getLine(self, lineNum):
        """Return a specific line from the active subplot.
        
        Args:
            lineNum (int): Line number (1-based indexing)
            
        Returns:
            matplotlib.lines.Line2D: The requested line object
            
        Raises:
            ValueError: If lineNum is out of range
        """
        if not 1 <= lineNum <= self.getNumLines():
            raise ValueError(f"Line number must be between 1 and {self.getNumLines()}")
        return self._lines[self._active_row][self._active_col][lineNum - 1]

# Add more padding between title and plot
# plot_manager.set_subplot_title('First line\\n\\nSecond line')  # double spacing
# plot_manager.set_figure_title('Title\\n\\nSubtitle')  # double spacing 