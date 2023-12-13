import html

def convert_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    html_content = '<!DOCTYPE html>\n<html>\n<head>\n    <title>Document</title>\n</head>\n<body>\n'

    current_paragraph = ''
    for line in lines:
        if line.strip() == '':
            if current_paragraph:
                html_content += f'    <p>{html.escape(current_paragraph.strip())}</p>\n'
                current_paragraph = ''
        else:
            current_paragraph += line + ' '

    # Add the last paragraph if it exists
    if current_paragraph:
        html_content += f'    <p>{html.escape(current_paragraph.strip())}</p>\n'

    html_content += '</body>\n</html>'

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# File paths
input_file = 'FOMC/FOMC_2023-12-13.txt'
output_file = 'FOMC/FOMC_2023-12-13.html'

# Converting the text to HTML
convert_to_html(input_file, output_file)

output_file
