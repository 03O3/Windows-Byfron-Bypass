import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

mitmproxy_cert_path = os.path.join(script_dir, "mitmproxy-ca-cert.pem")

command = f"certutil -addstore root \"{mitmproxy_cert_path}\""

print("Installing...")
try:
    subprocess.check_output(command, shell=True)
    print(f"Cert {mitmproxy_cert_path} successfully installed!")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
