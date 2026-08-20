#!/bin/bash
# Startup Monitor: Run all system checks at once
# Usage: bash ~/termux-utilities/system/startup_monitor.sh [--update]

# --- Check for --update flag ---
UPDATE_PACKAGES=false
if [ "$1" = "--update" ]; then
    UPDATE_PACKAGES=true
fi

# --- Run all scripts ---
echo "🔍 Running system checks..."

# 1. System analysis (Python)
echo "📊 Analyzing system metrics..."
python3 ~/termux-utilities/system/analyze_system.py \
    $(top -n 1 | grep "%Cpu" | awk '{print $2}' | tr -d '%') \
    $(free | grep "Mem:" | awk '{print $3}') \
    $(df -h / | grep -v "Use%" | awk '{print $5}' | tr -d '%')

# 2. Boot report
echo "📋 Generating boot report..."
bash ~/termux-utilities/system/termux_boot_report.sh

# 3. WiFi health check
echo "🌐 Checking WiFi health..."
bash ~/termux-utilities/system/wifi_health.sh

# 4. System monitor
echo "🖥️ Monitoring system..."
bash ~/termux-utilities/system/system_monitor.sh

# 5. Update packages (if --update flag is set)
if [ "$UPDATE_PACKAGES" = true ]; then
    echo "📦 Updating packages..."
    pkg update -y && pkg upgrade -y
else
    echo "💡 To update packages, run: bash ~/termux-utilities/system/startup_monitor.sh --update"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ All checks complete at $(date '+%Y-%m-%d %H:%M:%S')!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"