---
id: proc-uuid-2
tags:
  - csrf
  - payload-delivery
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
updated_at: '2025-12-13T23:55:20.718Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-XSS-Payload-via-CSRF

## Summary

This procedure involves hosting the generated CSRF PoC HTML and tricking a victim into interacting with it, causing an automatic POST submission of the XSS payload to the vulnerable endpoint.

## Description

Once the PoC is created, host it on a web server (local or remote) and deliver the link via email, social engineering, or embedded in a site. The form submits to echo.urbandictionary.biz, reflecting the payload as executable HTML in the victim's browser, leading to XSS. Expected outcomes include JavaScript execution without direct target interaction.

## Requirements

1. Hosted web server for the PoC HTML (e.g., Python SimpleHTTPServer)
2. Social engineering vector to reach the victim
3. Victim's browser must allow cross-origin POSTs (no strict CORS enforcement needed here)

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Monitor for unexpected POSTs from user agents
- Deploy web application firewalls (WAF) to block CSRF patterns

## Objectives

1. Induce victim interaction with the PoC
2. Trigger cross-site request to the target
3. Observe payload delivery in network traces

## Instructions

### Step 1: Host the PoC

**Context**: Serve the HTML file to make it accessible via URL.

**Instructions**: Use a simple server to host the file.

```bash
python -m http.server 8000
```

> Access via http://your-ip:8000/poc.html; note the URL for delivery.

### Step 2: Deliver to Victim

**Context**: Send the hosted PoC link to the victim.

**Instructions**: Embed in an email or link; the form auto-submits on load.

No command; rely on victim click.

> Confirm via Burp or logs that the POST reaches echo.urbandictionary.biz.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
