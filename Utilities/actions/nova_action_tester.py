import requests
import json

url = "https://shadowgate.shadownode.io/api/toolbox/nova/say"
flux_token = "nova_shadownode_io__jit_plugin"

def talk_to_nova(text):
    headers = {"Content-Type": "application/json"}
    payload = {
        "text": text,
        "fluxToken": flux_token
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"> Nova: {response.text}")

if __name__ == "__main__":
    while True:
        msg = input("You > ")
        if msg.lower() in ['exit', 'quit']:
            break
        talk_to_nova(msg)
