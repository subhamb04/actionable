import re
import json

def clean_ai_response(text: str) -> str:
    if not text:
        return text
    text = re.sub(r"^```[a-zA-Z]*\n?", "", text.strip())
    text = re.sub(r"\n?```$", "", text.strip())
    return text.strip()

def parse_json_safe(text: str) -> dict:
    try:
        return json.loads(text)
    except Exception:
        return {"category": "Unknown", "priority": "Unknown", "action": "Parsing failed"}
