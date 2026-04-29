import socket

def port_scan(hostname):
    try:
        ipAddress: str = socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Unable to resolve host"

    for i in range(1, 65536):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(.1)
            result = s.connect_ex((ipAddress, i))
            if result == 0:
                print('port '+ str(i) + ' is open')
    return 'Scan complete'