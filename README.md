# 🛠️ Termux Utilities

**A collection of useful, lightweight scripts for Termux on Android.**

Automate tasks, monitor your system, and supercharge your Termux experience with these **ready-to-use scripts**!

---

![GitHub stars](https://img.shields.io/github/stars/CtrlAltBeard/termux-utilities?style=social)
![License](https://img.shields.io/badge/license-MIT-green)

## **📂 Repository Structure**

This repository is organized into **categories** for easy navigation:

```
termux-utilities/
├── system/          # System monitoring, analysis, and startup scripts
├── battery/         # Battery monitoring and alerts
├── storage/         # File organization, cleanup, and APK management
├── weather/         # Weather data and notifications
├── fun/                # Fun and whimsical scripts
├── LICENSE          # MIT License
└── README.md        # This file
```

---

## **📌 Folders Overview**


| **Folder** | **Purpose**                    | **Key Scripts**                                                                                           |
| ---------- | ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `system/`  | System monitoring and analysis | `startup_monitor.sh`, `analyze_system.py`, `system_monitor.sh`, `termux_boot_report.sh`, `wifi_health.sh` |
| `battery/` | Battery monitoring and alerts  | `battery_check.sh`                                                                                        |
| `storage/` | File organization and cleanup  | `clean_logs.sh`, `delete_apk.sh`, `organize_downloads.sh`                                                 |
| `weather/` | Weather data and notifications | `weather.py`, `weather_notify.sh`                                                                         |
  | `fun/`       | Fun and whimsical scripts             | `random_cowfortune.sh`                                                                             |

---

## **⚡ Quick Start**

### **1. Clone the Repository**

```bash
git clone https://github.com/CtrlAltBeard/termux-utilities.git
cd termux-utilities
```

### **2. Make Scripts Executable**

```bash
# Make all scripts executable
find . -type f -name "*.sh" -exec chmod +x {} \;
find . -type f -name "*.py" -exec chmod +x {} \;
```

### **3. Run a Script**

```bash
# Example: Run the system monitor
bash system/startup_monitor.sh
```

### **4. Automate with Cron**

Edit your crontab:

```bash
crontab -e
```

Add entries like:

```bash
# Run system checks hourly
0 * * * * ~/termux-utilities/system/startup_monitor.sh

# Check battery every 15 minutes
*/15 * * * * ~/termux-utilities/battery/battery_check.sh

# Check WiFi every 30 minutes
*/30 * * * * ~/termux-utilities/system/wifi_health.sh

# Get weather updates at 7:30 AM
30 7 * * * ~/termux-utilities/weather/weather_notify.sh
```

---

## **🎯 Features by Category**

### **🖥️ System Scripts**

- **`startup_monitor.sh`**: Run all system checks at once (CPU, memory, disk, WiFi, boot logs).
- **`analyze_system.py`**: Analyze CPU, memory, and disk usage with alerts for high thresholds.
- **`system_monitor.sh`**: Log system metrics (CPU, memory, storage, processes).
- **`termux_boot_report.sh`**: Generate a report of system status at boot.
- **`wifi_health.sh`**: Monitor WiFi latency and connectivity (only runs during active hours to save battery).

### **🔋 Battery Scripts**

- **`battery_check.sh`**: Get notifications at customizable battery thresholds (15%, 30%, 50%). Runs efficiently via cron.

### **💾 Storage Scripts**

- **`clean_logs.sh`**: Delete logs older than a specified number of days.
- **`delete_apk.sh`**: Remove old APK files from your Downloads folder.
- **`organize_downloads.sh`**: Automatically sort files into `Pictures/`, `Videos/`, `APKs/`, and `Docs/` folders.

### **🌤️ Weather Scripts**

- **`weather.py`**: Fetch and display detailed weather data (using Open-Meteo API).
- **`weather_notify.sh`**: Get weather notifications with customizable city settings.

### **🎪 Fun Scripts**
- **`random_cowfortune.sh`**: Random fortune quotes delivered by random cowsay animals. Perfect for startup surprises!

---

## **📜 Customization**

### **Set Your City for Weather**

Edit `weather/weather_notify.sh` and set your city:

```bash
WEATHER_CITY="London"  # Change this to your city
```

### **Adjust Battery Thresholds**

Edit `battery/battery_check.sh` to change alert thresholds:

```bash
if [ "$level" -le 15 ]; then
    termux-vibrate -d 500
    termux-notification -c "CRITICAL: Battery at $level%! Plug it in now!"
elif [ "$level" -le 30 ]; then
    termux-vibrate -d 200
    termux-notification -c "Warning: Battery is at $level%."
... 
```

### **Add Custom Scan Directories**

Edit `storage/organize_downloads.sh` to add more file types or directories.

---

## **🤝 Contributing**

- **Report bugs** or suggest features via GitHub Issues.
- **Pull requests** are welcome!
- **Star the repo** if you find it useful.

---

## **📜 License**

This project is **MIT Licensed**. See [LICENSE](LICENSE) for details.

---

**Happy automating!** 🚀
