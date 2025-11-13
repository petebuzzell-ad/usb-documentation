#!/usr/bin/env python3
"""
Improved Markdown to HTML converter with better table and code block handling
"""

import re
import os
from pathlib import Path

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def convert_table(md_table):
    """Convert markdown table to HTML"""
    lines = md_table.strip().split('\n')
    if len(lines) < 2:
        return md_table
    
    # Parse header
    header_line = lines[0]
    separator_line = lines[1]
    
    # Extract columns
    header_cols = [col.strip() for col in header_line.split('|') if col.strip()]
    
    html = ['<table>', '<thead>', '<tr>']
    for col in header_cols:
        html.append(f'<th>{col}</th>')
    html.extend(['</tr>', '</thead>', '<tbody>'])
    
    # Parse rows
    for line in lines[2:]:
        if not line.strip() or line.strip().startswith('|') and '---' in line:
            continue
        cols = [col.strip() for col in line.split('|') if col.strip()]
        if cols:
            html.append('<tr>')
            for col in cols:
                # Convert markdown in cells
                col = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', col)
                col = re.sub(r'`([^`]+)`', r'<code>\1</code>', col)
                html.append(f'<td>{col}</td>')
            html.append('</tr>')
    
    html.extend(['</tbody>', '</table>'])
    return '\n'.join(html)

