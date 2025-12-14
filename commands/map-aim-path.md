---
id: cmd-map-aim-path
data: map aim_path
tags:
  - map-load
  - game-command
type: command
output: Map loads after a short wait
executor: source_engine_console
platforms:
  - Windows
  - Source Engine
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.069Z'
verified: false
validated: true
submitted: true
---
# map aim_path

## Command

```bash
map aim_path
```

## Description

Loads the specified map (aim_path) in Counter-Strike: Source via the game console, processing any associated materials and setting up the environment for further exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| aim_path | Name of the map to load (PoC map with malicious files) | Yes |

## Examples

### Basic Usage

```bash
map aim_path
```

### Advanced Usage

In scripts or with parameters (if supported):
```bash
map aim_path +sv_cheats 1
```

## Expected Output

Console shows loading progress; map spawns after 10-30 seconds with no errors.

## Related

- [[Related Procedure: Launch-Game-and-Load-Malicious-Map]]
