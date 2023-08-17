#The Owner of the key
import socket
import pickle
from RSA import RSA_Steps,Dec_Sum_To_Original_Message,Decrypt_Packet

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
# connection to hostname on the port.
client_socket.connect((host, 8000))

#Generate Keys
(n,e,d)=RSA_Steps(27)

#Send my public key
public_key = pickle.dumps([e,n])
client_socket.send(public_key)

#Recieve data
Decrypted_Text=""
Recieved_Message=client_socket.recv(1024)

while(Recieved_Message):
   ciphertext=Recieved_Message.decode()
   #check the end of the message
   if(ciphertext=="."):
    break
   #check if the Sender close the connection
   if(ciphertext==''):
    #close the socket
    client_socket.close()
    print("Close Connection")
    break
   print(f"recieved: {ciphertext}")
   Dec_Sum=Decrypt_Packet(int(ciphertext),d,n)
   Decrypted_Text+=Dec_Sum_To_Original_Message(Dec_Sum)
   print(f"decrypted: {Decrypted_Text}")
   Recieved_Message=client_socket.recv(1024)

print(f"Complete Message: {Decrypted_Text}")
