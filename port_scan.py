import socket

class PortScanner:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = self.establish_connection(hostname)



    def establish_connection(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except socket.gaierror:
            raise ValueError(f"unable to resolve host: {hostname}")
        except socket.error as e:
            raise ConnectionError(f"Socket Error Occurred: {e}")


    def scan_ports(self, start_port = 1, end_port = 1024):
        for i in range(start_port, end_port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                result = s.connect_ex((self.ip, i))
                if result == 0:
                    print('port '+ str(i) + ' is open')
        return 'Scan complete'


