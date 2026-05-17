import asyncio
import socket
import json

from pydantic import BaseModel


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

        async with self.semaphore:
            try:
                async with asyncio.timeout(.3):
                    reader, writer = await asyncio.open_connection(self.hostname, port)
                    writer.close()
                    await writer.wait_closed()
                    return "open"
            except Exception as e:
                return "closed"



    async def scan_ports(self):

        tasks = []
        async with asyncio.TaskGroup() as tg:
            for i in self.port_range:
                port_status = tg.create_task(self.connect_socket(i))
                tasks.append(port_status)

        # for i in range(0, len(tasks)):
        #     if tasks[i].result() != "closed":
        #         print(f'port {str(i + 1)} is {tasks[i].result()}')

        results = {}
        for i in range(0, len(tasks)):
            if tasks[i].result() != "closed":
                results.update({(i+1) : str(tasks[i].result())})
        return results








