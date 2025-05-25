# 提供上下文機制，未來可以擴充如 user_id, time_range, etc.
class QueryContext:
    def __init__(self, question: str):
        self.question = question
        self.sql = None
