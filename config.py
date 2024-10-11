# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24935975"))
API_HASH = getenv("API_HASH", "0f628b53aba7debe2de4b24dd85c1a49")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "7593890865"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://officialstoryhindi:<BPl66X2Rghdbvyti>@cluster0.gmdzu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "TGJokerSave"))
FORCESUB = getenv("FORCESUB", "TGJokerSave")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
