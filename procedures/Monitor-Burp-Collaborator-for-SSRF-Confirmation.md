---
tags:
  - ssrf
  - oob-detection
  - monitoring
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.251Z'
sub_techniques: []
id: ea3ed2ef-dc01-4516-ad71-55f7736239cf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Monitor-Burp-Collaborator-for-SSRF-Confirmation

## Summary

This procedure involves observing interactions in Burp Collaborator to confirm the Blind SSRF, detecting HTTP and DNS requests from the target server to validate the vulnerability exploitation.

## Description

After sending the payload, the Collaborator tool captures out-of-band communications, such as DNS queries and HTTP fetches (e.g., for test.png), indicating the server followed the injected URL. This reveals the vulnerability's presence and potential for deeper attacks like internal service access. The target environment is web-based, with outcomes including logged request details for analysis.

## Requirements

1. Active Burp Collaborator polling enabled
2. Payload sent from prior procedure
3. Burp Suite interface open for real-time monitoring

## Defense

Defensive measures and detection strategies:

- Block outbound requests to unknown domains from web applications
- Implement request signing or allowlisting for external fetches
- Use intrusion detection systems (IDS) to alert on anomalous DNS/HTTP from app servers

## Objectives

1. Capture evidence of server-side request forgery
2. Analyze leaked information (e.g., internal IPs)
3. Confirm exploit success for reporting

## Instructions

### Step 1: Poll Collaborator Interface

**Context**: Check for incoming interactions post-payload submission.

Use Burp Suite (no CLI):

```bash
# In Burp Collaborator: Refresh history tab
```

> Expected output: List of DNS/HTTP events appears.

### Step 2: Analyze Interactions

**Context**: Review details to confirm SSRF and assess impact.

Manual review:

```bash
# Look for: DNS resolve of collaborator domain, HTTP GET to /test.png
# Note source IP and headers for internals
```

> Expected output: Logs show server IP making requests, potentially with sensitive headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[oob-detection]]
