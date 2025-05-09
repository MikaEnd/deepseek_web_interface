#!/bin/bash
# Скрипт синхронизации с GitHub

git add .
git commit -m "sync update $(date '+%Y-%m-%d %H:%M:%S')"
git push
