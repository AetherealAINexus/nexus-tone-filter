import yaml
from pathlib import Path

CONFIG_FILE = Path(__file__).parent.parent / "config" / "pulse_config.yaml"

def load_pulse_config():
    with open(CONFIG_FILE, 'r') as f:
        return yaml.safe_load(f)

def save_pulse_config(data):
    with open(CONFIG_FILE, 'w') as f:
        yaml.dump(data, f)

def update_colony_name(new_name):
    config = load_pulse_config()
    config['colony_name'] = new_name
    save_pulse_config(config)
