import asyncio
import socket



class PortScanner:
    def __init__(self, hostname, max_port = 1024, semaphore = 500):
        self.hostname = hostname
        self.ip = self.establish_connection(hostname)
        self.port_range = range(1, max_port+1)
        self.semaphore = asyncio.Semaphore(semaphore)


    def establish_connection(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except socket.gaierror:
            raise ValueError(f"unable to resolve host: {hostname}")
        except socket.error as e:
            raise ConnectionError(f"Socket Error Occurred: {e}")

    async def connect_socket(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setblocking(False)
            s.settimeout(.1)
            return s.connect_ex((self.hostname, port))




    async def scan_ports(self):

        tasks = []
        async with asyncio.TaskGroup() as tg:
            for i in self.port_range:
                port_status = tg.create_task(self.connect_socket(i))
                tasks.append(port_status)


        for task in tasks:
            print(task)





