import StatesReader
import HTMLReader
import os
def initiate():
    batman = """
    _____                                                                                                                 _____ 
   ( ___ )                                                                                                               ( ___ )
    |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
    |   |  ________  ________  ________          ________       ___    ___ ________   _________  ________     ___    ___  |   | 
    |   | |\   __  \|\   ___ \|\   __  \        |\   ____\     |\  \  /  /|\   ___  \|\___   ___\\   __  \   |\  \  /  /|  |   | 
    |   | \ \  \|\  \ \  \_|\ \ \  \|\  \       \ \  \___|_    \ \  \/  / | \  \\ \  \|___ \  \_\ \  \|\  \  \ \  \/  / /  |   | 
    |   |  \ \   ____\ \  \ \\ \ \   __  \       \ \_____  \    \ \    / / \ \  \\ \  \   \ \  \ \ \   __  \  \ \    / /    |   | 
    |   |   \ \  \___|\ \  \_\\ \ \  \ \  \       \|____|\  \    \/  /  /   \ \  \\ \  \   \ \  \ \ \  \ \  \  /     \/     |   | 
    |   |    \ \__\    \ \_______\ \__\ \__\        ____\_\  \ __/  / /      \ \__\\ \__\   \ \__\ \ \__\ \__\/  /\   \    |   | 
    |   |     \|__|     \|_______|\|__|\|__|       |\_________\\___/ /        \|__| \|__|    \|__|  \|__|\|__/__/ /\ __\   |   | 
    |   |                                          \|_________\|___|/                                        |__|/ \|__|  |   | 
    |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
   (_____)                                                                                                               (_____)   
    """

    print(batman)

    while True:
        file_path = input("Enter the HTML File Path: ")
        
        if os.path.exists(file_path):
            print(f"The file {file_path} exists.")
            print("\nHTML CHECKER \n")
            break
        else:
            print(f"The file {file_path} does not exist. Please enter a valid file path.") 
    return file_path

class Stack:
    def __init__(S):
        S.items = []

    def is_empty(S):
        return len(S.items) == 0

    def push(S, item):
        S.items.append(item)

    def pop(S):
        if not S.is_empty():
            return S.items.pop()
        else:
            raise IndexError("pop pada stack kosong")

    def Top(S):
        if not S.is_empty():
            return S.items[-1]
        else:
            raise IndexError("stack kosong")

    def size(S):
        return len(S.items)
    
def display_stack(stack):
    if stack.is_empty():
        print("Stack is empty")
    else:
        print("Stack:")
        for item in reversed(stack.items):
            print("|", item, "|")
            print("|" + "-" * (len(str(item)) + 2) + "|")

# Example usage:
stack = Stack()

# Push elements onto the stack
stack.push("Z")
# stack.push("AF")

# Display the stack
# display_stack(stack)

file_path = initiate()

states,input_symbols,stack_symbols,start_state,start_stack_symbol,accept_states,accept_condition,transitions_matrix = StatesReader.StatesReader()

currentState=start_state

with open('example.txt', 'r') as file:
    for line in file:
        html = line.strip()
        if not html:
            continue
        processed_tokens = HTMLReader.process_line(html)
        cek1=0
        for array in processed_tokens:
            cek = 0
            for cs in transitions_matrix:
                if cs[0]==currentState and cs[1]==array:
                    if(cs[2]=='e' or stack.Top()==cs[2]):
                        if(cs[2]!='e'):
                            stack.pop()
                        if(cs[4][0]!='e'):
                            for i in range(len(cs[4])):
                                stack.push(cs[4][len(cs[4])-1-i])
                        currentState = cs[3]
                        cek=1
                        break
                elif cs[0]==currentState and cs[1]=='any':
                    if(stack.Top()==cs[2]):
                        cek=1
                        break
                    else:
                        for i in range(len(array)):
                            if(array[i]=='<' or array[i]=='>'):
                                cek = 0
                                break
                            else:
                                cek=1
                        #cek=1
            if(cek==0):
                cek1=0
                print(array)
                break
            else:
                cek1=1
        if(cek1==0):
            print("tidak accepted")
            print(line)
            break
        print(line)

display_stack(stack)



