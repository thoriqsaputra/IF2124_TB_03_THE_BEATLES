def process_line(line):
    processed_tokens = []
    current_token = ""
    in_tag = False  # Flag untuk melacak apakah saat ini berada di dalam tag
    in_attribute = False  # Flag untuk melacak apakah saat ini berada di dalam atribut
    current_attribute = ""  # Variabel untuk menyimpan nama atribut saat ini
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
                    # Pengecualian untuk tag penutup
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
            # Menangani kasus khusus atribut
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
                # Mengubah nilai atribut untuk 'type' dan 'method'
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
