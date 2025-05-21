#!/bin/bash
cd influxdb_uploader
nohup .venv/bin/python influxdb_uploader.py > uploader.log 2>&1 &
