---
id: 0431cf5a-69ba-4b55-bc0e-82f56517f3bc
name: install-socat-on-ubuntu
type: command
executor: bash
data: sudo apt-get install socat
output: null
created_at: '2023-04-06T03:56:24.983566+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
platforms:
  - Linux
tags:
  - installation
  - socat
verified: true
validated: true
---

# install-socat-on-ubuntu

## Command

```bash
sudo apt-get install socat
```

## Description

Installs socat, a multipurpose relay tool for creating advanced TCP listeners in post-exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Elevated privileges | Yes |
| apt-get | Package manager | Built-in |
| install | Install action | Built-in |
| socat | Package name | Yes |

## Examples

### Basic Install

```bash
sudo apt-get install socat
```

### With Update

```bash
sudo apt-get update && sudo apt-get install socat
```

## Expected Output

Package installation success message, similar to rlwrap install.

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
- [[commands/socat-tcp-listener-on-port]]
