from s2s.services.auth_service import AuthService
from fastapi import FastAPI


app = FastAPI()
auth_service = AuthService()
