# 💾 Storage Scripts

**Organize, clean, and manage your Termux storage efficiently.**

---

## **📂 Scripts**


| Script                  | Description                                        | Usage                        |
| ----------------------- | -------------------------------------------------- | ---------------------------- |
| `clean_logs.sh`         | Delete logs older than a specified number of days. | `bash clean_logs.sh`         |
| `delete_apk.sh`         | Remove old APK files from your Downloads folder.   | `bash delete_apk.sh`         |
| `organize_downloads.sh` | Automatically sort files into categorized folders. | `bash organize_downloads.sh` |


---

## **🚀 Setup**

### **1. Make Scripts Executable**

```bash
chmod +x ~/termux-utilities/storage/*.sh
```

### **2. Schedule with Cron (Optional)**

Edit your crontab:

```bash
crontab -e
```

Add entries like:

```bash
# Clean logs weekly
0 3 * * 0 ~/termux-utilities/storage/clean_logs.sh

# Delete old APKs monthly
0 4 1 * * ~/termux-utilities/storage/delete_apk.sh

# Organize downloads daily
0 2 * * * ~/termux-utilities/storage/organize_downloads.sh
```

---

## **📌 Script Details**

### **`clean_logs.sh`**

- **Purpose**: Deletes log files older than a specified number of days (default: 7).
- **Customization**: Edit the `DAYS` variable:
  ```bash
  DAYS=7  # Change this to your preferred retention period
  ```
- **Supported Directories**: By default, cleans:
  - `~/.config/logs`
  - `~/logs`
  - `~/var/log`
- **Add More Directories**: Edit the `LOG_DIRS` array:
  ```bash
  LOG_DIRS=(
      "$HOME/.config/logs"
      "$HOME/logs"
      "$HOME/var/log"
      "$HOME/your/custom/path"
  )
  ```

### **`delete_apk.sh`**

- **Purpose**: Deletes APK files older than **30 days** from your Downloads folder.
- **Customization**: Edit the path or age threshold:
  ```bash
  find "$HOME/storage/Download" -name "*.apk" -mtime +30 -delete
  ```
  \*(Change \`+30\` to your preferred age in days.)\*

### **`organize_downloads.sh`**

- **Purpose**: Automatically organizes files in your Downloads folder into subfolders:
  - `Pictures/` (JPG, PNG, GIF)
  - `Videos/` (MP4, MOV, MKV)
  - `APKs/` (APK files)
  - `Docs/` (PDF, DOCX, TXT)
- **Customization**: Add more file types or folders by editing the `case` statement:
  ```bash
  case "$file" in
      *.jpg|*.jpeg|*.png|*.gif) mv "$file" "$DOWNLOADS_DIR/Pictures/" ;;
      *.mp4|*.mov|*.mkv) mv "$file" "$DOWNLOADS_DIR/Videos/" ;;
      # Add more file types here
  esac
  ```

---

## **🔧 Customization Tips**

### **Change Default Directories**

Edit the scripts to use your preferred directories. For example, in `organize_downloads.sh`:

```bash
DOWNLOADS_DIR="$HOME/storage/Download"  # Default
# Or use:
DOWNLOADS_DIR="$HOME/Downloads"
```

### **Exclude Certain Files**

Modify the `find` or `case` statements to exclude specific files or patterns.

---

## **⚡ Pro Tips**

- **Test first**: Run scripts manually before scheduling with cron.
- **Backup important files**: Ensure `clean_logs.sh` and `delete_apk.sh` won’t delete files you need.
- **Dry run**: Use `echo` instead of `mv`/`rm` to test file organization/deletion:
  ```bash
  # In organize_downloads.sh, replace:
  mv "$file" "$DOWNLOADS_DIR/Pictures/"
  # With:
  echo "Would move: $file to $DOWNLOADS_DIR/Pictures/"
  ```

---

## **📜 License**

MIT License. See [LICENSE](../LICENSE) for details.
