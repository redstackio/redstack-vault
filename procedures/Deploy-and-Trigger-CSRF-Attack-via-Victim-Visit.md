---
id: proc-uuid-3
tags:
  - csrf
  - drive-by
  - phishing
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
updated_at: '2025-12-14T17:27:15.251Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deploy-and-Trigger-CSRF-Attack-via-Victim-Visit

## Summary

This procedure hosts the crafted malicious HTML page and lures the victim to visit it while authenticated in Liberapay, triggering the auto-submitted POST request to modify their profile name without interaction.

## Description

The attack relies on social engineering to get the victim to load the page in a browser sharing the Liberapay session. Hosting can be local or remote, with the form exploiting the lack of strict CSRF validation. Impact is limited to same-session attacks, as noted in the vulnerability report. Successful execution results in immediate profile update upon page load.

## Requirements

1. Completed malicious HTML from prior procedure
2. Web hosting capability (local server or public host)
3. Method to deliver link to victim (e.g., email, social media)
4. Victim authenticated in target browser

## Defense

Defensive measures and detection strategies:

- Deploy Content Security Policy (CSP) to block inline scripts in forms
- Use token double-submission or synchronized tokens tied to session
- Log and alert on unexpected POSTs to edit endpoints from unusual referrers

## Objectives

1. Expose the victim to the malicious page in an authenticated context
2. Achieve automatic request forgery without user awareness
3. Confirm session hijacking for low-interaction actions

## Instructions

### Step 1: Host the HTML File

**Context**: Make the malicious page accessible via URL.

Use a simple local server: Navigate to the directory containing csrf-attack.html and run `python -m http.server 8000` (Python 3). Access at http://localhost:8000/csrf-attack.html. For remote, upload to a free host like GitHub Pages or ngrok for tunneling.

> Expected output: Page loads and auto-submits when visited.

### Step 2: Lure the Victim

**Context**: Trick the victim into visiting the hosted URL while logged into Liberapay.

Send a phishing link, e.g., "Check this Liberapay update: http://yourhost.com/csrf-attack.html". Ensure the link appears legitimate.

> The form submits on load if the browser shares the session cookies.

### Step 3: Monitor Execution

**Context**: Observe if the request succeeds without intervention.

From your server logs or victim's browser network tab (if accessible), confirm the POST to https://liberapay.com/<username>/edit/username with status 200.

> Success: No user prompts; profile update occurs silently.

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
- [[drive-by]]
