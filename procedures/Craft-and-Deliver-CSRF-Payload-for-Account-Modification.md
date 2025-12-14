---
tags:
  - csrf
  - web-exploit
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
updated_at: '2025-12-14T17:32:58.273Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c35a2b57-0676-4477-9edd-902cd1fbdb95
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-and-Deliver-CSRF-Payload-for-Account-Modification

## Summary

This procedure involves creating a malicious HTML file that exploits a CSRF vulnerability in the account details endpoint to change the victim's email and username to the attacker's values, enabling subsequent takeover steps.

## Description

In a web application lacking CSRF protections, an attacker crafts an HTML page with a hidden form that auto-submits a POST request to the vulnerable endpoint (e.g., /account/details). The form includes fields for email and username, with special characters like '@' URL-encoded as '%40' to bypass any basic filtering. The victim is tricked into opening this file while authenticated, causing the browser to send the request using the victim's session cookies. This modifies the account without the victim's knowledge, similar to previously reported issues on the same domain.

## Requirements

1. Knowledge of the target endpoint URL (e.g., https://█████████/account/details)
2. Attacker's desired email and username values
3. Method to deliver the HTML file to the victim (e.g., phishing email or shared link)
4. Victim must be authenticated in the target application

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing POST endpoints
- Use SameSite cookies to prevent cross-site requests
- Monitor for unusual account detail changes and alert users via email confirmation
- Employ CAPTCHAs or secondary authentication for sensitive updates

## Objectives

1. Modify victim's account email and username to attacker's
2. Maintain stealth by avoiding direct interaction with the application
3. Set up for password reset exploitation

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Determine the exact POST endpoint for account updates by inspecting the application's network requests during a legitimate update.

**Instructions**: Use browser developer tools to capture the form action URL and required parameters while testing a manual update.

### Step 2: Craft Malicious HTML

**Context**: Build the CSRF payload as an auto-submitting form with encoded values.

**Instructions**: Create an HTML file with hidden inputs for email and username. Ensure the form targets the correct endpoint and auto-submits via JavaScript.

Example payload:

```html
<!DOCTYPE html>
<html>
<body>
<form action="https://█████████/account/details" method="POST" id="csrf-form">
    <input type="hidden" name="email" value="attacker%40example.com">
    <input type="hidden" name="username" value="attacker_user">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

### Step 3: Deliver to Victim

**Context**: Induce the victim to load the page while their session is active.

**Instructions**: Send the HTML file via email, social engineering, or host it on a controllable server and share the link. Ensure the victim opens it in a browser logged into the target site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[account-modification]]
