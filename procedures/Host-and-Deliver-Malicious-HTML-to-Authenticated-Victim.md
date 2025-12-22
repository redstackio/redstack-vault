---
id: 311222fa-c716-43e3-8eb6-11eb665fda42
name: Host-and-Deliver-Malicious-HTML-to-Authenticated-Victim
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.409Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - shopify
  - phishing
  - hosting
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---

# Host-and-Deliver-Malicious-HTML-to-Authenticated-Victim

## Summary

This procedure hosts the CSRF exploit HTML and delivers it to victims via social engineering, triggering data export when visited by authenticated Shopify partners.

## Description

In a web attack scenario, this involves serving the malicious page from an attacker-controlled server and luring targets (e.g., via email links). Upon visit, the victim's browser submits the forged request using their session, exfiltrating app user data. Expected outcomes: Silent data leak. Requires hosting setup and phishing capabilities.

## Requirements

1. Web server access (local or remote)
2. Method to contact victims (email, messaging)
3. Target list of authenticated partners

## Defense

Defensive measures and detection strategies:

- Train users to avoid unsolicited links
- Implement URL filtering and safe browsing
- Log and alert on unexpected export requests

## Objectives

1. Expose the exploit to victims
2. Confirm execution via logs or data receipt
3. Achieve data collection without detection

## Instructions

### Step 1: Host the HTML File

**Context**: Serve the page accessibly over HTTP/HTTPS.

Place index.html in a directory and start a server, e.g., using Python:

```bash
python3 -m http.server 8000
```

Note the URL: http://your-ip:8000.

### Step 2: Craft Delivery Mechanism

**Context**: Create a phishing lure embedding the URL.

Compose an email or message: "Check this urgent update: [http://your-ip:8000]". Ensure it appears legitimate, e.g., spoof sender as Shopify support.

### Step 3: Monitor Execution

**Context**: Track victim visits and request triggers.

Watch server logs for accesses. On success, the victim's browser will request the Shopify endpoint; attacker may redirect post-submit to mask intent.

> Logs show GET to / from victim IP; subsequent Shopify request inferred from timing.

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
- [[shopify]]
- [[Phishing]]
- [[hosting]]
