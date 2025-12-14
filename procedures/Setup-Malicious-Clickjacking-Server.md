---
id: proc-uuid-2
name: Setup Malicious Clickjacking Server
tags:
  - clickjacking
  - flask
  - poc-server
type: procedure
tools:
  - '[[tools/Flask]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python-flask-server]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:18.747Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Setup Malicious Clickjacking Server

## Summary

This procedure sets up a Flask-based server to host the initial lure page (index.html) and the clickjacking popup (attack.html), configuring them with OAuth parameters for the double clickjacking exploit.

## Description

The attacker downloads PoC code (e.g., 250805_wakatime_double_clickjacking.zip), updates index.html with the client_id and redirect_uri, and runs a Flask app to serve the pages. index.html redirects to the OAuth URL and opens attack.html in a new tab, where the 'Double Click' button aligns over the authorization button. This enables the variant clickjacking that evades X-Frame-Options.

## Requirements

1. Python environment with Flask installed
2. PoC source code downloaded
3. Client_id and redirect_uri from prior step

## Defense

Defensive measures and detection strategies:

- Block or scan for suspicious Flask-hosted pages
- Implement CSP to prevent popup manipulations
- Educate users on unexpected tab behaviors

## Objectives

1. Host malicious pages locally or publicly
2. Integrate OAuth parameters into HTML
3. Verify server accessibility

## Instructions

### Step 1: Prepare PoC Files

**Context**: Download and configure the source code for hosting.

No command; unzip 250805_wakatime_double_clickjacking.zip, edit index.html to insert client_id=joUNHCTnWqQ9hsmrWS5CTokR and redirect_uri=https://webhook.site/15495620-7c98-4643-a6df-9e7864c0dead.

> Ensure attack.html has CSS for button alignment (position: absolute; z-index: high).

### Step 2: Start Flask Server

**Context**: Launch the server to serve the pages.

**Command** ([[commands/python-flask-server]]):
```bash
python main.py
```

> This starts the development server on http://127.0.0.1:5000, serving / (index.html) and /attack (attack.html). Expected output: * Running on http://127.0.0.1:5000.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/python-flask-server]]

## Tools Used

- [[tools/Flask]]

## Tags

- [[clickjacking]]
- [[tools/Flask]]
- [[poc-server]]
