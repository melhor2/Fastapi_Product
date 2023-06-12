from pydantic import BaseModel,Field
from typing import Optional

class Supplier(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=100, min_length=5, description="Name of supplier")
    address : str = Field(max_length=100, min_length=8, description="Addres of supplier")
    phone : str = Field(max_length=15, min_length=9)
    email : str = Field(max_length=50, min_length=10)

    class Config:
        schema_extra = {
            "example":{
                "id": 1,
                "name": "Mars Incorporated",
                "address": "Candy Jobs",
                "phone": "320 3555663",
                "email": "candyjobsprincipal@gmail.com"
            }
        }