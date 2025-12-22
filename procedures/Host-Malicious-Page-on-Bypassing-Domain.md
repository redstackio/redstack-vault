---
tags:
  - xss
  - postmessage
  - domain-setup
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
updated_at: '2025-12-13T23:56:19.907Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c147352f-5389-4029-a0bb-bf455b23e981
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-Malicious-Page-on-Bypassing-Domain

## Summary

This procedure involves registering and hosting a malicious HTML page on a domain crafted to bypass the target's postMessage origin validation by including 'https://hq.upserve.com' as a substring, setting the stage for a DOM-based XSS attack.

## Description

In the Upserve inventory login vulnerability, the postMessage handler checks origins using an incomplete indexOf match. By hosting on a domain like 'hq.upserve.com.evil.com', the malicious page can communicate with the target window. The page opens the login page and prepares to send payloads, tricking users into interaction for drive-by compromise.

## Requirements

1. Access to a domain registrar to create a bypassing subdomain (e.g., via a service like Namecheap).
2. Web hosting to serve the HTML file (e.g., GitHub Pages or a simple VPS).
3. Basic JavaScript knowledge to embed window.open or iframe for targeting.

## Defense

Defensive measures and detection strategies:

- Implement strict origin validation using exact matches or structured parsing instead of indexOf.
- Content Security Policy (CSP) to restrict postMessage sources.
- Monitor for anomalous domains registering substrings of trusted origins.

## Objectives

1. Establish a malicious endpoint that passes the target's origin check.
2. Prepare user interaction to load the target page.
3. Enable payload delivery without raising immediate suspicions.

## Instructions

### Step 1: Register Bypassing Domain

**Context**: Choose a domain that contains the trusted string as a substring to fool the indexOf check.

No specific command; manually register 'hq.upserve.com.evil.com' or similar via a registrar.

> Expected: Domain ownership confirmed via DNS propagation.

### Step 2: Create and Host Malicious HTML

**Context**: Build the page with a link or auto-script to open the target and prepare postMessage.

```html
<!DOCTYPE html>
<html>
<body>
    <a href="#" id="trigger">Click Here</a>
    <script>
        var target = window.open('https://inventory.upserve.com/login/', '_blank');
        document.getElementById('trigger').onclick = function() { /* prepare payload */ };
    </script>
</body>
</html>
```

> Upload to hosting service. Expected: Page accessible at https://hq.upserve.com.evil.com/upserve_xss.html.

### Step 3: Verify Accessibility

**Context**: Ensure the page loads and can reference the target without CORS issues.

Open the malicious URL in a browser and confirm the target opens.

> Expected: No errors; target login page visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- domain-bypass
