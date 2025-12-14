---
id: proc-line-keep-upload-001
tags:
  - file-upload-bypass
  - macos
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:29.937Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-Terminal-File-to-LINE-Keep

## Summary

This procedure exploits the incomplete file extension blacklist in LINE's Keep service to upload executable .terminal files, which are not filtered despite general restrictions on executables, enabling delivery of malicious payloads.

## Description

In the LINE Mac app, the Keep service allows file storage and sharing but blocks common executable extensions. However, .terminal files (used for Terminal app configurations on macOS) are overlooked, allowing attackers to upload files containing base64-encoded commands that execute upon launch. This sets up chaining with path traversal exploits for remote execution. Prerequisites include a LINE account and macOS environment.

## Requirements

1. LINE Mac client installed and logged in
2. macOS system for creating .terminal files
3. Knowledge of base64 encoding for command payloads

## Defense

Defensive measures and detection strategies:

- Implement comprehensive file extension whitelisting in upload services, explicitly blocking .terminal and similar
- Scan uploaded files for executable content using antivirus or sandboxing
- Monitor Keep storage for anomalous file types and sharing patterns

## Objectives

1. Store malicious executable in Keep without rejection
2. Prepare for sharing to victims
3. Enable payload delivery bypassing filters

## Instructions

### Step 1: Create Malicious .terminal File

**Context**: Generate a .terminal file with embedded executable commands to run upon opening.

Use TextEdit or a script to create a file named 'malicious.terminal' with content like:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>echo 'Payload executed' &gt; /tmp/pwned.txt; open /System/Applications/Calculator.app</string>
    </array>
</dict>
</plist>
```

Save as .terminal. This will execute the bash command when launched.

### Step 2: Upload to Keep

**Context**: Use LINE's Keep feature to store the file, exploiting the filter bypass.

In the LINE app, navigate to Keep, select 'Upload File', and choose the .terminal file. Confirm upload succeeds without error.

**Expected Output**: File listed in Keep library.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload-bypass
- line-keep
