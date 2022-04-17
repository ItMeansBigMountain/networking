class RouterConnection():
    def __init__(self, ip , port , protocol = {"connection": "tcp" }):
        self.ip = ip
        self.port = port
        self.protocol = protocol
    
    def __repr__(self):
        return f"{self.ip} , {self.port} \n{self.protocol}"


    # fetch data functions
    def fetch_ip(self):
        return self.ip
    def fetch_port(self):
        return self.port
    def fetch_protocol(self):
        return self.protocol

    # change configuration functions
    