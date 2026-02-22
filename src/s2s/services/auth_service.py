from datetime import datetime, timedelta
import secrets

from s2s.clients.spotify.auth import SpotifyAuth
from s2s.db.token_storage import UserCredentials
from s2s.clients.spotify.schemas import SpotifyAuthResponse


def _generate_random_state() -> str:
    return "xyz"


def _store_refresh_token(response: SpotifyAuthResponse):
    user = UserCredentials(
        refresh_token=response.refresh_token, expires_in=response.expires_in
    )

    return user


def get_updated_token(auth_client: SpotifyAuth, user: UserCredentials):
    token_last_second = timedelta(seconds=user.expires_in, user.createddate)

    if token_last_second > 0:
        token = auth_client.update_token()

    return token_last_second


def main():
    auth_client = SpotifyAuth()

    state = _generate_random_state()
    code = auth_client._get_auth_code(state)

    response: SpotifyAuthResponse = auth_client.handle_callback(code, state, ...)

    user = _store_refresh_token(response)


class AuthService():
    def __init__(self):
        self.auth_manager = SpotifyAuth()

    def get_login_url(self) -> str:
        state = secrets.token_urlsafe(16)
        return self.auth_manager.get_auth_code(state)