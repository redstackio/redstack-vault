---
tags:
  - xss
  - server-setup
  - payload-hosting
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.572Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 81e10b2d-17f3-47f7-9eea-87020ad85a4e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-Malicious-Server-with-XSS-Payload

## Summary

This procedure sets up a simple web server to host and serve a malicious XSS payload, which will be fetched and executed when targeted by VK.com's unsanitized callback API. It enables the delivery of arbitrary JavaScript in a DOM-based XSS attack scenario.

## Description

In the context of exploiting VK.com's community callback API, this procedure involves creating a server that responds to HTTP requests with an HTML payload containing executable JavaScript, such as a script tag for alerts or data exfiltration. The server must be publicly accessible to receive requests from VK.com. This step assumes basic web development knowledge and access to a hosting environment. Expected outcomes include the server logging incoming requests and serving the payload without modification, setting the stage for the XSS execution.

## Requirements

1. Access to a machine with Python 3 or similar for serving (or Node.js/Apache)
2. Publicly accessible URL (use ngrok for local testing or deploy to a VPS)
3. Basic HTML/JavaScript knowledge for crafting the payload

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound requests to unknown domains from web applications
- Implement Content Security Policy (CSP) to restrict script sources
- Log and alert on HTTP responses containing script tags from external sources

## Objectives

1. Host a server that delivers an XSS payload on demand
2. Ensure the payload is served as plain HTML to bypass basic filters
3. Prepare for integration with VK.com's callback mechanism

## Instructions

### Step 1: Create the Payload File

**Context**: Craft the malicious HTML response containing the XSS payload. For testing, use a simple alert; for real attacks, include code to steal cookies or session data.

Create a file named `payload.html`:

```html
<!DOCTYPE html>
<html>
<body>
<script>alert('DOM-based XSS via Callback API');</script>
</body>
</html>
```

> This file will be served as the response body. When inserted into VK.com's DOM, the script executes in the page context.

### Step 2: Start the Web Server

**Context**: Launch a server to host the payload file on a specific port, making it available for external access.

Use Python's built-in HTTP server:

```bash
cd /path/to/payload/directory
python3 -m http.server 8000
```

> The server starts on port 8000. Access it locally at http://localhost:8000/payload.html to verify it serves the file correctly. For public access, tunnel with ngrok: `ngrok http 8000` and note the public URL (e.g., https://abc123.ngrok.io).

### Step 3: Verify Server Accessibility

**Context**: Test that the server responds with the payload from an external perspective.

Open the public URL in a browser or use curl:

```bash
curl https://your-public-url.ngrok.io/payload.html
```

> Expected output: The HTML content with the script tag. Success confirms the payload is ready for callback configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload-hosting]]
