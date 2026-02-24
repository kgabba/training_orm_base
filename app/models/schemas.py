from pydantic import BaseModel, Field

class User(BaseModel):
    username: str
    team_id: int
    rating: int
    position: str = Field(..., pattern="^(fw|df|gk)$")

class Team(BaseModel):
    name: str
