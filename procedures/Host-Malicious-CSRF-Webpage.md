---
tags:
  - csrf
  - web-vulnerability
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
updated_at: '2025-12-14T17:27:30.052Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7694f05d-4313-46cb-b54e-aa18045cf84a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-CSRF-Webpage

## Summary

This procedure involves creating and hosting a malicious HTML webpage that uses JavaScript to automate a CSRF attack against the Starbucks card deactivation feature, tricking an authenticated user into submitting unauthorized requests.

## Description

The attack relies on the absence of CSRF protection tokens in the Starbucks endpoints for reporting a card as lost or stolen. The malicious page loads JavaScript that opens the target page and submits forms automatically. This is effective against users who are logged into Starbucks and visit the attacker's site, such as via phishing or malicious links. Expected outcome is the deactivation of the victim's digital card, leading to loss of balance access.

## Requirements

1. Web server or hosting service to serve the HTML file (e.g., local Python server or GitHub Pages)
2. Basic knowledge of HTML and JavaScript
3. Victim's browser must have an active Starbucks session cookie

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing POST endpoints
- Use Content Security Policy (CSP) to restrict frame and script execution
- Educate users on avoiding untrusted links and monitoring account activity

## Objectives

1. Deliver the malicious payload to the victim
2. Initiate automated form submissions
3. Achieve unauthorized card deactivation

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Build the base HTML structure with onload JavaScript to trigger the attack sequence.

Create a file named `csrf-poc.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body onload="abc()">
<script>
function abc() {
  // Subsequent steps will be called here
}
</script>
</body>
</html>
```

> This sets up the page to execute JavaScript immediately upon loading.

### Step 2: Host the File

**Context**: Make the page accessible via HTTP to lure the victim.

Serve the file using a simple web server, e.g., Python:

```bash
python -m http.server 8000
```

> Access at http://localhost:8000/csrf-poc.html. For remote, deploy to a public host.

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
- [[web-vulnerability]]
