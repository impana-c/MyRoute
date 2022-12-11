import socket
#server script

quote= '"'
quote2= '"'

def get_local_ip_address(target):
 ipaddr = ''
 try:
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect((target, 8000))
   ipaddr = s.getsockname()[0]
   s.close()
 except:
   pass

 return ipaddr
ip_add = get_local_ip_address('google.com')
ip_addr = quote + ip_add + quote2


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("10.0.0.13",12345))
sock.listen(2)
(client,(ip,port))=sock.accept()

while True:
    gpsdata = client.recv(1204)
    file = open("file2","w")
    file.write(gpsdata)
    file.close()