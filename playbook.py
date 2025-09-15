def run_playbook(alert):
    action = alert.get("Action", "").lower()
    ip = alert.get("Source IP", "Unknown")

    if "block ip" in action:
        return f"🔒 Simulated: Blocking IP {ip} in firewall"
    elif "quarantine" in action:
        return f"🛡️ Simulated: Quarantining host {ip} via EDR"
    elif "escalate" in action or "alert" in action:
        return f"📢 Simulated: Escalating alert for {ip} to Tier-2 SOC"
    elif "no action" in action or "benign" in action:
        return f"✅ Simulated: No action needed for {ip}"
    else:
        return f"⚙️ Simulated: Generic action executed for {ip}"
