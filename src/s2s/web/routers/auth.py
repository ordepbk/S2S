from fastapi.responses import RedirectResponse

from s2s.web.app import app
from s2s.services.auth_service import AuthService


@app.get("/login")
async def login():
    auth_handler = AuthService()
    url = auth_handler.get_login_url()
    return RedirectResponse(url)
