from typing import Optional

from pydantic import BaseModel

from sqlmodel import Field, SQLModel

class ItemPayload(BaseModel):
    item_id: Optional[int]
    item_name: str
    quantity: int

class ItemPayloadV2(SQLModel, table=True):
    item_id: int | None = Field(default=None, primary_key=True)
    item_name: str = Field(index=True)
    quantity: int | None = Field(default=None, index=True)