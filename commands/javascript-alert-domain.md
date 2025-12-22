---
data: 'javascript:alert(document.domain)'
tags:
  - xss
  - test
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.654Z'
id: 18f3f50b-a345-42b7-84a8-3b0a32b6469e
verified: false
validated: true
submitted: true
---
# javascript-alert-domain

## Command

```javascript
javascript:alert(document.domain)
```

## Description

This JavaScript URI payload, when injected into a linkable field like a domain input, alerts the current document domain upon execution, demonstrating stored XSS by confirming the execution context (e.g., admin panel domain).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Simple alert payload; no parameters | No |

## Examples

### Basic Usage

```javascript
javascript:alert(document.domain)
```

Inject into a form field that becomes a hyperlink.

### Advanced Usage

Adapt for stealth: Combine with other JS, but this is the base test.

## Expected Output

Alert box showing the document domain, such as 'localhost' or the admin site's domain.

## Related

- [[commands/javascript-alert-domain-semicolon]]
- [[commands/javascript-eval-stealthy]]
