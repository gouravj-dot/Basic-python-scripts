from ipaddress import ip_address
import socket

target =  input('Enter the IP address: ')
portrange  = input('enter the port-range to scan: ')

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print('scaning host',target,'from port',lowport,'to port',highport)

for port in range(lowport,highport):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    status = s.connect_ex((target,port))
    if (status==0):
        print('port',port,'open')
    
    s.close
