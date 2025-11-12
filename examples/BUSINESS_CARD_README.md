# Full Stack Science Business Card Generator

A professional, print-ready digital business card generator that adheres to Full Stack Science brand guidelines and is optimized for both digital sharing and physical printing.

![Full Stack Science Brand](https://img.shields.io/badge/Full_Stack_Science-Brand_Compliant-0A1628?style=for-the-badge)
![Print Ready](https://img.shields.io/badge/Print-Ready-F97316?style=for-the-badge)
![Interactive](https://img.shields.io/badge/Interactive-HTML-3D4656?style=for-the-badge)

---

## 📋 Overview

This business card generator creates professional, brand-compliant business cards for Full Stack Science team members. The cards are:

- **Print-ready**: 3.5" × 2" @ 300dpi (1050px × 600px)
- **Customizable**: Real-time editing of contact information
- **Professional**: Follows Full Stack Science brand guidelines
- **Exportable**: PDF and PNG export capabilities
- **Dual-sided**: Front and back designs included

---

## 🎨 Brand Guidelines

### Colors

| Color | Hex Code | Usage |
|-------|----------|-------|
| Navy Blue | `#0A1628` | Primary brand color, main text |
| Professional Orange | `#F97316` | Accent elements, highlights |
| White | `#FFFFFF` | Background |
| Charcoal | `#3D4656` | Secondary text |

### Typography

- **Display/Headers**: JetBrains Mono (bold, monospace)
- **Body Text**: Inter (clean, professional sans-serif)

### Design Elements

- **Logo**: Geometric triangle in navy, light blue, and orange
- **Tagline**: "Turning Data Into Value"
- **Accent**: 6px orange gradient line on left edge
- **Pattern**: Subtle grid pattern at 3% opacity

---

## 🚀 Quick Start

### Option 1: Standalone HTML (Recommended)

1. Open `business_card_generator.html` in your web browser
2. Customize your information in the form fields
3. Click "Flip Card" to preview both sides
4. Export as PDF or PNG

```bash
# Simply open in your browser
open examples/business_card_generator.html

# Or with Python
python -m http.server 8000
# Then visit: http://localhost:8000/examples/business_card_generator.html
```

### Option 2: Python Integration

Use the provided Python example to integrate with pySlides:

```python
from examples.business_card_example import generate_custom_card

# Generate a custom card
card_html = generate_custom_card(
    name="Your Name",
    title="Your Title",
    email="your.email@fullstackscience.com",
    phone="+1 (555) 000-0000",
    website="fullstackscience.com"
)
```

---

## 📐 Specifications

### Physical Dimensions

- **Size**: 3.5" × 2" (standard US business card)
- **Resolution**: 1050px × 600px @ 300dpi
- **Safe Area**: 0.1" margin on all sides (30px @ 300dpi)

### Card Layout

#### Front Side (70/30 Split)

**Left Section (70%)**:
- Full Stack Science logo (top)
- Name (large, bold, JetBrains Mono)
- Title (medium, Inter)
- Tagline (small, orange, uppercase)

**Right Section (30%)**:
- Email (with icon)
- Phone (with icon)
- Website (with icon)

**Accent Element**:
- 6px orange gradient line on left edge
- Subtle grid pattern background (3% opacity)

#### Back Side (Centered)

- Large logo (200px)
- Company name (JetBrains Mono, 48px)
- Tagline (orange, uppercase)
- Decorative orange line
- Subtitle with value propositions

---

## 🖨️ Export Instructions

### Export as PDF (For Printing)

1. Click the **"Print / Export PDF"** button
2. In the print dialog:
   - Set **Destination** to "Save as PDF"
   - Set **Paper size** to "Custom" (3.5" × 2")
   - Set **Margins** to "None"
   - Enable **Background graphics**
3. Save the PDF file
4. Send to professional printer or print on cardstock

### Export as PNG (For Digital Use)

1. Click the **"Download as PNG"** button
2. The card will be saved as a 1050×600px PNG image
3. Use for:
   - Email signatures
   - Social media profiles
   - Digital portfolios
   - Website contact pages

### Professional Printing Tips

- **Cardstock**: Use minimum 300gsm (14pt) cardstock
- **Finish**: Matte or silk finish recommended for professional look
- **Color Profile**: CMYK for professional printing
- **Bleed**: Add 0.125" bleed if required by printer
- **Quantity**: Most printers offer discounts at 250+ cards

---

## 🎯 Features

### Interactive Customization

- Real-time form editing
- Instant card preview
- No page reload required
- Front/back card flip animation

### Brand Compliance

✅ Official Full Stack Science colors
✅ Approved typography (JetBrains Mono + Inter)
✅ Professional geometric triangle logo
✅ "Turning Data Into Value" tagline
✅ Clean, minimal design aesthetic

### Export Options

- **PDF**: Print-ready, exact dimensions
- **PNG**: High-resolution (300dpi)
- **Screenshot**: Direct browser capture
- **Print**: Direct to printer support

### Accessibility

- High contrast text (WCAG compliant)
- Readable at small sizes
- Clear visual hierarchy
- Semantic HTML structure

---

## 📝 Customization Guide

### Editing Contact Information

The form allows you to customize:

1. **Full Name**: Your complete name (appears in large JetBrains Mono font)
2. **Title**: Your role or position (appears below name)
3. **Email**: Professional email address
4. **Phone**: Contact phone number (format: +1 (XXX) XXX-XXXX)
5. **Website**: Company or personal website

### Default Values

```
Name: Sarah Chen
Title: Senior ML Consultant
Email: sarah@fullstackscience.com
Phone: +1 (650) 555-0142
Website: fullstackscience.com
```

### Advanced Customization

To modify the HTML directly:

```html
<!-- Edit the card content in business_card_generator.html -->
<h1 id="cardName">Your Name Here</h1>
<p id="cardTitle">Your Title Here</p>
```

---

## 🔧 Technical Details

### Dependencies

- **Tailwind CSS**: Via CDN (styling framework)
- **Google Fonts**: Inter and JetBrains Mono
- **html2canvas**: For PNG export (loaded dynamically)

### Browser Compatibility

- ✅ Chrome/Edge (recommended for export)
- ✅ Firefox
- ✅ Safari
- ✅ Modern browsers with ES6 support

### File Structure

```
examples/
├── business_card_generator.html    # Main standalone generator
├── business_card_example.py        # Python integration example
└── BUSINESS_CARD_README.md        # This documentation
```

### Print Styles

The HTML includes optimized `@media print` styles:

```css
@media print {
    @page {
        size: 3.5in 2in;
        margin: 0;
    }
    .no-print { display: none; }
    .safe-area-guide { display: none; }
}
```

---

## 📊 Use Cases

### 1. Individual Business Cards

Perfect for Full Stack Science team members who need professional business cards with their personal contact information.

### 2. Event Materials

Generate cards for conferences, meetups, and networking events. Export as PNG for digital event platforms.

### 3. Email Signatures

Download PNG version and embed in email signatures for a professional touch.

### 4. Presentation Materials

Integrate into pySlides presentations using the Python example.

### 5. Client Meetings

Print high-quality cards for in-person client meetings and consultations.

---

## 🎓 Examples

### Example 1: Basic Usage

```python
# Generate a card with default styling
from business_card_example import generate_custom_card

card = generate_custom_card(
    name="Alex Johnson",
    title="Data Scientist",
    email="alex@fullstackscience.com",
    phone="+1 (555) 123-4567"
)
```

### Example 2: Integration with pySlides

```python
from pyslides import Presentation, Slide
from business_card_example import generate_custom_card

pres = Presentation(title="Team Directory")
slide = Slide(title="Contact Information")

# Add custom business card to slide
card_html = generate_custom_card(
    name="Dr. Maria Garcia",
    title="Chief AI Architect",
    email="maria@fullstackscience.com",
    phone="+1 (555) 987-6543"
)

slide.add_html(card_html)
pres.add_slide(slide)
pres.save("team_directory.html")
```

### Example 3: Batch Generation

```python
# Generate cards for entire team
team_members = [
    {"name": "John Doe", "title": "ML Engineer", "email": "john@fss.com", "phone": "+1 (555) 111-1111"},
    {"name": "Jane Smith", "title": "Data Analyst", "email": "jane@fss.com", "phone": "+1 (555) 222-2222"},
    # ... more team members
]

for member in team_members:
    card = generate_custom_card(**member)
    # Process or save each card
```

---

## ❓ FAQ

### Q: Can I change the colors?

**A**: The colors are part of Full Stack Science brand guidelines and should remain consistent. However, you can modify the HTML/CSS if needed for special use cases.

### Q: What if I don't have the logo file?

**A**: The HTML includes an embedded SVG geometric triangle logo that matches the brand guidelines.

### Q: How do I add a QR code?

**A**: You can add a QR code to the back of the card by:
1. Generating a QR code (vCard format recommended)
2. Adding an `<img>` tag to the `.card-back` section
3. Positioning it in the desired location

### Q: Can I make the text smaller to fit more information?

**A**: While possible, it's not recommended. Business cards should be readable at small sizes. Stick to essential contact information only.

### Q: Is this compatible with Vistaprint, Moo, etc.?

**A**: Yes! Export as PDF with proper dimensions (3.5" × 2") and upload to any professional printing service.

### Q: Can I make double-sided prints?

**A**: Yes! The generator includes both front and back designs. Most printers support duplex printing with the provided PDF.

---

## 🐛 Troubleshooting

### Issue: PDF export cuts off content

**Solution**: Ensure print settings have:
- Margins set to "None"
- Scale set to 100%
- Background graphics enabled

### Issue: PNG download not working

**Solution**: The tool automatically loads html2canvas library. Ensure you have internet connection for CDN access.

### Issue: Fonts look different

**Solution**:
- Ensure internet connection for Google Fonts
- Wait for fonts to fully load before exporting
- Use Chrome/Edge for best font rendering

### Issue: Colors look different when printed

**Solution**:
- Use professional printing service with CMYK color profile
- Request color proof before full print run
- Specify that colors match Pantone equivalents if needed

---

## 📄 License

This business card generator is part of the pySlides project and follows the same license terms.

---

## 🤝 Contributing

To improve the business card generator:

1. Test on various browsers and devices
2. Suggest design improvements that maintain brand compliance
3. Report bugs or issues
4. Contribute additional export formats or features

---

## 📞 Support

For questions or assistance:

- **Documentation**: See this README
- **Examples**: Check `business_card_example.py`
- **Issues**: Open GitHub issue on pySlides repository

---

## ✅ Quality Checklist

Before exporting your final card, verify:

- [ ] Logo is clearly visible
- [ ] Text is readable at thumbnail size
- [ ] Colors match Full Stack Science brand (#0A1628, #F97316, #FFFFFF, #3D4656)
- [ ] Layout fits 3.5" × 2" dimensions
- [ ] Orange accent is visible but not overwhelming
- [ ] Typography hierarchy is clear (name → title → contact)
- [ ] All contact information is accurate
- [ ] Safe area margins are respected (0.1" from edges)
- [ ] Both front and back designs are complete
- [ ] Export quality is suitable for intended use (print or digital)

---

**Created with ❤️ by Full Stack Science**
*Turning Data Into Value*
