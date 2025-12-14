---
data: >-
  curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent:
  Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H
  $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
  $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H
  $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1'
  $'https://target.example.com/%2bCSCOE%2b/portal_inc.lua'
tags:
  - http
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.583Z'
id: f1f464a3-1412-42d3-bcb6-f18d0971856f
verified: false
validated: true
submitted: true
---
# curl-direct-file-access

## Command

```bash
curl -i -s -k -X $'GET' -H $'Host: target.example.com' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'DNT: 1' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' $'https://target.example.com/%2bCSCOE%2b/portal_inc.lua'
```

## Description

Attempts direct HTTP access to a protected sensitive file in Cisco ASA/FTD to verify access denial, supporting CVE-2020-3452 testing by confirming traversal necessity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Show headers | Yes |
| `-s` | Silent operation | Yes |
| `-k` | Insecure SSL | Yes |
| `-H` | Custom headers | Yes |
| URL | Direct path to file | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k ... https://target.example.com/%2bCSCOE%2b/portal_inc.lua
```

### Advanced Usage

With verbose: ```bash
curl -v -i -s -k ... 
```

## Expected Output

HTTP/1.1 500 Internal Server Error\n[Body: Wrong URL or access denied message]

## Related

- [[commands/curl-translation-table-traversal]]
- [[procedures/Verify-Direct-File-Access-Protection]]
