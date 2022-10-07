from fastapi import FastAPI
from dotenv import load_dotenv
from roblox import Client
import os
import uvicorn

load_dotenv()

app = FastAPI()

client = Client(os.getenv("COOKIE"))
groupid = 14235672

async def set_rank(userid: any, rank: int) -> None:
   Group = client.get_base_group(groupid)
   await Group.set_rank(userid,rank)

@app.post("/group/members/set")
async def promote(userid: int, rank: int):
    await set_rank(int(userid),int(rank))
    return "ranked"

uvicorn.run(app)
