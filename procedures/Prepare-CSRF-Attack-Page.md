---
tags:
  - csrf
  - web-vulnerability
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.380Z'
sub_techniques: []
id: 9ba8016b-5e9b-428c-8f0c-f9c184fff5e0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-CSRF-Attack-Page

## Summary

This procedure creates a simple HTML page with a malicious link that exploits a CSRF vulnerability in the Lichess /account/network endpoint by sending a GET request to change the usingAltSocket parameter to false, switching network routing to direct.

## Description

In the context of the Lichess network feature, the endpoint lacks CSRF protection, allowing an attacker to forge requests from an external site. The page disguises the link as innocuous content to lure the victim into clicking it while authenticated, resulting in unauthorized settings changes that may degrade connection performance by bypassing CDN routing.

## Requirements

1. Basic knowledge of HTML
2. Text editor (e.g., Notepad, VS Code)
3. Understanding of the target endpoint URL and parameters

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use POST instead of GET for sensitive actions
- Monitor for anomalous account setting changes in logs

## Objectives

1. Generate a functional HTML payload for CSRF exploitation
2. Ensure the link targets the correct vulnerable parameter
3. Prepare for hosting without alerting the victim

## Instructions

### Step 1: Create the HTML File

**Context**: Draft the HTML content that embeds the exploitative link, making it appear benign to encourage clicks.

**Command** (Manual HTML Creation):

```html
<html>
<body>
<h1>Interesting Chess Strategy</h1>
<p>Click <a href="https://lichess.org/account/network?usingAltSocket=false">here</a> to learn more.</p>
</body>
</html>
```

> This creates a page with a link that, when clicked by an authenticated user, sends the GET request to alter settings. Save as csrf.html and open in a browser to verify the link works (test without auth to see the request).

### Step 2: Validate the Payload

**Context**: Test the HTML locally to ensure the link forms correctly without executing the exploit.

Open the file in a browser and inspect the network tab; confirm the href attribute points to the Lichess endpoint with the parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-vulnerability]]
