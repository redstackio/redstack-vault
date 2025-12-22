---
id: 39018158-e103-41aa-a0e1-2b03fef209ee
type: command
executor: bash
data: nc -lvnp $_PORT
output: |-
  root@kali:~# nc -lvnp 4444
  Ncat: Version 7.80 ( https://nmap.org/ncat )
  Ncat: Listening on :::4444
  Ncat: Listening on 0.0.0.0:4444
created_at: '2020-03-17T00:17:21.484805+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - listener
  - reverse-shell
verified: true
validated: true
---

# Create Netcat Listener

## Command

```bash
nc -lvnp $_PORT
```

## Description

Sets up a TCP listener to catch incoming reverse shells from targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -v | Verbose output | Yes |
| -n | No DNS resolution | Yes |
| -p $_PORT | Local port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -lvnp 4444
```

### UDP Variant

```bash
nc -lvup 4444
```

## Expected Output

"Ncat: Listening on 0.0.0.0:$_PORT" until connection.

## Related

- [[procedures/upgrade-website-rce-to-netcat-reverse-shell-windows]]
- [[tools/Netcat]]
