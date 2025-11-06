# pySlides 2.0

**Create beautiful, interactive HTML presentations with Python**

pySlides is a modern Python library for creating stunning slide decks with interactive visualizations, custom themes, and professional layouts. Built on **Reveal.js 5.1.0**, it's perfect for data scientists, researchers, and anyone who wants to create engaging presentations programmatically.

## ✨ Features

- 📊 **Interactive Visualizations** - Embed Plotly and Matplotlib charts
- 🎨 **Beautiful Themes** - 11 built-in themes + custom CSS support
- 📐 **Flexible Layouts** - Title, two-column, image-left, image-right, and more
- 🗣️ **Speaker Notes** - Built-in presenter view with notes
- 📄 **PDF Export** - One-line export to PDF
- 🌐 **Modern & Maintained** - Built on Reveal.js 5.1.0 (2024)
- 📱 **Responsive** - Works on desktop, tablet, and mobile
- 🔌 **Works Offline** - Optional bundling of all assets
- 🚀 **Easy to Use** - Simple, intuitive Python API

## 🎯 What's New in 2.0?

pySlides 2.0 is a complete rewrite with modern dependencies:

- ✅ Migrated from WebSlides (unmaintained) to **Reveal.js 5.1.0**
- ✅ Updated all dependencies (Jinja2 3.x, Plotly 5.x)
- ✅ Added support for **Matplotlib** figures
- ✅ New flexible layout system
- ✅ Speaker notes support
- ✅ Built-in PDF export
- ✅ Custom theming for corporate branding
- ✅ Better documentation and examples

## 📦 Installation

```bash
# Basic installation
pip install pyslides

# With PDF export support
pip install pyslides[export]

# Development installation
pip install pyslides[dev]
```

## 🚀 Quick Start

```python
import pyslides as pys

# Create a presentation
slides = pys.Slides(
    title="My Presentation",
    theme="white"  # black, white, league, beige, sky, night, serif, simple, solarized, blood, moon
)

# Add a title slide
slides.add_slide(
    layout='title',
    title="Welcome to pySlides",
    subtitle="Modern presentations with Python"
)

# Add a content slide
slides.add_slide(
    title="Key Features",
    content="""
    <ul>
        <li>Interactive visualizations</li>
        <li>Beautiful themes</li>
        <li>Export to PDF</li>
    </ul>
    """
)

# Save the presentation
slides.save("presentation.html")
```

Open `presentation.html` in your browser and use arrow keys to navigate!

## 📊 Interactive Charts

### Plotly

```python
import plotly.graph_objects as go

# Create an interactive chart
fig = go.Figure(data=[
    go.Bar(name='Q1', x=['A', 'B', 'C'], y=[20, 14, 23]),
    go.Bar(name='Q2', x=['A', 'B', 'C'], y=[25, 18, 26])
])
fig.update_layout(title='Sales by Quarter', barmode='group')

# Add to presentation
slides.add_slide(
    title="Quarterly Sales",
    figure=fig
)
```

### Matplotlib

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a matplotlib figure
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')
ax.legend()
ax.set_title('Trigonometric Functions')

# Add to presentation
slides.add_slide(
    title="Math Visualization",
    figure=fig
)
```

## 📐 Layout Options

pySlides supports multiple layout types:

### Two-Column Layout

```python
slides.add_slide(
    title="Comparison",
    layout='two-column',
    content_left="<p>Left column content</p>",
    content_right="<p>Right column content</p>"
)
```

### Image Left/Right

```python
slides.add_slide(
    title="Data Analysis",
    layout='image-right',
    content="<p>Analysis details here...</p>",
    figure=my_chart  # Plotly or Matplotlib figure
)
```

## 🎨 Themes & Styling

### Built-in Themes

Choose from 11 professionally designed themes:

```python
slides = pys.Slides(
    title="My Presentation",
    theme="solarized"  # black, white, league, beige, sky, night, serif, simple, solarized, blood, moon
)
```

### Custom CSS for Corporate Branding

```python
# Load custom theme
with open('pyslides/themes/corporate_blue.css', 'r') as f:
    custom_css = f.read()

slides = pys.Slides(
    title="Company Presentation",
    theme="white",
    custom_css=custom_css  # Apply corporate branding
)
```

See `pyslides/themes/` for example custom themes!

## 🗣️ Speaker Notes

Add speaker notes that appear in presenter view (press `S` during presentation):

```python
slides.add_slide(
    title="Important Topic",
    content="<p>Key points...</p>",
    notes="Remember to mention the Q3 results and the new strategy."
)
```

## 🎬 Customization

### Slide Backgrounds

```python
# Solid color background
slides.add_slide(
    title="Custom Background",
    background_color="#2C3E50",
    content="<p style='color: white;'>Content here</p>"
)

# Image background
slides.add_slide(
    title="Image Background",
    background="https://example.com/image.jpg"
)
```

### Transitions

```python
slides.add_slide(
    title="Animated Slide",
    transition="zoom",  # none, fade, slide, convex, concave, zoom
    content="<p>This slide zooms in!</p>"
)
```

### Global Configuration

```python
slides = pys.Slides(
    title="My Presentation",
    theme="black",
    config={
        'transition': 'slide',
        'controls': True,
        'progress': True,
        'slide_number': True,
        'width': 1920,
        'height': 1080
    }
)
```

## 📄 Export to PDF

```python
# Requires: pip install pyslides[export]

slides.save("presentation.html")
slides.export_pdf("presentation.pdf")
```

## 📚 Examples

Check out the `examples/` directory:

- **quick_start.py** - Minimal example to get started
- **demo_presentation.py** - Comprehensive demo of all features

Run an example:

```bash
cd examples
python demo_presentation.py
```

## ⌨️ Keyboard Shortcuts (During Presentation)

- **Arrow keys** - Navigate slides
- **F** - Fullscreen
- **S** - Speaker notes view
- **O** - Overview mode
- **B** or **.** - Pause (black screen)
- **ESC** - Exit fullscreen/overview

## 🔧 Requirements

- Python 3.7+
- Internet connection (for CDN resources) or offline mode
- For PDF export: Playwright (installed with `[export]` extra)

## 📖 Documentation

### Main Class: `Slides`

```python
Slides(
    title: str = None,
    author: str = None,
    description: str = None,
    theme: str = 'black',
    custom_css: str = None,
    config: dict = None
)
```

### Adding Slides: `add_slide()`

```python
slides.add_slide(
    title: str = None,
    subtitle: str = None,
    content: str = None,
    layout: str = 'default',  # 'title', 'two-column', 'image-left', 'image-right'
    figure: Any = None,  # Plotly or Matplotlib figure
    notes: str = None,
    background: str = None,
    background_color: str = None,
    transition: str = None,
    **kwargs  # Layout-specific parameters
)
```

### Saving: `save()` and `export_pdf()`

```python
slides.save("presentation.html")
slides.export_pdf("presentation.pdf")  # Requires playwright
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📜 License

pySlides is completely free and open-source and licensed under the MIT license.

## 🙏 Credits

- Built on [Reveal.js](https://revealjs.com/) by Hakim El Hattab
- Uses [Plotly](https://plotly.com/) for interactive charts
- Uses [Matplotlib](https://matplotlib.org/) for static visualizations

---

**Made with ❤️ for the Python community**
