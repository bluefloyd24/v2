from os import getenv

from dotenv import load_dotenv

load_dotenv()

api_id = int(getenv("api_id", 25048157))
api_hash = getenv("api_hash", "f7af78e020826638ce203742b75acb1b")
session = getenv("session", "AQF-NF0AxRGF_4W7uTx4tWeibsayBK1Q3UcLuR8EbhlMdA4fOZAx5LfjxuobqobZkZkOm5ix6eEdZpWeFBNMOvp82INZq-nh5HJ9qJvhoQgSl5Pa5wztpGm839dm8tL6ey_WTnIa4CgpJhq19R3vHyxEkWfzpveRi8Lgl3q5xyif-P5g1Q5i0jQisi829QYT-dhd7ILxAacUdIhqCWB_que4SVMIrXETzkVHv_TVMVxcV1r5Cak5GfCBrplKFP_9th_f_zbZNt8uyxAXjGvPHEuk60LluxPfrCbRDgK9NAKWRK4g2XeoyTxuFvWm9XtMW25QG5opJeHR09Rmuimum8_oWNnzaAAAAAFn2t60AA")
bot_token = getenv("bot_token", "7582356038:AAFEmbPTC9YIx5h2NcP7_IxrQZfqzAbnKcA")
db_name = getenv("db_name", "KntDB")
mongo_uri = getenv("mongo_uri", "mongodb+srv://satumailseribuakuntele:dimarb24@cluster0.o10mi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
def_bahasa = getenv("def_bahasa", "id")
log_pic = getenv("log_pic", "https://telegra.ph/file/78fbd9d73e1f456857222.jpg")
heroku_api = getenv("heroku_api")
heroku_app_name = getenv("heroku_app_name")
upstream_repo = getenv(
    "upstream_repo",
    "https://github.com/bluefloyd24/v2",
)
upstream_branch = getenv("upstream_branch", "main")
git_token = getenv("git_token", "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")
log_channel = getenv("log_channel", None)
genius_api = getenv(
    "genius_api",
    "zhtfIphjnawHBcLFkIi-zE7tp8B9kJqY3xGnz_BlzQM9nhJJrD7csS1upSxUE0OMmiP3c7lgabJcRaB0hwViow",
)

