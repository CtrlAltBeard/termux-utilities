#!/bin/bash

# Get the battery percentage
level=$(termux-battery-status | grep percentage | awk '{print $2}' | tr -d '%,')

# Check levels and trigger alerts
if [ "$level" -le 15 ]; then
    termux-vibrate -d 500
    termux-notification -c "CRITICAL: Battery at $level%! Plug it in now!"
elif [ "$level" -le 30 ]; then
    termux-vibrate -d 200
    termux-notification -c "Warning: Battery is at $level%."
elif [ "$level" -le 50 ]; then
    termux-notification -c "Heads up: Battery has dipped to $level%."
fi
