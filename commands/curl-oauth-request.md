---
id: cmd-curl-oauth-001
name: curl-oauth-request
type: command
executor: bash
data: >-
  curl -X GET
  "https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info,projects.info,siteaudit.info&client_id=seoquake&redirect_uri=https://oauth.šemrush.com/oauth2/success"
  -v -c cookies.txt
output: null
created_at: '2024-09-18T12:00:00Z'
updated_at: '2025-12-14T17:24:39.200Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - oauth
  - web-request
verified: false
validated: true
submitted: true
---

# curl-oauth-request

## Command

```bash
curl -X GET "https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info,projects.info,siteaudit.info&client_id=seoquake&redirect_uri=https://oauth.šemrush.com/oauth2/success" -v -c cookies.txt
```

## Description

Sends a GET request to the Semrush OAuth authorize endpoint with a malicious IDN homograph in the redirect_uri to test bypass. Use when simulating the initial OAuth flow for vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `URL` | Full OAuth authorize URL with parameters | Yes |
| `-v` | Verbose output for debugging | Yes |
| `-c cookies.txt` | Save session cookies | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://oauth.semrush.com/oauth2/authorize?response_type=code&client_id=seoquake&redirect_uri=https://oauth.šemrush.com" -v
```

### Advanced Usage

```bash
curl -X GET "https://oauth.semrush.com/oauth2/authorize?response_type=code&scope=user.info&client_id=seoquake&redirect_uri=https://oauth.šemrush.com/oauth2/success" -v -c cookies.txt -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Verbose HTTP response showing 200 OK with HTML approval form if redirect_uri is accepted, or error if validation fails. Look for no 'invalid redirect_uri' in response headers/body.

## Related

- [[Related Procedure: Construct-Malicious-OAuth-Authorization-URL-with-IDN-Homograph]]
