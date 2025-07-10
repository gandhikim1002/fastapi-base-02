from sqlmodel import Field, SQLModel

class ItemPayloadV3(SQLModel, table=True):
    item_id: int | None = Field(default=None, primary_key=True)
    item_name: str = Field(index=True)
    quantity: int | None = Field(default=None, index=True)

class ItemPayloadV4(SQLModel, table=True):
    item_id: int | None = Field(default=None, primary_key=True)
    item_name: str = Field(index=True)
    quantity: int | None = Field(default=None, index=True)
