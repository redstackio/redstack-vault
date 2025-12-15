---
id: p2b2c3d4-e5f6-7890-abcd-ef1234567892
name: Create-Malicious-Batch-Script-for-URL-Logging
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.884Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Windows Command Shell]]'
sub_techniques: []
tags:
  - batch-script
  - logging
  - rce
commands:
  - '[[commands/capture-url-argument]]'
  - '[[commands/log-url-to-file]]'
  - '[[commands/launch-firefox-masked]]'
platforms:
  - Windows
tools:
  - '[[tools/Malstaller-Batch-Script]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---

# Create-Malicious-Batch-Script-for-URL-Logging

## Summary

This procedure creates a batch script (malstaller.bat) that captures triggered URLs from hijacked protocol handlers, logs them to a protected admin directory, and launches the legitimate browser to avoid detection, demonstrating elevated file write capabilities.

## Description

The script is placed on the desktop and serves as the payload for the registry hijack. When invoked elevated (e.g., during installer URL clicks), it uses %1 to grab the URL, appends it with the date to C:\mal_log.txt (requiring admin rights), and then opens Firefox with the URL using a specific flag to mask the malicious action. This allows URL sniffing, system tampering, or further exploitation like AV blocking.

## Requirements

1. Write access to user desktop (low-priv sufficient)
2. Firefox installed at default path
3. Elevated trigger later for full effect

## Defense

Defensive measures and detection strategies:

- Scan for suspicious .bat files on desktop with unusual content
- Monitor file creation in C:\ root via Sysmon (Event ID 11)
- Block batch execution in elevated contexts using GPO restrictions

## Objectives

1. Capture and persist sensitive URL data elevated
2. Demonstrate admin-level file writes
3. Maintain user experience to evade suspicion

## Instructions

### Step 1: Initialize Script with Argument Capture

**Context**: Start the batch file to store the passed URL parameter.

**Command** ([[commands/capture-url-argument]]):
```cmd
set arg1=%1
```

> Sets variable for later use. Expected output: Variable assigned silently.

### Step 2: Log URL to Protected File

**Context**: Append date and URL to admin-only directory for proof of elevation.

**Command** ([[commands/log-url-to-file]]):
```cmd
echo %date% : %1 >> C:\mal_log.txt
```

> Writes to C:\ (fails without elevation). Expected output: New line in log file.

### Step 3: Launch Legitimate Browser

**Context**: Open Firefox with the URL to complete the expected action.

**Command** ([[commands/launch-firefox-masked]]):
```cmd
"C:\Program Files (x86)\Mozilla Firefox\firefox.exe" -osint -url "%1"
```

> Masks attack by navigating normally. Expected output: Browser opens to URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques

- None

## Commands Used

- [[commands/capture-url-argument]]
- [[commands/log-url-to-file]]
- [[commands/launch-firefox-masked]]

## Tools Used

- [[tools/Malstaller-Batch-Script]]

## Tags

- [[batch-script]]
- [[logging]]
- [[rce]]
