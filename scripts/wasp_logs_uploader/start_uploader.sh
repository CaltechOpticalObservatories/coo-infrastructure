#!/bin/bash
cd influxdb_uploader
nohup python influxdb_uploader.py > uploader.log 2>&1 &
