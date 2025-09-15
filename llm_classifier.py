from config import client
from utils import clean_ai_response, parse_json_safe

def classify_alert(log_entry):
    prompt = f"""
    You are a SOC (Security Operations Center) AI assistant.
    Analyze the following security alert and classify it.

    Alert details:
    Timestamp: {log_entry.get('timestamp')}
    Source IP: {log_entry.get('source_ip')}
    Event: {log_entry.get('event')}
    Threat Intelligence: Reputation = {log_entry.get('ip_reputation')}, Note = {log_entry.get('intel_note')}
    GeoIP: {log_entry.get('geo_location')}

    Tasks:
    1. Categorize the attack type (e.g., brute force, malware, data exfiltration, benign).
    2. Assign a priority (High, Medium, Low).
    3. Suggest next action.

    Return response in JSON with keys: category, priority, action.
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role": "user", "content": prompt}],
    )

    raw_output = response.choices[0].message.content
    cleaned = clean_ai_response(raw_output)
    return parse_json_safe(cleaned)
