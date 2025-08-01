from fastapi import FastAPI
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print(f"Using Supabase URL: {SUPABASE_URL}")
print(f"Using Supabase Key: {SUPABASE_KEY[:5]}...")  # only print prefix

app = FastAPI()
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI with Supabase is running"}

@app.get("/users")
def get_users():
    data = supabase.table("users").select("*").execute()
    return data.data

@app.post("/users")
def create_user(user: dict):
    data = supabase.table("users").insert(user).execute()
    return data.data