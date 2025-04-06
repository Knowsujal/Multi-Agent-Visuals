import os

# Path where your HTML and images are stored
visual_folder = "visualizations"
output_html_path = "index.html"

# Get list of all .png images
images = sorted([f for f in os.listdir(visual_folder) if f.endswith(".png")])

# Start HTML content
html = """
<!DOCTYPE html>
<html>
<head>
  <title>Multi-Agent Inventory Visuals</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    img { max-width: 90%; margin-bottom: 20px; border: 1px solid #ccc; }
    h2 { color: #333; }
  </style>
</head>
<body>
  <h1>Multi-Agent Inventory Visuals</h1>
  <div id="charts">
"""

# Add each image to HTML
for img in images:
    html += f'    <h2>{img}</h2>\n'
    html += f'    <img src="visualizations/{img}" alt="{img}">\n'

# Add CSV report download link
html += """
  </div>
  <div>
    <h2>Download Report</h2>
    <a href="simulation_report.csv" download>Download CSV Report</a>
  </div>
</body>
</html>
"""

# Save HTML file
with open(output_html_path, "w") as f:
    f.write(html)

print(f"Generated {output_html_path} with {len(images)} images.")