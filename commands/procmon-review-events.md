---
id: review-procmon-logs
data: procmon.exe /OpenLog acronis_capture.pml
tags:
  - log-review
  - procmon
type: command
output: Log opened in GUI.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.192Z'
verified: false
validated: true
submitted: true
---
# procmon-review-events

## Command

```cmd
procmon.exe /OpenLog acronis_capture.pml
```

## Description

Opens a saved Procmon log file for analysis of captured events, such as CreateFile on program.exe.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /OpenLog | Path to PML file | Yes |

## Examples

### Basic Usage

```cmd
procmon.exe /OpenLog capture.pml
```

### With Filters

Launch then apply GUI filters.

## Expected Output

GUI loads events; filter for success on Program.exe.

## Related

- [[tools/Procmon]]
- [[procedures/Observe-SYSTEM-Execution-of-Hijacked-EXE]]
