import socket 

s= socket.socket()
print("socket created..............")

s.bind(('localhost', 9999))
print("socket binded....................")

s.listen(5)
print("server listening.......")
c,addr= s.accept()
print(f"connnect with {addr}")


c.send(bytes("Hi advait here",'utf-8'))


while True:
    rmsg = c.recv(1024).decode('utf-8')
    print(rmsg)
    if rmsg == 'break':
        print("disconnetcting ...")
        break
    
    smsg= input("ENter msg: ")
    c.send(bytes(smsg ,'utf-8'))
    
    if smsg== 'break':
        print("disconnecting ...")
        break