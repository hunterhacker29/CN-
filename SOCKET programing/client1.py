import socket

s= socket.socket()

s.connect(('localhost',9999))
print(s.recv(1024).decode('utf-8'))
while True:
    
    smsg = input("ENter msg: ")
    s.send(bytes(smsg,'utf-8'))
    
    if smsg == 'exit':
        print("Disconnecting .....")
        break
    
    rmsg = s.recv(1024).decode('utf-8')
    if rmsg == 'break':
        print("Disconnetcing ..")
        break
    print("msg :",rmsg)
    
    
s.close()
    