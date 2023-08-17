import math
from sympy import randprime
import random

mapping={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,
"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26,"r":27,"s":28,"t":29,"u":30,
"v":31,"w":32,"x":33,"y":34,"z":35
}
#Large size of packet occures when all the characters are spaces
#So, the large packet sum is [69343956] which is represented bu 27 bits
#So , n must be at least 27 bits
#To get at least n_bits key size==? p,q will be at least n_bits and at most n_bits+1
def RSA_Steps(key_size):
    p = randprime(pow(2,(key_size)), pow(2,(key_size+1)))
    q = randprime(pow(2,(key_size)), pow(2,(key_size+1)))
    n=p*q
    phi=(p-1)*(q-1)
    e = random.randrange(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d=pow(e,-1,phi)
    return (n,e,d)


def Encrypt_Packet(packet_sum,e,n):
    encrypted_packet=pow(packet_sum,e,n)
    return encrypted_packet

def Decrypt_Packet(encrypted_packet,d,n):
    decrypted_packet=pow(encrypted_packet,d,n)
    return decrypted_packet

def Number_From_Char(charcter):
    charcter=charcter.lower()
    if(charcter in mapping):
        return mapping[charcter]
    else:
        return 36

def Char_From_Number(number):
    if(number==36):
        return " "
    elif(number<10):
        return str(number)
    else:
        return chr(number + 87)

def Dec_Sum_To_Original_Message(Sum):
    a4=pow(37,4)
    a3=pow(37,3)
    a2=pow(37,2)
    a1=pow(37,1)
    packet=""
    c4=Sum//a4
    c3=(Sum-c4*a4)//a3
    c2=(Sum-c4*a4-c3*a3)//a2
    c1=(Sum-c4*a4-c3*a3-c2*a2)//a1
    c0=(Sum-c4*a4-c3*a3-c2*a2-c1*a1)
    packet+=Char_From_Number(c4)
    packet+=Char_From_Number(c3)
    packet+=Char_From_Number(c2)
    packet+=Char_From_Number(c1)
    packet+=Char_From_Number(c0)

    return packet


