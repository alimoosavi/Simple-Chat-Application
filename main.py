from fastapi import FastAPI
from database.db_utils import create_tables
from routes import interaction_routes, message_routes

app = FastAPI()

app.include_router(interaction_routes.router, prefix="/interaction", tags=["interaction"])
app.include_router(message_routes.router, prefix="/message", tags=["message"])


@app.on_event("startup")
async def startup_event():
    await create_tables()
