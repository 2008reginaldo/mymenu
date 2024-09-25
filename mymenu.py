from menus import *
import sys

menu = menu_0
keep_going = 1

def print_menu(menu):
    for key in menu.keys():
        print(f"{key}: {menu[key][0]}")

def navigate():
    global menu, keep_going
    print_menu(menu)
    choice = int( input("\n--> escolha uma opção: "))

    msg = menu[choice][0]
    #print(f'--> opção escolhida {choice}: {msg}')

    value = menu[choice][1][0]
    if callable(value):
        # if true, value is a function
        print(f'------------------------------\nexecuting: {value.__name__}')
        if len(menu[choice][1]) == 1:
            value()
            keep_going = 0
            return

        parameter = menu[choice][1][1]
        value(parameter)
        keep_going = 0
        return

    menu = menu[choice][1][0]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Execute directly based on command-line argument
        # execute_task_directly(sys.argv[1])
        print('ainda não implementado')
    else:
        # Display interactive menu
        print('Options:')
        while keep_going:
            navigate()