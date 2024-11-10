# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=37
import os
from operator import itemgetter

import pytest
from pytest_mysql import factories
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import NullPool

from introduction.model import Base

host, port, user, password = itemgetter(
    "MYSQL_HOST", "MYSQL_PORT", "MYSQL_USER", "MYSQL_PASSWORD"
)(os.environ)

mysql_noproc = factories.mysql_noproc(host=host, port=port, user=user)
mysql_fixture = factories.mysql("mysql_noproc", passwd=password, dbname="test")


@pytest.fixture
def test_session(mysql_fixture):
    url = URL.create(
        drivername="mysql+pymysql",
        username=user,
        password=password,
        host=host,
        port=port,
        database="test",
        query={"charset": "utf8"},
    )
    engine = create_engine(url, echo=False, poolclass=NullPool)
    Base.metadata.create_all(engine)
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    try:
        yield session
    except Exception:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
        Base.metadata.drop_all(engine)
