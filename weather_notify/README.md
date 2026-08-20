# 🌤️ Weather Scripts

**Fetch and display weather data with notifications.**

Uses the **free Open-Meteo API** (no API key required).

---

## **📂 Scripts**


| Script              | Description                                         | Usage                            |
| ------------------- | --------------------------------------------------- | -------------------------------- |
| `weather.py`        | Fetch and display detailed weather data for a city. | `python3 weather.py "Your City"` |
| `weather_notify.sh` | Get weather notifications for your city.            | `bash weather_notify.sh`         |


---

## **🚀 Setup**

### **1. Make Scripts Executable**

```bash
chmod +x ~/termux-utilities/weather/*.py
chmod +x ~/termux-utilities/weather/*.sh
```

### **2. Set Your City**

Edit `weather_notify.sh` and set your city:

```bash
WEATHER_CITY="London"  # <-- Change this to your city
```

### **3. Install Dependencies**

```bash
pkg install python requests rich
```

### **4. Schedule with Cron (Optional)**

Edit your crontab:

```bash
crontab -e
```

Add this line to get weather updates **daily at 7:30 AM**:

```bash
30 7 * * * ~/termux-utilities/weather/weather_notify.sh
```

---

## **📌 Script Details**

### **`weather.py`**

- **Purpose**: Fetches **detailed weather data** from the Open-Meteo API and displays it in a **rich, formatted output**.
- **Features**:
  - Current weather conditions (temperature, humidity, wind, etc.).
  - Tomorrow’s forecast (high/low temps, precipitation, UV index).
  - Color-coded temperatures and UV index.
  - Compass direction for wind.
- **Usage**:
  ```bash
  python3 ~/termux-utilities/weather/weather.py "London"
  ```

### **`weather_notify.sh`**

- **Purpose**: Fetches weather data and sends a **Termux notification** with the current conditions.
- **Features**:
  - Uses `weather.py` to fetch data.
  - Extracts key details (condition, temperature, humidity, wind).
  - Sends a **clean, formatted notification** to your device.
- **Customization**:
  - Edit `WEATHER_CITY` to set your default city.
  - Modify the notification content in the script.

---

## **🔧 Customization**

### **Change the Weather API**

The scripts use **Open-Meteo** (free, no API key). To use a different API:

1. Edit `weather.py` to fetch data from your preferred provider.
2. Update `weather_notify.sh` to parse the new API’s response format.

### **Adjust Notification Content**

Edit `weather_notify.sh` to include/exclude specific weather details:

```bash
CLEAN_WEATHER=$(echo "$WEATHER_OUTPUT" | grep -E "Condition|Temperature|Feels Like|Humidity|Wind|Time")
```

*(Modify the `grep` pattern to include/exclude fields.)*

### **Change Update Frequency**

Adjust the cron schedule to update more/less frequently:

```bash
# Every 12 hours
0 */12 * * * ~/termux-utilities/weather/weather_notify.sh

# Twice daily (8 AM and 6 PM)
0 8,18 * * * ~/termux-utilities/weather/weather_notify.sh
```

---

## **🌍 Supported Cities**

Works with **any city worldwide** (via Open-Meteo’s geocoding API). Examples:

- `"London"`
- `"New York"`
- `"Tokyo"`
- `"Berlin"`
- `"Sydney"`

---

## **⚡ Pro Tips**

- **Test first**: Run manually to ensure the API works for your city:
  ```bash
  python3 ~/termux-utilities/weather/weather.py "Your City"
  ```
- **Offline fallback**: The script will fail gracefully if offline (no spammy errors).
- **Rich output**: Requires the `rich` Python library for pretty formatting. Install with:
  ```bash
  pip install rich
  ```

---

## **📜 License**

MIT License. See [LICENSE](../LICENSE) for details.
