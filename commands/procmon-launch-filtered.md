---
id: launch-procmon-capture
data: procmon.exe /AcceptEula /BackingFile acronis_capture.pml
tags:
  - procmon
  - monitoring
type: command
output: Procmon launched successfully.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.209Z'
verified: false
validated: true
submitted: true
---
# procmon-launch-filtered

## Command

```cmd
procmon.exe /AcceptEula /BackingFile acronis_capture.pml
```

## Description

Launches Process Monitor with EULA acceptance and saves capture to a PML file for later review, used to monitor service file operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /AcceptEula | Auto-accepts license | Yes (first run) |
| /BackingFile | PML file for capture | No |

## Examples

### Basic Usage

```cmd
procmon.exe /AcceptEula
```

### With File

```cmd
procmon.exe /AcceptEula /BackingFile capture.pml
```

## Expected Output

Procmon GUI opens; ready for filters and capture.

## Related

- [[tools/Procmon]]
- [[procedures/Monitor-File-Operations-with-Procmon]]
