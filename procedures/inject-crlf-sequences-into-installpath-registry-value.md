---
tags:
  - windows
  - crlf-injection
  - registry
type: procedure
tools:
  - '[[tools/regedit]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Modify Registry]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 1d08d89a-2c66-423f-8fe2-e96fda5860d1
created_at: '2025-12-14T17:26:48.998Z'
updated_at: '2025-12-14T17:26:48.998Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Modify Registry]]'
---
# Inject CRLF Sequences into InstallPath Registry Value

## Summary

This procedure uses binary editing of the InstallPath registry value to inject CRLF (\r\n) characters, enabling control over the content appended to the service log file when an error occurs, as the unnormalized path with newlines is used in log formatting.

## Description

By editing the registry value as binary data, non-printable characters like CRLF can be inserted, which are interpreted as newlines in the log output. The service logs the path in error messages, allowing semi-controlled content (custom lines between service-generated first and last lines). This builds on traversal verification and is key for crafting payloads in redirected logs. Prerequisites: Verified traversal setup.

## Requirements

1. Access to regedit for binary modifications
2. Test environment with empty logs
3. Understanding of hex editing (CRLF as 0D 0A)

## Defense

Defensive measures and detection strategies:

- Validate registry values for control characters before use
- Log and alert on binary registry changes to application keys
- Use integrity checks on Steam configuration

## Objectives

1. Insert CRLF to split log lines
2. Append custom content to logs
3. Verify injection without service disruption

## Instructions

### Step 1: Binary Edit InstallPath

**Context**: Insert CRLF and custom text into the value.

**Command** (Using [[tools/regedit]]):
```reg
# In regedit: HKLM\Software\wow6432node\valve\steam\InstallPath > Modify Binary Data
# Append hex: 0D 0A (CRLF) followed by ASCII bytes for 'Custom line\r\n'
```

> Value now includes injection. Expected output: Binary data shows inserted bytes.

### Step 2: Start Service and Check Log

**Context**: Trigger log creation with injected content.

**Command** (PowerShell):
```powershell
Start-Service -Name "Steam Client Service"
```

> Service runs. Expected output: Log created.

### Step 3: View Injected Content

**Context**: Confirm custom lines in log.

**Command** (CMD):
```cmd
type C:\test\logs\service_log.txt
```

> Shows service error + 'Custom line'. Expected output: CRLF-separated custom text.

### Step 4: Cleanup

**Context**: Reset for next step.

**Command** (CMD):
```cmd
del C:\test\logs\service_log.txt
```

> Cleaned. Expected output: Empty directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Modify Registry]] Modify Registry

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/regedit]]

## Tags

- [[windows]]
- [[crlf-injection]]
- [[registry]]
