---
id: c7ada726-0fc8-4ad7-848b-4caf286957b4
name: ncat-listen-on-port
type: command
executor: bash
data: ncat -lvp $_PORT
output: |-
  Ncat: Version 7.80 ( https://nmap.org/ncat )
  Ncat: Listening on :::9999
  Ncat: Listening on 0.0.0.0:9999
  Ncat: Connection from 192.168.11.7.
  Ncat: Connection from 192.168.11.7:56753.
created_at: '2020-08-01T18:06:44.460012+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - listener
  - reverse-shell
verified: true
validated: true
---

# ncat-listen-on-port

## Command

```bash
ncat -lvp $_PORT
```

## Description

This command starts ncat in listening mode on a specified port, enabling the capture of incoming TCP connections, such as those from reverse shells in exploitation scenarios like blind command injection. It provides verbose output for monitoring connections and is commonly used during post-exploitation to receive callbacks from targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (e.g., 9999 for high-numbered ports to evade basic filters) | Yes |
| -l | Listen mode for incoming connections | Built-in |
| -v | Verbose output to show connection details | Built-in |
| -p | Specify the port explicitly | Built-in |

## Examples

### Basic Usage

```bash
ncat -lvp 9999
```

### Advanced Usage

```bash
ncat -lvp 4444 -k
```
(Add -k to keep listening after first connection for multiple callbacks.)

## Expected Output

When run successfully, ncat will display version info and listening status. Upon a connection:

```
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::9999
Ncat: Listening on 0.0.0.0:9999
Ncat: Connection from 192.168.11.7.
Ncat: Connection from 192.168.11.7:56753.
```

The shell prompt appears after connection, allowing command input.

## Related

- [[procedures/Blind-OS-Command-Injection-via-Reverse-Connection]]
- [[tools/ncat]]
