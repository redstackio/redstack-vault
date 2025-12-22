---
tags:
  - csrf
  - web
  - logout
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
updated_at: '2025-12-14T17:27:29.500Z'
sub_techniques: []
id: 9dc73017-40ca-4ab8-9c26-fc7ef07884f1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-CSRF-Page-to-Force-Logout

## Summary

This procedure demonstrates how to exploit a CSRF vulnerability in a web application's logout endpoint by creating a malicious webpage that automatically submits a forged POST request, forcing an authenticated user to log out without their knowledge or consent. It targets applications lacking anti-CSRF tokens, such as the Legal Robot logout functionality reported in 2015.

## Description

In a CSRF attack on logout, the attacker crafts an HTML page with a hidden form that points to the target's logout URL (e.g., /logout). When the victim visits the attacker's page while authenticated to the target site, their browser automatically sends the request using the active session cookies, triggering the logout. This disrupts the user's session, potentially forcing re-authentication and interrupting workflows. The vulnerability arises from the absence of CSRF protections like synchronizer tokens or same-site cookies. Prerequisites include the victim being logged into the target site and clicking a malicious link (e.g., via email or social media). Expected outcomes include session invalidation without user interaction, verifiable via application logs or victim reports of sudden logout.

## Requirements

1. Knowledge of the target's logout endpoint URL (e.g., https://legalrobot.com/logout)
2. Ability to host or serve a malicious HTML page (e.g., on a personal server or free hosting)
3. Social engineering access to trick the victim into visiting the page while authenticated

## Defense

Defensive measures and detection strategies:

- Implement anti-CSRF tokens (e.g., unique tokens per session validated on state-changing requests)
- Use SameSite=Strict or Lax cookies to prevent cross-site requests
- Monitor for anomalous logout requests from unexpected referers
- Educate users on phishing and suspicious links

## Objectives

1. Force involuntary logout of authenticated users
2. Disrupt ongoing sessions to cause denial of service for the user
3. Highlight and exploit missing CSRF protections

## Instructions

### Step 1: Identify Logout Endpoint

**Context**: Determine the exact URL and method (typically POST) for the logout action by inspecting the target's application or reviewing source code/network traffic.

For Legal Robot, the endpoint was /logout via POST.

### Step 2: Create Malicious HTML Page

**Context**: Build an HTML form that auto-submits to the logout endpoint, embedding it in a seemingly innocuous page to lure the victim.

Save the following as index.html and host it on a server:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Click here for free content!</title>
</head>
<body>
    <h1>Welcome! Loading your content...</h1>
    <form id="csrf-form" action="https://legalrobot.com/logout" method="POST" style="display:none;">
        <!-- No additional fields needed for simple logout -->
    </form>
    <script>
        document.getElementById('csrf-form').submit();
    </script>
</body>
</html>
```

> This page loads, displays a message, and immediately submits the hidden form using the victim's cookies if they are authenticated to legalrobot.com.

### Step 3: Distribute the Malicious Link

**Context**: Send the hosted page URL to the victim via email, chat, or other means, ensuring they are logged into the target site.

Host the file (e.g., via GitHub Pages or a local server with ngrok) and share the link: https://attacker-site.com.

**Expected Output**: Upon visit, the browser sends the POST to /logout, ending the session.

### Step 4: Verify Exploitation

**Context**: Confirm the logout by checking if the victim reports being logged out or by monitoring target logs for the request.

**Success Indicators**:
- Victim's session terminates
- No CSRF token validation error in logs

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
- [[session-hijacking]]
