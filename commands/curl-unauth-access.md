---
data: 'curl -v https://ci-cd.example.com/endpoint'
tags:
  - http
  - recon
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 006f9f18-ffc3-429f-b727-4a9fb99b777d
created_at: '2025-12-14T17:29:36.275Z'
updated_at: '2025-12-14T17:29:36.275Z'
verified: false
validated: true
submitted: true
---
# curl-unauth-access

## Command

```bash
curl -v https://ci-cd.example.com/endpoint
```

## Description

This command uses curl to send a verbose HTTP GET request to a target CI/CD endpoint, testing for improper authentication by attempting access without any credentials or headers. It's useful for verifying unauthorized access vulnerabilities in web-based systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show request/response details including headers | Yes |
| `https://ci-cd.example.com/endpoint` | The target URL of the CI/CD interface or API | Yes |

## Examples

### Basic Usage

```bash
curl -v https://ci-cd.example.com/dashboard
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" https://ci-cd.example.com/api/pipelines
```

## Expected Output

Successful execution without auth shows detailed headers and a 200 OK response body with internal content, such as:

```
* Connected to ci-cd.example.com (1.2.3.4) port 443
> GET /dashboard HTTP/1.1
> Host: ci-cd.example.com
< HTTP/1.1 200 OK
< Content-Type: text/html

<html><body>CI/CD Dashboard: Welcome, pipelines active...</body></html>
```
If vulnerable, no 401/403 errors appear.

## Related

- [[Related Procedure|procedures/Exploit-Improper-Authentication-in-CI-CD-System]]
