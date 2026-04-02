import os
import subprocess
import platform
import json
from pathlib import Path

# --- CONFIGURATION ---
CONFIG_FILE = "backup_config.txt"
SOURCE_FOLDERS = ["DCIM", "Pictures", "Download"]
IS_WINDOWS = platform.system() == "Windows"
RCLONE_BIN = "rclone.exe" if IS_WINDOWS else "rclone"

def get_base_directory():
    """Reads or sets the main backup folder on the computer."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return f.read().strip()
    
    print("--- First Time Setup ---")
    path = input("Enter the FULL PATH where backups should be stored: ").strip()
    # Normalize path for the current OS
    path = str(Path(path).resolve())
    with open(CONFIG_FILE, "w") as f:
        f.write(path)
    return path

def run_sync(source, base_dir, device_name):
    """Executes the high-performance rclone command."""
    # Build path using pathlib for cross-platform slashes (\ vs /)
    target_path = Path(base_dir) / device_name / "Master_Storage" / source
    target_path.mkdir(parents=True, exist_ok=True)

    print(f"\n>>> Syncing {source} to {target_path}...")

    # High-performance flags tuned for Android FTP/SFTP limits
    cmd = [
        RCLONE_BIN, "copy",
        f"phone:{source}",
        str(target_path),
        "--progress",            # Show real-time speed/ETA
        "--transfers", "4",      # 4 files at a time (Safe for Android)
        "--checkers", "8",       # Fast indexing
        "--buffer-size", "32M",  # Better throughput
        "--stats", "5s"          # Update stats every 5 seconds
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✔ {source} Backup Complete.")
    except subprocess.CalledProcessError as e:
        print(f"✘ Error syncing {source}: {e}")
    except FileNotFoundError:
        print(f"✘ Error: {RCLONE_BIN} not found. Ensure it is installed and in your PATH.")

def main():
    base_dir = get_base_directory()
    
    # Device Identification
    device_name = input("Enter Device Name (e.g., Pixel7A): ").strip()
    if not device_name:
        device_name = "Default_Device"

    print(f"\nSystem Detected: {platform.system()}")
    print(f"Using Engine: {RCLONE_BIN}")
    print(f"Storing in: {base_dir}")
    print("---------------------------------------")

    for folder in SOURCE_FOLDERS:
        run_sync(folder, base_dir, device_name)

    print("\n=======================================")
    print("ALL BACKUPS FINISHED SUCCESSFULLY")
    print("=======================================")

if __name__ == "__main__":
    main()