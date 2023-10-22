import os


DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "5433")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "chat-application")
DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "postgres")

GSPREAD_SA_FILENAME = "~/.config/gspread/service_account.json"
