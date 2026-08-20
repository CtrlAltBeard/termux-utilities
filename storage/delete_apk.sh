#!/bin/bash
find "$HOME/storage/Download" -name "*.apk" -mtime +30 -delete
