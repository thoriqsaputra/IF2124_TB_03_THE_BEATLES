from bs4 import BeautifulSoup
import re

spesial_case = ['type', 'method']

def parse_html(html):
    result_array = []
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.recursiveChildGenerator():
        if tag.name:
            result_array.append(f'<{tag.name}')

            for attr, value in tag.attrs.items():
                if attr in spesial_case:
                    result_array.append(f'{attr}="{value}"')
                else:
                    result_array.append(f'{attr}="_"')

            if tag.string:
                result_array.append('>')
                result_array.extend(tag.string.split())
                result_array.append(f'</{tag.name}>')
                
            else:
                # Check if the tag is self-closing
                if not tag.find_all(recursive=False):
                    result_array.append('>')
                else:
                    result_array.append('>')
    if not result_array:
        spesial = re.split(r'(?<=>|\s)', html, 1)
        spesial = list(map(lambda s: s.replace(" ", ""), spesial))
        spesial = [item for item in spesial if item != ""]
        result_array.extend(spesial) 

    return result_array

def parse_html_file(filename):
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
    list_html = []
    # Iterate through each line and append to the array after parsing
    for line in lines:
        list_html.append(parse_html(line.strip()))
    return list_html

print(parse_html_file('example.txt'))
