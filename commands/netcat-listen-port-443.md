---
id: cmd-nc-listen-001
data: nc -l -n -vv -p 443
tags:
  - capture
  - network
type: command
output: Captured POST request
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.625Z'
verified: false
validated: true
submitted: true
---
---

# netcat-listen-port-443

## Command

```bash
nc -l -n -vv -p 443
```

## Description

Listens for TCP connections on port 443 to capture incoming requests, used to verify SSRF exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Listen mode | Yes |
| -n | No DNS | Yes |
| -vv | Verbose | Yes |
| -p 443 | Port 443 | Yes |

## Examples

### Basic Usage

```bash
nc -l -n -vv -p 443
```

### Advanced Usage

Adjust port if needed: nc -l -n -vv -p 80

## Expected Output

Connection details and captured HTTP POST with form data.

## Related

- [[procedures/Capture-Exfiltrated-Request-with-Netcat]]
- [[tools/netcat]]

---
