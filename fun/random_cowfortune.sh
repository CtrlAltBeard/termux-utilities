#!/bin/bash
# Random fortune quotes with random cowsay animals
fortune | cowsay -f $(ls /data/data/com.termux/files/usr/share/cowsay/cows/ | shuf -n 1 | sed 's/\.cow$//')
EOF

