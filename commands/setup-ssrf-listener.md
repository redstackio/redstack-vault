---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: python3 -m http.server 8080
tags:
  - ssrf
  - listener
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.291Z'
verified: false
validated: true
submitted: true
---
# setup-ssrf-listener

## Command

```bash
python3 -m http.server 8080
```

## Description

This command starts a simple HTTP server on port 8080 to listen for incoming SSRF requests, logging details like source IP, headers, and payload for verification of exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `python3` | Python 3 interpreter | Yes |
| `-m http.server` | Module to run the built-in HTTP server | Yes |
| `8080` | Port to bind the server to | Yes (customizable) |

## Examples

### Basic Usage

```bash
python3 -m http.server 8080
```

### Advanced Usage

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

> Binds to all interfaces for external access.

## Expected Output

Server starts with output like:

Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...

When a request hits (e.g., from SSRF), logs: 192.0.2.1 - - [01/Oct/2023 12:00:00] "GET /test HTTP/1.1" 200 -

## Related

- [[Related Procedure|procedures/Trigger-SSRF-via-ActiveCampaign-Export-in-Stripo]]
