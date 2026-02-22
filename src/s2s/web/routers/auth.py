from fastapi.responses import RedirectResponse

from s2s.web.app import app, auth_service


@app.get("/login")
async def login():
    url = auth_service.get_login_url()
    return RedirectResponse(url)


@app.get("/callback")
async def callback(code: str, state: str):
    auth_service.callback_handler(code, state)
