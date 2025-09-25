from fastapi import Response
from fastapi_users.authentication import CookieTransport
from core.config import settings


class CustomCookieTransport(CookieTransport):
    """
    Кастомный транспорт для Cookie, httponly, samesite, 
    """
    async def get_login_response(self, token: str) -> Response:
        response = Response()
        response.set_cookie(
            key=self.cookie_name,
            value=token,
            max_age=self.cookie_max_age,
            path=self.cookie_path,
            domain=self.cookie_domain,
            secure=self.cookie_secure,
            httponly=True,  
            samesite="lax",
        )
        return response

# Настройка Cookie транспорта
cookie_transport = CustomCookieTransport(
    cookie_name="auth_token",
    cookie_max_age=settings.jwt_auth.LIFETIME_SECONDS,
    cookie_secure=False, 
)