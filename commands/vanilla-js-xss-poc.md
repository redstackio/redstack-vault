---
id: cmd-vanilla-poc-001
data: >-
  document.getElementsByTagName('input')[0].addEventListener('change',e=>{
  document.getElementsByTagName('div')[0].innerHTML =
  Autolinker.link(e.srcElement.value); });
tags:
  - xss
  - poc
type: command
output: Event listener attached; XSS on input change.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.615Z'
verified: false
validated: true
submitted: true
---
# vanilla-js-xss-poc

## Command

```javascript
document.getElementsByTagName('input')[0]
.addEventListener('change',e=>{
  document.getElementsByTagName('div')[0].innerHTML = Autolinker.link(e.srcElement.value);
});
```

## Description

Vanilla JS proof-of-concept attaching a change listener to demo Autolinker XSS directly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| e | Event object | Yes |

## Examples

### Basic Usage

Run in browser console with input and div present.

## Expected Output

innerHTML updates on input change, executing payloads.

## Related

- [[commands/inject-malicious-xss-payload]]
