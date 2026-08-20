#!/bin/bash
DOWNLOADS_DIR="$HOME/storage/Download"  # Or define in a new config
mkdir -p "$DOWNLOADS_DIR/Pictures" "$DOWNLOADS_DIR/Videos" "$DOWNLOADS_DIR/APKs" "$DOWNLOADS_DIR/Docs"

# Create target directories
mkdir -p "$DOWNLOADS_DIR/Pictures" "$DOWNLOADS_DIR/Videos" "$DOWNLOADS_DIR/APKs" "$DOWNLOADS_DIR/Docs"

# Move files to respective folders
ORGANIZED_FILES=0
find "$DOWNLOADS_DIR" -maxdepth 1 -type f | while read -r file; do
    case "$file" in
        *.jpg|*.jpeg|*.png|*.gif)
            mv "$file" "$DOWNLOADS_DIR/Pictures/" && ((ORGANIZED_FILES++))
            ;;
        *.mp4|*.mov|*.mkv)
            mv "$file" "$DOWNLOADS_DIR/Videos/" && ((ORGANIZED_FILES++))
            ;;
        *.apk)
            mv "$file" "$DOWNLOADS_DIR/APKs/" && ((ORGANIZED_FILES++))
            ;;
        *.pdf|*.docx|*.txt)
            mv "$file" "$DOWNLOADS_DIR/Docs/" && ((ORGANIZED_FILES++))
            ;;
    esac
done

echo "Files organized: $ORGANIZED_FILES"
