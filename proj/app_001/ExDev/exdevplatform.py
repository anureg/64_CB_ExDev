from fastapi import APIRouter

from pydantic import BaseModel
from typing import List, Union

from datetime import datetime, timezone, timedelta


class Login_in(BaseModel):
    username: str
    password: str
    device_id: str


router = APIRouter(
    prefix="/ExDevPlatform",
    tags=["ExDevPlatform"],
)


@router.get("/")
def login_platform(usrname: str, password: str, device_id: str):
    # Time zone in Thailand UTC+7
    tz = timezone(timedelta(hours=7))
    # Create a date object with given timezone
    timestr = datetime.now(tz=tz).isoformat(sep=" ")
    # hash(device_id + timestr)
    token = hash(device_id + timestr)  # type token int

    if usrname == 'facebook':
        username = usrname
        name = 'Face'
        surname = 'book'
        icon = '/ExDev/icon_platform/Facebook.png'

    elif usrname == 'twitter':
        username = usrname
        name = 'Twit'
        surname = 'ter'
        icon = '/ExDev/icon_platform/Twitter.png'

    elif usrname == 'instagram':
        username = usrname
        name = 'Insta'
        surname = 'gram'
        icon = '/ExDev/icon_platform/Instagram.png'

    return {
        "token": token,
        "username": username,
        "name": name,
        "surname": surname,
        "icon": icon
    }
