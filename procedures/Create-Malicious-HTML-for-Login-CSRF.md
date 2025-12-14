---
id: proc-login-csrf-html-171398
tags:
  - csrf
  - login-csrf
  - saml
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:39.394Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-HTML-for-Login-CSRF

## Summary

This procedure creates a malicious HTML page that uses an iframe to manipulate the victim's session on HackerOne and automatically initiates a SAML login flow via JavaScript redirect, exploiting the lack of CSRF protection.

## Description

In the context of HackerOne's SSO-SAML login, the attacker crafts an HTML page embedding an iframe to a logout or session manipulation endpoint (redacted URL) to clear the victim's session. After a 5-second delay, JavaScript redirects the browser to the SAML sign_in endpoint with the victim's email pre-filled, forcing an unauthenticated login attempt. This bypasses standard CSRF defenses as the action is performed via a simple GET request without tokens. Prerequisites include knowing the victim's email and hosting capabilities. Expected outcome is the victim's browser starting the login process without their direct interaction, leading to potential session compromise.

## Requirements

1. Victim's email address for the SAML sign_in parameter
2. Access to a web server to host the HTML file
3. Basic HTML and JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens for all state-changing login actions, even GET requests
- Require user confirmation for automated logins or redirects
- Monitor for unusual iframe loads or rapid redirects in login flows

## Objectives

1. Clear or manipulate the victim's existing session
2. Initiate SAML login without user consent
3. Set up for chaining with other exploits like Open Redirect

## Instructions

### Step 1: Craft the HTML Structure

**Context**: Create the base HTML with an iframe to trigger session manipulation.

Embed the iframe loading the redacted session endpoint:

```html
<iframe src="https://hackerone.com/redacted-logout-endpoint" style="display:none;"></iframe>
```

> This loads invisibly and alters the session without user notice.

### Step 2: Add JavaScript for Delayed Redirect

**Context**: Use setTimeout to wait 5 seconds, then redirect to SAML sign_in.

Add the script:

```javascript
setTimeout(function() {
  window.location.href = 'https://hackerone.com/users/saml/sign_in?email=victim@example.com&remember_me=true';
}, 5000);
```

> The delay ensures the iframe completes; replace email with victim's actual address. Host the full HTML on your server.

### Step 3: Host and Test the Page

**Context**: Serve the page and verify it triggers the login flow.

Use a simple server like Python: `python -m http.server 8000`. Visit the page in a test browser with clear cookies to confirm redirect.

> Expected: Browser navigates to SAML endpoint after delay.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[saml]]
