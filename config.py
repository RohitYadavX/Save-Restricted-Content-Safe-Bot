# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7593890865").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://officialstoryhindi:<BPl66X2Rghdbvyti>@cluster0.gmdzu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002295215916")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002388870358"))
