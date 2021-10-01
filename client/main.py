
import time
import os
import requests
import constants

def print_title():
    os.system('clear')
    print('CDH Team presents...')
    print('''
        _____   _       _          _  ____  
        |  __ \\ (_)     | |        (_)|  _ \\ 
        | |  | | _  ___ | |_  _ __  _ | |_) |
        | |  | || |/ __|| __|| '__|| ||  _ < 
        | |__| || |\__ \| |_ | |   | || |_) |
        |_____/ |_||___/ \\__||_|   |_||____/ 
    ''')

    print('Welcome to DistriB CLI!', end='\n\n')

def elemental_commands(cmd, args):
    # Manual
    if cmd == "man":
        if args:
            print(f'No manual entry for {args[0]}')
        else:
            print('What manual page do you want?\tTry \'man man\'')
    
    # Change Directory
    elif cmd == "cd":
        try:
            if args:
                if args[0] == "--help" or args[0] == '-h':
                    print('Usage: cd [dir]\nChange the shell working directory.\n')
                else:
                    directory = args if len(args) > 1 else args[0] 
                    os.chdir(directory)

        except FileNotFoundError as e:
            print(f'cd: {args[0]}: No such file or directory')
        except TypeError as e:
            print('cd: too many arguments')
    
    # List files
    elif cmd == "ls":
        params = [s for s in args if s[0] == "-"]
        no_params = [s for s in args if s[0] != "-"]
        args = no_params if len(params) != len(args) else []
        
        hidden = False
        if "-a" in params: hidden = True
        if "--help" in params:
            print('Usage: ls [OPTION]... [FILE]...\nList information about the FILEs (the current directory by default).\n\nMandatory arguments to long options are mandatory for short options too.\n\t-a                  do not ignore entries starting with .\n')
            return

        if len(args) > 1:
            for elem in args:
                try:
                    dirs = os.listdir(elem)
                    print(f'{elem}:')
                    for d in dirs:
                        if d[0] != "." or hidden:
                            print(d, end='  ')
                    print('\n')
                
                except FileNotFoundError as e:
                    print(f'ls: cannot access \'{elem}\': No such file or directory')
        else:
            dirs = os.listdir()
            for d in dirs:
                if d[0] != "." or hidden:
                    print(d, end='  ')
            print('')

    # Clear
    elif cmd == "clear":
        print_title()
    
    return cmd == "man" or cmd == "cd" or cmd == "ls" or cmd == "clear"

def command_checker(cmd, args):
    if not elemental_commands(cmd, args):
        if cmd == "upload":
            print('UPLOAD')
        elif cmd == "list-files":
            to_list_files()
        elif cmd == "download":
            print('DOWNLOAD')
        else:
            print(f'{cmd}: command not found')


def main():
    print('***********************************')
    user_input = ""

    os.system('clear')
    print_title()
    try:
        while True:
            pwd = '[' + os.getcwd().replace("\\\\", "/") + ']'
            user_input = input(pwd + ' # ').split()
            command = user_input[0]
            args = user_input[1:] if len(user_input) > 1 else []

            #print(f'<<TEST STRING: COMMAND: {command}; args {args}>>')
            command_checker(command, args)
            
    except KeyboardInterrupt:
        print('\n\nBye!\n')

def test_connection(url, port):
    try:
        requests.get(url+':'+port+"/ping")
    except ConnectionRefusedError:
        os.system('clear')
        print('Connection refused! Please contact the administrator')
        time.sleep(3)
        raise ConnectionRefusedError

def to_list_files():
    try:
        test_connection(constants.HERMES_URL, constants.HERMES_PORT)
        r = requests.get(constants.HERMES_URL+':'+constants.HERMES_PORT+'/')
        print(str(r.json()))
    except:
        return

if __name__ == '__main__':
    main()

# Test connection
# try:
#     conn = http.client.HTTPConnection(constants.TABLE_SERVER, constants.TABLE_PORT)
#     conn.request("GET", "/ping")
# except ConnectionRefusedError:
#     os.system('clear')
#     print('Connection refused! Please contact the administrator')
#     time.sleep(3)
#     continue

# Connection
# try:
#     conn = http.client.HTTPConnection(constants.CONVERT_SERVER, constants.CONVERT_PORT)
#     conn.request("GET", f'/?value={ir}&actualIrType={actual_irt}&newIrType={new_irt}')
#     res = conn.getresponse()
#     # ANSWER
#     answer = res.read().decode(constants.ENCODING_FORMAT)
#     print('\nAnswer')
#     print(f': {answer} % {new_irt}')

#     print('\nPress any key to go back...')
#     input()
# except ConnectionRefusedError:
#     os.system('clear')
#     print('Connection refused! Please contact the administrator')
#     time.sleep(3)
#     continue

# MONTHS
# print_gen_table_header(init_value, ir, months)
# print('\nSet the periods amount to pay (enter \'q\' to quit)')
# data_to_send = input(': ')

# while(not (is_float(data_to_send) or data_to_send == 'q')):
#     print('Please, input an int number')
#     data_to_send = input(': ')
# if (data_to_send == 'q'): continue