import os

# Define the base URL for the Jacket images
base_url = "https://raw.githubusercontent.com/XingYanTW/Simai-Project/refs/heads/main"

# Desired image dimensions
image_width = 120  # Set your preferred width
image_height = 120  # Set your preferred height

# Scan current directory for folders
folders = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.')]

# Sanitize folder names for use in URLs
def sanitize_name(folder):
    return folder.replace(" ", "%20").replace("[", "%5B").replace("]", "%5D").replace("(", "%28").replace(")", "%29")

# Generate markdown content
markdown_content = """# Simai Project

Collection of some projects

| Jacket | Song Name |
|--------|-----------|
"""

for folder in sorted(folders):
    sanitized_folder = sanitize_name(folder)
    jacket_url = f"{base_url}/{sanitized_folder}/bg.png"
    # Use HTML for resized image
    image_tag = f'<img src="{jacket_url}" width="{image_width}" height="{image_height}">'
    markdown_content += f"|{image_tag}|{folder}|\n"

# Write the output to README.md
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(markdown_content)

print("README.md has been updated.")
