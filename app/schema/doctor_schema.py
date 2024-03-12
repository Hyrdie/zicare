from pydantic import BaseModel
from typing import Optional

class DocterRequest(BaseModel):
    name: str
    specialize: str

class DocterResponse(BaseModel):
    id: int
    name: str
    specialize: str

class DocterDeletedResponse(BaseModel):
    id: int
    detail: str