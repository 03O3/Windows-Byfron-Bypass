import subprocess
import os
import json
import time

print("Script by hex_array.t.me")

time.sleep(1)

cert_installed_file = "cert_installed.json"

if not os.path.exists(cert_installed_file):
    print("Installing cert...")
    subprocess.call(["python", "cert.py"])
    
    with open(cert_installed_file, 'w') as f:
        json.dump({"cert_installed": True}, f)
else:
    with open(cert_installed_file, 'r') as f:
        data = json.load(f)
        if data.get("cert_installed"):
            print("Cert already installed")
            
            
subprocess.call(["mitmproxy", "--mode", "transparent", "-s", "request.py"])