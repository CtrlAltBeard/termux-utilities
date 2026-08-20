#!/bin/bash
# File: ~/termux-utilities/weather/weather_notify.sh

# Set your city here (for cron automation)
WEATHER_CITY="London"  # <-- Edit this line

# Fetch weather data 
WEATHER_OUTPUT=$(python3 ~/termux-utilities/weather/weather.py "$WEATHER_CITY" 2>&1)
if [ $? -ne 0 ]; then
    termux-notification --title "Weather Error" --content "$WEATHER_OUTPUT"
    exit 1
fi

# Extract just the useful lines without box chars
CLEAN_WEATHER=$(echo "$WEATHER_OUTPUT" | grep -E "Condition|Temperature|Feels Like|Humidity|Wind|Time" | sed 's/│//g' | sed 's/^[[:space:]]*//')

termux-notification \
  --title "Weather - $WEATHER_CITY" \
  --content "$CLEAN_WEATHER" \
  --priority high
