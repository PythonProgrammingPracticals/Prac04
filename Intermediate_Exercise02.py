
def main ():

    print("Hello There!")

    username = input("Enter your username:")

    status = security_check(username)
    while status == "Access denied":
        print(status)
        username = input("Enter your username again:")
        status = security_check(username)
    print(status)


def security_check(username):

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye','swei45' ,
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState','InteractiveConsole',
                 'InterpreterInterface', 'StartServer', 'bob']

    if username in usernames:
        return "Access granted"
    else:
        return "Access denied"


main()