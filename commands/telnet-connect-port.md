---
data: telnet ci.nextcloud.com 53
tags:
  - verification
  - connectivity
type: command
output: null
executor: bash
platforms:
  - Linux
id: a2f78552-2ef0-4ab8-9713-c4cfefe43a0d
created_at: '2025-12-14T17:26:36.882Z'
updated_at: '2025-12-14T17:26:36.882Z'
verified: false
validated: true
submitted: true
---
# telnet-connect-port

## Command

```bash
telnet ci.nextcloud.com 53
```

## Description

Establishes a TCP connection to the specified host and port to test service accessibility, commonly used to verify DNS port responsiveness before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host (positional) | Target hostname or IP | Yes |
| Port (positional) | Target port number (e.g., 53) | Yes |

## Examples

### Basic Usage

```bash
telnet ci.nextcloud.com 53
```

### Advanced Usage

```bash
telnet localhost 22
```

## Expected Output

Trying XX.XX.XX.XX...
Connected to ci.nextcloud.com.
Escape character is '^]'.

## Related

- [[Related Procedure: Verify-DNS-Service-Accessibility]]
