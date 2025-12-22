---
id: cmd-uuid-001
data: cmd.exe /k calc
tags:
  - rce
  - execution
type: command
output: Launches Windows Calculator and keeps console open.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:55:20.496Z'
verified: false
validated: true
submitted: true
---
# Spawn Cmd Calc

## Command

```cmd
cmd.exe /k calc
```

## Description

This Windows command spawns a new cmd.exe instance to execute 'calc', launching the Calculator app, and uses /k to keep the shell running post-execution. Used in RCE payloads to demonstrate arbitrary process spawning via Electron's process binding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /k | Carries out the command and keeps the processor running (vs /c to close) | Yes |
| calc | The executable to run (Windows Calculator) | Yes |

## Examples

### Basic Usage

```cmd
cmd.exe /k calc
```

### Advanced Usage

```cmd
cmd.exe /k whoami > output.txt
```

## Expected Output

Opens the calc.exe GUI application window; console remains open for further input.

## Related

- [[Related Procedure: Host RCE via Prototype Pollution]]
