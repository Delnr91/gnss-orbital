# APEX-1 Start Script (FastAPI + Jupyter)
# Run this script to start the whole platform.

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ProjectRoot = Split-Path -Parent $ScriptDir

Write-Host "Navigating to $ProjectRoot..."
Set-Location -Path $ProjectRoot

# Set PYTHONPATH so absolute imports like "from src.orbital" work perfectly.
$env:PYTHONPATH = $ProjectRoot

Write-Host "Starting Jupyter Lab..."
Start-Process -NoNewWindow -FilePath "jupyter" -ArgumentList "lab --no-browser --port 8888 --ServerApp.token='' --ServerApp.password='' --ServerApp.tornado_settings=`"{'headers':{'Content-Security-Policy':`"frame-ancestors 'self' http://localhost:8000`"}}`""

Write-Host "Starting FastAPI Backend..."
# Uvicorn will automatically pick up src.backend.main:app
uvicorn src.backend.main:app --port 8000 --host 0.0.0.0

Write-Host "Servers stopped."
