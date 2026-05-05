from models.models import PlayerAchievementsResponse, GameSchemaResponse, OwnedGamesResponse, GlobalAchievementPercentagesResponse
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

def get_owned_games() -> OwnedGamesResponse:
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    params = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID,
        "include_appinfo": True,
        "include_played_free_games": True
    }
    response = requests.get(url, params=params)
    return OwnedGamesResponse(**response.json())

def get_global_achievement_percentages_for_app(game_id: int) -> GlobalAchievementPercentagesResponse:
    url = "https://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/"
    params = {
        "gameid": game_id
    }
    response = requests.get(url, params=params)
    return GlobalAchievementPercentagesResponse(**response.json())
    
# Test block
app_id = 1903340

# print("=== Game Schema ===")
# schema = get_schema_for_game(app_id)
# print(schema.model_dump_json(indent=4))

# print("\n=== Player Achievements ===")
# achievements = get_player_achievements(app_id)
# print(achievements.model_dump_json(indent=4))

print("\n=== Owned Games ===")
try:
    owned_games = get_owned_games()
    print(owned_games.model_dump_json(indent=4))
except Exception as e:
    print(f"Error fetching owned games: {e}")

print("\n=== Global Achievement Percentages ===")
try:
    global_percentages = get_global_achievement_percentages_for_app(app_id)
    print(global_percentages.model_dump_json(indent=4))
except Exception as e:
    print(f"Error fetching global percentages: {e}")