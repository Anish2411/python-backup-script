#!/bin/zsh

# --- CONFIG ---
SCRIPT_DIR="$(dirname "$0")"
cd "$SCRIPT_DIR"
CONFIG_FILE="backup_config.txt"

clear
echo "==========================================="
echo "      MOBILE BACKUP TOOL"
echo "==========================================="

# 1. Test Connection
echo -n "[?] Testing connection to phone... "
if rclone lsf phone: --max-depth 1 &> /dev/null; then
    echo "CONNECTED ✅"
else
    echo "FAILED ❌"
    echo "[!] Start the FTP server on your phone."
    exit 1
fi

# 2. Path Logic
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo -n "\nEnter the FULL path for Backup Storage: "
    read USER_BASE_PATH
    echo "$USER_BASE_PATH" > "$CONFIG_FILE"
fi
BASE_DATA_DIR=$(cat "$CONFIG_FILE")

# 3. Device Selection
echo "\n--- EXISTING DEVICES ---"
# Find folders inside the backup directory
devices=($BASE_DATA_DIR/*(/N))
count=0
for d in "${devices[@]}"; do
    count=$((count+1))
    echo "[$count] ${d:t}"
done

ADD_NEW=$((count + 1))
echo "[$ADD_NEW] ADD NEW DEVICE"
echo "[$((count + 2))] EXIT"

echo -n "\nSelect a number: "
read choice

if [[ "$choice" -eq "$ADD_NEW" ]]; then
    echo -n "Enter New Device ID: "
    read DEVICE_ID
    mkdir -p "$BASE_DATA_DIR/$DEVICE_ID"
elif [[ "$choice" -gt "$ADD_NEW" ]]; then
    exit
else
    # Get the folder name from the list
    SELECTED_PATH="${devices[$choice]}"
    DEVICE_ID="${SELECTED_PATH:t}"
fi

# 4. Action Menu
echo "\n--- ACTION FOR $DEVICE_ID ---"
echo "[1] Backup  [2] Merge"
echo -n "Select: "
read -k 1 act

if [[ "$act" == "1" ]]; then
    echo "\n🚀 Launching Backup Engine...\n"
    # CRITICAL: We pass exactly two arguments
    python3 "$SCRIPT_DIR/backup_pro.py" "$DEVICE_ID" "$BASE_DATA_DIR"
fi

echo "\nDone. Press any key to exit."
read -k 1