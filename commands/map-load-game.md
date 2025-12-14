---
id: cmd-map-load-001
data: map de_RCE
tags:
  - rce
  - game-exploit
  - buffer-overflow
type: command
output: 'Map loads with RCE execution (e.g., calc.exe launches)'
executor: game_console
platforms:
  - Windows
  - Game Engine (GoldSrc)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.482Z'
verified: false
validated: true
submitted: true
---
# map-load-game

## Command

```console
map de_RCE
```

## Description

This command loads a specified map file (e.g., de_RCE.bsp) into a GoldSrc-based game via the console, triggering BSP file processing. In the context of exploitation, it invokes the vulnerable TEX_InitFromWad function, leading to a buffer overflow and remote code execution if the map is malformed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| map | The name of the BSP map file to load (without .bsp extension) | Yes |
| de_RCE | Example: Name of the malformed BSP exploiting the buffer overflow | Yes |

## Examples

### Basic Usage

```console
map de_RCE
```

### Advanced Usage

In a running game console, enter directly to load and process the file.

## Expected Output

The game attempts to load the map, processes WAD textures, and if malformed, executes arbitrary code such as launching calc.exe. Normal output would show map loading progress; exploitation may cause a brief freeze or direct payload execution without full load.

## Related

- [[Related Procedure: Exploit-GoldSrc-Buffer-Overflow-with-Malformed-BSP]]
