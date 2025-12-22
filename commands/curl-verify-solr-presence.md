---
id: cmd-uuid-001
data: >-
  curl -i -s -k -X $'GET' -H $'Host: www.example.com' -H $'User-Agent:
  Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/35.0.3319.102 Safari/537.36' -H $'Accept-Language: en' -H $'Connection:
  close' -H $'Accept-Encoding: gzip' -H $'Content-Length: 6' --data-binary
  $'TEST\x0d\x0a' $'https://www.example.com/solr/admin/cores?wt=json'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.535Z'
verified: false
validated: true
submitted: true
---
# curl-verify-solr-presence

## Command

```bash
curl -i -s -k -X $'GET' -H $'Host: www.example.com' -H $'User-Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36' -H $'Accept-Language: en' -H $'Connection: close' -H $'Accept-Encoding: gzip' -H $'Content-Length: 6' --data-binary $'TEST\x0d\x0a' $'https://www.example.com/solr/admin/cores?wt=json'
```

## Description

This curl command verifies Apache Solr presence by sending a GET request to the admin cores endpoint with JSON output, using spoofed headers to mimic a browser and evade detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in output | Yes |
| `-s` | Silent mode, no progress meter | Yes |
| `-k` | Insecure SSL, skip certificate verification | Yes |
| `-X GET` | Specify GET method | Yes |
| `-H Host: www.example.com` | Set target host header | Yes |
| `-H User-Agent: ...` | Spoof browser user agent | Yes |
| `-H Accept-Language: en` | Set language preference | Yes |
| `-H Connection: close` | Close connection after request | Yes |
| `-H Accept-Encoding: gzip` | Accept gzip compression | Yes |
| `-H Content-Length: 6` | Set body length (despite GET) | Yes |
| `--data-binary 'TEST\x0d\x0a'` | Append test binary data | Yes |
| URL | Target Solr endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X GET -H 'Host: www.example.com' https://www.example.com/solr/admin/cores?wt=json
```

### Advanced Usage

```bash
curl -i -s -k -X $'GET' -H $'Host: www.example.com' -H $'User-Agent: Mozilla/5.0 ...' ... $'https://www.example.com/solr/admin/cores?wt=json'
```

## Expected Output

HTTP/1.1 200 OK followed by JSON like {"responseHeader":{"status":0,"QTime":1},"response":{"numFound":1,"start":0,"docs":[{"name":"core0"}]}} indicating Solr cores.

## Related

- [[Related Procedure|procedures/Confirm-Apache-Solr-Presence-via-Admin-Endpoint]]
