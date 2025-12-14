---
tags:
  - canarytokens
  - monitoring
  - jndi-lookup
  - confirmation
type: procedure
tools:
  - '[[tools/Canarytokens]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:42.535Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: aaf097f0-389b-4eeb-9871-8a50772d58a3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Monitor-JNDI-Lookup-with-Canarytokens

## Summary

This procedure uses Canarytokens to generate a detection token and monitor for incoming LDAP requests, confirming successful Log4Shell exploitation via JNDI lookup from the targeted server.

## Description

After submitting the payload, the attacker's LDAP server (via Canarytokens) waits for connections from the partner's server, indicating the Log4j vulnerability triggered a remote lookup. This confirms RCE potential without needing further interaction. Applicable in web-based supply chain attacks where callbacks validate exploitation.

## Requirements

1. Canarytokens account and generated LDAP token domain
2. Network access to monitor the token dashboard
3. Prior payload submission with the token domain

## Defense

Defensive measures and detection strategies:

- Block outbound LDAP/JNDI connections from application servers
- Use network segmentation to isolate third-party services
- Implement endpoint detection for anomalous DNS resolutions to unknown domains
- Regularly scan for Log4Shell indicators in logs

## Objectives

1. Detect incoming request to confirm payload execution
2. Identify source IP for attribution to partner server
3. Validate attack success for reporting

## Instructions

### Step 1: Generate Token

**Context**: Create a unique canary for LDAP detection.

Visit https://www.canarytokens.org, select LDAP token type, customize the domain, and generate. Note the full URL (e.g., canarytoken-domain.a).

> This provides a disposable domain that alerts on hits.

### Step 2: Monitor Dashboard

**Context**: Watch for callbacks post-submission.

Return to the Canarytokens dashboard and refresh periodically. Look for new alerts showing request details like IP, timestamp, and user-agent.

> A hit from the partner's IP confirms the JNDI lookup and RCE trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Canarytokens]]

## Tags

- [[tools/Canarytokens]]
- [[monitoring]]
- [[jndi-lookup]]
- [[confirmation]]
