# Mobile Wi-Fi Backup Tool

A robust system to wirelessly back up a mobile device’s photos, videos, and documents to a computer. This tool is designed to handle large libraries exceeding 50GB that typically cause standard file transfer methods to fail.

## Prerequisites

Before running the tool for the first time, complete these four setup steps on your computer.

### 1. Install Rclone
Rclone is the engine that moves the files.
* **On macOS:** Open the Terminal app, type `brew install rclone`, and press Enter. (If you do not have Homebrew, visit [brew.sh](https://brew.sh) first).
* **On Windows:** Download the Intel/AMD 64-bit version from [rclone.org](https://rclone.org), extract the folder, and add the location to your System Path.

### 2. Install Python
Python is the controller that runs the backup logic.
* **On macOS:** Python is usually pre-installed. Verify by typing `python3 --version` in Terminal.
* **On Windows:** Download Python from [python.org](https://python.org). Ensure the box "Add Python to PATH" is checked during installation.

### 3. Configure the Phone Connection
You must create a profile named "phone" in Rclone so the computer can communicate with your device.

1. **Start the Phone App:** Open an FTP server app on your mobile device and press Start. Note the Server URL (e.g., `ftp://192.168.1.5:2221`).
2. **Open Terminal:** Type `rclone config` and press Enter.
3. **Create the Remote:**
    * Type `n` for New Remote and press Enter.
    * **Name:** Type `phone` and press Enter. (Must be lowercase).
    * **Storage Type:** Select `ftp` from the list and press Enter.
4. **Enter Connection Details:**
    * **Host:** Type the IP address shown on your phone (e.g., `192.168.1.5`) and press Enter.
    * **User:** Enter the username shown in your app, or press Enter if none is required.
    * **Port:** Type the port number shown on your phone (e.g., `2221`) and press Enter.
    * **Password:** If your app uses a password, type `y`, enter it twice, and press Enter. Otherwise, type `n`.
5. **Finish:** Type `n` for advanced config, `y` to confirm the details, and `q` to quit.

### 4. Set Backup Directories and Source Folders
You must tell the script where to save your data and which folders to copy from your phone.

1. **Set Storage Location:** When you run the tool for the first time, it will ask for a **Full Path**. Enter the folder on your computer where you want all backups to be stored (e.g., `/Users/Name/Documents/Phone_Backups`).
2. **Configure Source Folders:** Open `backup_pro.py` in a text editor. Look for the line `SOURCE_FOLDERS = [...]`.
3. **Customize Folders:** Add or remove folder names to match your phone's storage. Common examples include:
    * `DCIM` (Camera photos and videos)
    * `Pictures` (WhatsApp, Screenshots, Instagram)
    * `Download` (Received files)
    * `Documents` (Saved PDFs and logs)

---

## How to Run a Backup

1. **Start the Phone App:** Ensure the FTP server on your mobile device is active.
2. **Open the Tool:** Double-click the `Mobile_ToolBox.command` file on macOS or the launcher file on Windows.
3. **Choose Your Device:** Select your device from the numbered list and press Enter.
4. **Start Backup:** Press `1` to begin copying. A progress bar will display the current speed and estimated time remaining.

---

## File Descriptions

| File | Function |
| :--- | :--- |
| **Mobile_ToolBox.command** | The main menu used to start and manage backups. |
| **backup_pro.py** | The core script that moves files safely and manages connection limits. |
| **restore_master.py** | An optional tool to sort files into Year and Month folders. |
| **backup_config.txt** | Stores your preferred backup folder location. |

---

## Technical Performance and Safety

* **Master Storage:** Files are saved to a folder named `Master_Storage`. This acts as a 1:1 mirror of your phone.
* **Resume Capability:** If the connection is interrupted, simply run the tool again. It will skip files already on the computer and resume exactly where it stopped.
* **One-Way Copy:** This tool only copies data. It does not delete or move original files from your mobile device.
* **Privacy:** All data remains on your local Wi-Fi network. No files are uploaded to third-party cloud services.

---

## Tips for Success

* **Network Speed:** Keep the phone and computer in the same room as the Wi-Fi router for maximum speed.
* **Power Management:** Wireless transfers are battery-intensive. Connect both devices to a power source.
* **Stay Awake:** On macOS, use the `caffeinate` command in a separate Terminal window to prevent the computer from entering sleep mode during long transfers.
