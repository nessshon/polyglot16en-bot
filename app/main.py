from aiogram import Dispatcher


async def on_startup(dp: Dispatcher):
    from app.db.manage import Database
    db: Database = Database()
    await db.run_sync()
    dp.bot["db"] = db

    from .bot import filters
    filters.setup(dp)

    from .bot import middlewares
    middlewares.setup(dp)

    from .bot import handlers
    handlers.errors.register(dp)
    handlers.commands.register(dp)
    handlers.messages.register(dp)
    handlers.callbacks.register(dp)

    await handlers.commands.setup(dp.bot)


async def on_shutdown(dp: Dispatcher):
    from app.db.manage import Database
    db: Database = dp.bot.get("db")
    await db.engine.dispose()

    await dp.storage.close()
    await dp.storage.wait_closed()

    session = await dp.bot.get_session()
    await session.close()
