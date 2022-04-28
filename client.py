import socket
import threading


# SERVER SETTINGS
host = "127.0.0.1"
port = 55555
nickname = input("Please choose username: ")


client = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
client.connect( (host , port) )



def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)

        except:
            print("an error occurred...")
            client.close()
            break



def write_message():
    while True:
        try:
            message = f"{nickname}: {input('')}"
            client.send(message.encode("ascii"))
        except:
            print("an error occurred...")
            client.close()
            break
      







recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()