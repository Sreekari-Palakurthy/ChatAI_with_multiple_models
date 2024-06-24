from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        from users.models import User
        from keys.models import Key
        from threads.models import Thread
        from messages.models import Message
        await conn.run_sync(User.metadata.create_all)
        await conn.run_sync(Key.metadata.create_all)
        await conn.run_sync(Thread.metadata.create_all)
        await conn.run_sync(Message.metadata.create_all)
