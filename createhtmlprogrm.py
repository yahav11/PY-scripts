# Import the os module to interact with the file system
import os

# Define the HTML content as a string
html_content = '''
<!DOCTYPE html>
<html>
<head>
<title>My HTML File</title>
</head>
<body>
<h1>Hello, World!</h1>
<p>This is a generated HTML file created using Python.</p>
</body>
</html>
'''

# Create a new directory to store the HTML file (if it doesn't exist)
if not os.path.exists('output'):
    os.makedirs('output')

# Specify the file path and name for the HTML file
file_path = os.path.join('output', 'my_html_file.html')

# Write the HTML content to the file
with open(file_path, 'w') as f:
    f.write(html_content)

# Print a success message
print(f'HTML file created successfully at: {file_path}')
