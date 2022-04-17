import nmap 
import socket
import requests
import netifaces
import pprint



'''
PROCEDURE 
"local ipV4 address"
1.  Determine your own IP address
2.  Determine your own netmask
3.  Determine the network range
4.  Scan all the addresses 

EXTRAS
global_ip = requests.get("http://ifconfig.me/ip").text
'''





subnetMask_Table = (
    (  '/30'  ,  '255.255.255.252'  ), # 4 devices
    (  '/29'  ,  '255.255.255.248'  ), # 8 devices
    (  '/28'  ,  '255.255.255.240'  ), # 16 devices
    (  '/27'  ,  '255.255.255.224'  ), # 32 devices
    (  '/26'  ,  '255.255.255.192'  ), # 64 devices
    (  '/25'  ,  '255.255.255.128'  ), # 128 devices
    (  '/24'  ,  '255.255.255.0'  ), # 256 devices
    (  '/23'  ,  '255.255.254.0'  ), # 512 devices
    (  '/22'  ,  '255.255.252.0'  ), # 102 devices
    (  '/21'  ,  '255.255.248.0'  ), # 2,048 devices
    (  '/20'  ,  '255.255.240.0'  ), # 4,096 devices
    (  '/19'  ,  '255.255.224.0'  ), # 8,192 devices
    (  '/18'  ,  '255.255.192.0'  ), # 16,384 devices
    (  '/17'  ,  '255.255.128.0'  ), # 32,768 devices
    (  '/16'  ,  '255.255.0.0'  ), # 65,536 devices
)



# Determine your own IP address
'''
// Finding default ip that sockets will find first
VARIABLES:
    ip
'''
hostname = socket.gethostname() 
ip = socket.gethostbyname(hostname)





# Determine your own netmask FETCH MACHINE CONNECTIONS' IP ADDR
'''
// creating a dictionary that holds all network interfaces and their data 
VARIABLES:
    interface_output
    unused_interfaces
'''
interfaces = netifaces.interfaces()
interface_output = {}
unused_interfaces = []
for inf in interfaces:
    try:
        addrs = netifaces.ifaddresses(  inf  )
        output = addrs[netifaces.AF_INET]
        interface_output[inf] = output
    except:
        unused_interfaces.append(inf)
        # print(f"No ip for interface: {inf}")



'''
// Finding default ip address data, end program if not found
VARIABLES:
    default_addr

FIND INTERFACE IP ADDR SAME AS SOCKET.GET_HOST()
'''
default_addr = None
nested_break = False
for inf in interface_output:
    for inf_ip in interface_output[inf]:
        if inf_ip['addr'] == ip:
            default_addr = inf_ip
            nested_break = True
            break
    if nested_break == True:
        break
if not default_addr:
    print("Please make sure you are connected to the internet...")
    exit()





# Determine the network range
'''
// iterate through subnetMask_Table and find mask that maches default_addr["netmask"]
VARIABLES
    mask_range
'''
mask_range = None
for mask in subnetMask_Table:
    if mask[1] == default_addr["netmask"]:
        mask_range = mask[0]
if not mask_range:
    print("Not enough / Too many devices to filter through!")
    exit()




# Scan all the addresses 

'''
Condition ip string for nmap scan
'''
nmap_input = ""
ip_dummy = ip.split(".")
for x in range( 0   , len(ip_dummy) -1  , 1  ):
    nmap_input += ip_dummy[x] + "."
nmap_input += "0" +  mask_range



'''
// uses command line to run nmap scan of ip 0/mask_range
'''
nm = nmap.PortScanner()
nm.scan(
    hosts =  nmap_input ,
    arguments = "",
    timeout=60
)






# scan what ports are open and posssibly ssh into an open vibe















# debug
print( nm.command_line()   )

# print(ip)
# pprint.pprint(interface_output)
# print(default_addr)
# print(mask_range)
# print( nmap_input  )
print( nm.all_hosts()   )
# print(  nm.scaninfo()  )