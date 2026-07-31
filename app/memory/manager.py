from app.memory.session import Session


class MemoryManager:
    """
    Manages active conversation sessions.
    """

    def __init__(self) -> None:
        self._sessions: dict[str, Session] = {}

    def create_session(self) -> Session:
        """
        Create and register a new session.
        """
        session = Session()
        self._sessions[session.id] = session
        return session

    def get_session(self, session_id: str) -> Session | None:
        """
        Retrieve an existing session.
        """
        return self._sessions.get(session_id)

    def get_or_create(self, session_id: str | None = None) -> Session:
        """
        Return an existing session or create a new one.
        """
        if session_id and session_id in self._sessions:
            return self._sessions[session_id]

        return self.create_session()

    def delete_session(self, session_id: str) -> None:
        """
        Remove a session.
        """
        self._sessions.pop(session_id, None)

    def clear(self) -> None:
        """
        Remove all sessions.
        """
        self._sessions.clear()

    def session_count(self) -> int:
        """
        Number of active sessions.
        """
        return len(self._sessions)