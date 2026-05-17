from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    hostname: str
    max_port: int = Field(..., ge=1, le=65535)
    semaphore: int = Field(..., ge=1)