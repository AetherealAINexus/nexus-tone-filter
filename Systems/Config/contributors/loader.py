# nova_engine/modules/contributors/loader.py

import os
import yaml
import time

CONTRIBUTOR_DIR = "memory/streams"

def load_contributors():
    """
    Scans all contributor directories under memory/streams/
    Loads each agent's seed.yaml and includes muted status
    """
    contributors = []

    if not os.path.exists(CONTRIBUTOR_DIR):
        print("🌀 No contributors yet.")
        return contributors

    for name in os.listdir(CONTRIBUTOR_DIR):
        agent_path = os.path.join(CONTRIBUTOR_DIR, name)
        if not os.path.isdir(agent_path):
            continue

        seed_path = os.path.join(agent_path, "seed.yaml")
        muted_path = os.path.join(agent_path, "muted.lock")

        if not os.path.exists(seed_path):
            continue

        try:
            with open(seed_path, "r") as f:
                seed = yaml.safe_load(f)
                seed["id"] = name
                seed["muted"] = os.path.exists(muted_path)

                # Check TTL for muted.lock (optional)
                if seed["muted"]:
                    try:
                        with open(muted_path, "r") as lock:
                            until = float(lock.read().strip())
                            if time.time() > until:
                                os.remove(muted_path)
                                seed["muted"] = False
                    except Exception:
                        pass

                contributors.append(seed)

        except Exception as e:
            print(f"⚠️ Failed to load {name}: {e}")

    return contributors


def load_contributor(name):
    """
    Loads a single contributor by directory name (e.g., 'grimoire')
    """
    seed_path = os.path.join(CONTRIBUTOR_DIR, name, "seed.yaml")
    if not os.path.exists(seed_path):
        print(f"⚠️ Contributor '{name}' not found.")
        return None

    try:
        with open(seed_path, "r") as f:
            data = yaml.safe_load(f)
            data["id"] = name
            data["muted"] = os.path.exists(os.path.join(CONTRIBUTOR_DIR, name, "muted.lock"))
            return data
    except Exception as e:
        print(f"⚠️ Failed to load contributor '{name}': {e}")
        return None
