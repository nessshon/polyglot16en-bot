from __future__ import annotations

from sqlalchemy import *
from sqlalchemy.ext.asyncio import async_sessionmaker

from .base import Base


class Lesson(Base):
    """
    Represents a user object in the database.

    Attributes:
        id (int):
        title (str):
        description (str):
        video_url (str):
        audio_url (str):
        text_url (str):
    """
    __tablename__ = "lessons"

    id = Column(
        BigInteger,
        unique=True,
        primary_key=True,
        autoincrement=False,
    )
    title = Column(
        VARCHAR(length=64),
        nullable=False,
    )
    description = Column(
        VARCHAR(length=2048),
    )
    video_url = Column(
        VARCHAR(length=512),
        nullable=False,
    )
    audio_url = Column(
        VARCHAR(length=512),
        nullable=False,
    )
    text_url = Column(
        VARCHAR(length=512),
        nullable=False,
    )

    def __init__(self, sessionmaker=None, *args, **kwargs) -> None:
        """
        Initializes a new Lesson object.

        :param sessionmaker: The async sessionmaker to use for database operations.
        :param args: Additional arguments to pass to the parent class.
        :param kwargs: Additional keyword arguments to pass to the parent class.
        """
        self.async_sessionmaker: async_sessionmaker = sessionmaker
        super().__init__(*args, **kwargs)

    async def add(self, **kwargs) -> Lesson:
        """
        Add a new user to the database.

        :param kwargs: The attributes of the new user.
        :return: The newly created :class:`Lesson` object.
        """
        async with self.async_sessionmaker() as session:
            model = Lesson(**kwargs)
            session.add(model)

            await session.commit()
            await session.refresh(model)
            return model

    async def get(self, lesson_id: int) -> Lesson:
        """
        Retrieve a user from the database by ID.

        :param lesson_id: The ID of the user to retrieve.
        :return: The :class:`Lesson` object.
        """
        async with self.async_sessionmaker() as session:
            query = await session.execute(
                select(Lesson).
                where(Lesson.id == lesson_id)
            )
            return query.scalar()

    async def update(self, lesson_id: int, **kwargs) -> None:
        """
        Update a user in the database by ID.

        :param lesson_id: The ID of the user to update.
        :param kwargs: The attributes to update.
        :return: None
        """
        async with self.async_sessionmaker() as session:
            await session.execute(
                update(Lesson).
                where(Lesson.id == lesson_id).
                values(**kwargs)
            )
            await session.commit()

    async def delete(self, lesson_id: int) -> None:
        """
        Delete a user from the database by ID.

        :param lesson_id: The ID of the user to delete.
        :return: None
        """
        async with self.async_sessionmaker() as session:
            await session.execute(
                delete(Lesson).
                where(Lesson.id == lesson_id)
            )
            await session.commit()

    async def is_exists(self, lesson_id: int) -> bool:
        """
        Check if a user with the given user ID exists in the database.

        :param lesson_id: The ID of the user to check.
        :return: True if the user exists, False otherwise.
        """
        async with self.async_sessionmaker() as session:
            query = await session.execute(
                select(Lesson.id).
                where(Lesson.id == lesson_id)
            )
            return query.scalar() is not None

    async def get_all(self) -> list[Lesson]:
        """
        Retrieve all users from the database.

        :return: A list of :class:`Lesson` objects.
        """
        async with self.async_sessionmaker() as session:
            query = await session.execute(
                select(Lesson).
                order_by(Lesson.id)
            )
            return [i[0] for i in query.all()]
