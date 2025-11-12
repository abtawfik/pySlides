"""
Full Stack Science Business Card Generator Example

This example demonstrates how to create a professional business card
using pySlides with the Full Stack Science brand guidelines.

The business card can be:
1. Viewed in a web browser
2. Exported as PDF for printing
3. Downloaded as a high-resolution PNG
4. Customized with personal information
"""

from pyslides import Presentation, Slide


def create_business_card_slide():
    """
    Creates a presentation with an embedded business card generator.

    This demonstrates how to integrate the standalone business card HTML
    into a pySlides presentation for easy distribution and viewing.
    """

    # Create a new presentation
    pres = Presentation(
        title="Full Stack Science Business Card",
        author="Full Stack Science",
        theme="white"
    )

    # Create a slide with instructions
    intro_slide = Slide(title="Business Card Generator")
    intro_slide.add_html("""
        <div style="font-family: 'Inter', sans-serif; padding: 40px;">
            <h2 style="color: #0A1628; font-size: 48px; margin-bottom: 20px;">
                Full Stack Science Business Card
            </h2>
            <p style="color: #3D4656; font-size: 24px; line-height: 1.6;">
                This presentation includes a professional business card generator
                following Full Stack Science brand guidelines.
            </p>
            <div style="margin-top: 40px; padding: 30px; background: #f8fafc; border-left: 4px solid #F97316; border-radius: 8px;">
                <h3 style="color: #0A1628; font-size: 32px; margin-bottom: 15px;">Features:</h3>
                <ul style="color: #3D4656; font-size: 20px; line-height: 2;">
                    <li>✓ Print-ready design (3.5" × 2" @ 300dpi)</li>
                    <li>✓ Customizable contact information</li>
                    <li>✓ Front and back card designs</li>
                    <li>✓ Export as PDF or PNG</li>
                    <li>✓ Professional Full Stack Science branding</li>
                </ul>
            </div>
            <div style="margin-top: 40px; padding: 20px; background: #fef3c7; border-radius: 8px;">
                <p style="color: #92400e; font-size: 18px;">
                    <strong>Note:</strong> For the full interactive experience,
                    open <code>business_card_generator.html</code> directly in your browser.
                </p>
            </div>
        </div>
    """)
    pres.add_slide(intro_slide)

    # Create a slide with usage instructions
    usage_slide = Slide(title="How to Use")
    usage_slide.add_html("""
        <div style="font-family: 'Inter', sans-serif; padding: 40px;">
            <h2 style="color: #0A1628; font-size: 42px; margin-bottom: 30px;">
                Quick Start Guide
            </h2>

            <div style="margin-bottom: 30px;">
                <h3 style="color: #F97316; font-size: 28px; margin-bottom: 15px;">
                    1. Open the Business Card Generator
                </h3>
                <p style="color: #3D4656; font-size: 20px; line-height: 1.6;">
                    Navigate to <code>examples/business_card_generator.html</code>
                    and open it in your web browser.
                </p>
            </div>

            <div style="margin-bottom: 30px;">
                <h3 style="color: #F97316; font-size: 28px; margin-bottom: 15px;">
                    2. Customize Your Information
                </h3>
                <p style="color: #3D4656; font-size: 20px; line-height: 1.6;">
                    Fill in your name, title, email, phone, and website in the form fields.
                    The card updates in real-time.
                </p>
            </div>

            <div style="margin-bottom: 30px;">
                <h3 style="color: #F97316; font-size: 28px; margin-bottom: 15px;">
                    3. Export Your Card
                </h3>
                <p style="color: #3D4656; font-size: 20px; line-height: 1.6;">
                    Click "Print / Export PDF" for printing, or "Download as PNG"
                    for digital sharing.
                </p>
            </div>

            <div style="background: #ecfdf5; padding: 20px; border-radius: 8px; border-left: 4px solid #10b981;">
                <p style="color: #065f46; font-size: 18px;">
                    <strong>Tip:</strong> Use the "Flip Card" button to preview both
                    the front and back designs before exporting.
                </p>
            </div>
        </div>
    """)
    pres.add_slide(usage_slide)

    # Create a slide showing brand guidelines
    brand_slide = Slide(title="Brand Guidelines")
    brand_slide.add_html("""
        <div style="font-family: 'Inter', sans-serif; padding: 40px;">
            <h2 style="color: #0A1628; font-size: 42px; margin-bottom: 30px;">
                Full Stack Science Brand
            </h2>

            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px;">
                <!-- Colors -->
                <div>
                    <h3 style="color: #F97316; font-size: 28px; margin-bottom: 15px;">Colors</h3>
                    <div style="margin-bottom: 15px;">
                        <div style="background: #0A1628; height: 60px; border-radius: 8px; margin-bottom: 8px;"></div>
                        <p style="color: #3D4656; font-size: 16px;">Navy Blue: #0A1628</p>
                    </div>
                    <div style="margin-bottom: 15px;">
                        <div style="background: #F97316; height: 60px; border-radius: 8px; margin-bottom: 8px;"></div>
                        <p style="color: #3D4656; font-size: 16px;">Professional Orange: #F97316</p>
                    </div>
                    <div style="margin-bottom: 15px;">
                        <div style="background: #3D4656; height: 60px; border-radius: 8px; margin-bottom: 8px;"></div>
                        <p style="color: #3D4656; font-size: 16px;">Charcoal: #3D4656</p>
                    </div>
                </div>

                <!-- Typography -->
                <div>
                    <h3 style="color: #F97316; font-size: 28px; margin-bottom: 15px;">Typography</h3>
                    <div style="margin-bottom: 20px;">
                        <p style="font-family: 'JetBrains Mono', monospace; font-size: 24px; color: #0A1628; font-weight: 700;">
                            JetBrains Mono
                        </p>
                        <p style="color: #3D4656; font-size: 14px;">Headings & Brand</p>
                    </div>
                    <div style="margin-bottom: 20px;">
                        <p style="font-family: 'Inter', sans-serif; font-size: 24px; color: #0A1628;">
                            Inter
                        </p>
                        <p style="color: #3D4656; font-size: 14px;">Body Text</p>
                    </div>
                    <div style="background: #f8fafc; padding: 15px; border-radius: 8px;">
                        <p style="color: #F97316; font-size: 14px; font-weight: 600; letter-spacing: 0.1em;">
                            TURNING DATA INTO VALUE
                        </p>
                        <p style="color: #3D4656; font-size: 12px; margin-top: 5px;">Brand Tagline</p>
                    </div>
                </div>
            </div>
        </div>
    """)
    pres.add_slide(brand_slide)

    # Save the presentation
    output_file = "examples/business_card_presentation.html"
    pres.save(output_file)
    print(f"Business card presentation saved to: {output_file}")
    print("\nNext steps:")
    print("1. Open business_card_generator.html in your browser")
    print("2. Customize your contact information")
    print("3. Export as PDF or PNG")
    print("\nFor best printing results:")
    print("- Use 300gsm cardstock or higher")
    print("- Print at actual size (3.5\" × 2\")")
    print("- Ensure color profile is set to CMYK for professional printing")

    return pres


