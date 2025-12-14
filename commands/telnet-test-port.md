---
data: telnet owncloud.com 53
tags:
  - verification
  - port-test
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.380Z'
id: fa8730cc-bbd3-48ab-a1bd-8317d7fc8c35
verified: false
validated: true
submitted: true
---
# telnet-test-port

## Command

```bash
telnet owncloud.com 53
```

## Description

Attempts a TCP connection to port 53 on owncloud.com to test DNS service availability, typically used post-mitigation to confirm port closure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| owncloud.com | Target hostname | Yes |
| 53 | Target port | Yes |

## Examples

### Basic Usage

```bash
telnet owncloud.com 53
```

### Advanced Usage

```bash
telnet 50.30.33.235 53
```

## Expected Output

Trying 50.30.33.235...
Connected to owncloud.com.
Escape character is '^]'.
(Pre-mitigation) or "Connection refused" (post-mitigation).

## Related

- [[Related Procedure: Verify-DNS-Service-Mitigation-with-Telnet]]
