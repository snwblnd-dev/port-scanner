from port_scan import PortScanner


def main():
    scanner = PortScanner('scanme.nmap.org')
    scanner.scan_ports()


if __name__ == '__main__':
    main()


