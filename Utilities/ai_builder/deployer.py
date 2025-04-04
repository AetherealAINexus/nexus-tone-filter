# nova_engine/modules/ai_builder/deployer.py

import os
import subprocess

def deploy_to_docker(path: str) -> str:
    try:
        print(f"🧠 Deploying AI from: {path}")
        os.chdir(path)

        # Build the Docker image
        subprocess.run(["docker", "build", "-t", "nova-generated-ai", "."], check=True)

        # Run the container
        subprocess.run(["docker", "run", "-d", "-p", "8081:8080", "nova-generated-ai"], check=True)

        return "🟢 Deployed and running on port 8081"
    except subprocess.CalledProcessError as e:
        return f"❌ Docker deployment failed: {str(e)}"
    except Exception as ex:
        return f"❌ Unexpected error during deployment: {str(ex)}"
