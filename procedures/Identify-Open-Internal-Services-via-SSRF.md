---
id: proc-uuid-2
tags:
  - ssrf
  - service-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-submit-url-to-validator]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.561Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Open-Internal-Services-via-SSRF

## Summary

This procedure uses SSRF to scan for open internal ports and services, differentiating HTTP responses from non-HTTP (e.g., SSH) to map the target's infrastructure.

## Description

Exploiting the validator's SSRF, submit URLs to common ports like 22 (SSH) and 4680 (custom HTTP). HTTP ports yield successful fetches with metatags, while SSH shows protocol errors. This reveals internal service exposure. Requires validator access; outcomes include port/service identification for escalation.

## Requirements

1. Confirmed SSRF from prior testing
2. List of potential ports (e.g., 22, 4680)
3. POST submission capability

## Defense

Defensive measures and detection strategies:

- Firewall internal ports from localhost requests
- Log and alert on fetches to privileged ports (e.g., 22)
- Disable unnecessary internal services

## Objectives

1. Detect open HTTP services for further exploitation
2. Confirm non-HTTP services to avoid false positives
3. Build internal network map

## Instructions

### Step 1: Probe Non-HTTP Port (SSH)

**Context**: Test SSH port to confirm open but non-HTTP service via error type.

**Command** ([[commands/curl-submit-url-to-validator]]):
```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:22'
```

> Expect protocol mismatch error (e.g., no HTTP response).

### Step 2: Probe Open HTTP Port

**Context**: Target HTTP service to fetch content and extract metatags.

**Command** ([[commands/curl-submit-url-to-validator]]):
```bash
curl -X POST https://cards-dev.twitter.com/validator -d 'url=http://0.0.0.0:4680'
```

> Successful fetch with metatag detection in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-url-to-validator]]

## Tools Used


## Tags

- ssrf
- service-discovery
