from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv("api_id", None))
api_hash = getenv("api_hash", None)
session = getenv("session", None)
bot_token = getenv("bot_token", None)
db_name = getenv("db_name", None)
mongo_uri = getenv("mongo_uri", None)
def_bahasa = getenv("def_bahasa", "id")
log_pic = getenv("log_pic", "https://telegra.ph/file/78fbd9d73e1f456857222.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/bluefloyd24/bfyd",
)
upstream_branch = getenv("upstream_branch", "final")
git_token = getenv("git_token", None)
log_channel = getenv("log_channel", None)
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)

