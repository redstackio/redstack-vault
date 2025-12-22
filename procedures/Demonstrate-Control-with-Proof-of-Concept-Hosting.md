---
id: p4d5e6f7-g8h9-0123-defg-456789012345
tags:
  - poc
  - hosting
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud (Microsoft Azure)
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:38:49.547Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Demonstrate-Control-with-Proof-of-Concept-Hosting

## Summary

This procedure hosts a proof-of-concept page on the taken-over subdomain to validate control and illustrate potential abuse vectors like phishing or XSS.

## Description

Once the Traffic Manager is claimed, configure it to serve content from an attacker server. For the Starbucks subdomain, hosting poc.html at http://wfmnarptpc.starbucks.com/poc.html proves the takeover, enabling further exploits like malware distribution or SSL cert acquisition via Let's Encrypt.

## Requirements

1. Controlled web server (e.g., VPS with HTTP service)
2. Configured Traffic Manager endpoints
3. DNS propagation time allowance

## Defense

Defensive measures and detection strategies:

- Monitor subdomain traffic for anomalies using WAF or SIEM
- Certificate Transparency logs for unauthorized SSL issuance
- Real-time DNS change detection

## Objectives

1. Verify subdomain resolution to controlled content
2. Showcase impact (phishing, XSS, etc.)
3. Highlight vulnerability severity

## Instructions

### Step 1: Set Up PoC Server

**Context**: Host a simple HTML page on a server and note its IP.

Create poc.html with content like "<h1>Subdomain Taken Over</h1>" and serve via Python: `python -m http.server 80` on the server.

### Step 2: Route Traffic via Azure

**Context**: Update Traffic Manager to point to the PoC server IP.

In Azure portal, add an external endpoint with the server IP and priority 1.

> Wait for propagation, then browse http://wfmnarptpc.starbucks.com/poc.html.

### Step 3: Validate Access

**Context**: Confirm the page loads, demonstrating control.

Use curl or browser to access the URL.

> Expected: PoC page displays, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[hosting]]
- [[Execution]]
