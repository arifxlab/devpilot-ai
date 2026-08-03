from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Conversation


class ConversationRepository:
    """
    Repository responsible for Conversation database operations.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, conversation: Conversation) -> Conversation:
        """
        Create a new conversation.
        """
        self.session.add(conversation)
        await self.session.commit()
        await self.session.refresh(conversation)
        return conversation

    async def get(self, conversation_id: int) -> Conversation | None:
        """
        Retrieve a conversation by ID.
        """
        stmt = select(Conversation).where(
            Conversation.id == conversation_id,
        )

        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def list_all(self) -> list[Conversation]:
        """
        Retrieve all conversations.
        """
        stmt = select(Conversation).order_by(
            Conversation.created_at.desc(),
        )

        result = await self.session.execute(stmt)

        return list(result.scalars().all())

    async def update_title(
        self,
        conversation: Conversation,
        title: str,
    ) -> Conversation:
        """
        Update conversation title.
        """
        conversation.title = title

        await self.session.commit()
        await self.session.refresh(conversation)

        return conversation

    async def delete(
        self,
        conversation: Conversation,
    ) -> None:
        """
        Delete a conversation.
        """
        await self.session.delete(conversation)
        await self.session.commit()