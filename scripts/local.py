#/usr/bin/env python3
import os

LOG_DIR = '../data/logs'

paths = [LOG_DIR]

for path in paths:
    if not os.path.exists(path):
        os.makedirs(path)