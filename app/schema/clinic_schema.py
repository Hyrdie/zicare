from pydantic import BaseModel
from typing import Optional

class ClinicRequest(BaseModel):
    name: str
    address: str
    doctor_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "dipa",
                    "address": "Perum Masnaga Blok D203",
                    "list_doctor": "Dr. Verstappen",
                }
            ]
        }
    }

class ClinicUpdateRequest(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    doctor_name: Optional[str] = None

class ClinicResponse(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None

class ClinicDeleteResponse(BaseModel):
    id: int
    detail: str