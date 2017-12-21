import socket

target_host = "127.0.0.1"
target_port = 80 

# create socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind for test comment out when server up
client.bind((target_host, target_port))

#send some data... 
client.sendto("AAABBBCCC" ,(target_host, target_port))

#receive data 
data, addr = client.recvfrom(4096)

print data, addr
