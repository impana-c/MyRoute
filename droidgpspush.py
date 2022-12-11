import androidhelper
import socket
import time

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

port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.0.13",12345)) #connecting to pi as client
droid.makeToast("Starting location fetch") #notify me
while True:
    location = droid.getLastKnownLocation().result
    location = location.get('network', location.get('gps')) #fetch location
    data = str(location)
    s.send(data) #send to server
    time.sleep(5) #wait for 5 seconds