from pydantic import BaseModel
from typing import List, Optional


# -----------------------------
# Player Achievement Models
# -----------------------------

class PlayerAchievement(BaseModel):
    apiname: str
    achieved: int
    unlocktime: int


class PlayerStats(BaseModel):
    steamID: str
    gameName: str
    achievements: List[PlayerAchievement]
    success: bool


class PlayerAchievementsResponse(BaseModel):
    playerstats: PlayerStats


# -----------------------------
# Game Schema Models
# -----------------------------

class GameAchievement(BaseModel):
    name: str
    defaultvalue: int
    displayName: str
    hidden: int
    description: Optional[str] = None
    icon: str
    icongray: str


class AvailableGameStats(BaseModel):
    achievements: List[GameAchievement]


class GameSchema(BaseModel):
    gameName: str
    gameVersion: str
    availableGameStats: AvailableGameStats


class GameSchemaResponse(BaseModel):
    game: GameSchema