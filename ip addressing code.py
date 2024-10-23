def clasIP(a):
    foctant= int(a[0])
    
    if foctant >=1 and foctant <=126 :
        print (f"{a} is class A .")
        mask = [255,0,0,0]
        one =8
        print (f"Subnet mask is {mask} or /{one}")
        n= 32-one
        host = 2**n 
        print(f"Number of total host is : {host}")
        print(f"Number of valid or usable host is : {host-2}")
        start = []
        end = []
        for i in range (len(a)-1):
            start.append(a[i])

        for i in range(len(a)-3):
            end.append(a[i])
        
        start.append(0)
        end.append([255,255,255])
        print(f"Starting address is : {start}")
        print(f"Broadcast address is : {end}")
    elif foctant >=128 and foctant <=191 :
        print (f"{a} is class B .")
        mask = [255,255,0,0]
        one =16
        print (f"Subnet mask is {mask} or /{one}")
        n= 32-one
        host = 2**n 
        print(f"Number of total host is : {host}")
        print(f"Number of valid or usable host is : {host-2}")
        start = []
        end = []
        for i in range (len(a)-1):
            start.append(a[i])

        for i in range(len(a)-3):
            end.append(a[i])
        
        start.append(0)
        end.append([255,255,255])
        print(f"Starting address is : {start}")
        print(f"Broadcast address is : {end}")
    elif foctant >=192 and foctant <=239 :
        print (f"{a} is class C .")
        mask = [255,255,255,0]
        one =24
        print (f"Subnet mask is {mask} or /{one}")
        n= 32-one
        host = 2**n 
        print(f"Number of total host is : {host}")
        print(f"Number of valid or usable host is : {host-2}")
        start = []
        end = []
        for i in range (len(a)-1):
            start.append(a[i])

        for i in range(len(a)-3):
            end.append(a[i])
        
        start.append(0)
        end.append([255,255,255])
        print(f"Starting address is : {start}")
        print(f"Broadcast address is : {end}")


ip = input("Enter IP address")
a= ip.split('.')

print(f"Input ip address is : {ip}")
clasIP(a)
