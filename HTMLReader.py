def process_line(line):
    processed_tokens = []
    current_token = ""
    in_tag = False  # Flag to track whether currently inside a tag
    in_attribute = False  # Flag to track whether currently inside an attribute
    current_attribute = ""  # Variable to store the current attribute name
    first = True
    
    for char in line:
        if char.isspace() and not in_attribute:
            if current_token:
                processed_tokens.append(current_token)
                current_token = ""
        elif char == '<':
            if current_token:
                processed_tokens.append(current_token)
                current_token = ""
            current_token += char
            in_tag = True
            in_attribute = False
        elif char == '>':
            if in_tag:
                if current_token.startswith('</') or current_token.startswith('--'):
                    # Exception for closing tags
                    current_token += char
                    processed_tokens.append(current_token)
                else:
                    processed_tokens.append(current_token)
                    processed_tokens.append(char)
                current_token = ""
                in_tag = False
            else:
                processed_tokens.append(current_token)
                processed_tokens.append(char)
                current_token = ""
        elif char == '=' and in_tag:
            # Handle the special case for attributes
            current_attribute = current_token.lower()
            current_token += char
            in_attribute = True
            attribute_value = ""
        elif char == '"' and in_attribute and first:
            current_token += char
            in_attribute = True
            first = False
        elif (char.isalpha() or char.isspace()) and in_attribute:
            attribute_value += char
        elif char == '"' and not first and in_attribute:
            if current_attribute in ['type', 'method']:
                # Change the attribute value for 'type' and 'method'
                current_token += f'{attribute_value}"'
            else:
                current_token += '_"'
            in_attribute = False
            first = True
            attribute_value = ''
            current_attribute = ''
        elif not in_attribute:
            current_token += char

    if current_token:
        processed_tokens.append(current_token)

    return processed_tokens