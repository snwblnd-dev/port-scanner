import argparse
import asyncio

from parser import create_parser
from port_scan import PortScanner


def main():
    parser = create_parser()
    args = parser.parse_args()

    scanner = PortScanner(hostname=args.url, max_port=args.port, semaphore=args.semaphore)

    try:
        asyncio.run(scanner.scan_ports())
    except KeyboardInterrupt as e:
        print(e)



if __name__ == '__main__':
    main()


