from fastapi import APIRouter

from port_scanner.port_scan import PortScanner

router = APIRouter()

@router.post("/scan/")
async def scan_target(scan_params: PortScanner):
    scanner = PortScanner(scan_params)
    scanner.establish_connection(scan_params.hostname)
    results = await PortScanner.scan_ports(scan_params)
    return results

    return
