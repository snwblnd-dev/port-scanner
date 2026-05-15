import json

from pydantic import BaseModel


class ScanResponse(BaseModel):
    results: dict[str, str]