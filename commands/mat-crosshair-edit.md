---
id: cmd-mat-crosshair-edit
data: mat_crosshair_edit
tags:
  - rce
  - vulnerable-command
type: command
output: calc.exe launches on victim's machine
executor: source_engine_console
platforms:
  - Windows
  - Source Engine
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.061Z'
verified: false
validated: true
submitted: true
---
# mat_crosshair_edit

## Command

```bash
mat_crosshair_edit
```

## Description

Opens the crosshair material editor in Source Engine, but exploits path truncation to execute a .js payload for RCE when cheats are enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses default or loaded materials | No |

## Examples

### Basic Usage

```bash
mat_crosshair_edit
```

### Advanced Usage

After cheats:
```bash
sv_cheats 1; mat_crosshair_edit
```

## Expected Output

Intended: Material editor opens. Exploited: calc.exe or arbitrary command runs due to truncation.

## Related

- [[Related Procedure: Trigger-Mat-Crosshair-Edit-for-RCE]]
