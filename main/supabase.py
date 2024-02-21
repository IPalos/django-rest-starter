from  environs import Env
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions

env = Env()
env.read_env()

url: str = env.str("SUPABASE_URL")
key: str = env.str("SUPABASE_KEY")


def get_supabase_client(schema="public"):
    options = ClientOptions().replace(schema=schema)
    return create_client(url, key, options=options)
