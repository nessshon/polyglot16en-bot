from dataclasses import dataclass

from environs import Env

TIMEZONE = "Europe/Moscow"


@dataclass
class Config:
    REDIS_HOST: str
    BOT_TOKEN: str
    DEV_ID: int


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        REDIS_HOST=env.str("REDIS_HOST"),
        BOT_TOKEN=env.str("BOT_TOKEN"),
        DEV_ID=env.int("DEV_ID"),
    )
