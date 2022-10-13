import jwt
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Header
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from tklauthtools.feature_flags import FeatureFlagService

from app.internal import do_stuff, do_other_stuff, do_not_do_stuff
from app.flags import init_feature_flags
from app.secrets import init_secrets_manager

load_dotenv()
init_secrets_manager()

app = FastAPI()
app.mount("/assets", StaticFiles(directory="./dist/assets"), name="dist")

def user(authorization: str = Header(default="")):
    decoded = jwt.decode(authorization, options={"verify_signature": False})
    audiences = decoded['aud']
    audience_key = next((aud for aud in audiences if any(map(lambda key: key.startswith(aud), decoded.keys()))), "")
    return decoded[f"{audience_key}/user_data"]

@app.get("/")
async def index():
    return FileResponse("dist/index.html")

@app.get("/data")
async def super_amazing_app(
    ffs: FeatureFlagService = Depends(init_feature_flags),
    user: dict = Depends(user)
):
    ffs.set_user_from_auth0(user)
    flag_value = ffs.get_flag_for_user("ab-vendor-awesome-new-feature", "default")

    if flag_value == "version1":
        return do_stuff()
    elif flag_value == "version2":
        return do_other_stuff()
    else:
        return do_not_do_stuff()
