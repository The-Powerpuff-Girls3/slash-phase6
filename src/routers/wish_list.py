"""
Copyright (c) 2023 Sathiya Narayanan Venkatesan
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

# importing necessary modules


from fastapi import Depends, status, APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from database import engine
from sqlalchemy.orm import Session
import models
from src.routers.auth import get_current_user, get_db
import sys
sys.path.append("..")

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/wishlist",
    tags=["wishlist"],
    responses={404: {"description": "Not found"}}
)
models.Base.metadata.create_all(bind=engine)


# get all the products in the wishlist of a user
@router.get("/")
async def get_from_wishlist(request: Request, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

    list = db.query(models.Products).filter(models.Products.user_id == user.get("id")).all()
    if list is None:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    json_data = {}

    for product in list:
        product_id = product.product_id
        product_info = product.product
        json_data[product_id] = product_info

    return JSONResponse(content=json_data, status_code=200, headers={"X-Custom-Header": "value"})


# Add to the wishlist of a user
@router.post("/")
async def add_to_wishlist(request: Request, product_info: str = Form(...), db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    product = models.Products()
    product.user_id = user.get("id")
    product.product = product_info
    db.add(product)
    db.commit()
    return True


# Delete from the wishlist of a user
@router.delete("/{product_id}")
async def delete_from_wishlist(request: Request, product_id: int, db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

    list = db.query(models.Products).filter(models.Products.product_id == product_id).filter(models.Products.user_id == user.get("id")).first()

    if list is None:
        return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)

    db.query(models.Products).filter(models.Products.product_id == product_id).delete()
    db.commit()

    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
