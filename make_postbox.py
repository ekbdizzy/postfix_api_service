import bcrypt


def encrypt_password(password: str) -> str:
    return str(bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()))