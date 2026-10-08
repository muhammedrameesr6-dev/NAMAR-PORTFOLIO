import re

with open('index.html', 'r') as f:
    html = f.read()

# Update Google Fonts
html = re.sub(
    r'<link href="https://fonts.googleapis.com/css2\?family=Poppins.*?rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Bebas+Neue&display=swap" rel="stylesheet">',
    html
)

# Update Hero
new_hero = """        <!-- Main Logo / Hero -->
        <header class="main-header">
            <div class="hero-top">
                <span>Updated</span>
                <span class="orange-pill">2026</span>
            </div>
            <h1 class="logo-text">PORTFOLIO</h1>
            <div class="hero-bottom">
                <span>Social Media & Content</span>
                <span>Mohammed Namar</span>
            </div>
        </header>"""
html = re.sub(r'<!-- Main Logo / Hero -->.*?</header>', new_hero, html, flags=re.DOTALL)

# Update Hello Heading
html = html.replace('<h3 class="hello-heading">HELLO!</h3>', '<h3 class="hello-heading">HELLO<span style="color: var(--primary-color);">!</span></h3>')

# Write back
with open('index.html', 'w') as f:
    f.write(html)

print("HTML rewritten successfully!")
