"""Module providing a function printing python version."""
from typing import Optional
from datetime import date
from pydantic import BaseModel

from fastapi import FastAPI, Query, Depends

app = FastAPI()


class HotelSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: Optional[int] = Query(None, ge=1, le=5),
            has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels")
async def get_hotels(
    search_args: HotelSearchArgs = Depends()
) -> list[SHotel]:
    hotels = [
        {
            "address": "ул. Гагарина 98",
            "name": "Super Hotel",
            "stars": 5
        }
    ]
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/booking")
async def add_booking(booking: SBooking):
    pass

def asd():
    pass
