from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

app = FastAPI()
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class User(BaseModel):
    username: str
    email: str
    password: str
    full_name: str = None
    is_active: bool = True

@app.get("/")
def read_root():
    return {"message": "FastAPI with Supabase is running"}

@app.get("/users")
def get_users():
    data = supabase.table("users").select("*").execute()
    return data.data

@app.post("/users")
async def create_user(user: User):
    try:
        data = supabase.table("users").insert({
            "username": user.username,
            "email": user.email,
            "password": user.password,
            "full_name": user.full_name,
            "is_active": user.is_active
        }).execute()
        return data.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))