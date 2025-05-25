# 模擬 Model Context Protocol 的語意對應 registry
MCP_REGISTRY = {
    "列出所有API呼叫量": "SELECT * FROM API_DAILY;",
    "有幾筆資料": "SELECT COUNT(*) FROM API_DAILY;",
    "查詢 clmExt-prod-MphoneToRocid 呼叫成功數": "SELECT success FROM API_DAILY WHERE API_NAME = 'clmExt-prod-MphoneToRocid';"
}

def match_query(nl_question: str) -> str | None:
    return MCP_REGISTRY.get(nl_question.strip())
