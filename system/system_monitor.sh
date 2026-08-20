#!/bin/bash
LOG_FILE="$HOME/logs/system_monitor.log"
{
  echo "=== System Monitor: $(date) ==="
  echo -e "\nCPU Usage:"
  top -n 1 | grep "%Cpu"

  echo -e "\nMemory Usage:"
  free -h | grep "Mem"

  echo -e "\nStorage:"
  df -h $HOME/storage
} >> "$LOG_FILE"
