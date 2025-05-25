from sqlalchemy import text
from backend.db.session import engine
import traceback

def execute_sql(sql: str) -> tuple[list[dict], str | None, str | None]:
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = [dict(row) for row in result.mappings()]
        return rows, None, None
    except Exception as e:
        return [], str(e), traceback.format_exc()
