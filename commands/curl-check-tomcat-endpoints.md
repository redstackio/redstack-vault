---
data: 'curl -s -I http://target-host:8080/admin'
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c5f671ad-fe57-4494-a31d-eafaa74d24a5
created_at: '2025-12-14T17:31:19.723Z'
updated_at: '2025-12-14T17:31:19.723Z'
verified: false
validated: true
submitted: true
---
# curl-check-tomcat-endpoints

## Command

```bash
curl -s -I http://target-host:8080/admin
```

## Description

This command uses curl to perform a silent HEAD request to the Tomcat /admin endpoint, checking for exposure without authentication. It's useful for initial reconnaissance of misconfigured web servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `-I` | Fetch headers only | Yes |
| `http://target-host:8080/admin` | Target URL (replace with actual host and port) | Yes |

## Examples

### Basic Usage

```bash
curl -s -I http://example.com:8080/admin
```

### Advanced Usage

```bash
curl -s -I -H "User-Agent: Mozilla/5.0" http://target:8080/manager/html
```

## Expected Output

HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Content-Type: text/html;charset=UTF-8

(No WWW-Authenticate header indicates no auth required.)

## Related

- [[Related Procedure]]
