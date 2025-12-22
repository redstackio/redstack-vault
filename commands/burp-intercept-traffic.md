---
data: |-
  # Burp Suite configuration for interception (GUI-based)
  Proxy > Options > Proxy Listeners > Add (127.0.0.1:8080)
  Proxy > Intercept > Turn on interception
tags:
  - recon
  - proxy
type: command
output: null
executor: gui
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.055Z'
id: 898c26d8-cd15-4be4-9422-de372001e739
verified: false
validated: true
submitted: true
---
# burp-intercept-traffic

## Command

```bash
# GUI Configuration in Burp Suite
```

## Description

Configures Burp Suite to intercept HTTP/HTTPS traffic from a browser, allowing inspection of API requests like GraphQL queries during web application testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Proxy Listener Port | Port for interception (default 8080) | Yes |
| Intercept Mode | Toggle to enable/disable request capture | Yes |

## Examples

### Basic Usage

Configure listener and enable intercept in Burp GUI, then set browser proxy.

### Advanced Usage

```bash
# Export CA cert for HTTPS: Visit http://burp/cert in proxied browser
```

## Expected Output

Intercepted requests displayed in Burp Proxy > HTTP history, with option to forward or drop.

## Related

- [[Related Procedure]]
