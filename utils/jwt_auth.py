import jwt
from core.config import settings
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt




def encode_jwt(payload: dict, private_key = settings.jwt_auth.private_key_path.read_text(), algorithm = settings.jwt_auth.algorithm):
    encoded = jwt.encode(payload, private_key, algorithm)
    return encoded


def decode_jwt(token, public_key = settings.jwt_auth.public_key_path.read_text(),  algorithm = settings.jwt_auth.algorithm):
    decoded = jwt.decode(token, public_key, algorithm)
    return decoded



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Получает хэшированный пароль и обычный, сверяет их и возвращает True/False
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Получает пароль и хэширует его.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict) -> str:
    """
    Принимает данные, добавляет время жизни токена и кодирует его.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return encode_jwt(payload=to_encode)
