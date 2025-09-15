---
title: actionable
app_file: app.py
sdk: gradio
sdk_version: 5.44.1
---
## SOC Dashboard – Live Random Alert Streaming

A lightweight SOC-style dashboard that streams synthetic security alerts, enriches them with threat intel and GeoIP, classifies them using an LLM, and surfaces recommended actions. Built with Gradio for a simple, responsive UI.

### Features
- **Live alert stream**: Generates up to 10 synthetic logs per session.
- **Enrichment**: Adds IP reputation and GeoIP context.
- **AI classification**: Uses a Gemini-compatible OpenAI client to categorize alerts, set priority, and suggest actions.
- **Export**: Saves the current session’s alerts to `alerts_export.csv`.
- **Playbooks**: Simulates actions (e.g., block IP, quarantine host) based on AI suggestions.

### Repository Structure
- `app.py`: Gradio UI and app orchestration.
- `config.py`: Environment loading and Gemini-compatible OpenAI client initialization.
- `enrichment.py`: Threat intel and GeoIP enrichment.
- `llm_classifier.py`: Prompting and parsing for LLM classification.
- `log_generator.py`: Synthetic log generation.
- `playbook.py`: Maps AI-recommended actions to simulated playbooks.
- `utils.py`: Helper utilities for cleaning/parsing model output.
- `alerts_export.csv`: Created after exporting from the UI.

### Requirements
- Python 3.9+
- Pip

Python dependencies are listed in `requirements.txt`:
- `pandas`
- `gradio`
- `python-dotenv`
- `openai`

### Environment Variables
Create a `.env` file in the project root with your Gemini API key. This project uses the OpenAI SDK pointed at Google’s Gemini-compatible endpoint.

Example `.env`:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Installation
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment (recommended).
   - Windows (PowerShell):
     ```powershell
     py -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS/Linux (bash):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create the `.env` file as shown above.

### Running Locally
Start the Gradio app:
```bash
python app.py
```
Gradio will print a local URL (e.g., `http://127.0.0.1:7860`). Open it in your browser.

### Using the App
1. Click **Start Streaming** to begin generating alerts (up to 10 per session).
2. Watch the table populate with enriched and classified alerts.
3. Click **Stop Streaming** to halt early.
4. Click **Export Alerts** to save the current table to `alerts_export.csv` in the project root, then download it from the UI.
5. Click **Run Playbooks** to simulate actions suggested by the AI; results appear in the text box.

### How It Works
- `log_generator.generate_random_log` produces timestamped events with random IPs and messages.
- `enrichment.enrich_alert` augments each log with IP reputation and GeoIP info from in-memory lookups.
- `llm_classifier.classify_alert` sends a structured prompt to the Gemini-compatible endpoint via the OpenAI SDK and returns `{ category, priority, action }`.
- `app.py` builds the session table and wires up the Gradio UI for starting/stopping, exporting, and running playbooks.

### Troubleshooting
- **No output / classification errors**: Verify `.env` contains a valid `GOOGLE_API_KEY` and you have network connectivity.
- **Package errors**: Re-create/activate the virtual environment and re-run `pip install -r requirements.txt`.
- **Port in use**: Set a different port when launching Gradio:
  ```python
  # in app.py main block
  demo.queue().launch(server_port=7861)
  ```

### Notes
- Exported CSV only includes alerts from the current session.
- The playbook executions are simulated; no real systems are modified.
- IP reputation and GeoIP data are in-memory examples for demonstration.


