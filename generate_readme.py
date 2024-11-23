import os

# Define the base URLs for the Jacket images and ZIP downloads
base_url = "https://raw.githubusercontent.com/XingYanTW/Simai-Project/refs/heads/main"
zip_base_url = "https://download-directory.github.io?url=https://github.com/XingYanTW/Simai-Project/tree/main/"  # Adjust this if ZIPs are hosted elsewhere

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

| Jacket | Song Name | Download |
|--------|-----------|----------|
"""

for folder in sorted(folders):
    sanitized_folder = sanitize_name(folder)
    jacket_url = f"{base_url}/{sanitized_folder}/bg.png"
    zip_url = f"{zip_base_url}/{sanitized_folder}&filename={sanitized_folder}"
    # Use HTML for resized image
    image_tag = f'<img src="{jacket_url}" width="{image_width}" height="{image_height}">'
    # Add download link
    markdown_content += f"|{image_tag}|{folder} | [Download]({zip_url})|\n"

# Write the output to README.md
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(markdown_content)

print("README.md has been updated.")
