import os

from dotenv import load_dotenv
from supabase import Client, create_client


load_dotenv()

SUPABASE_URL = os.getenv("VITE_SUPABASE_URL")
SUPABASE_KEY = os.getenv("VITE_SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "❌ Configure VITE_SUPABASE_URL "
        "e VITE_SUPABASE_KEY no .env"
    )

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
)


def get_supabase():
    return supabase