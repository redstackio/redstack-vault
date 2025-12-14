---
id: uuid-placeholder
data: 'start "" "C:\\Program Files (x86)\\GlassWire\\GlassWire.exe"'
tags:
  - application-launch
  - persistence
type: command
output: Application launches without console output.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.820Z'
verified: false
validated: true
submitted: true
---
# launch-glasswire-gui

## Command

```cmd
start "" "C:\\Program Files (x86)\\GlassWire\\GlassWire.exe"
```

## Description

Launches the GlassWire GUI executable to trigger user-context DLL hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "" | Empty title for window | No |
| Path to exe | Full path to GlassWire.exe | Yes |

## Examples

### Basic Launch

```cmd
start "" "C:\\Program Files (x86)\\GlassWire\\GlassWire.exe"
```

### With Wait

```cmd
start /wait "" "C:\\Program Files (x86)\\GlassWire\\GlassWire.exe"
```

## Expected Output

GUI window opens; no direct console output.

## Related

- [[procedures/Trigger-GlassWire-GUI-for-User-Execution]]
- [[commands/start-glasswire-service]]
