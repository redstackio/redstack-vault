---
id: cmd-uuid-3
data: 'document.querySelector(''a[href^="javascript:"]'').click();'
tags:
  - xss
  - trigger
  - browser
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.828Z'
verified: false
validated: true
submitted: true
---
---

# observe-xss-trigger

## Command

```javascript
document.querySelector('a[href^="javascript:"]').click();
```

## Description

Triggers the XSS payload by simulating a click on the vulnerable anchor tag in the browser console.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `querySelector` | Selects anchor with javascript: href | Yes |
| `click()` | Executes the href | Yes |

## Examples

### Basic Usage

```javascript
document.querySelector('a[href^="javascript:"]').click();
```

### Advanced Usage

```javascript
const link = document.querySelector('a');
if (link.href.startsWith('javascript:')) link.click();
```

## Expected Output

Browser alert with "1"; console may log click event.

## Related

- [[Related Procedure: Verify-XSS-Execution-via-Alert]]

