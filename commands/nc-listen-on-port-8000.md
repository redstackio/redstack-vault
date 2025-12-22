---
id: d64f7aaa-3c32-476c-b69e-9467eb24ebc7
name: nc-listen-on-port-8000
type: command
executor: bash
data: nc -lnvp 8000
output: null
created_at: '2023-04-06T03:56:39.728280+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - listener
  - reverse-shell
verified: true
validated: true
---

# nc-listen-on-port-8000

## Command

```bash
nc -lnvp 8000
```

## Description

This command starts a netcat listener on port 8000 to accept incoming TCP connections, commonly used to receive reverse shells from exploited targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode for incoming connections | Yes |
| -n | No DNS resolution | Yes |
| -v | Verbose output | Yes |
| -p 8000 | Local port to bind | Yes |

## Examples

### Basic Usage

```bash
nc -lnvp 8000
```

### Advanced Usage

For UDP: nc -lnvu 8000

## Expected Output

Listening on [0.0.0.0] (family 0, port 8000)
Connection from target_ip port on successful connect.

## Related

- [[procedures/Jinja2-RCE-via-Server-Side-Template-Injection]]
- [[tools/Netcat]]
