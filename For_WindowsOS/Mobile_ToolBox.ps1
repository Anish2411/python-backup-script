# Windows PowerShell Launcher for Mobile Backup
Clear-Host
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "   MOBILE BACKUP TOOL (WINDOWS)      " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

# Check if rclone is available
if (!(Get-Command rclone.exe -ErrorAction SilentlyContinue)) {
    Write-Host "Error: rclone.exe not found in Path!" -ForegroundColor Red
    Write-Host "Please install rclone and add it to your Environment Variables."
    Pause
    Exit
}

Write-Host "1) Start High-Performance Backup"
Write-Host "2) Organize/Merge Files (Master View)"
Write-Host "3) Reset Configuration"
Write-Host "4) Exit"
Write-Host ""

$choice = Read-Host "Select an option"

switch ($choice) {
    "1" { python backup_pro.py }
    "2" { python restore_master.py }
    "3" { 
        Remove-Item "backup_config.txt" -ErrorAction SilentlyContinue
        Write-Host "Config reset. Restart the tool to set new path."
    }
    "4" { Exit }
    Default { Write-Host "Invalid Selection." }
}

Write-Host "Task Complete. Press any key to close."
Pause
