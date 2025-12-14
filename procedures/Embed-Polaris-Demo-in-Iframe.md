---
tags:
  - xss
  - iframe
  - postmessage
  - shopify
type: procedure
tools:
  - '[[tools/prettier]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/add-message-event-listener]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6f20a88c-2963-4f67-b287-fd9f5ac8d50a
created_at: '2025-12-14T03:16:02.501Z'
updated_at: '2025-12-14T03:16:02.501Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Embed-Polaris-Demo-in-Iframe

## Summary

This procedure embeds the vulnerable Shopify Polaris demo page into an iframe on an attacker-controlled HTML page, setting the stage for postMessage-based XSS exploitation by allowing cross-frame communication without origin restrictions.

## Description

The Shopify Polaris demo at https://polaris.shopify.com/demo is publicly accessible and can be embedded in iframes. The demo's JavaScript adds a message event listener without origin validation, making it susceptible to payloads from any parent frame. This procedure creates the initial malicious page, loads the demo, and optionally sets up a listener for testing. It requires basic HTML and JavaScript knowledge and targets web browsers. Successful execution confirms the demo loads, enabling the next step of payload injection.

## Requirements

1. Web browser for testing (e.g., Chrome, Firefox)
2. Local web server to host the HTML file (e.g., Python's http.server)
3. Access to format JS code with [[tools/prettier]] if analyzing the demo's source

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with frame-ancestors to restrict embedding
- Validate e.origin in all message event listeners to match trusted domains
- Monitor for unexpected iframe embeds in web logs

## Objectives

1. Load the Polaris demo in a controlled iframe environment
2. Prepare for postMessage communication
3. Verify no embedding restrictions block the attack

## Instructions

### Step 1: Create Malicious HTML File

**Context**: Build the base HTML structure with an iframe to embed the demo, including dimensions for visibility.

**Command** ([[commands/add-message-event-listener]]):
```html
<!DOCTYPE html>
<html>
<head><title>Exploit Page</title></head>
<body>
  <iframe id="ifrm" src="https://polaris.shopify.com/demo" width="800" height="600" frameborder="0"></iframe>
  <script>
    window.addEventListener("message", function(e) { console.log(e.data); });
  </script>
</body>
</html>
```

> This creates exploit.html. The optional listener logs incoming messages for debugging. Save and serve via a local server.

### Step 2: Load and Verify Embed

**Context**: Open the HTML in a browser to confirm the demo loads without errors.

**Command** (No specific command; manual verification):
```bash
# Serve the file
python3 -m http.server 8000
# Then visit http://localhost:8000/exploit.html
```

> Expected: Demo renders in iframe. Check browser console for any CSP violations (none expected).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/add-message-event-listener]]

## Tools Used

- [[tools/prettier]]

## Tags

- [[xss]]
- [[iframe]]
- [[postmessage]]
