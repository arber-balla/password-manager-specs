import re

def generate_anchor(text):
    """Generate GitHub-style anchor link from header text."""
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'[^\w\s-]', '', text)  # Remove non-word chars except spaces and hyphens
    text = re.sub(r'[\s_]+', '-', text)  # Replace spaces and underscores with hyphens
    text = re.sub(r'^-+|-+$', '', text)  # Trim leading/trailing hyphens
    text = re.sub(r'-+', '-', text)  # Collapse multiple hyphens
    return text

def generate_toc(lines):
    """Generate table of contents from markdown headers."""
    toc = []
    for line in lines:
        line = line.rstrip('\n')
        if match := re.match(r'^(#+)\s+(.*)$', line):
            level = len(match.group(1))
            text = match.group(2).strip()
            anchor = generate_anchor(text)
            indent = '  ' * (level - 1)
            toc.append(f"{indent}- [{text}](#{anchor})")
    return '\n'.join(toc)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python toc_generator.py <markdown_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    print("## Table of Contents\n")
    print(generate_toc(lines))

if __name__ == '__main__':
    main()
