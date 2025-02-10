import configparser
import numpy as np

class PlotConfigParser:
    """Parser for plot configuration files."""
    
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
    
    def get_color_sequence(self):
        """Get the color sequence as RGB tuples."""
        colors_str = self.config.get('lines', 'color_sequence')
        return [color.strip() for color in colors_str.split(',')]
    
    def get_linestyle_sequence(self):
        """Get the line style sequence."""
        styles_str = self.config.get('lines', 'linestyle_sequence')
        return [style.strip() for style in styles_str.split(',')]
    
    def get_background_color(self):
        """Get the background color as RGB tuple."""
        bg_str = self.config.get('axes', 'background_color')
        return tuple(float(x) for x in bg_str.split(','))
    
    def get_font_settings(self, element):
        """Get font settings for a specific element."""
        return {
            'font': self.config.get('text', f'{element}.font'),
            'fontsize': self.config.getint('text', f'{element}.fontsize')
        } 