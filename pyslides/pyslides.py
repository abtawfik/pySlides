######################
# Standard libraries #
######################
import dataclasses import dataclass

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
        self.header = header
        self.styles = styles
        self.slides = []
        
    def add(self, title, content, layout, figure):
        self.slides += [{'title':title, 'content':content, 'layout':layout, 'figure':figure}]
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
        env = Environment(loader=file_loader,
                          autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('base.html')
        plotly_html_args = dict(full_html=False, include_mathjax=False, include_plotlyjs=False)
        #--------------------------------
        # Render and output slides
        #--------------------------------
        msg = template.render(slides=self.slides)
        #---------------------------------------------#
        #             Render the report               # 
        #---------------------------------------------#
        with open(outname, 'w') as f:
            f.write(msg)
        return None


@dataclass
class Slide:
    layout : str
    


