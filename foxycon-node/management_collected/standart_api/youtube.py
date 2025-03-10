from datetime import datetime
from typing import Optional

import httpx
from pydantic import BaseModel


class Auth(BaseModel):
    key: str


class Link(Auth):
    link: str
    type: str | None = None

class AnalyticsObj(BaseModel):
    url: str
    social_network: str
    content_type: str
    code: str

class FullDataVideo(Auth):
    system_id: str
    channel_id: str
    title: str
    likes: int
    link: str
    views: int
    channel_url: str
    publish_date: datetime
    subtitles: Optional[str] = None
    type: str|None = None

async def send_single_data_to_server(data):
    async with httpx.AsyncClient() as client:
        data = FullDataVideo(
        key="B00XgwofN.Aw",
        system_id=data.system_id,
        channel_id=data.channel_id,
        title=data.title,
        likes=data.likes,
        link=data.link,
        views=data.views,
        channel_url=data.channel_url,
        publish_date=data.publish_date,  # Должен быть формат ISO 8601
        subtitles=data.subtitles if data.subtitles else None,
    )
        response = await client.post("http://127.0.0.1:2222/youtube/add_full_data_video", json=data.model_dump(mode='json'), timeout=30.0)
        print(response.status_code)
        print(response.text)