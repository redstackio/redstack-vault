---
id: proc-001
tags:
  - deserialization
  - payload-generation
  - file-read
type: procedure
tools:
  - '[[tools/YSoSerial.net]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ysoserial-dotnetnuke-read-file]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:49.757Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-DNN-Deserialization-Payload-for-File-Read

## Summary

This procedure uses YSoSerial.net to generate an XML deserialization payload targeting the DotNetNuke DNNPersonalization cookie, enabling remote file read via CVE-2017-9822 exploitation.

## Description

In vulnerable DNN versions (5.0.0-9.3.0), the DNNPersonalization cookie is deserialized using XmlSerializer without type validation during 404 handling. This procedure leverages the DotNetNuke plugin in YSoSerial.net to create a gadget chain invoking FileSystemUtils.WriteFile to read arbitrary files. Prerequisites include a compiled YSoSerial.net on Windows and knowledge of the target file path.

## Requirements

1. YSoSerial.net installed and compiled (Release build)
2. Target DNN version confirmed vulnerable
3. PowerShell access on attacker's machine

## Defense

Defensive measures and detection strategies:

- Disable custom 404 pages or validate cookie deserialization
- Use WAF rules to block suspicious cookie content
- Monitor for anomalous file access logs on IIS

## Objectives

1. Generate valid XML payload for cookie insertion
2. Enable file read without direct server access
3. Validate deserialization gadget chain

## Instructions

### Step 1: Check YSoSerial.net DotNetNuke Plugin Help

**Context**: Understand available modes and options for DNN payloads.

**Command** ([[commands/ysoserial-dotnetnuke-help]]):
```powershell
PS C:\ysoserial.net\ysoserial\bin\Debug> .\ysoserial.exe -p DotNetNuke --help
```

> This displays usage, including read_file mode with -f for target file.

### Step 2: Generate the File Read Payload

**Context**: Create the specific payload for reading C:\Windows\win.ini.

**Command** ([[commands/ysoserial-dotnetnuke-read-file]]):
```powershell
PS C:\>ysoserial.net\ysoserial\bin\Release\ysoserial.exe -p DotNetNuke -m read_file -f C:\Windows\win.ini
```

> Outputs XML string; copy for cookie use. Success if no errors and XML includes ObjectDataProvider.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-dotnetnuke-help]]
- [[commands/ysoserial-dotnetnuke-read-file]]

## Tools Used

- [[tools/YSoSerial.net]]

## Tags

- deserialization
- rce
- dotnetnuke
