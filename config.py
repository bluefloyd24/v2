from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv("api_id", 22264168))
api_hash = getenv("api_hash", 9c08e17d0578aab749db0b147a7402eb )
session = getenv("session", BQFTuWgAPo5ha7FGG1u_vvb4DCyHn5EMciOQY3GKxtKY_UZ-DvokoKK3jAL7-SFnMUxVFvjHNfIuw2xGjQdky5Z7StOHzLtjHK4UJ-2c_cSUZKWPwKHXhgbuBEo0JOZhnaL23EjMkH3lTZB5jLyFQ7K2W25wYD3fXz7EBhMvyJggYn8plH-0iQgaRpVoHAFtZ6lR7kybT9q3u9Irz7OkPz3tr5nLgPdY5aQg96y8lvHlL4zFE19pajyCQfBXuoBz4rTjJSgMLwDTS--nFlG1fWpBTG3fZkHwNO2tikV9ktCVZSh5St4uH-bChjLyx14eOA55DOzQzJKx39NHf9-Ge1au8DqcuAAAAAGZ95bIAA )
bot_token = getenv("bot_token", 8124800648:AAFFyBeUDOu18a5fam7fVTOV_7XU81eZq_o)
db_name = getenv("db_name", NewBDB)
mongo_uri = getenv("mongo_uri", mongodb+srv://akkagdba:dimarb11@cluster0.6zz04.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)
def_bahasa = getenv("def_bahasa", "id")
log_pic = getenv("log_pic", "https://telegra.ph/file/78fbd9d73e1f456857222.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/bluefloyd24/v2",
)
upstream_branch = getenv("upstream_branch", "main")
git_token = getenv("git_token", None)
log_channel = getenv("log_channel", None)
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)

