import os

from dotenv import load_dotenv

load_dotenv()

TEST = False

LINK = os.getenv("LINK")

HOST_DATABASE = os.getenv("HOST_DATABASE")
PORT_DATABASE = os.getenv("PORT_DATABASE")
NAME_DATABASE = os.getenv("NAME_DATABASE")
USER_DATABASE = os.getenv("USER_DATABASE")
PASSWORD_DATABASE = os.getenv("PASSWORD_DATABASE")

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{USER_DATABASE}:{PASSWORD_DATABASE}@{HOST_DATABASE}:{PORT_DATABASE}/{NAME_DATABASE}"

