import StatesReader
import HTMLReader

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
# stack.push("AE")
# stack.push("AF")

# Display the stack
# display_stack(stack)

file_path = 'example.txt'
html_arrays = HTMLReader.parse_html_to_arrays(file_path)

states,input_symbols,stack_symbols,start_state,start_stack_symbol,accept_states,accept_condition,transitions_matrix = StatesReader.StatesReader()

currentState=start_state

i = 1
for array in html_arrays[0]:
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
            cek=1
    if(cek==0):
        print("tidak accepted")
        break
    if(i==5):
        break
    i = i+1
display_stack(stack)


