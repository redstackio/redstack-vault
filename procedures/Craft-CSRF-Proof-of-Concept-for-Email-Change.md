---
tags:
  - csrf
  - proof-of-concept
  - web
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
updated_at: '2025-12-14T17:32:58.133Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f8737a2e-e90b-48bf-b0ff-c2c7516ba08f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft CSRF Proof-of-Concept for Email Change

## Summary

This procedure details creating a malicious HTML page that exploits the CSRF vulnerability in IRCCloud's account settings to automatically change the victim's email address when the page is loaded in their authenticated browser session.

## Description

The CSRF POC targets the vulnerable account settings endpoint by embedding a form in an HTML page that submits a POST request with the new email parameter. When the victim visits the attacker's page (e.g., via phishing link), the form auto-submits using JavaScript, forging the request as if it originated from IRCCloud. This requires no user interaction beyond loading the page and assumes the victim is logged in. The outcome is the victim's email being redirected to the attacker's control, paving the way for takeover.

## Requirements

1. Knowledge of IRCCloud's settings endpoint URL and form parameters (e.g., from prior identification)
2. A web server or file hosting to serve the HTML POC
3. Attacker's controlled email address for the change

## Defense

Defensive measures and detection strategies:

- Require unique CSRF tokens per session and validate them server-side
- Use Content-Security-Policy (CSP) headers to restrict form submissions
- Educate users on phishing risks and verify unexpected links

## Objectives

1. Forge a request to alter the victim's email
2. Demonstrate seamless exploitation without user awareness
3. Prepare for subsequent account control steps

## Instructions

### Step 1: Build the HTML Form

**Context**: Create the core form structure targeting the vulnerable endpoint.

Use a text editor to write HTML with a form action set to IRCCloud's settings URL (e.g., https://www.irccloud.com/account/settings) and method POST. Include input fields for email (set to attacker's email) and any other required params.

```html
<form action="https://www.irccloud.com/account/settings" method="POST">
  <input type="hidden" name="email" value="attacker@evil.com">
</form>
```

> This form will submit the email change when triggered.

### Step 2: Add Auto-Submission Script

**Context**: Use JavaScript to submit the form immediately upon page load.

Embed a script in the HTML to call document.forms[0].submit() on window.onload.

```html
<script>
  window.onload = function() { document.forms[0].submit(); };
</script>
```

> Expected output: Form submits automatically, changing the email if victim is authenticated.

### Step 3: Host and Test POC

**Context**: Deploy the page and verify it works in a test scenario.

Host the HTML file on a server (e.g., GitHub Pages or local Apache). Visit it while logged into a test IRCCloud account to confirm the email change.

> Success: Email updates to the specified value without alerts or blocks.

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
- [[proof-of-concept]]
