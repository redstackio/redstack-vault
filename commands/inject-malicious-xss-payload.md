---
id: cmd-inject-payload-001
data: '// Enter into input field: ''<img src=x onerror=alert()>'''
tags:
  - xss
  - payload
type: command
output: Payload injected; triggers execution on render.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.619Z'
verified: false
validated: true
submitted: true
---
# inject-malicious-xss-payload

## Command

```javascript
// Enter into input field: '<img src=x onerror=alert()>'
```

## Description

Simulates user input of a malicious payload to trigger XSS via onerror attribute.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload string | Malicious HTML/JS | Yes |

## Examples

### Basic Usage

Type into input: `<img src=x onerror=alert()> `

## Expected Output

Alert dialog executes JavaScript.

## Related

- [[commands/observe-invokelink-execution]]
