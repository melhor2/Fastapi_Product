from pydantic import BaseModel, Field
from typing import Optional


class Supplies(BaseModel):
    id : Optional[int] = None
    sup_id : int = Field(su = 1, description="ForegnKey of supplier")
    pro_id : int = Field(pr = 1, description="ForeignKey of product")
    purchase_price: float = Field(description='Purchase price of product the product from the supplier')

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "sup_id":1,
                "pro_id":1,
                "purchase_price":11101
            }
        }