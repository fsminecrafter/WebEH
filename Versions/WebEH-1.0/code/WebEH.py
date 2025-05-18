import os
import sys
import subprocess
from flask import Flask
from app import app
import argparse
import platform

Red = "\033[31m"
Reset = "\033[0m"

def main():
    parser = argparse.ArgumentParser(description="Host websites easily")
    parser.add_argument("port", type=int, default=500, help="Port to host on, Default 500")
    parser.add_argument("--https", action="store_true", help="Host with https")
    parser.add_argument("--debug", action="store_true", help="Run with debug enabled")
    parser.add_argument("--helpihaveaerror", action="store_true", help="Need help with errors? well i only know about the ones on about this program. (:")
    parser.add_argument("--install", action="store_true", help="Install dependencies")
    args = parser.parse_args()
    
    port = args.port
    
    if args.install:
        os = platform.system()
        if os == "Windows":
            print("[*] Running: pip install flask")
            subprocess.run(["pip", "install", "flask"], capture_output=True)
            exit(0)
        elif os == "Linux":
            print("[*] Running: sudo apt install python3-flask")
            subprocess.run(["sudo", "apt", "install", "python3-flask"], capture_output=True)
            exit(0)
        else:
            print(Red + "[~] Error system is not supported...")
            exit(0)
    
    if args.helpihaveaerror:
        print("[*] Check list:")
        print("[*] Have you enabled --https without creating the certificate files? use openssl")
        print("[-] Maybe this will help:")
        print("[-] openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes")
        print("[*] Do you have flask installed?")
        print("[-] Try running with the --install")
        print("[*] Is your issue not on this list?")
        print("[-] Please leave a issue on the WebEH github page! (:")
        exit(0)
    
    if args.debug:
        debugstate = True
    else:
        debugstate = False
    
    if args.https:
        app.run(
        host='0.0.0.0',
        port=port,
        ssl_context=('cert.pem', 'key.pem'),
        debug = debugstate
        )
    else:
        app.run(
        host='0.0.0.0',
        port=port,
        debug = debugstate
        )
        
if __name__ == "__main__":
    main()
