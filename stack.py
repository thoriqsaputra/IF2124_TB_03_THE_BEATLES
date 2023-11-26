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

