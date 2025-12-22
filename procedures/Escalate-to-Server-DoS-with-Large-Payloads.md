---
id: proc-uuid-4
tags:
  - dos
  - large-payload
  - resource-exhaustion
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.228Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Escalate-to-Server-DoS-with-Large-Payloads

## Summary

This procedure escalates the attack by crafting and sending oversized payloads to the password reset endpoint, causing resource exhaustion on the server and mail infrastructure, resulting in denial of service.

## Description

Building on spamming, this targets unrestricted input sizes by injecting large strings (e.g., 2MB) into the email field, bypassing client-side limits. Each request consumes excessive memory and processing on the server and mail relays, leading to slowdowns and crashes. After 40-50 requests, the site returns 503/502 errors and becomes unavailable. Applicable to web apps without payload validation; outcomes include temporary site downtime and delayed email delivery.

## Requirements

1. Burp Intruder configured from prior steps
2. Ability to generate large payloads (e.g., via Burp's payload generator)
3. Monitoring tools for response times and errors

## Defense

Defensive measures and detection strategies:

- Enforce server-side length limits on inputs (e.g., 1024 chars for email)
- Use resource quotas and auto-scaling for mail servers
- Alert on high content-length requests or error spikes

## Objectives

1. Overload server resources with large requests
2. Cause mail delivery delays and site crashes
3. Achieve full DoS impact

## Instructions

### Step 1: Modify Payload

**Context**: Craft oversized email inputs to increase content-length.

In Intruder, set payload type to 'Character fuzzer' or manual large string (e.g., repeat 'A' 2MB times) on the email position.

> Update the request to show ~2MB content-length. Expected: Payload ready for oversized injection.

### Step 2: Launch DoS Attack

**Context**: Send multiple large requests and observe degradation.

Set attack type to sniper, threads low to avoid detection, launch 40-50 iterations, monitor responses.

> Initial emails slow (25-30 min for 100), then 503/502 errors; site down 5-10 min. Success: Confirmed DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[dos]]
- [[large-payload]]
- [[resource-exhaustion]]
