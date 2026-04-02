import os, shutil, sys
from pathlib import Path

DEVICE_ID, BASE_DIR = sys.argv[1], Path(sys.argv[2])
MASTER_DIR = BASE_DIR.parent / "Mobile_Master_View" / DEVICE_ID

def merge():
    dev_path = BASE_DIR / DEVICE_ID
    MASTER_DIR.mkdir(parents=True, exist_ok=True)
    sessions = sorted([d for d in os.listdir(dev_path) if d.startswith("Backup_")])
    
    for s in sessions:
        s_path = dev_path / s
        for root, _, files in os.walk(s_path):
            rel = os.path.relpath(root, s_path)
            (MASTER_DIR / rel).mkdir(parents=True, exist_ok=True)
            for f in files:
                if f in ["log.txt", "session_log.txt"]: continue
                src, dst = Path(root) / f, MASTER_DIR / rel / f
                if not dst.exists() or src.stat().st_size != dst.stat().st_size:
                    shutil.copy2(src, dst)
    print(f"Master View updated at: {MASTER_DIR}")

if __name__ == "__main__": merge()