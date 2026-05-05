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

# -----------------------------
# Owned Games Models
# -----------------------------

class OwnedGame(BaseModel):
    appid: int
    name: Optional[str] = None
    playtime_forever: int
    img_icon_url: Optional[str] = None
    has_community_visible_stats: Optional[bool] = None
    playtime_windows_forever: Optional[int] = None
    playtime_mac_forever: Optional[int] = None
    playtime_linux_forever: Optional[int] = None
    rtime_last_played: Optional[int] = None


class OwnedGames(BaseModel):
    game_count: int
    games: List[OwnedGame]


class OwnedGamesResponse(BaseModel):
    response: OwnedGames

# -----------------------------
# Global Achievement Percentages Models
# -----------------------------

class GlobalAchievementPercentage(BaseModel):
    name: str
    percent: float

class GlobalAchievementPercentages(BaseModel):
    achievements: List[GlobalAchievementPercentage]

class GlobalAchievementPercentagesResponse(BaseModel):
    achievementpercentages: GlobalAchievementPercentages
