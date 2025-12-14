---
id: cmd-tasklist
data: tasklist /fi "imagename eq calc.exe" /fo table
tags:
  - verification
type: command
output: |-
  Image Name                     PID Session Name        Session#    Mem Usage
  ========================= ======== ================ =========== =============
  calc.exe                     5678 Console                    1     12,456 K
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.537Z'
verified: false
validated: true
submitted: true
---
# tasklist-filter

## Command

```cmd
tasklist /fi "imagename eq calc.exe" /fo table
```

## Description

Lists processes to verify execution and privileges of spawned binary.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /fi | Filter by image name | Yes |
| imagename eq calc.exe | Target process | Yes |

## Examples

### Basic Usage

```cmd
tasklist /fi "imagename eq calc.exe" /fo table
```

## Expected Output

Table showing PID and session for calc.exe under SYSTEM.

## Related

- [[procedures/Local-Privilege-Escalation-via-LaunchProcess-Command]]
