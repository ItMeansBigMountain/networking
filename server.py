import socket
import threading
#if you wanna send objects import pickle and check out some docs on pickle and sockets

HEADER = 64 #byts
FORMAT = 'utf-8'

PORT = 5050

#ip adress that the server is gonna run on 
#if you want to run off the internet change SERVER = 'publicIPaddress string'
SERVER = socket.gethostbyname(socket.gethostname()) #more flexible than local hardcoded IPv4 address
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #adds ip address of client into connection
server.bind(ADDR) #binding the SERVER & PORT

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}] {msg}')
            conn.send('Message Recieved'.encode(FORMAT))
    conn.close()



def start():
    server.listen()
    print(f'[LISTENING] server is listening on {SERVER}')
    while True:
        conn, addr = server.accept() #wait for a new connection and then store conn. as object
        thread = threading.Thread(target = handle_client, args=(conn,addr)) #pass object to handle function
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1 }')


print('[RUNNING] server is starting...')
start()