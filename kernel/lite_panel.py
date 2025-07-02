"""
Lite Monitor Panel
Reads kernel/lite_metrics.json and returns a dict
for quick display inside Streamlit dashboard.
"""
import json
from pathlib import Path

_METRICS = Path(__file__).with_name("lite_metrics.json")

def load_latest() -> dict:
    if not _METRICS.exists():
        # fallback dummy values
        return dict(aggressive=0.1, emotion=0.3, bias=8)
    return json.loads(_METRICS.read_text())
