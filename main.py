import os
import subprocess
import requests
import json

def is_installed(app_name):
    # Verifică dacă există un folder cu numele aplicației în locuri cunoscute
    possible_paths = [
        os.environ.get("ProgramFiles", ""),
        os.environ.get("ProgramFiles(x86)", ""),
        os.environ.get("LOCALAPPDATA")
    ]
    for base_path in possible_paths:
        if base_path and os.path.exists(base_path):
            try:
                for folder in os.listdir(base_path):
                    if app_name.lower().replace(" ", "") in folder.lower().replace(" ", ""):
                        return True
            except PermissionError:
                pass  # unele foldere refuză accesul, da' noi nu ne certăm cu ele
    return False


def download_and_run(url, name):
    filename = f"{name.replace(' ', '_')}.exe"
    print(f"⬇️  Downloading {name}...")
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"🚀 Running installer for {name}...")
    subprocess.run(filename, shell=True)

def show_menu(apps):
    print("💾 Select what you want to install (type numbers separated by comma):\n")
    for i, name in enumerate(apps.keys()):
        print(f"{i + 1}. {name}")
    choice = input("\nYour picks: ")
    selected = []
    try:
        indexes = [int(i.strip()) - 1 for i in choice.split(",")]
        for i in indexes:
            if 0 <= i < len(apps):
                selected.append(list(apps.keys())[i])
    except:
        print("❌ Bro... nah. Try again.")
        return show_menu(apps)
    return selected

def main():
    print("🎮 Welcome to Gamer Setup Wizard v1.0")
    print("⚡ Preparing your gamer destiny...")

    with open("apps.json", "r") as f:
        apps = json.load(f)

    selected_apps = show_menu(apps)

    for name in selected_apps:
        print(f"\n🔍 Checking if {name} is already installed...")
        if is_installed(name):
            print(f"✅ {name} is already installed, chill bro.")
        else:
            download_and_run(apps[name], name)

    print("\n🏁 You're done! Now go frag some noobs 💀")

if __name__ == "__main__":
    main()

