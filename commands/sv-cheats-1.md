---
id: cmd-sv-cheats-1
data: sv_cheats 1
tags:
  - cheats
  - cvar-set
type: command
output: 'Cheats enabled, allowing execution of mat_crosshair_edit'
executor: source_engine_console
platforms:
  - Windows
  - Source Engine
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.065Z'
verified: false
validated: true
submitted: true
---
# sv_cheats 1

## Command

```bash
sv_cheats 1
```

## Description

Sets the server variable to enable cheat commands in the Source Engine, required for accessing developer tools like mat_crosshair_edit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 1 | Enables cheats (use 0 to disable) | Yes |

## Examples

### Basic Usage

```bash
sv_cheats 1
```

### Advanced Usage

Combined with other cvars:
```bash
sv_cheats 1; mat_crosshair_edit
```

## Expected Output

Console echoes "sv_cheats 1" with no errors; subsequent cheat commands work.

## Related

- [[Related Procedure: Enable-Cheats-in-Source-Engine]]
