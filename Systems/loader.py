# nova_enginemodulescontributorsloader.py

import os
import yaml

CONTRIBUTOR_DIR = memorystreams

def load_contributors()
    contributors = []
    if not os.path.exists(CONTRIBUTOR_DIR)
        print(🌀 No contributor streams yet.)
        return contributors

    for file in os.listdir(CONTRIBUTOR_DIR)
        if file.endswith(.yaml)
            path = os.path.join(CONTRIBUTOR_DIR, file)
            with open(path, r) as f
                try
                    data = yaml.safe_load(f)
                    contributors.append(data)
                except Exception as e
                    print(f⚠️ Failed to load contributor {file} {e})
    return contributors
