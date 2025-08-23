from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import secrets




#print (secrets.token_hex(32))

pwd_context = CryptContext (schemes=["bcrypt"], deprecated='auto')

SECRET_KEY = "c223ca6a71f386f7af5951c2dcd3861b2f69b22963a393bfde65ea7905276264"
ALGORITHM = "HS256"
ACCESS_TOKEN_eXPIRE_MINUTES = 30

def get_password_hash (password:str):
    return pwd_context.hash(password)




def verify_password (plain_password: str, hashed_password: str):
    return pwd_context.verify (plain_password, hashed_password)


def get_password_hash (password):
    return pwd_context.hash(password)


def create_access_token (data:dict, expires_delta: timedelta=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + (expires_delta if expires_delta else timedelta(minutes=15))

    
    to_encode.update ({"exp": expire})
    encoded_jwt = jwt.encode (claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt









