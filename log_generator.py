import random
from datetime import datetime, timedelta
ips = ["192.168.1.10", "185.234.219.45", "10.0.0.15", "172.16.0.5"]
events = [
    "Multiple failed login attempts",
    "Unusual outbound traffic to known bad IP",
    "User downloaded large file from unknown domain",
    "Normal login from corporate network",
    "Suspicious admin privilege escalation",
    "Excessive DNS queries from single host"
]

def generate_random_log(base_time, i):
    return {
        "timestamp": (base_time + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": random.choice(ips),
        "event": random.choice(events)
    }
