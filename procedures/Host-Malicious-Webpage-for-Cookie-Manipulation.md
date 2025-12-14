---
tags:
  - phishing
  - malicious-page
  - https-hosting
type: procedure
tools:
  - '[[tools/jQuery-for-Cross-Domain-AJAX]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
id: e21d3958-abad-452b-92f5-980006e0e100
created_at: '2025-12-14T17:33:34.378Z'
updated_at: '2025-12-14T17:33:34.378Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-Webpage-for-Cookie-Manipulation

## Summary

This procedure involves hosting a malicious HTML webpage over HTTPS to deliver JavaScript that manipulates cookies on the target domain, circumventing mixed-content protections and enabling subsequent XSS exploitation.

## Description

In the context of the Grammarly attack, a simple HTML page is served from an attacker-controlled HTTPS domain. The page loads jQuery and executes a script to set a malicious cookie via POST to gnar.grammarly.com/cookies, then redirects the victim. This requires the victim to visit the page while logged into Grammarly, allowing cross-domain cookie setting due to the lack of referer checks.

## Requirements

1. HTTPS hosting capability (e.g., via a VPS or service like ngrok with HTTPS)
2. Basic web server setup (e.g., Apache, Nginx, or Python's http.server with SSL)
3. Attacker domain name for hosting poc.js

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block external script loads
- Monitor for anomalous cookie-setting requests from third-party domains
- Educate users on phishing links leading to Grammarly-themed pages

## Objectives

1. Deliver the initial payload without browser blocks
2. Set up for cookie injection
3. Redirect victim seamlessly to trigger exploitation

## Instructions

### Step 1: Prepare and Host the HTML Page

**Context**: Create an HTML file that loads jQuery and includes the cookie-setting script.

**Command** (No shell command; use file creation):

Create `Grammarly.html`:
```html
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
<body>
<script>
// Cookie setting script here (detailed in next procedure)
window.location.replace('https://www.grammarly.com/upgrade?...');
</script>
</body>
</html>
```

> Host this file on an HTTPS server. Access via https://yourdomain.com/Grammarly.html. Expected output: Page loads, script prepares to execute.

### Step 2: Verify Hosting

**Context**: Ensure the page is accessible and HTTPS-secured.

Use browser or curl to test:
```bash
curl -I https://yourdomain.com/Grammarly.html
```

> Expected output: HTTP 200 with content-type text/html. Success if no SSL errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/jQuery-for-Cross-Domain-AJAX]]

## Tags

- [[Phishing]]
- [[malicious-page]]
