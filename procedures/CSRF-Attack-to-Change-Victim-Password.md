---
id: 4f1e2c41-fcc7-4f71-954c-d6391bbfd498
name: CSRF-Attack-to-Change-Victim-Password
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T15:22:16.095479+00:00'
updated_at: '2023-05-26T01:35:18.100053+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/CSRF]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# CSRF-Attack-to-Change-Victim-Password

## Summary

This procedure demonstrates a Cross-Site Request Forgery (CSRF) attack to unauthorizedly change a victim's password in a web application by tricking the victim into loading a malicious HTML page that auto-submits a password change form using the victim's existing authenticated session.

## Description

CSRF attacks exploit the trust a web application has in a user's browser by forging requests from authenticated users. In this scenario, the attacker identifies a state-changing operation like password change, crafts an HTML page with a hidden form that mimics the legitimate request, and lures the victim to visit it while logged in. The browser automatically includes the session cookie, submitting the forged request to the application. This procedure targets web applications lacking CSRF protections like tokens, allowing account takeover via password modification. It applies to any web app with session-based authentication and mutable user data endpoints.

## Requirements

1. The victim must be authenticated in the target web application (e.g., logged in with an active session cookie).
2. Knowledge of the password change endpoint URL and required form parameters (e.g., new password fields).
3. Ability to host or deliver the malicious HTML page to the victim (e.g., via phishing link, malicious site).
4. A web browser to test the attack locally or against a vulnerable app like bWAPP.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens: Require unique, unpredictable tokens in forms and validate them server-side.
- Use SameSite cookies: Set session cookies to Strict or Lax to prevent cross-site submission.
- Enforce HTTPS and referrer checks: Validate request origins and referrers.
- Monitor for anomalous password changes: Alert on rapid or unusual updates from the same IP/session.
- User education: Warn users against clicking untrusted links while logged in.

## Objectives

1. Forge a request to change the victim's password without direct access to their credentials.
2. Demonstrate exploitation of missing CSRF protections in web applications.
3. Achieve account takeover by setting a known password for subsequent access.

## Instructions

### Step 1: Identify the Password Change Endpoint

**Context**: Analyze the target application to locate the password change functionality and capture the exact form submission details, including method (GET/POST), URL, and parameters. This ensures the forged request matches the legitimate one.

Use browser developer tools or a proxy like Burp Suite to inspect the form. Look for fields like 'password_new', 'password_conf', and 'action'.

### Step 2: Craft the Malicious HTML Page

**Context**: Create an HTML document with a hidden form that auto-submits the password change request upon page load, using JavaScript to trigger submission without user interaction.

Reference the CSRF payload: [[codes/HTML-CSRF-Form-for-Password-Change]]

Embed or save the following HTML, customizing the action URL and password values:

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

Host this file on a web server or share via a link.

### Step 3: Deliver and Execute the Attack

**Context**: Trick the victim into visiting the malicious page while they are authenticated in the target application. The browser will submit the form using the victim's session, changing their password to the attacker's chosen value.

Send the link via email, social engineering, or embed in a phishing site. When the victim loads the page, the form submits automatically.

Verify success by attempting login with the new password ('hacked' in this example).

## Expected Output

Upon successful submission, the target application processes the request as legitimate, updating the password without errors. The victim may see a success message or be logged out, and the attacker can confirm by logging in with the new credentials.
