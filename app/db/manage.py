from environs import Env
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.db import models
from .models.base import Base


class Database:

    def __init__(self):
        env = Env()
        env.read_env()

        self.engine = create_async_engine(
            f"mysql+aiomysql://"
            f"{env.str('DB_USER')}:"
            f"{env.str('DB_PASS')}@"
            f"{env.str('DB_HOST')}:"
            f"{env.int('DB_PORT')}/"
            f"{env.str('DB_NAME')}",
            pool_pre_ping=True,
        )
        self.sessionmaker = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def run_sync(self) -> None:
        async with self.engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)

    @property
    def lesson(self) -> models.Lesson:
        return models.Lesson(self.sessionmaker)

    @property
    def user(self) -> models.User:
        return models.User(self.sessionmaker)
