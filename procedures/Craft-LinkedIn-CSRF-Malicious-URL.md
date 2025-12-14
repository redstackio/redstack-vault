---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - url-crafting
  - linkedin
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.351Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-LinkedIn-CSRF-Malicious-URL

## Summary

This procedure constructs a malicious URL exploiting the CSRF-vulnerable discovery-see-all endpoint on LinkedIn, simulating an email recommendation to trigger unauthorized follow actions.

## Description

The endpoint https://www.linkedin.com/comm/mynetwork/discovery-see-all/ processes GET requests without CSRF token validation, allowing forged requests. By embedding the victim's user ID in entityUrn and using parameters like usecase=EMAIL_MIXED_RECOMMENDATIONS, the URL mimics legitimate traffic. Tracking tokens (trk, midToken, etc.) are added to blend in. Prerequisites include the user ID from prior recon; outcome is a clickable link that executes the follow on click.

## Requirements

1. Victim's fsd_profile user ID
2. Knowledge of LinkedIn endpoint parameters
3. Text editor or URL builder for construction

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Validate request origins and parameters server-side
- Log and monitor unusual GET requests to discovery endpoints

## Objectives

1. Create a forged request that bypasses CSRF protections
2. Simulate legitimate recommendation traffic
3. Prepare URL for social engineering delivery

## Instructions

### Step 1: Assemble Base URL and Parameters

**Context**: Start with the vulnerable endpoint and add core parameters.

Use https://www.linkedin.com/comm/mynetwork/discovery-see-all/ as base, append ?usecase=EMAIL_MIXED_RECOMMENDATIONS&entityUrn=urn:li:fs_DiscoveryEntity:(urn:li:member:<USER-ID>,PEOPLE_FOLLOW).

> Replace <USER-ID> with the extracted ID, e.g., urn:li:fs_DiscoveryEntity:(urn:li:member:123456789,PEOPLE_FOLLOW).

### Step 2: Add Tracking Tokens

**Context**: Include obfuscation parameters to mimic real requests.

Append &trk=some-tracking-id&midToken=token-value&midSig=sig-value&trkEmail=email-hash&lipi=li_token-value.

> Generate plausible tokens from observed legitimate requests or use static values; test URL in a controlled environment if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[url-crafting]]
- [[linkedin]]
