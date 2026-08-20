#!/bin/bash

# --- SETTINGS ---
TARGET="8.8.8.8"
START_HOUR=8   # Don't check before 8 AM
END_HOUR=23    # Don't check after 11 PM
# ----------------

# 1. Time Check: Get current hour (0-23)
current_hour=$(date +%H)
if [ "$current_hour" -lt "$START_HOUR" ] || [ "$current_hour" -gt "$END_HOUR" ]; then
    exit 0 # It's sleeping time! Exit quietly.
fi

# 2. The actual Health Check
if ping -c 1 -W 2 $TARGET > /dev/null 2>&1; then
    latency=$(ping -c 1 $TARGET | grep 'time=' | awk -F'time=' '{print $2}' | cut -d' ' -f1)
    if (( $(echo "$latency > 200" | bc -l) )); then
        termux-notification -c "WiFi is laggy! Latency: ${latency}ms"
    fi
else
    termux-vibrate -d 500
    termux-notification -c "INTERNET IS DOWN! Check the router!"
fi