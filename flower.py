import cv2
import os 
import string

img = cv2.imread("flower.jpg")
msg = input("Enter Secret Message: ")
password = input("Enter The Passcode: ")

d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

    
#incryption
n=0;
m=0;
z=0;
for i in range(len(msg)):
    img[n,m,z] = d [msg[i]]
    n = n+1
    m = m+1
    z = (z+1) % 3
cv2.imwrite("encryptedMsg.jpg" , img)
os.startfile("encryptedMsg.jpg" )


#Decryption 
message=""
n=0
m=0
z=0
pas = input("Enter Passcode For Decryption: ")
if (password == pas):
    for i in range (len(msg)):
        message = message + c[img[n,m,z]]
        n = n+1 
        m = m+1
        z = (z+1) % 3
    print("Decrypted message: " , message)
else :
    print("Your Not Authenticated")
