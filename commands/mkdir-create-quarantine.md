---
data: 'mkdir "C:\Acronis Active Protection Storage\Quarantine\"'
tags:
  - setup
  - directory
type: command
output: Directory created successfully if it didn't exist.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.585Z'
id: c325e4c3-9632-45dc-8f4a-c86bf46facc7
verified: false
validated: true
submitted: true
---
# mkdir-create-quarantine

## Command

```cmd
mkdir "C:\Acronis Active Protection Storage\Quarantine\"
```

## Description

Creates the Acronis quarantine directory if it does not exist, allowing an unprivileged user to prepare for symlink placement since the path is writable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | The directory path to create | Yes |

## Examples

### Basic Usage

```cmd
mkdir "C:\Acronis Active Protection Storage\Quarantine\"
```

### Advanced Usage

Not applicable; standard mkdir.

## Expected Output

The directory is created without errors if parent exists and user has write access.

## Related

- [[procedures/Download-and-Setup-Symbolic-Link-Tools]]
