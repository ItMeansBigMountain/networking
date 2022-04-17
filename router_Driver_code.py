import json
import requests
from Router import RouterConnection
import socket


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


cisco1 = RouterConnection( local_ip , "4444")

print(cisco1)