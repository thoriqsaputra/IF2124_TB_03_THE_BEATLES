from lxml import etree

def parse_html_to_arrays(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()

    root = etree.fromstring(html_content)

    def process_element(element):
        result = [f'<{element.tag}']
        for key, value in element.attrib.items():
            # Replace the value inside quotation marks with an underscore
            result.append(f'{key}="_"')
        result.append('>')
        if element.text:
            result.extend(element.text.split())
        for child in element:
            result.extend(process_element(child))
        result.append(f'</{element.tag}>')
        return result

    result_arrays = process_element(root)
    return [result_arrays]

# Example usage:
file_path = 'example.txt'
html_arrays = parse_html_to_arrays(file_path)
for array in html_arrays:
    print(array)
