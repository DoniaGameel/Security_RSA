#Has only the public key
import socket
import pickle
from RSA import Encrypt_Packet,Number_From_Char
import time


# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
# bind the socket to a public host, and a well-known port
server_socket.bind((host, 8000))
# become a server socket
server_socket.listen(1)

print("Server started. Waiting for client to connect...")
# accept connections from outside
(client_socket, address) = server_socket.accept()
print(f"Client connected: {address}")

#Recieve the public key
Public_key=client_socket.recv(1024)
Public_key = pickle.loads(Public_key)
print(f"data recieved from reciever:{Public_key}")
[e,n]=Public_key

while(1):
    message = input("Enter the message to encrypt: ")
    #appending spaces to fill out the last grouping to be 5 characters
    SpacesNum=5-len(message)%5
    if SpacesNum!=5:
        for i in range(SpacesNum):
            message+=" "
    for packet_index in range(0,len(message),5):
        sum=0
        for i in range(5):
            sum+=Number_From_Char(message[packet_index+i])*pow(37,4-i)
        encrypted_message=Encrypt_Packet(sum,e,n)
        client_socket.send(str(encrypted_message).encode())
        #Sleep because sometimes sender is faster than reciever
        time.sleep(0.01)
    end_of_the_message="."
    client_socket.send(end_of_the_message.encode())

# close the socket
client_socket.close()
