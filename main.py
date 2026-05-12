import asyncio
from concurrent.futures import ThreadPoolExecutor

from port_scan import PortScanner


def main():

    scanner = PortScanner('scanme.nmap.org', 1024)
    # futures = [executor.submit(scanner.scan_ports(scanner.port_range))]
    # executor.map(scanner.scan_ports, scanner.port_range)
    asyncio.run(scanner.scan_ports())



if __name__ == '__main__':
    main()


