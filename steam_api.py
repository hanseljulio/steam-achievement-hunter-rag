from models.models import PlayerAchievementsResponse, GameSchemaResponse
import requests
from settings import STEAM_API_KEY, STEAM_ID

def get_schema_for_game(app_id: int) -> GameSchemaResponse:
    url = "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v0002"
    params = {
        "key": STEAM_API_KEY,
        "appid": app_id
    }
    response = requests.get(url, params=params)
    return GameSchemaResponse(**response.json())

def get_player_achievements(app_id: int) -> PlayerAchievementsResponse:
    url = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001"
    params = {
        "key": STEAM_API_KEY,
        "appid": app_id,
        "steamid": STEAM_ID
    }
    response = requests.get(url, params=params)
    return PlayerAchievementsResponse(**response.json())
    
# Test block
# app_id = 1903340

# print("=== Game Schema ===")
# schema = get_schema_for_game(app_id)
# print(schema.model_dump_json(indent=4))

# print("\n=== Player Achievements ===")
# achievements = get_player_achievements(app_id)
# print(achievements.model_dump_json(indent=4))