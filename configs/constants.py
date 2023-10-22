import os


DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "5433")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "chat-application")
DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "postgres")

OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY", "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")
