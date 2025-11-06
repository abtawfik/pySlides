"""
pySlides 2.0 Demo Presentation

This example demonstrates all the features of the modernized pySlides library,
including:
- Multiple layout types
- Interactive Plotly charts
- Matplotlib figures
- Custom themes
- Speaker notes
- Background customization
- PDF export
"""

import sys
sys.path.insert(0, '..')

import pyslides as pys
import plotly.graph_objects as go

# Create a presentation with custom configuration
slides = pys.Slides(
    title="pySlides 2.0 Demo",
    author="Your Name",
    description="Demonstrating modern HTML presentations with Python",
    theme='white',  # Available: black, white, league, beige, sky, night, serif, simple, solarized, blood, moon
    config={
        'transition': 'slide',  # none/fade/slide/convex/concave/zoom
        'controls': True,
        'progress': True,
        'slide_number': True,
        'width': 1920,
        'height': 1080
    }
)

# ==========================================
# Slide 1: Title Slide
# ==========================================
slides.add_slide(
    layout='title',
    title="pySlides 2.0",
    subtitle="Modern HTML Presentations with Python",
    author="Built with Reveal.js 5.1.0",
    background_color='#0066CC',
    notes="Welcome! Press 'S' to open speaker notes view."
)

# ==========================================
# Slide 2: Introduction
# ==========================================
slides.add_slide(
    title="What is pySlides?",
    content="""
    <p>A modern Python library for creating beautiful, interactive HTML presentations.</p>
    <ul>
        <li>🚀 Powered by Reveal.js 5.1.0</li>
        <li>📊 Interactive Plotly & Matplotlib charts</li>
        <li>🎨 Multiple themes and custom branding</li>
        <li>📱 Responsive and mobile-friendly</li>
        <li>📄 Export to PDF</li>
        <li>🗣️ Speaker notes support</li>
    </ul>
    """,
    notes="Highlight the key features and improvements over the old version."
)

# ==========================================
# Slide 3: Interactive Plotly Chart
# ==========================================
# Create an interactive Plotly chart
fig_bar = go.Figure(data=[
    go.Bar(name='Q1', x=['Product A', 'Product B', 'Product C'], y=[20, 14, 23]),
    go.Bar(name='Q2', x=['Product A', 'Product B', 'Product C'], y=[25, 18, 26]),
    go.Bar(name='Q3', x=['Product A', 'Product B', 'Product C'], y=[30, 22, 29]),
])
fig_bar.update_layout(
    title='Quarterly Sales Performance',
    barmode='group',
    height=500,
    margin=dict(l=50, r=50, t=80, b=50)
)

slides.add_slide(
    title="Interactive Charts",
    subtitle="Hover over the bars to see details!",
    figure=fig_bar,
    notes="This is a fully interactive Plotly chart. Users can zoom, pan, and hover to see details."
)

# ==========================================
# Slide 4: Two-Column Layout
# ==========================================
# Create a scatter plot for the two-column layout
fig_scatter = go.Figure(data=[
    go.Scatter(x=[1, 2, 3, 4, 5], y=[10, 11, 12, 13, 14], mode='lines+markers', name='Revenue')
])
fig_scatter.update_layout(
    title='Growth Trend',
    xaxis_title='Month',
    yaxis_title='Revenue ($M)',
    height=400,
    margin=dict(l=50, r=50, t=80, b=50)
)

slides.add_slide(
    title="Two-Column Layout",
    layout='two-column',
    content_left="""
    <h3>Key Features</h3>
    <ul>
        <li>Flexible layouts</li>
        <li>Mix text and visuals</li>
        <li>Responsive design</li>
        <li>Easy to customize</li>
    </ul>
    <p style="color: #666; font-size: 0.9em; margin-top: 1em;">
    Perfect for comparing information side-by-side.
    </p>
    """,
    figure_right=fig_scatter,
    notes="Two-column layout allows you to present information and visualizations side by side."
)

# ==========================================
# Slide 5: Image Left Layout
# ==========================================
# Create a pie chart
fig_pie = go.Figure(data=[go.Pie(
    labels=['Desktop', 'Mobile', 'Tablet'],
    values=[45, 40, 15],
    hole=.3
)])
fig_pie.update_layout(
    title='Traffic Distribution',
    height=450,
    margin=dict(l=50, r=50, t=80, b=50)
)

slides.add_slide(
    title="Different Layout Options",
    subtitle="Image on the left, content on the right",
    layout='image-left',
    figure=fig_pie,
    content="""
    <p>pySlides supports multiple layout types:</p>
    <ul>
        <li><strong>default</strong> - Standard single-column</li>
        <li><strong>title</strong> - Title slide</li>
        <li><strong>two-column</strong> - Equal columns</li>
        <li><strong>image-left</strong> - Visual on left</li>
        <li><strong>image-right</strong> - Visual on right</li>
    </ul>
    """,
    notes="You can choose the layout that best fits your content."
)

# ==========================================
# Slide 6: Matplotlib Support
# ==========================================
try:
    import matplotlib.pyplot as plt
    import numpy as np

    # Create a matplotlib figure
    fig_mpl, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), label='sin(x)', linewidth=2)
    ax.plot(x, np.cos(x), label='cos(x)', linewidth=2)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Matplotlib Integration')
    ax.legend()
    ax.grid(True, alpha=0.3)

    slides.add_slide(
        title="Matplotlib Support",
        subtitle="Both Plotly and Matplotlib are supported",
        figure=fig_mpl,
        notes="Matplotlib figures are automatically converted to high-quality PNG images."
    )

    plt.close(fig_mpl)
