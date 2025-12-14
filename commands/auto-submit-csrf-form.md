---
id: cmd-js-csrf-submit-001
data: document.getElementById("csrf-form").submit();
tags:
  - csrf
  - javascript
  - auto-submit
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.475Z'
verified: false
validated: true
submitted: true
---
# auto-submit-csrf-form

## Command

```javascript
document.getElementById("csrf-form").submit();
```

## Description

This JavaScript command automatically submits a hidden HTML form with ID 'csrf-form', triggering a CSRF attack by sending a POST request to the target endpoint without user interaction. Use it in malicious pages to exploit unprotected web forms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `csrf-form` | The ID of the target form element containing POST data | Yes |

## Examples

### Basic Usage

Embed in an HTML script tag after defining the form:

```javascript
document.getElementById("csrf-form").submit();
```

### Advanced Usage

Wrap in a window.onload for delayed execution:

```javascript
window.onload = function() { document.getElementById("csrf-form").submit(); };
```

## Expected Output

Silent form submission; browser sends POST request to the form's action URL. Success is indicated by no errors and server-side action completion (e.g., ban applied).

## Related

- [[Related Procedure: Craft-Malicious-CSRF-HTML-Page]]
