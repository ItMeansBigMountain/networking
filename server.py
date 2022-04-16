import socket
import _thread
import sys

server = '76.16.112.102'  # IPV4 is local IP address
port = 5555

socketLIB = socket.socket(  socket.AF_INET, socket.SOCK_STREAM  )

try:
    socketLIB.bind(  (server,port) )
except socket.error as e  :
    print(str(e))

socketLIB.listen(2)   # this will listen for connections
print("waiting for connection , Server Started\n")









# we do not want to wait for this function to finish each time its executed, backing up our server
def threaded_Client(conn):
    conn.send(str.encode("Connection ID")) #connection ID 
    reply = ""
    while True:
        try:
            data = conn.recv(2048) #the amount of bits we are trying to revie
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: " , reply)
                print("Sending: " , reply)
            conn.sendall(  str.encode(reply)  )  # encode details sent over to client SECURITY
        except:
            break
    
    print("Lost Connection")
    conn.close()


# constantly look for connections
while True:
    conn , addr = socketLIB.accept() # conn is an object of the connection & addr is the IP address
    print( 'Connected to : ', addr  )

    _thread.start_new_thread(threaded_Client, (conn ,  )  )