---
id: cmd-exec-cfg-001
name: exec-game-config-file
type: command
executor: game_console
data: exec rce.cfg
output: >-
  Triggers execution of cfg contents, potentially leading to buffer overflow and
  RCE (e.g., calc.exe popup)
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:37.269Z'
platforms:
  - Windows
  - Game Engine
tags:
  - rce
  - exploit
verified: false
validated: true
submitted: true
---

# exec-game-config-file

## Command

```bash
exec rce.cfg
```

## Description

Executes the contents of a specified configuration file (.cfg) in the GoldSrc game console, loading commands sequentially. Used here to run a malicious 'spk' command triggering a buffer overflow for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rce.cfg | Path to the malicious configuration file containing the overflow payload | Yes |

## Examples

### Basic Usage

```bash
exec rce.cfg
```

### Advanced Usage

```bash
exec ./valve/rce.cfg
```
(If file is in a subdirectory)

## Expected Output

The console processes the file's commands, invoking VOX_LoadSound and causing memcpy overflow in VOX_GetDirectory, resulting in stack corruption and potential RCE (e.g., calc.exe launches without explicit output).

## Related

- [[Related Procedure|procedures/Exploit-GoldSrc-spk-Buffer-Overflow]]
