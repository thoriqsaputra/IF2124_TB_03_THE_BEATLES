import StatesReader
import HTMLReader
import initiate
import stack
from termcolor import colored

run = True

while run:
    
    S = stack.Stack()

    S.push("Z")

    file_path = initiate.initiate()

    states,input_symbols,stack_symbols,start_state,start_stack_symbol,accept_states,accept_condition,transitions_matrix = StatesReader.StatesReader()

    currentState=start_state

    jumlah_line = 0

    with open(file_path, 'r') as file:
        for line in file:
            html = line.strip()
            jumlah_line += 1
            if not html:
                continue
            processed_tokens = HTMLReader.process_line(html)
            cek1=0
            for array in processed_tokens:
                cek = 0
                for cs in transitions_matrix:
                    if cs[0]==currentState and cs[1]==array:
                        if(cs[2]=='e' or S.Top()==cs[2]):
                            if(cs[2]!='e'):
                                S.pop()
                            if(cs[4][0]!='e'):
                                for i in range(len(cs[4])):
                                    S.push(cs[4][len(cs[4])-1-i])
                            currentState = cs[3]
                            cek=1
                            break
                    elif cs[0]==currentState and cs[1]=='any':
                        if(S.Top()==cs[2]):
                            cek=1
                            break
                        elif(cs[2]=='e'):
                            for i in range(len(array)):
                                if(array[i]=='<' or array[i]=='>'):
                                    cek = 0
                                    break
                                else:
                                    cek=1
                            #cek=1
                if(cek==0):
                    cek1=0
                    break
                else:
                    cek1=1
            if(cek1==0):
                print(colored("Syntax Error",'red', attrs=['bold']))
                line = line.strip()
                print(f"Error at line {jumlah_line} : {line}")
                break

    if S.is_empty():
        print(colored('Accepted','green', attrs=['bold']))

    while True:
        Retry = input(colored("Do you want to try another HTML FILE (Y/N)?  ", 'magenta'))

        if Retry == 'Y':
            initiate.clear_terminal()
            print(colored("\nProgram Restarted", 'light_blue', attrs=['blink','underline']))
            break
        elif Retry == 'N':
            print(colored("\nProgram Ended", 'light_magenta', attrs=['bold']))
            run = False
            break
        else:
            print(colored("Try again only input 'Y' or 'N' ", 'red'))
