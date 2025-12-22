---
id: cmd-configure-burp-proxy
data: >-
  # Burp Suite UI configuration: Enable Intercept in Proxy > Options > Proxy
  Listeners
tags:
  - proxy
  - interception
type: command
output: null
executor: gui
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.595Z'
verified: false
validated: true
submitted: true
---
# Configure-Burp-Proxy

## Command

```bash
# GUI-based: Launch Burp Suite and configure proxy listener
```

## Description

Sets up Burp Suite as an HTTP proxy to intercept browser traffic, essential for capturing requests in web vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Listener Port | Port for proxy (default 8080) | Yes |
| Intercept Mode | Enable to pause requests | Yes |

## Examples

### Basic Usage

```bash
# Run Burp and set listener: 127.0.0.1:8080
```

### Advanced Usage

```bash
# Enable invisible proxying for seamless interception
```

## Expected Output

Proxy listener active, browser configurable to route through it.

## Related

- [[Related Procedure]]
