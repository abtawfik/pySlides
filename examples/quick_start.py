"""
Quick Start Example for pySlides 2.0

A minimal example to get you started quickly.
"""

import sys
sys.path.insert(0, '..')

import pyslides as pys
import plotly.graph_objects as go

# Create a presentation
slides = pys.Slides(
    title="Quick Start Demo",
    theme="white"
)

# Add a title slide
slides.add_slide(
    layout='title',
    title="Welcome to pySlides",
    subtitle="Create presentations in minutes"
)

# Add a content slide
slides.add_slide(
    title="Why pySlides?",
    content="""
    <ul>
        <li>Easy to use Python API</li>
        <li>Interactive visualizations</li>
        <li>Beautiful themes</li>
        <li>Export to PDF</li>
    </ul>
    """
)

# Add a slide with a chart
fig = go.Figure(data=[
    go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr'], y=[10, 15, 13, 17])
])
fig.update_layout(title='Monthly Growth', height=500)

slides.add_slide(
    title="Interactive Charts",
    figure=fig
)

# Save the presentation
slides.save("quick_start.html")
print("✓ Presentation saved to quick_start.html")
print("Open it in your browser to view!")
