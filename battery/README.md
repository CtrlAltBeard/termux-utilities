# 🔋 Battery Scripts

**Monitor your device's battery and get alerts at customizable thresholds.**

---

## **📂 Scripts**


| Script             | Description                                                             | Usage                   |
| ------------------ | ----------------------------------------------------------------------- | ----------------------- |
| `battery_check.sh` | Monitor battery level and get notifications at customizable thresholds. | `bash battery_check.sh` |


---

## **🚀 Setup**

### **1. Make Script Executable**

```bash
chmod +x ~/termux-utilities/battery/battery_check.sh
```

### **2. Schedule with Cron (Recommended)**

Edit your crontab:

```bash
crontab -e
```

Add this line to check battery **every 15-20 minutes** (adjust as needed):

```bash
*/15 * * * * ~/termux-utilities/battery/battery_check.sh
```

---

## **📌 Script Details**

### **`battery_check.sh`**

- **Purpose**: Monitors battery percentage and sends **Termux notifications** when thresholds are reached.
- **Features**:
  - **Vibrates** + notification at **≤15% battery** (CRITICAL).
  - **Vibrates** + notification at **≤30% battery** (Warning).
  - **Notification only** at **≤50% battery** (Heads up).
- **Battery-efficient**: Runs **only when scheduled** (no background drain).

---

## **🔧 Customization**

### **Adjust Battery Thresholds**

Edit `battery_check.sh` to change the thresholds:

```bash
if [ "$level" -le 15 ]; then
    termux-vibrate -d 500
    termux-notification -c "CRITICAL: Battery at $level%! Plug it in now!"
elif [ "$level" -le 30 ]; then
    termux-vibrate -d 200
    termux-notification -c "Warning: Battery is at $level%."
elif [ "$level" -le 50 ]; then
    termux-notification -c "Heads up: Battery has dipped to $level%."
fi
```

### **Change Notification Messages**

Modify the `termux-notification` messages to your preference.

### **Adjust Vibration Duration**

Change the `-d` flag in `termux-vibrate` (milliseconds):

```bash
termux-vibrate -d 500  # 500ms vibration
```

---

## **⚡ Pro Tips**

- **Save battery**: Increase the cron interval (e.g., `*/20 * * * *` for every 20 minutes).
- **Disable vibrations**: Remove `termux-vibrate` lines if you prefer silent notifications.
- **Test it**: Run manually to ensure notifications work:
  ```bash
  bash ~/termux-utilities/battery/battery_check.sh
  ```

---

## **📜 License**

MIT License. See [LICENSE](../LICENSE) for details.
