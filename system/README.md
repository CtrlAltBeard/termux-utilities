# 🖥️ System Scripts

**Monitor and analyze your Termux system.**

---

## **📂 Scripts**


| Script                  | Description                                                            | Usage                                          |
| ----------------------- | ---------------------------------------------------------------------- | ---------------------------------------------- |
| `startup_monitor.sh`    | Run all system checks at once (CPU, memory, disk, WiFi, boot logs).    | `bash startup_monitor.sh [--update]`           |
| `analyze_system.py`     | Analyze CPU, memory, and disk usage with alerts.                       | `python3 analyze_system.py <cpu> <mem> <disk>` |
| `system_monitor.sh`     | Log system metrics (CPU, memory, storage, processes).                  | `bash system_monitor.sh`                       |
| `termux_boot_report.sh` | Generate a report of system status at boot.                            | `bash termux_boot_report.sh`                   |
| `wifi_health.sh`        | Monitor WiFi latency and connectivity (runs only during active hours). | `bash wifi_health.sh`                          |


---

## **🚀 Setup**

### **1. Make Scripts Executable**

```bash
chmod +x ~/termux-utilities/system/*.sh
chmod +x ~/termux-utilities/system/analyze_system.py
```

### **2. Add to `~/.bashrc` (Optional)**

To run **automatically on Termux startup**, add this to `~/.bashrc`:

```bash
# Run system checks on Termux startup
bash ~/termux-utilities/system/startup_monitor.sh
```

Apply changes:

```bash
source ~/.bashrc
```

### **3. Schedule with Cron (Recommended)**

Edit your crontab:

```bash
crontab -e
```

Add entries like:

```bash
# Run system checks every hour
0 * * * * ~/termux-utilities/system/startup_monitor.sh

# Run with package updates daily at 3 AM
0 3 * * * ~/termux-utilities/system/startup_monitor.sh --update

# Check WiFi every 30 minutes (only runs 8 AM - 11 PM)
*/30 * * * * ~/termux-utilities/system/wifi_health.sh
```

---

## **📌 Script Details**

### **`startup_monitor.sh`**

- **Purpose**: Runs all system scripts at once for a comprehensive check.
- **Flags**:
  - `--update`: Also updates Termux packages (`pkg update && pkg upgrade`).
- **Example**:
  ```bash
  bash ~/termux-utilities/system/startup_monitor.sh
  bash ~/termux-utilities/system/startup_monitor.sh --update
  ```

### **`analyze_system.py`**

- **Purpose**: Analyzes CPU, memory, and disk usage. Alerts if thresholds are exceeded (CPU &gt; 80%, memory &gt; 80%, disk &gt; 85%).
- **Usage**:
  ```bash
  python3 ~/termux-utilities/system/analyze_system.py 20 45 60
  ```
  \*(Replace \`20 45 60\` with your current CPU%, memory%, and disk% values.)\*

### **`system_monitor.sh`**

- **Purpose**: Logs system metrics (CPU, memory, storage, processes) to `~/termux-utilities/system/system_monitor.log`.

### **`termux_boot_report.sh`**

- **Purpose**: Generates a boot-time report with disk usage, running processes, and network status. Saved to `~/termux_boot_report.log`.

### **`wifi_health.sh`**

- **Purpose**: Monitors WiFi latency and connectivity.
- **Features**:
  - Only runs between **8 AM - 11 PM** (configurable).
  - Only checks on **WiFi** (not mobile data).
  - Alerts if latency &gt; 200ms or if the internet is down.
- **Cron Example**:
  ```bash
  */30 * * * * ~/termux-utilities/system/wifi_health.sh
  ```

---

## **🔧 Customization**

### **Adjust WiFi Health Settings**

Edit `wifi_health.sh` to change:

- **Target server**: `TARGET="8.8.8.8"` (Google DNS).
- **Active hours**: `START_HOUR=8`, `END_HOUR=23`.
- **Latency threshold**: `if (( $(echo "$latency > 200" | bc -l) )); then`.

---

## **📜 License**

MIT License. See [LICENSE](../LICENSE) for details.




