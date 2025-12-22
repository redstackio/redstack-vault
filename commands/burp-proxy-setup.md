---
data: '# Launch Burp Suite and configure proxy'
tags:
  - proxy
type: command
executor: bash
platforms:
  - Windows
  - Linux
id: d4d86a18-43e2-4705-9d85-c0527699a7f0
created_at: '2025-12-11T06:10:30.647Z'
updated_at: '2025-12-11T06:10:30.647Z'
verified: false
validated: true
submitted: true
---
# burp-proxy-setup

## Command

```bash
# Launch Burp Suite and configure proxy listener for localhost
```

## Description

Sets up Burp Suite to proxy traffic, including WebSocket, for inspection. This is not a direct command but refers to the GUI configuration in Burp.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | GUI-based configuration | N/A |

## Examples

### Basic Usage

Launch Burp Suite, go to Proxy > Options, add a listener on port 8080 bound to 127.0.0.1.

## Expected Output

Burp Suite proxy ready to intercept traffic on configured port.

## Related
- [[procedures/Inspect-and-Proxy-WebSocket-Traffic]]
