import socket
import threading


# SERVER SETTINGS
host = "127.0.0.1"
port = 55555
server = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
server.bind( (host , port) )
server.listen()




# INIT SERVER OBJECTS
clients = []
nicknames = []





# SERVER METHODS
def broadcast(message):
    for c in clients:
        c.send(message)


def handle( c ):
    while True:
        try:
            message = c.recv(1024)
            broadcast(message)
        
        except:
            index = clients.index(c)
            clients.remove(index)
            clients.close()
            n = nicknames[index]
            nicknames.remove(n)
            broadcast(f"{n} left the chat...".encode("ascii"))
            break



def recieve():
    while True:
        c , address = server.accept()

        c.send(  "NICK".encode("ascii")  )
        n = c.recv(1024).decode("ascii")

        clients.append(c)
        nicknames.append(n)
        
        broadcast(f"{n} joined the chat".encode("ascii"))
        c.send("Connected to the server!".encode("ascii"))


        print(f"Connected with {str(address)}")
        thread = threading.Thread(  target=handle, args=(c,)   )
        thread.start()







if __name__ == "__main__":
    print("l?")
    recieve()