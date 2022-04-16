import socket

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


running_program = True
while running_program:

    user_message = input('\nPlease enter command(-help) or message: ')

    if user_message == '-help':
        print('\n***COMMANDS***\n')
        print('-DC : Disconnect [CASE SENSITIVE]')
    elif user_message == '-DC':
        send(DISCONNECT_MESSAGE)
        running_program == False
        break
        
    else:
        send(user_message)

