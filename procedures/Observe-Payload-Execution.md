---
id: uuid-observe-execution
tags:
  - xss
  - detection
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.029Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe Payload Execution

## Summary

This procedure monitors the execution of injected payloads when authenticated users view the comments, confirming the stored XSS impact through server logs.

## Description

After submission, payloads persist in storage. When employees from organizations like █████████ view the page, scripts execute: external JS loads, forms post data, or redirections occur. Attacker observes via weblog hits, credential receipts, or access logs.

## Requirements

1. Submitted payloads from prior steps
2. Attacker server with logging (e.g., for blind.js, POSTs)
3. Access to target users' viewing (social engineering or wait)

## Defense

Defensive measures and detection strategies:

- Audit comment views for anomalous behavior
- Implement anomaly detection on outbound requests from browsers
- Use SIEM to correlate script loads with user sessions

## Objectives

1. Verify persistent execution
2. Collect impact evidence (logs, data)
3. Assess escalation potential

## Instructions

### Step 1: Monitor Server and Induce View

**Context**: Wait for or prompt target to view comments, then check logs.

Direct a user to the comment page; monitor http://attackerip/ for requests from weblog or forms.

> Expected output: Logs show victim's IP hitting endpoints, confirming execution (e.g., blind XSS hit).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Exfiltration]]

