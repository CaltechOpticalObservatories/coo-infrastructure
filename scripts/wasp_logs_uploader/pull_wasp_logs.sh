#!/bin/bash

# === CONFIGURATION ===

# Remote source (log-generating) server
REMOTE_USER="developer"
REMOTE_HOST="131.215.200.52" # wasp in the lab, on the summit it is wasp.palomar.caltech.edu
REMOTE_LOG_DIR="/tmp/periodic-system-logs"
REMOTE_PATTERN="log*.csv" # log-YYYY-MM-DD.csv

# Local destination to save the logs
LOCAL_DEST_DIR="/home/langmayr/Software/wasp/logs_from_wasp"

# SSH port if not 22
SSH_PORT=22

# Logging
RSYNC_LOG="/home/langmayr/Software/wasp/log/pull_logs.log"

# === FETCH OPERATION ===
rsync -avz -e "ssh -p $SSH_PORT" \
  "$REMOTE_USER@$REMOTE_HOST:$REMOTE_LOG_DIR/$REMOTE_PATTERN" \
  "$LOCAL_DEST_DIR" \
  >> "$RSYNC_LOG" 2>&1