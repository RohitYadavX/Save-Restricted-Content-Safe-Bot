# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24975"))
API_HASH = getenv("API_HASH", "0f53aba7debe2de4b24dd85c1a49")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7593890865").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://officialstoryhindi:<66X2Rghvyti>@cluster0.gmdzu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-100229521516"
CHANNEL_ID = int(getenv("CHANNEL_ID", "-10023888358"))
