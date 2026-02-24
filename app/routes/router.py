from fastapi.routing import APIRoute
from main import api
from sqlalchemy.orm import Session
from models.model import UsersTable, TeamsTable
from fastapi import HTTPException
from models.model import Base
from models.schemas import User, Team


router_basic = APIRoute(prefix='/do')

mapped_dict = {'users' : UsersTable,
               'teams' : TeamsTable}

@router_basic.get('/{table_name}')
def get_data_from_table(table_name: str):
    class_table = mapped_dict.get(table_name)
    if not class_table:
        raise HTTPException(status_code=404, detail=f'table {table_name} not found in db')
    with Session(api.state.eng) as session:
       result = session.query(class_table).all()
       return result
    
@router_basic.get('/all_tables')
def get_tables_name():
    return list(Base.metadata.tables.keys())

@router_basic.post('/add_user')
def add_user_db(user: User):
    new_user = UsersTable(username=user.username,
                          team_id=user.team_id,
                          rating=user.rating,
                          position=user.position)
    with Session(api.state.eng) as session:
        session.add(new_user)
        session.commit()
    return new_user

@router_basic.post('/add_team')
def add_team_db(team: Team):
    new_team = TeamsTable(name=team.name)
    with Session(api.state.eng) as session:
        session.add(new_team)
        session.commit()
    return new_team