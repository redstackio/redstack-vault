---
id: 8e65c82e-2612-4e9b-b2bb-dbee623153ae
name: browser-enter-telnet-url
type: command
executor: browser
data: 'telnet://$_TARGET_HOST:$_PORT'
output: null
created_at: '2023-04-06T03:56:17.452387+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
  - Browser
tags:
  - protocol-handler
  - browser-escape
  - telnet
verified: true
validated: true
---

# browser-enter-telnet-url

## Command

In the browser address bar, enter:

```text
telnet://$_TARGET_HOST:$_PORT
```

## Description

This launches the Telnet client to connect to a remote host, providing interactive access for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Host IP or hostname (e.g., localhost) | Yes |
| $_PORT | Port number (default 23) | No |

## Examples

### Basic Usage

```text
telnet://localhost
```

### Advanced Usage

```text
telnet://192.168.1.100:23
```

## Expected Output

Telnet client connects, showing a login prompt or banner. Success: Interactive shell available.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
