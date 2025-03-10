import datetime
from sqlalchemy import ForeignKey, String, Text, Date, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy import select, text
import uuid
from uuid import UUID

from data_structures.engine import get_session_factory

Base: DeclarativeMeta = declarative_base()

uuid_func = uuid.uuid4()


class Base(DeclarativeBase):
    pass


class YoutubeChannels(Base):
    __tablename__ = 'youtube_channels'

    id: Mapped[UUID] = mapped_column(default=uuid.uuid4(), primary_key=True)
    system_id: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    name: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    link: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    views: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    subscribers: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    country: Mapped[str] = mapped_column(String, nullable=True, unique=False)

    contents = relationship("ContentsYoutube", back_populates="youtube_channel")

    async def add_youtube_channels(self):
        async with get_session_factory() as session:
            self.id = uuid.uuid4()
            session.add(self)
            id = self.id
            await session.commit()
            return id

    async def get_youtube_channels_system_id(self):
        async with get_session_factory() as session:
            if type(self.id) is str:
                self.id = UUID(self.id)
            query = select(YoutubeChannels).where(YoutubeChannels.system_id == self.system_id)
            data = await session.execute(query)
            data = data.scalars().all()
            if not data:
                return data
            else:
                return data[0]


class InstagramPages(Base):
    __tablename__ = 'instagram_pages'

    id: Mapped[UUID] = mapped_column(default=uuid.uuid4(), primary_key=True)
    system_id: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    name: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    link: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    subscribers: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)

    contents = relationship("ContentsInstagram", back_populates="instagram_page")

    async def add_instagram_pages(self):
        async with get_session_factory() as session:
            self.id = uuid.uuid4()
            session.add(self)
            id = self.id
            await session.commit()
            return id

    async def get_instagram_pages_system_id(self):
        async with get_session_factory() as session:
            if type(self.id) is str:
                self.id = UUID(self.id)
            query = select(InstagramPages).where(InstagramPages.system_id == self.system_id)
            data = await session.execute(query)
            data = data.scalars().all()
            if not data:
                return data
            else:
                return data[0]


class ContentsYoutube(Base):
    __tablename__ = 'contents_youtube'

    id: Mapped[UUID] = mapped_column(default=uuid.uuid4(), primary_key=True)
    system_id: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    title: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    link: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    types_content: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    number_views: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    number_likes: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    number_comments: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    updating_data: Mapped[Date] = mapped_column(Date, default=datetime.datetime.utcnow(),
                                                server_default=text("TIMEZONE('utc', now())"), nullable=True,
                                                unique=False)
    data_add: Mapped[Date] = mapped_column(Date, default=datetime.datetime.utcnow(),
                                           server_default=text("TIMEZONE('utc', now())"), nullable=True, unique=False)
    release_date: Mapped[Date] = mapped_column(Date, nullable=True, unique=False)
    youtube_channels_id: Mapped[UUID] = mapped_column(ForeignKey('youtube_channels.id'))

    youtube_channel = relationship("YoutubeChannels", back_populates="contents")

    async def add_contents_youtube(self):
        async with get_session_factory() as session:
            self.id = uuid.uuid4()
            session.add(self)
            id = self.id
            await session.commit()
            return id


    async def get_instagram_pages_system_id(self):
        async with get_session_factory() as session:
            query = select(ContentsYoutube).where(ContentsYoutube.system_id == self.system_id)
            data = await session.execute(query)
            data = data.scalars().all()
            if not data:
                return data
            else:
                return data[0]


class ContentsInstagram(Base):
    __tablename__ = 'contents_instagram'

    id: Mapped[UUID] = mapped_column(default=uuid.uuid4(), primary_key=True)
    system_id: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    title: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    link: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    types_content: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    number_views: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    number_likes: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    number_comments: Mapped[int] = mapped_column(BigInteger, nullable=True, unique=False)
    view_content: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    updating_data: Mapped[Date] = mapped_column(Date, default=datetime.datetime.utcnow(),
                                                server_default=text("TIMEZONE('utc', now())"), nullable=True,
                                                unique=False)
    data_add: Mapped[Date] = mapped_column(Date, default=datetime.datetime.utcnow(),
                                           server_default=text("TIMEZONE('utc', now())"), nullable=True, unique=False)
    release_date: Mapped[Date] = mapped_column(Date, nullable=True, unique=False)
    instagram_page_id: Mapped[UUID] = mapped_column(ForeignKey('instagram_pages.id'))

    instagram_page = relationship("InstagramPages", back_populates="contents")

    async def add_contents_instagram(self):
        async with get_session_factory() as session:
            self.id = uuid.uuid4()
            session.add(self)
            id = self.id
            await session.commit()
            return id



class YoutubeSubtitles(Base):
    __tablename__ = 'youtube_subtitles'

    id: Mapped[UUID] = mapped_column(default=uuid.uuid4(), primary_key=True)
    subtitles_text: Mapped[str] = mapped_column(Text, nullable=True, unique=False)
    contents_youtube_id: Mapped[UUID] = mapped_column(ForeignKey('contents_youtube.id'), nullable=True, unique=False)

    contents_youtube = relationship("ContentsYoutube")
