threat_intel_db = {
    "185.234.219.45": {"reputation": "malicious", "reason": "Known command & control server"},
    "10.0.0.15": {"reputation": "suspicious", "reason": "Unusual activity flagged in honeypot"},
}

geoip_db = {
    "192.168.1.10": "Private Network (Internal)",
    "185.234.219.45": "Russia",
    "10.0.0.15": "China",
    "172.16.0.5": "Private Network (Internal)"
}

def enrich_alert(log_entry):
    ip = log_entry.get("source_ip", "")
    threat_info = threat_intel_db.get(ip, {"reputation": "clean", "reason": "No malicious activity reported"})
    log_entry["ip_reputation"] = threat_info["reputation"]
    log_entry["intel_note"] = threat_info["reason"]
    log_entry["geo_location"] = geoip_db.get(ip, "Unknown Location")
    return log_entry
