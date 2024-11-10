# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=35
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from introduction.model import Base

# 説明の便宜上、環境変数から取得するというセキュアでない実装
DATABASE_CONFIG = {
    "drivername": "mysql+pymysql",
    "username": os.environ["MYSQL_USER"],
    "password": os.environ["MYSQL_PASSWORD"],
    "host": os.environ["MYSQL_HOST"],
    "port": os.environ["MYSQL_PORT"],
    "database": os.environ["MYSQL_DATABASE"],
    "query": {"charset": "utf8"},
}

engine = create_engine(URL.create(**DATABASE_CONFIG), echo=False)
Base.metadata.create_all(engine)

Session = scoped_session(sessionmaker(engine))
