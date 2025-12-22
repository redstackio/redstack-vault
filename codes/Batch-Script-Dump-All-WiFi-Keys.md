---
type: code
language: batch
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credential-access
  - wifi
  - script
validated: true
---

# Batch-Script-Dump-All-WiFi-Keys

## Code

```batch
cls & echo. & for /f "tokens=4 delims=: " %a in ('netsh wlan show profiles ^| find "Profile "') do @echo off > nul & (netsh wlan show profiles name=%a key=clear | findstr "SSID Cipher Content" | find /v "Number" & echo.) & @echo on
```

## Description

This batch script automates the extraction of all Wi-Fi profile details, including SSIDs and clear-text keys, from a Windows system. It clears the console, iterates over profiles using netsh, requests keys with elevation, and filters output to display only essential information like network name, encryption, and password. Useful for quick credential looting in privilege escalation scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | No user-defined variables; uses built-in netsh parsing | N/A |

## Usage

Run in an elevated Command Prompt (right-click cmd.exe > Run as administrator). The script executes immediately, outputting formatted details for each profile. Redirect output to a file for logging: `script.bat > wifi_creds.txt`. Integrates into procedures like [[procedures/Windows-Elevation-of-Privilege-Looting-WiFi-Passwords]] for automated post-exploitation.

## Detection

- Monitor for multiple 'netsh wlan show profiles' executions in quick succession via process auditing (Sysmon Event ID 1).
- Look for batch file runs or command-line arguments containing 'for /f' loops targeting netsh in EDR logs.
- Anomalous console clears (cls) followed by network-related outputs in session transcripts.

## Related

- [[procedures/Windows-Elevation-of-Privilege-Looting-WiFi-Passwords]]
- [[commands/netsh-wlan-show-profiles]]
