from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, column_property
from datetime import datetime
from sqlalchemy import func, ForeignKey, select

class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class UsersTable(Base):
    __tablename__ = 'users'
    username: Mapped[str]
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    rating: Mapped[int]
    position: Mapped[str]

class TeamsTable(Base):
    __tablename__ = 'teams'
    name: Mapped[str]
    power: Mapped[float] = column_property(
        select(func.round(func.avg(UsersTable.rating), 1))
        .where(UsersTable.team_id == id)  # связь по id команды
        .correlate_except(UsersTable)
        .scalar_subquery()
    )