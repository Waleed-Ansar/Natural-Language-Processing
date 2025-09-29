from pydantic import BaseModel, Field
from typing import Optional
import uuid

class API_Response_Model(BaseModel):
    success: bool = False
    message: Optional[str] = None
    error: Optional[str] = None
    data: Optional[str] = None

class Response_Model(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    book: str
    
    class Config:
        populate_by_name = True
