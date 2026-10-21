import os
import certifi
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# Read DATABASE_URL or construct from TIDB_* env vars, defaulting to local SQLite
database_url = os.environ.get("DATABASE_URL", "").strip()

if not database_url:
    tidb_host = os.environ.get("TIDB_HOST", "").strip()
    tidb_user = os.environ.get("TIDB_USERNAME", "").strip()
    tidb_password = os.environ.get("TIDB_PASSWORD", "").strip()
    tidb_database = os.environ.get("TIDB_DATABASE", "test").strip()
    tidb_port = os.environ.get("TIDB_PORT", "4000").strip()
    tidb_ca = os.environ.get("TIDB_CA_PATH", "").strip() or certifi.where()

    if tidb_host and tidb_user and tidb_password:
        database_url = (
            f"mysql+pymysql://{tidb_user}:{tidb_password}@{tidb_host}:{tidb_port}/{tidb_database}"
            f"?ssl_mode=VERIFY_IDENTITY&ssl_ca={tidb_ca}"
        )

# If still not set or contains unreplaced template placeholders, fall back to SQLite
if not database_url or "<PASSWORD>" in database_url or "<CA_PATH>" in database_url:
    database_url = "sqlite:///career_copilot.db"

# PyMySQL dialect is installed; ensure PyMySQL is used for MySQL URLs
if database_url.startswith("mysql+mysqldb://"):
    database_url = database_url.replace("mysql+mysqldb://", "mysql+pymysql://", 1)
elif database_url.startswith("mysql://"):
    database_url = database_url.replace("mysql://", "mysql+pymysql://", 1)

connect_args = {}
if database_url.startswith("sqlite"):
    connect_args["check_same_thread"] = False
elif "mysql" in database_url:
    ca_path = os.environ.get("TIDB_CA_PATH", "").strip() or certifi.where()
    if os.path.exists(ca_path):
        connect_args["ssl"] = {"ca": ca_path}

DATABASE_URL = database_url

engine = create_engine(DATABASE_URL, pool_pre_ping=True, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