except ImportError:
    print("Matplotlib not available, skipping matplotlib slide")

# ==========================================
# Slide 7: Custom Backgrounds
# ==========================================
slides.add_slide(
    title="Custom Backgrounds",
    content="""
    <p style="color: white;">You can customize slide backgrounds with:</p>
    <ul style="color: white;">
        <li>Solid colors</li>
        <li>Gradients</li>
        <li>Images (URLs)</li>
        <li>Videos</li>
    </ul>
    """,
    background_color='#2C3E50',
    transition='zoom',
    notes="Each slide can have its own background and transition effect."
)

# ==========================================
# Slide 8: Custom Themes
# ==========================================
slides.add_slide(
    title="Theming & Branding",
    content="""
    <h3>Built-in Themes</h3>
    <p>Choose from 11 built-in Reveal.js themes:</p>
    <p style="background: #f0f0f0; padding: 10px; border-radius: 5px; font-family: monospace;">
    black, white, league, beige, sky, night, serif, simple, solarized, blood, moon
    </p>

    <h3 style="margin-top: 1em;">Custom CSS</h3>
    <p>Or create your own theme with custom CSS for corporate branding:</p>
    <ul>
        <li>Custom colors and fonts</li>
        <li>Company logos</li>
        <li>Brand-specific styling</li>
    </ul>
    <p style="color: #666; font-size: 0.9em; margin-top: 1em;">
    See <code>pyslides/themes/</code> for examples!
    </p>
    """,
    notes="Theming is flexible - use built-in themes or create custom corporate themes."
)

# ==========================================
# Slide 9: Features Overview
# ==========================================
slides.add_slide(
    title="Key Features",
    layout='two-column',
    content_left="""
    <h3>📊 Visualizations</h3>
    <ul>
        <li>Plotly (interactive)</li>
        <li>Matplotlib (static)</li>
        <li>HTML/SVG support</li>
    </ul>

    <h3 style="margin-top: 1em;">🎨 Customization</h3>
    <ul>
        <li>11 built-in themes</li>
        <li>Custom CSS</li>
        <li>Flexible layouts</li>
    </ul>
    """,
    content_right="""
    <h3>⚙️ Configuration</h3>
    <ul>
        <li>Transitions & effects</li>
        <li>Speaker notes</li>
        <li>Slide numbers</li>
    </ul>

    <h3 style="margin-top: 1em;">📤 Export</h3>
    <ul>
        <li>HTML (always)</li>
        <li>PDF (built-in)</li>
        <li>Works offline</li>
    </ul>
    """,
    notes="Comprehensive feature set for professional presentations."
)

# ==========================================
# Slide 10: PDF Export
# ==========================================
slides.add_slide(
    title="Export to PDF",
    content="""
    <p>Presentations can be exported to PDF with one line of code:</p>
    <pre style="background: #f5f5f5; padding: 20px; border-radius: 5px;"><code>slides.export_pdf("presentation.pdf")</code></pre>

    <p style="margin-top: 1em;">Requirements:</p>
    <ul>
        <li>Install export dependencies: <code>pip install pyslides[export]</code></li>
        <li>Uses Playwright for high-quality PDF generation</li>
        <li>Maintains layout and styling (interactive charts become static)</li>
    </ul>

    <p style="color: #666; font-size: 0.9em; margin-top: 1em;">
    <strong>Note:</strong> PDF export is optional. HTML presentations work everywhere without extra dependencies.
    </p>
    """,
    notes="PDF export is great for sharing presentations offline or via email."
)

# ==========================================
# Slide 11: Getting Started
# ==========================================
slides.add_slide(
    title="Getting Started",
    content="""
    <h3>Installation</h3>
    <pre style="background: #f5f5f5; padding: 15px; border-radius: 5px;"><code>pip install pyslides</code></pre>

    <h3 style="margin-top: 1em;">Basic Example</h3>
    <pre style="background: #f5f5f5; padding: 15px; border-radius: 5px;"><code>import pyslides as pys

slides = pys.Slides(title="My Presentation", theme="white")

slides.add_slide(
    title="Hello World",
    content="&lt;p&gt;My first slide!&lt;/p&gt;"
)

slides.save("presentation.html")</code></pre>

    <p style="margin-top: 1em;">That's it! Open the HTML file in your browser.</p>
    """,
    notes="Getting started is quick and easy. Just install and start creating slides."
)

# ==========================================
# Slide 12: Thank You
# ==========================================
slides.add_slide(
    layout='title',
    title="Thank You!",
    subtitle="Start creating beautiful presentations with pySlides 2.0",
    content="""
    <p style="margin-top: 2em;">
        <a href="https://github.com/yourusername/pyslides" style="font-size: 1.5em;">
            github.com/yourusername/pyslides
        </a>
    </p>
    """,
    background_color='#2C3E50',
    notes="Thank you slide. Encourage questions and feedback."
)

# ==========================================
# Save the presentation
# ==========================================
print("Generating presentation...")
slides.save("demo_presentation.html")
print("✓ Demo presentation created!")
print("\nNext steps:")
print("1. Open 'demo_presentation.html' in your browser")
print("2. Press 'S' for speaker notes")
print("3. Press 'F' for fullscreen")
print("4. Use arrow keys to navigate")
print("\nTo export to PDF:")
print("pip install pyslides[export]")
print("Then uncomment the line below:")
# slides.export_pdf("demo_presentation.pdf")