def generate_custom_card(name, title, email, phone, website="fullstackscience.com"):
    """
    Generate a customized business card with specific contact information.

    Args:
        name (str): Full name
        title (str): Job title or role
        email (str): Email address
        phone (str): Phone number
        website (str): Website URL (defaults to fullstackscience.com)

    Returns:
        str: HTML string with customized business card
    """

    html_template = f"""
    <div style="width: 1050px; height: 600px; background: white; position: relative; box-shadow: 0 10px 40px rgba(10, 22, 40, 0.15);">
        <!-- Grid Pattern -->
        <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(10, 22, 40, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(10, 22, 40, 0.03) 1px, transparent 1px); background-size: 20px 20px;"></div>

        <!-- Orange Accent Line -->
        <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 6px; background: linear-gradient(to bottom, #F97316, #ea580c);"></div>

        <!-- Content -->
        <div style="position: absolute; inset: 0; padding: 60px 60px 60px 80px; display: flex; font-family: 'Inter', sans-serif;">

            <!-- Left Section -->
            <div style="flex: 1; display: flex; flex-direction: column; justify-content: space-between;">
                <!-- Logo -->
                <div style="width: 80px; height: 80px;">
                    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                        <polygon points="50,15 85,75 15,75" fill="#0A1628" opacity="0.9"/>
                        <polygon points="50,15 85,75 68,75" fill="#3B82F6" opacity="0.7"/>
                        <polygon points="68,75 85,75 76.5,60" fill="#F97316" opacity="0.9"/>
                    </svg>
                </div>

                <!-- Name and Title -->
                <div>
                    <h1 style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #0A1628; font-size: 42px; line-height: 1.1; letter-spacing: -0.02em; margin-bottom: 8px;">
                        {name}
                    </h1>
                    <p style="font-weight: 500; color: #3D4656; font-size: 20px; line-height: 1.3;">
                        {title}
                    </p>
                    <p style="color: #F97316; font-weight: 600; margin-top: 16px; font-size: 14px; letter-spacing: 0.05em;">
                        TURNING DATA INTO VALUE
                    </p>
                </div>
            </div>

            <!-- Right Section -->
            <div style="width: 320px; display: flex; flex-direction: column; justify-content: flex-end; text-align: right;">
                <div style="display: flex; flex-direction: column; gap: 12px;">
                    <div style="color: #3D4656; font-size: 16px;">{email}</div>
                    <div style="color: #3D4656; font-size: 16px;">{phone}</div>
                    <div style="color: #3D4656; font-size: 16px;">{website}</div>
                </div>
            </div>
        </div>
    </div>
    """

    return html_template


if __name__ == "__main__":
    # Create the full presentation
    presentation = create_business_card_slide()

    # Example: Generate a custom card programmatically
    custom_card_html = generate_custom_card(
        name="Dr. Jane Smith",
        title="Chief Data Scientist",
        email="jane.smith@fullstackscience.com",
        phone="+1 (415) 555-0199"
    )

    print("\n" + "="*60)
    print("Custom card HTML generated successfully!")
    print("You can embed this in presentations, emails, or websites.")
    print("="*60)
