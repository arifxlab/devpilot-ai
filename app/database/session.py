from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import settings

DATABASE_URL = settings.database_url.replace(
    "sqlite:///",
    "sqlite+aiosqlite:///",
)

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.debug,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    """
    Yield an async database session.
    """
    async with AsyncSessionLocal() as session:
        yield session