from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from s2s.services.auth_service import AuthService

auth_service = AuthService()

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login():
    url = auth_service.get_login_url()
    return RedirectResponse(url)


@router.get("/callback")
async def callback(code: str, state: str):
    token = await auth_service.callback_handler(code, state)
