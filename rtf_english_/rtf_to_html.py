
import pypandoc

# Set the input and output file names
input_file = 'Đọc hiểu 5 câu.docx.rtf'
output_file = 'output.html'

# Define the options for pandoc
options = ['--wrap=preserve']

# Convert the RTF file to HTML
output = pypandoc.convert_file(input_file, 'html', extra_args=options)

# Write the HTML output to a file
with open(output_file, 'w', encoding='utf-8', errors='ignore') as f:
    f.write("<html>\n<head>\n<title>RTF to HTML conversion</title>\n</head>\n<body>\n<div>\n")
    f.write(output)
    f.write("\n</div>\n</body>\n</html>")


