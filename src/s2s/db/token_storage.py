from dataclasses import field, dataclass
from datetime import datetime

from s2s.clients.spotify.schemas import ExchangeCodeResponse


@dataclass
class TokenData:
    refresh_token: str
    expires_in: int
    createddate: datetime = field(default_factory=datetime.now)


def store_refresh_token(response: ExchangeCodeResponse):
    user = TokenData(
        refresh_token=response.refresh_token, expires_in=response.expires_in
    )
