from RSA import RSA_Steps,Encrypt_Packet,Number_From_Char
from math import sqrt
from sympy import isprime
import time

for n_bits in range(27,50):
    print(f"For n_bits= {n_bits}\n")
    (n,e,d)=RSA_Steps(n_bits)
    Enc=[]
    Messages=[]
    message = "Hello, It is a plain text"
    #appending spaces to fill out the last grouping to be 5 characters
    SpacesNum=5-len(message)%5
    if SpacesNum!=5:
        for i in range(SpacesNum):
            message+=" "
    start_Encryption = time.time()*1000
    for packet_index in range(0,len(message),5):
        sum=0
        for i in range(5):
            sum+=Number_From_Char(message[packet_index+i])*pow(37,4-i)
        encrypted_message=Encrypt_Packet(sum,e,n)
        Enc.append(encrypted_message)
        Messages.append(sum)
    end_Encryption = time.time()*1000
    Encryption_time=end_Encryption-start_Encryption
    print(f"Encryption time: {Encryption_time} ms\n")

    start_attacking = time.time()
    for p in range(2,int(sqrt(n))+1):
        if(isprime(p) and n%p==0):
            q=n//p
            if(isprime(q)):
                phi=(p-1)*(q-1)
                d=pow(e,-1,phi)
                IsFound=True
                for i in range(len(Enc)):
                    decrypted=pow(int(Enc[i]),d,n)
                    if(decrypted!=Messages[i]):
                        IsFound=False
                        break
                if(IsFound==True):
                    end_attacking = time.time()
                    Attack_time=end_attacking-start_attacking
                    print(f"Attacking time: {Attack_time} s\n")
                    break
    print("=========================================\n")

        
    