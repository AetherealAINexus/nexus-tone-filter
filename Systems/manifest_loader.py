# nova_engine/manifest_loader.py

import yaml
import os

MANIFEST_PATH = os.path.join("manifest", "Nova_Manifest.yaml")

def load_directives():
    """Extract Nova's Prime Directives from the Manifest."""
    try:
        if not os.path.exists(MANIFEST_PATH):
            print(f"⚠️ Manifest file not found at {MANIFEST_PATH}")
            return []
        with open(MANIFEST_PATH, 'r') as f:
            manifest = yaml.safe_load(f)
            return manifest.get("prime_directives", [])
    except Exception as e:
        print(f"⚠️ Failed to load Nova Manifest directives: {e}")
        return []

def load_manifest_creed():
    """Load full Manifest file contents as Nova's self-identity creed."""
    try:
        if not os.path.exists(MANIFEST_PATH):
            print(f"⚠️ Manifest file not found at {MANIFEST_PATH}")
            return "⚠️ Manifest not found."

        with open(MANIFEST_PATH, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"⚠️ Failed to read Manifest creed: {e}")
        return "⚠️ Unable to retrieve Nova's creed."
