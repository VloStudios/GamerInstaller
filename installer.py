import os
import subprocess
import requests
import json


def download_and_run(url, name):
    filename = f"{name.replace(' ', '_')}.exe"
    print(f"⬇️  Downloading {name}...")
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"🚀 Running installer for {name}... wish you luck bro.")
    subprocess.run(filename, shell=True)


def main():
    print("🎮 Welcome to Gamer Setup Wizard v69.420")
    print("✨ Time to upgrade your potato PC to a gaming rig... sorta.")

    with open("apps.json", "r") as f:
        apps = json.load(f)

    for name, url in apps.items():
        print(f"\nChecking {name}...")
        # Simplu check: dacă exe-ul e deja descărcat
        if os.path.exists(f"{name.replace(' ', '_')}.exe"):
            print(f"🟢 {name} installer already exists! Skipping download...")
        else:
            download_and_run(url, name)

    print("\n✅ All done! Go play something or whatever 😎")


if __name__ == "__main__":
    main()
