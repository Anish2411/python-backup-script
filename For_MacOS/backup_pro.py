import os
import subprocess
import sys
from pathlib import Path

def run_backup():
    # --- DEBUG PRINT ---
    print(f"DEBUG: Script started with Args: {sys.argv}")
    
    if len(sys.argv) < 3:
        print("❌ Error: Missing arguments. Use: backup_pro.py [DeviceID] [BasePath]")
        return

    DEVICE_ID = sys.argv[1]
    BASE_DATA_DIR = Path(sys.argv[2])
    RCLONE_REMOTE = "phone:"
    
    # Common Android folders
    SOURCE_FOLDERS = ["DCIM", "Pictures", "Download"]

    dest_root = BASE_DATA_DIR / DEVICE_ID / "Master_Storage"
    dest_root.mkdir(parents=True, exist_ok=True)

    print(f"📂 Target: {dest_root}")
    
    for folder in SOURCE_FOLDERS:
        print(f"\n🔄 Syncing: {folder}...")
        
        # High-speed rclone command
        cmd = [
            "rclone", "copy", 
            f"{RCLONE_REMOTE}{folder}", 
            str(dest_root / folder),
            "--progress",
            "--transfers", "4",     # <--- Change 12 to 4
            "--checkers", "8",      # <--- Change 24 to 8
            "--multi-thread-streams", "0", # <--- Set to 0 for stability
            "--stats", "1s"
        ]
        
        try:
            subprocess.run(cmd, check=True)
        except Exception as e:
            print(f"⚠️ Could not sync {folder}: {e}")

    print("\n✅ Backup Session Finished.")

if __name__ == "__main__":
    run_backup()