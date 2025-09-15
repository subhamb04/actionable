import time
import pandas as pd
import gradio as gr
from datetime import datetime

from enrichment import enrich_alert
from llm_classifier import classify_alert
from log_generator import generate_random_log
from playbook import run_playbook

stop_streaming = False
results_store = []

def stream_logs():
    global stop_streaming, results_store
    stop_streaming = False
    results_store = []

    base_time = datetime.now()

    for i in range(10):
        if stop_streaming:
            break

        log = generate_random_log(base_time, i)
        enriched = enrich_alert(log.copy())
        ai_result = classify_alert(enriched)

        row = {
            "Timestamp": enriched.get("timestamp"),
            "Event": enriched.get("event"),
            "Source IP": enriched.get("source_ip"),
            "Reputation": enriched.get("ip_reputation"),
            "Location": enriched.get("geo_location"),
            "Category": ai_result.get("category"),
            "Priority": ai_result.get("priority"),
            "Action": ai_result.get("action"),
        }
        results_store.append(row)

        yield pd.DataFrame(results_store)
        time.sleep(3)

def stop_logs():
    global stop_streaming
    stop_streaming = True
    return None

def export_alerts():
    global results_store
    if not results_store:
        return None
    df = pd.DataFrame(results_store)
    export_path = "alerts_export.csv"
    df.to_csv(export_path, index=False)
    return export_path

def execute_playbooks():
    global results_store
    if not results_store:
        return "No alerts to act on."
    actions = [run_playbook(alert) for alert in results_store]
    return "\n".join(actions)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🛡️ Actionable : SOC Dashboard – Live Alert Prioritization & Triage")

    with gr.Row():
        start_btn = gr.Button("▶ Start Streaming", variant="primary")
        stop_btn = gr.Button("⏹ Stop Streaming", variant="stop")
        export_btn = gr.Button("💾 Export Alerts", variant="huggingface")
        playbook_btn = gr.Button("⚡ Run Playbooks")

    output_table = gr.Dataframe(
        headers=["Timestamp", "Event", "Source IP", "Reputation", "Location", "Category", "Priority", "Action"],
        wrap=True
    )

    download_file = gr.File(label="Download Exported Alerts")
    playbook_output = gr.Textbox(label="Playbook Execution Log", lines=8)

    start_btn.click(fn=stream_logs, outputs=output_table)
    stop_btn.click(fn=stop_logs, outputs=None)
    export_btn.click(fn=export_alerts, outputs=download_file)
    playbook_btn.click(fn=execute_playbooks, outputs=playbook_output)

if __name__ == "__main__":
    demo.queue().launch()
