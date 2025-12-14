---
tags:
  - ssrf
  - external-request
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
  - '[[tools/pingb-in]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.205Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c9c20b4a-bac7-41d7-bd3f-c21c1926c540
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-with-External-URL

## Summary

This procedure exploits Server-Side Request Forgery (SSRF) by injecting an external URL into the chatbox on the login page, causing the server to fetch unauthorized resources and enabling attack surface mapping.

## Description

The chatbox lacks validation, allowing arbitrary URLs to be processed server-side. By submitting a unique external URL like a Burp Collaborator payload, the attacker can confirm SSRF through out-of-band interactions, potentially exposing internal networks or metadata.

## Requirements

1. Access to Burp Collaborator or alternative like pingb.in
2. Target login page loaded
3. Monitoring setup for incoming requests

## Defense

Defensive measures and detection strategies:

- Whitelist allowed domains for server-side requests
- Disable or restrict chat features on unauthenticated pages
- Log and alert on outbound traffic from web servers

## Objectives

1. Force server to make external HTTP requests
2. Confirm SSRF vulnerability
3. Gather evidence of server behavior

## Instructions

### Step 1: Generate Payload URL

**Context**: Create a unique URL for tracking interactions using Burp Collaborator.

Launch Burp Suite and generate a Collaborator payload, e.g., http://abc123.burpcollaborator.net, or use http://pingb.in/.

> Payload ready for injection.

### Step 2: Inject URL into Chatbox

**Context**: Submit the external URL via the chat input to trigger the SSRF.

Paste the URL into the chatbox and submit the message.

> No page response expected; rely on external monitoring for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]
- [[tools/pingb-in]]

## Tags

- [[ssrf]]
- [[external-request]]
