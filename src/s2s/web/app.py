from s2s.services.auth_service import AuthService
from fastapi import FastAPI
from s2s.web.routers import auth


app = FastAPI()
auth_service = AuthService()

# Incluir routers
app.include_router(auth.router)
# app.include_router(playlists.router)  # TODO
