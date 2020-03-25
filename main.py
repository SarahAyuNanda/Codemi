MAX_LOKER = 0

while True:
    command = input().split()
    type_input = command[0]

    if type_input == 'init':
        MAX_LOKER = int(command[1])
    
    if type_input == 'exit':
        break
