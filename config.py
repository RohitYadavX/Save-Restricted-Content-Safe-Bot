# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "8875"))
API_HASH = getenv("API_HASH", "0f54dd85c1a49")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8965").split()))
MONGO_DB = getenv("MONGO_DB", "monryhindi:<66X2Rghvyter0.gmdzu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-10022516"
CHANNEL_ID = int(getenv("CHANNEL_ID", "-10023358"))
