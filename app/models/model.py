from datetime import datetime
from sqlalchemy import ForeignKey, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class UsersTable(Base):
    __tablename__ = "users"

    username: Mapped[str]
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    rating: Mapped[int]
    position: Mapped[str]

class TeamsTable(Base):
    __tablename__ = "teams"

    name: Mapped[str]