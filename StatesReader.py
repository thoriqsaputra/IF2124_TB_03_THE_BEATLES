# Tentukan jalur file
file_path = 'PDA.txt'

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

    # Read the rest of the lines and populate the matrix
    for line in lines[7:]:
        current_array = line.strip().split()
        transitions_matrix.append(current_array)

print("States:", states)
print("Input Symbols:", input_symbols)
print("Stack Symbols:", stack_symbols)
print("Start State:", start_state)
print("Start Stack Symbol:", start_stack_symbol)
print("Accept States:", accept_states)
print("Accept Condition:", accept_condition)

print("Transitions Matrix:")
for row in transitions_matrix:
    print(row)
