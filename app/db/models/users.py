from __future__ import annotations

from datetime import datetime

import pytz
from sqlalchemy import *
from sqlalchemy.ext.asyncio import async_sessionmaker

from .base import Base
from app.config import TIMEZONE


class User(Base):
    """
    Represents a user object in the database.

    Attributes:
        id (int): The ID of the user.
        first_name (str): The first name of the user.
        created_at (datetime): The date and time when the user was created.
    """
    __tablename__ = "users"

    id = Column(
        BigInteger,
        unique=True,
        primary_key=True,
        autoincrement=False,
    )
    first_name = Column(
        VARCHAR(length=64),
        nullable=False,
    )
    created_at = Column(
        DateTime,
        default=datetime.now(
            tz=pytz.timezone(TIMEZONE),
        ),
    )

    def __init__(self, sessionmaker=None, *args, **kwargs) -> None:
        """
        Initializes a new User object.

        :param sessionmaker: The async sessionmaker to use for database operations.
        :param args: Additional arguments to pass to the parent class.
        :param kwargs: Additional keyword arguments to pass to the parent class.
        """
        self.async_sessionmaker: async_sessionmaker = sessionmaker
        super().__init__(*args, **kwargs)

    async def add(self, **kwargs) -> User:
        """
        Add a new user to the database.

        :param kwargs: The attributes of the new user.
        :return: The newly created :class:`User` object.
        """
        async with self.async_sessionmaker() as session:
            model = User(**kwargs)
            session.add(model)

            await session.commit()
            await session.refresh(model)
            return model

    async def get(self, user_id: int) -> User:
        """
        Retrieve a user from the database by ID.

        :param user_id: The ID of the user to retrieve.
        :return: The :class:`User` object.
        """
        async with self.async_sessionmaker() as session:
            query = await session.execute(
                select(User).
                where(User.id == user_id)
            )
            return query.scalar()

    async def update(self, user_id: int, **kwargs) -> None:
        """
        Update a user in the database by ID.

        :param user_id: The ID of the user to update.
        :param kwargs: The attributes to update.
        :return: None
        """
        async with self.async_sessionmaker() as session:
            await session.execute(
                update(User).
                where(User.id == user_id).
                values(**kwargs)
            )
            await session.commit()

    async def delete(self, user_id: int) -> None:
        """
        Delete a user from the database by ID.

        :param user_id: The ID of the user to delete.
        :return: None
        """
        async with self.async_sessionmaker() as session:
            await session.execute(
                delete(User).
                where(User.id == user_id)
            )
            await session.commit()

    async def is_exists(self, user_id: int) -> bool:
        """
        Check if a user with the given user ID exists in the database.

        :param user_id: The ID of the user to check.
        :return: True if the user exists, False otherwise.
        """
        async with self.async_sessionmaker() as session:
            query = await session.execute(
                select(User.id).
                where(User.id == user_id)
            )
            return query.scalar() is not None
