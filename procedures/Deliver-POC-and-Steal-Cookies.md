---
id: uuid-proc-6
tags:
  - exfiltration
  - cookie-theft
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:16:25.871Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Deliver-POC-and-Steal-Cookies

## Summary

This procedure involves distributing the clickjacking POC to victims and capturing exfiltrated cookies via an attacker-controlled endpoint.

## Description

Once the POC is developed, host it on a malicious site or deliver via social engineering. Victim interaction executes the hidden XSS, sending cookies to the attacker, enabling session hijacking. This final step realizes the full impact on web sessions across the domains.

## Requirements

1. Attacker-controlled server for receiving data
2. Delivery vector (e.g., email, phishing link)
3. POC HTML files

## Defense

Defensive measures and detection strategies:

- Educate users on phishing recognition
- Monitor for anomalous data exfiltration to external domains

## Objectives

1. Trick victim into opening and interacting with POC
2. Execute XSS to steal cookies
3. Receive and utilize stolen session data

## Instructions

### Step 1: Host and Distribute POC

**Context**: Make the POC accessible to victims.

Upload POC.html to a web server and send a link disguised as a legitimate offer from Meredith sites.

> Victim clicks link, loads POC, and interacts with overlay.

### Step 2: Capture Exfiltrated Data

**Context**: Set up endpoint to log incoming cookies.

On attacker server, monitor requests to /steal endpoint for cookie parameters.

> Successful attack appends stolen cookies to URL, allowing log capture for replay.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[cookie-theft]]
- [[Phishing]]
