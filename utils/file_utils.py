import json
import os
import re

import requests

from utils.config import DATA_PATH, IMAGES_DIR


def save_json(core_values, filepath=DATA_PATH):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    to_save = [{"headline": v["headline"], "description": v["description"]} for v in core_values]
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(to_save, file, indent=2, ensure_ascii=False)


def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9]+", "_", name.strip().lower())
    return safe


def download_images_named_by_headline(core_values, target_dir=IMAGES_DIR):
    os.makedirs(target_dir, exist_ok=True)
    for v in core_values:
        url = v["image_url"]
        filename = sanitize_filename(v["headline"]) + ".jpg"
        path = os.path.join(target_dir, filename)
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
