import socket

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
print ip_addr