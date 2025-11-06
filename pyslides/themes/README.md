# Custom Themes for pySlides

This directory contains custom CSS themes for corporate branding and styling.

## Using Custom Themes

You can use a custom theme by reading the CSS file and passing it to the `custom_css` parameter:

```python
import pyslides as pys

# Read custom theme
with open('pyslides/themes/corporate_blue.css', 'r') as f:
    custom_css = f.read()

# Create presentation with custom theme
slides = pys.Slides(
    title="My Presentation",
    theme='white',  # Base theme
    custom_css=custom_css  # Custom branding
)
```

## Available Custom Themes

### corporate_blue.css
Professional theme with blue branding. Perfect for corporate presentations.

**Colors:**
- Primary: #0066CC (Blue)
- Secondary: #004D99 (Dark Blue)
- Accent: #00A3E0 (Light Blue)

### corporate_minimal.css
Clean, minimalist theme for professional presentations.

**Colors:**
- Primary: #1a1a1a (Almost Black)
- Accent: #e74c3c (Red)
- Background: #fafafa (Light Gray)

## Creating Your Own Theme

To create a custom theme:

1. Create a new CSS file in this directory
2. Define CSS custom properties (variables) for colors
3. Customize the `.reveal` class and its child elements
4. Load the CSS file in your presentation

### CSS Structure

```css
:root {
    --primary-color: #YOUR_COLOR;
    --secondary-color: #YOUR_COLOR;
    --accent-color: #YOUR_COLOR;
}

.reveal {
    /* Global styles */
}

.reveal h1, .reveal h2 {
    /* Heading styles */
}

.reveal p {
    /* Paragraph styles */
}
```

## Corporate Branding Checklist

When customizing for your organization:

- [ ] Update color scheme to match brand colors
- [ ] Change fonts to corporate typeface
- [ ] Add company logo (use custom HTML in slides)
- [ ] Adjust spacing and sizing for readability
- [ ] Test on different screen sizes
- [ ] Ensure sufficient color contrast for accessibility
