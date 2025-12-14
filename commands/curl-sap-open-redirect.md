---
data: >-
  curl -s -L
  "https://██████████.jetblue.com/sap/public/bc/icf/logoff?redirecturl=https://google.com"
  -I
tags:
  - redirect
  - http
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 31fee408-1b76-482a-87cb-ec7fb47ca89e
created_at: '2025-12-14T17:25:13.433Z'
updated_at: '2025-12-14T17:25:13.433Z'
verified: false
validated: true
submitted: true
---
# curl-sap-open-redirect

## Command

```bash
curl -s -L "https://██████████.jetblue.com/sap/public/bc/icf/logoff?redirecturl=https://google.com" -I
```

## Description

Tests open redirect by following to an external site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `-L` | Follow redirects | Yes |
| `-I` | Headers only | Yes |
| URL | With redirecturl param | Yes |

## Examples

### Basic Usage

```bash
curl -s -L "https://██████████.jetblue.com/sap/public/bc/icf/logoff?redirecturl=https://google.com" -I
```

### Advanced Usage

```bash
curl -s -L "https://█████████.jetblue.com/sap/public/bc/icf/logoff?redirecturl=https://evil.com" -I
```

## Expected Output

HTTP 302 headers pointing to the external URL.

## Related

- [[Related Procedure: Exploit-Open-Redirect-in-SAP-Logoff-Endpoint]]
