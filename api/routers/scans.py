from fastapi import APIRouter

from port_scanner.port_scan import PortScanner
from schemas.scan_request_schema import ScanRequest

router = APIRouter()

@router.post("/scan")
async def scan_target(scan_params: ScanRequest):
    scanner = PortScanner(scan_params.hostname, scan_params.max_port, scan_params.semaphore)
    scanner.establish_connection(scan_params.hostname)
    return await scanner.scan_ports()

