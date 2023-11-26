def StatesReader():
    file_path = 'data/PDA.txt'

    # Inisialisasi array kosong
    states = []
    input_symbols = []
    stack_symbols = []
    start_state = ""
    start_stack_symbol = ""
    accept_states = []
    accept_condition = ""

    # Baca file dan isi array
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Membaca setiap baris dan menyimpannya dalam array
        states = lines[0].strip().split()
        input_symbols = lines[1].strip().split()
        stack_symbols  = lines[2].strip().split()
        start_state = lines[3].strip()
        start_stack_symbol = lines[4].strip()
        accept_states = lines[5].strip().split()
        accept_condition = lines[6].strip()

        # Inisialisasi list untuk menyimpan array (matriks)
        transitions_matrix = []

        # Line setelahnya akan dimasukkan ke sebuah matriks
        for line in lines[7:]:
            current_array = line.strip().split()
            transitions_matrix.append(current_array)
    
    return states,input_symbols,stack_symbols,start_state,start_stack_symbol,accept_states,accept_condition,transitions_matrix