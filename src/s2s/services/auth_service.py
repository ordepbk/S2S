import secrets

from s2s.clients.spotify.auth import SpotifyAuth
from s2s.db.token_storage import store_refresh_token
from s2s.clients.spotify.schemas import ExchangeCodeResponse


class AuthService:
    def __init__(self):
        self.auth_manager = SpotifyAuth()
        self.state = secrets.token_urlsafe(16)

    def get_login_url(self) -> str:
        return self.auth_manager.get_auth_code(self.state)

    async def callback_handler(self, code, state) -> ...:

        if not state or self.state != state:
            return None

        token_data = await self.auth_manager.exchange_code_for_token(code)

        store_refresh_token(token_data)

        return token_data.access_token
