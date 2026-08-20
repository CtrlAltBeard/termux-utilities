#!/bin/bash

echo "=== Termux System Info ==="
echo ""
echo "Device: $(getprop ro.product.model)"
echo "Android Version: $(getprop ro.build.version.release)"
echo "CPU: $(getprop ro.hardware)"
echo ""
echo "=== Storage ==="
df -h | grep storage
echo ""
echo "=== Memory ==="
free -h
echo ""
echo "=== Running Processes ==="
ps | wc -l
