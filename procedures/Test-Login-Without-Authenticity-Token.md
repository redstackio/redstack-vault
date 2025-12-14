---
id: proc-uuid-2
tags:
  - csrf
  - exploitation
  - web
  - authentication
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-14T17:27:22.834Z'
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
# Test-Login-Without-Authenticity-Token

## Summary

This procedure tests the Login CSRF vulnerability by submitting a modified POST request to the /login endpoint without the authenticity_token, verifying if the server accepts forged cross-site requests and allows authentication as an arbitrary account.

## Description

Login CSRF occurs when a web application fails to validate CSRF tokens on authentication endpoints, enabling attackers to create malicious webpages that submit forged login forms. In the Mavenlink case, removing the authenticity_token from the captured request still allowed successful login with provided credentials. This can force victims to log in as attacker-controlled accounts, leading to session fixation or data exposure. The target is a Rails-based web app; prerequisites include a captured request and valid credentials. Expected outcome: Confirmation of vulnerability and ability to craft exploit pages.

## Requirements

1. Captured legitimate login request details
2. Valid test credentials (e.g., email: haxthat_f@yahoo.com, password: fatalsky)
3. Browser dev tools or proxy for request modification
4. Optional: Local server to host malicious form for victim testing

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation on all POST endpoints, especially login
- Use SameSite cookies to prevent cross-site submission
- Log and alert on logins from unexpected user agents or referers
- Implement multi-factor authentication to mitigate forced logins

## Objectives

1. Confirm the endpoint accepts requests without CSRF token
2. Demonstrate successful authentication via forged request
3. Enable deployment of malicious page for victim targeting

## Instructions

### Step 1: Modify Captured Request

**Context**: Alter the request to remove the CSRF protection parameter.

In browser dev tools (Network tab) or a tool like Burp Suite, edit the captured POST /login request. Remove the line `authenticity_token=abc123...` from the body. Retain other parameters: `login[email_address]=haxthat_f@yahoo.com`, `login[password]=fatalsky`, etc. Keep headers like Content-Type: application/x-www-form-urlencoded.

### Step 2: Resubmit Modified Request

**Context**: Test if the server processes the incomplete request.

Replay the modified request. If using dev tools, right-click the original request > Edit and Resend, then remove the token and send.

**Expected Output**: Server responds with successful authentication (e.g., 302 redirect to /dashboard, Set-Cookie for session).

### Step 3: Craft and Test Malicious Form

**Context**: Simulate cross-site attack by creating an HTML page that auto-submits the forged form.

Create an HTML file: `<form action="https://target.com/login" method="post"> <input type="hidden" name="login[email_address]" value="attacker@example.com"> <input type="hidden" name="login[password]" value="attackerpass"> </form> <script>document.forms[0].submit();</script>`. Host it locally or online, then visit in a browser with an active session to the target (but different account). The form submits cross-site without token.

**Expected Output**: Victim's browser logs in as attacker account, potentially overwriting their session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csrf]]
- [[exploitation]]
- [[web]]
- [[authentication]]
