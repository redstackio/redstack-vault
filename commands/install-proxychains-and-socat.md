---
type: command
executor: bash
data: sudo apt install proxychains socat
output: null
created_at: '2023-04-06T03:56:16.220633+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - installation
  - proxy
  - networking
  - debian
verified: true
validated: true
---

# install-proxychains-and-socat

## Command

```bash
sudo apt install proxychains socat
```

## Description

Installs Proxychains for proxying TCP connections and Socat for general networking utilities on Debian-based systems, useful for C2 traffic redirection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | Installs the specified packages | Yes |
| `proxychains` | Proxy chaining tool | Yes |
| `socat` | Socket CAT for networking | Yes |

## Examples

### Basic Usage

```bash
sudo apt install proxychains socat
```

## Expected Output

Reading package lists... Done
... (installation progress)
Setting up proxychains (4.14-...) ...
Setting up socat (1.7.3.4-...) ...

## Related

- [[procedures/Cobalt-Strike-Team-Server-Installation-and-Execution]]
