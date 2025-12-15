---
id: cmd-uuid-1
data: >-
  curl -X POST
  "https://█████████/api/Account/SendTempPassword/?userName=test@example.com" -H
  "Host: ██████████" -H "Cookie: ████████" -H "Content-Length: 0" -H "Sec-Ch-Ua:
  \"\")" -H "Sec-Ch-Ua-Mobile: ?0" -H "Sec-Ch-Ua-Platform: \"Windows\"" --http2
tags:
  - web
  - api
  - auth
type: command
output: >-
  {"status":false,"errorMessage":"Username does not exist. Please enter correct
  Username."}
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.031Z'
verified: false
validated: true
submitted: true
---
# send-temp-password-request

## Command

```bash
curl -X POST "https://█████████/api/Account/SendTempPassword/?userName=test@example.com" -H "Host: ██████████" -H "Cookie: ████████" -H "Content-Length: 0" -H "Sec-Ch-Ua: \"\")" -H "Sec-Ch-Ua-Mobile: ?0" -H "Sec-Ch-Ua-Platform: \"Windows\"" --http2
```

## Description

This command simulates sending a POST request to the UPS site's temporary password endpoint using curl over HTTP/2, typically intercepted with a proxy like Burp for modification. It targets non-existent users to elicit a failing response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `userName` | Arbitrary username/email to request temp password for | Yes |
| `-H Host` | Target host header | Yes |
| `-H Cookie` | Session cookie if any | No |
| `--http2` | Use HTTP/2 protocol | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://█████████/api/Account/SendTempPassword/?userName=nonexistent@example.com" -H "Content-Length: 0" --http2
```

### Advanced Usage

```bash
curl -X POST "https://█████████/api/Account/SendTempPassword/?userName=test@example.com" -H "Host: ██████████" -H "Cookie: ████████" -H "Sec-Ch-Ua: \"Not/A)Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"" -H "Sec-Ch-Ua-Mobile: ?0" -H "Sec-Ch-Ua-Platform: \"Windows\"" --http2
```

## Expected Output

JSON response indicating failure for non-existent user: {"status":false,"errorMessage":"Username does not exist. Please enter correct Username."}. Headers include Cache-Control: no-cache, Content-Type: application/json.

## Related

- [[Related Procedure: Initiate-and-Intercept-Temp-Password-Request]]
