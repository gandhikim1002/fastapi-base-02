import uuid

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.src.dependencies import get_token_header, get_db
from app.src.domain.item import service, models as item_models
from app.resources.strings import ITEM_DOES_NOT_EXIST_ERROR


router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/{item_id}", response_model=item_models.Item)
def read_item(item_id: uuid.UUID, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return db_item


@router.get("/test/{item_id}", response_model=item_models.Item)
def read_item_test(item_id: uuid.UUID, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)
    return db_item

@router.get("/", response_model=List[item_models.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = service.get_items(db, skip=skip, limit=limit)
    return items

# raise HTTPException(status_code=404, detail=ITEM_DOES_NOT_EXIST_ERROR)

'''
@router.get("/{car_id}", response_model=schemas.Car)
def read_car(car_id: int, db: Session = Depends(get_db)):
    return service.get_car(db, car_id=car_id)

@router.get("/{id}", response_model=ItemPublic)
def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Get item by ID.
    """
    item = session.get(Item, id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item

    
@router.get("/{stock_id}", response_model=schemas.Stock)
def read_stock(stock_id: int, db: Session = Depends(get_db)):
    db_stock = service.get_stock(db, stock_id=stock_id)
    if db_stock is None:
        raise HTTPException(status_code=404, detail=STOCK_DOES_NOT_EXIST_ERROR)
    return service.get_stock(db, stock_id=stock_id)

@router.get("/{seller_id}", response_model=schemas.Seller)
def read_seller(seller_id: int, db: Session = Depends(get_db)):
    db_seller = service.get_seller(db, seller_id=seller_id)
    if db_seller is None:
        raise HTTPException(status_code=404, detail=SELLER_DOES_NOT_EXIST_ERROR)
    return db_seller
'''