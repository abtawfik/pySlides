"""
pySlides - Create beautiful, interactive HTML presentations with Python

Modern slide deck generation using Reveal.js framework
"""

######################
# Standard libraries #
######################
from dataclasses import dataclass
from typing import Any, Optional, Dict, List, Union
from pathlib import Path
import base64
from io import BytesIO

###################
# HTML templating #
###################
from jinja2 import Environment, PackageLoader

# Optional imports for visualization support
try:
    import plotly.graph_objects as go
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

try:
    import matplotlib.figure
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


class Slides:
    """
    Main class for creating slide presentations.

    Parameters
    ----------
    title : str, optional
        Presentation title
    author : str, optional
        Author name
    description : str, optional
        Presentation description
    theme : str, optional
        Reveal.js theme name. Options: 'black', 'white', 'league', 'beige',
        'sky', 'night', 'serif', 'simple', 'solarized', 'blood', 'moon'
        Default: 'black'
    custom_css : str, optional
        Custom CSS to inject into the presentation
    config : dict, optional
        Reveal.js configuration options

    Examples
    --------
    >>> slides = Slides(title="My Presentation", theme="white")
    >>> slides.add_slide(title="Introduction", content="Hello World!")
    >>> slides.save("presentation.html")
    """

    AVAILABLE_THEMES = [
        'black', 'white', 'league', 'beige', 'sky',
        'night', 'serif', 'simple', 'solarized', 'blood', 'moon'
    ]

    def __init__(
        self,
        title: Optional[str] = None,
        author: Optional[str] = None,
        description: Optional[str] = None,
        theme: str = 'black',
        custom_css: Optional[str] = None,
        config: Optional[Dict] = None
    ):
        self.header = {
            'title': title or 'PySlides Presentation',
            'author': author or '',
            'description': description or 'Interactive presentation created with pySlides'
        }

        if theme not in self.AVAILABLE_THEMES:
            print(f"Warning: Theme '{theme}' not recognized. Using 'black'. Available: {self.AVAILABLE_THEMES}")
            theme = 'black'

        self.theme = theme
        self.custom_css = custom_css
        self.config = config or {}
        self.slides = []

    def add_slide(
        self,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        content: Optional[str] = None,
        layout: str = 'default',
        figure: Optional[Any] = None,
        notes: Optional[str] = None,
        background: Optional[str] = None,
        background_color: Optional[str] = None,
        transition: Optional[str] = None,
        **kwargs
    ):
        """
        Add a slide to the presentation.

        Parameters
        ----------
        title : str, optional
            Slide title
        subtitle : str, optional
            Slide subtitle
        content : str, optional
            Slide content (supports HTML)
        layout : str, optional
            Slide layout. Options: 'default', 'title', 'two-column', 'image-left', 'image-right'
        figure : plotly.graph_objects.Figure or matplotlib.figure.Figure, optional
            Interactive figure to embed
        notes : str, optional
            Speaker notes (visible in presenter mode)
        background : str, optional
            Background image URL
        background_color : str, optional
            Background color (e.g., '#FF0000' or 'rgb(255, 0, 0)')
        transition : str, optional
            Slide transition effect: 'none', 'fade', 'slide', 'convex', 'concave', 'zoom'
        **kwargs : dict
            Additional layout-specific parameters

        Returns
        -------
        self : Slides
            Returns self for method chaining

        Examples
        --------
        >>> slides.add_slide(title="Welcome", content="<p>Hello!</p>")
        >>> slides.add_slide(
        ...     title="Two Columns",
        ...     layout='two-column',
        ...     content_left="Left side",
        ...     content_right="Right side"
        ... )
        """
        slide = {
            'title': title,
            'subtitle': subtitle,
            'content': content,
            'layout': layout,
            'notes': notes,
            'background': background,
            'background_color': background_color,
            'transition': transition
        }

        # Handle figure conversion
        if figure is not None:
            slide['figure'] = self._convert_figure(figure)

        # Add layout-specific parameters
        for key, value in kwargs.items():
            slide[key] = value

        # Remove None values
        slide = {k: v for k, v in slide.items() if v is not None}

        self.slides.append(slide)
        return self

    # Convenience method for backward compatibility
    def add(self, **kwargs):
        """Legacy method for adding slides (backward compatibility)"""
        # Convert old parameter names
        if 'head_style' in kwargs:
            kwargs.pop('head_style')  # No longer needed with Reveal.js
        return self.add_slide(**kwargs)

    def _convert_figure(self, figure: Any) -> str:
        """Convert various figure types to HTML"""

        # Plotly figure
        if HAS_PLOTLY and isinstance(figure, go.Figure):
            return PlotlyFigure(figure).to_html()

        # Matplotlib figure
        if HAS_MATPLOTLIB and isinstance(figure, matplotlib.figure.Figure):
            return MatplotlibFigure(figure).to_html()

        # Already HTML string
        if isinstance(figure, str):
            return figure

        raise ValueError(f"Unsupported figure type: {type(figure)}")

    def save(self, output_path: str):
        """
        Save the presentation to an HTML file.

        Parameters
        ----------
        output_path : str
            Path to output HTML file

        Examples
        --------
        >>> slides.save("presentation.html")
        """
        # Create Jinja2 template environment
        file_loader = PackageLoader(__name__, 'data')
        env = Environment(loader=file_loader)
        template = env.get_template('base.html')

        # Render template
        html_content = template.render(
            slides=self.slides,
            header=self.header,
            theme=self.theme,
            custom_css=self.custom_css,
            config=self.config
        )

        # Write to file
        output_file = Path(output_path)
        output_file.write_text(html_content, encoding='utf-8')

        print(f"✓ Presentation saved to: {output_path}")
        return None

    def export_pdf(self, output_path: str, html_path: Optional[str] = None):
        """
        Export presentation to PDF (requires playwright).

        Parameters
        ----------
        output_path : str
            Path to output PDF file
        html_path : str, optional
            Path to HTML file (if None, will save to temp file first)

        Examples
        --------
        >>> slides.export_pdf("presentation.pdf")
        """
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise ImportError(
                "PDF export requires playwright. Install with: "
                "pip install pyslides[export]"
            )

        # Save HTML first if not provided
        if html_path is None:
            html_path = output_path.replace('.pdf', '.html')
            self.save(html_path)

        # Convert to PDF using Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file://{Path(html_path).absolute()}?print-pdf")
            page.wait_for_timeout(2000)  # Wait for content to load
            page.pdf(path=output_path, format='A4', landscape=True)
            browser.close()

        print(f"✓ PDF exported to: {output_path}")


@dataclass
class PlotlyFigure:
    """Convert Plotly figure to HTML"""
    figure: Any

    def to_html(self) -> str:
        """Convert to HTML string"""
        plotly_html_args = dict(
            full_html=False,
            include_mathjax=False,
            include_plotlyjs=False,
            config={'responsive': True}
        )
        return self.figure.to_html(**plotly_html_args)


@dataclass
class MatplotlibFigure:
    """Convert Matplotlib figure to HTML (as base64 encoded image)"""
    figure: Any

    def to_html(self) -> str:
        """Convert to HTML img tag with base64 encoded data"""
        buffer = BytesIO()
        self.figure.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        return f'<img src="data:image/png;base64,{image_base64}" style="max-width: 100%; height: auto;" />'


@dataclass
class Styler:
    """Convert style dict to CSS string"""
    style: dict

    def __post_init__(self):
        self.to_string = ''.join([f'{item}:{value};' for item, value in self.style.items()])
    

