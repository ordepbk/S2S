from dataclasses import field, dataclass
from datetime import datetime


@dataclass
class UserCredentials:
    refresh_token: str
    expires_in: int
    createddate: datetime = field(default_factory=datetime.now)
