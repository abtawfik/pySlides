######################
# Standard libraries #
######################
from dataclasses import dataclass
from typing import Any

#####################
# Package resources #
##################### 
import pkg_resources

###################
# HTML templating #
###################
from jinja2 import Template
from jinja2 import Environment, PackageLoader, select_autoescape

class Slides(object):
    def __init__(self,
                 header=None,
                 styles=None):
        self.header = {} if header is None or not isinstance(header,dict) else header
        self.styles = styles
        self.slides = []
        
    def add(self,
            title=None,
            subtitle=None,
            content=None,
            layout=None,
            figure=None,
            head_style=None):
        slide = {'title'      : title,
                 'head_style' : Styler(head_style).to_string if head_style is not None else None,
                 'subtitle'   : subtitle,
                 'content'    : content,
                 'layout'     : layout,
                 'figure'     : PlotlyFigure(figure).figure if figure is not None else None}
        slide = {k:v for k,v in slide.items() if v is not None}
        self.slides += [slide]
        return self

    def save(self, outname):
        '''Save the slides to an html file

        Parameters
        ----------
        outname : str
           name of the output html file. good idea to include .html extension

        Return
        ------
        None
        '''
        #-----------------------------------------
        # Create a Jinja2 template environment
        #-----------------------------------------
        file_loader = PackageLoader(__name__, 'data')
        env = Environment(loader=file_loader)
        template = env.get_template('base.html')
        #--------------------------------
        # Render and output slides
        #--------------------------------
        msg = template.render(slides=self.slides,
                              header=self.header)
        #---------------------------------------------#
        #             Render the report               # 
        #---------------------------------------------#
        with open(outname, 'w') as f:
            f.write(msg)
        return None

@dataclass
class PlotlyFigure:
    figure : Any
    def __post_init__(self):
        plotly_html_args = dict(full_html=False, include_mathjax=False, include_plotlyjs=False)
        self.figure = self.figure.to_html(**plotly_html_args)

@dataclass
class Styler:
    style : dict
    def __post_init__(self):
        self.to_string = ''.join([item+':'+value+';' for item,value in self.style.items()])

@dataclass
class Slide:
    layout : str
    