def markdown_to_html(md_content):
    """Convert markdown to HTML with improved handling"""
    html = md_content
    
    # Convert tables first (before other processing)
    table_pattern = r'(\|.+\|\n\|[-\s\|]+\|\n(?:\|.+\|\n?)+)'
    def replace_table(match):
        return convert_table(match.group(1))
    html = re.sub(table_pattern, replace_table, html)
    
    # Convert code blocks (triple backticks)
    def replace_code_block(match):
        lang = match.group(1) or ''
        code = match.group(2)
        lang_class = f' class="language-{lang}"' if lang else ''
        return f'<pre><code{lang_class}>{code}</code></pre>'
    html = re.sub(r'```(\w+)?\n(.*?)```', replace_code_block, html, flags=re.DOTALL)
    
    # Convert inline code (single backticks, but not in code blocks)
    # This is tricky - we'll do it after code blocks are converted
    html = re.sub(r'(?<!`)(?<!<code>)`([^`\n]+)`(?!`)', r'<code>\1</code>', html)
    
    # Convert headers and wrap in sections
    lines = html.split('\n')
    result = []
    for i, line in enumerate(lines):
        # Match headers
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            slug = slugify(title)
            
            # Close previous section if needed
            if level <= 2 and i > 0:
                # Look back to find if we need to close sections
                pass
            
            # Open section and add header
            result.append(f'<section id="{slug}">')
            result.append(f'<h{level}>{title}</h{level}>')
        else:
            result.append(line)
    
    html = '\n'.join(result)
    
    # Convert horizontal rules
    html = re.sub(r'^---$', '<hr>', html, flags=re.MULTILINE)
    
    # Convert bold
    html = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', html)
    
    # Convert italic (but not bold)
    html = re.sub(r'(?<!\*)\*([^\*]+)\*(?!\*)', r'<em>\1</em>', html)
    
    # Convert links
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Convert unordered lists
    lines = html.split('\n')
    in_list = False
    result = []
    for line in lines:
        stripped = line.strip()
        # Match list items (starting with - or *)
        if re.match(r'^[-*]\s+', stripped):
            if not in_list:
                result.append('<ul>')
                in_list = True
            content = re.sub(r'^[-*]\s+', '', stripped)
            # Process nested markdown in list items
            content = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
            result.append(f'<li>{content}</li>')
        elif re.match(r'^\d+\.\s+', stripped):
            # Ordered list
            if in_list:
                result.append('</ul>')
                in_list = False
            # Handle ordered lists separately
            if not any('</ol>' in r or '<ol>' in r for r in result[-5:]):
                result.append('<ol>')
            content = re.sub(r'^\d+\.\s+', '', stripped)
            content = re.sub(r'\*\*([^\*]+)\*\*', r'<strong>\1</strong>', content)
            content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
            result.append(f'<li>{content}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
    if in_list:
        result.append('</ul>')
    html = '\n'.join(result)
    
    # Close ordered lists
    lines = html.split('\n')
    result = []
    in_ol = False
    for line in lines:
        if '<ol>' in line and '</ol>' not in line:
            in_ol = True
            result.append(line)
        elif '</ol>' in line:
            in_ol = False
            result.append(line)
        elif in_ol and not line.strip().startswith('<li>') and line.strip() and not line.strip().startswith('<'):
            result.append('</ol>')
            in_ol = False
            result.append(line)
        else:
            result.append(line)
    if in_ol:
        result.append('</ol>')
    html = '\n'.join(result)
    
    # Convert paragraphs (simplified)
    lines = html.split('\n')
    result = []
    in_paragraph = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_paragraph:
                result.append('</p>')
                in_paragraph = False
            result.append('')
        elif (stripped.startswith('<') or 
              stripped.startswith('#') or
              stripped.startswith('|') or
              '<table>' in stripped or
              '<ul>' in stripped or
              '<ol>' in stripped or
              '<pre>' in stripped or
              '<hr>' in stripped or
              '<section' in stripped or
              '<h' in stripped):
            if in_paragraph:
                result.append('</p>')
                in_paragraph = False
            result.append(line)
        else:
            if not in_paragraph:
                result.append('<p>')
                in_paragraph = True
            result.append(line)
    if in_paragraph:
        result.append('</p>')
    html = '\n'.join(result)
    
    # Close all open sections at the end
    # Count opening sections and close them
    open_sections = html.count('<section')
    closed_sections = html.count('</section>')
    html += '\n</section>' * (open_sections - closed_sections)
    
    return html

def extract_toc(md_content):
    """Extract table of contents from markdown"""
    toc = []
    lines = md_content.split('\n')
    skip_next = False
    
    for line in lines:
        # Skip horizontal rules and TOC sections
        if line.strip() == '---':
            continue
        if 'table of contents' in line.lower():
            skip_next = True
            continue
        if skip_next and line.strip() == '':
            continue
        if skip_next and not line.strip().startswith('#'):
            continue
        skip_next = False
        
        # Match headers
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            # Skip the main title
            if level == 1 and ('guide' in title.lower() or 'architecture' in title.lower() or 'data' in title.lower() or 'integration' in title.lower()):
                continue
            
            slug = slugify(title)
            toc.append({
                'level': level,
                'title': title,
                'slug': slug
            })
    
    return toc

def generate_toc_html(toc):
    """Generate HTML for table of contents with proper nesting"""
    if not toc:
        return '<h3>Table of Contents</h3>'
    
    html = ['<h3>Table of Contents</h3>', '<ul>']
    stack = [0]  # Track nesting levels
    
    for item in toc:
        level = item['level']
        title = item['title']
        slug = item['slug']
        
        # Close lists if moving up levels
        while len(stack) > 1 and stack[-1] >= level:
            html.append('</ul>')
            html.append('</li>')
            stack.pop()
        
        # Open nested list if going deeper
        if level > stack[-1]:
            if stack[-1] > 0:  # Not the root
                html.append('<ul>')
            stack.append(level)
        
        html.append(f'<li><a href="#{slug}">{title}</a>')
    
    # Close all remaining lists
    while len(stack) > 1:
        html.append('</li>')
        html.append('</ul>')
        stack.pop()
    
    html.append('</ul>')
    return '\n'.join(html)

def convert_file(md_file, output_dir):
    """Convert a markdown file to HTML"""
    print(f"Converting {md_file.name}...")
    
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Documentation"
    
    # Extract TOC
    toc = extract_toc(md_content)
    
    # Convert markdown to HTML
    html_content = markdown_to_html(md_content)
    
    # Generate HTML page
    html_page = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
    <title>{title} - USB - McDavid eCommerce Documentation</title>
    <link rel="icon" type="image/webp" href="../assets/favicon.webp">
    <link rel="stylesheet" href="../arcadia-style.css">
</head>
<body>
    <!-- Header will be loaded dynamically by component-loader.js -->
    <div id="header-container"></div>
    
    <div class="container">
        <div class="two-column-layout">
            <!-- Enhanced Table of Contents Sidebar -->
            <nav class="toc-sidebar">
                {generate_toc_html(toc)}
            </nav>
            
            <!-- Main Content Area -->
            <main>
                {html_content}
            </main>
        </div>
    </div>
    
    <!-- Footer will be loaded dynamically by component-loader.js -->
    <div id="footer-container"></div>
    
    <!-- Component Loader: Dynamically loads header.html and footer.html -->
    <script src="../component-loader.js"></script>
    
    <!-- Enhanced TOC: Adds scroll-based highlighting and smooth navigation -->
    <script src="../enhanced-toc/enhanced-toc.js"></script>
</body>
</html>'''
    
    # Write output file
    output_file = output_dir / f"{md_file.stem}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"✓ Created {output_file.name}")

def main():
    """Main conversion function"""
    docs_dir = Path(__file__).parent / 'docs'
    output_dir = docs_dir
    
    md_files = sorted(docs_dir.glob('*.md'))
    
    print(f"Converting {len(md_files)} markdown files to HTML...\n")
    
    for md_file in md_files:
        convert_file(md_file, output_dir)
    
    print(f"\n✓ Successfully converted {len(md_files)} files to HTML")

if __name__ == '__main__':
    main()

