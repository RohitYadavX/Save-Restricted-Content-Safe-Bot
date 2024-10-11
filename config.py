# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "249375"))
API_HASH = getenv("API_HASH", "0f628b53aba7debe24b24dd85c1a49")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "75938865"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://officialstoryhindi:<Rghdbvyti>@cluster0.gmdzu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002388870358"))
FORCESUB = getenv("FORCESUB", "-100238358")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "BQEtWHgAgU5z87BpOsNGF36Ah0MaiaEYP5sgoaT2bHaowLEbeyu3sVr00IvxuPQ2ga9YihADtnfYuwgrFihXsk5us0ev126e6aeNYMgfkSKju1JPP_m-yYW4VtzRBMnUgJ410n5QtTvFtwwr1QlyA-XuBBezCTFltf1tanY7_PgbKTfURfD-gsnWs7dvBPLUcMNXsV5HjaFc8OEfKXr4QVN1qPkAIx8nY8-hD2w0j7YynAWg9oAIeVtlZ8RCbwJ_1msYpUVCdi33nahUtzsTvtLqQGW6vJHMcGFwMNbvyMXBVV2xNKhRncoX5QJnwkFPxU0oz3ZQKXZ5a0x1_QAAAAHEoZQxAA") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
