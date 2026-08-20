#!/usr/bin/env python3
import sys
from datetime import datetime

def analyze_system(cpu, mem, disk):
    cpu = float(cpu)
    mem = float(mem)
    disk = int(disk)
    
    alerts = []
    
    if cpu > 80:
        alerts.append(f"⚠️  HIGH CPU: {cpu}%")
    if mem > 80:
        alerts.append(f"⚠️  HIGH MEMORY: {mem}%")
    if disk > 85:
        alerts.append(f"⚠️  LOW DISK SPACE: {disk}% used")
    
    if alerts:
        print("\n" + "="*40)
        print(f"🚨 SYSTEM ALERTS - {datetime.now().strftime('%H:%M:%S')}")
        print("="*40)
        for alert in alerts:
            print(alert)
        print("="*40 + "\n")
    else:
        print("✓ System healthy!")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        cpu, mem, disk = sys.argv[1], sys.argv[2], sys.argv[3]
        analyze_system(cpu, mem, disk)
