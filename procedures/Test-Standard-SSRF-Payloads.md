---
tags:
  - ssrf
  - payload-testing
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/throw-if-local-ip-validation]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.286Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fecb3bbe-7aa8-4d75-8980-f266087dae9c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Standard-SSRF-Payloads

## Summary

This procedure tests conventional SSRF payloads against the replicated validation to confirm baseline protections.

## Description

Target cloud metadata endpoints like Alibaba's 100.100.100.200 and AWS's 169.254.169.254 using the test script's ?ip= parameter. These should trigger exceptions via `filter_var` and `IpUtils`, validating the environment before attempting bypasses. Outcomes confirm the need for advanced payloads.

## Requirements

1. Running local PHP test script
2. Knowledge of target metadata IPs
3. cURL or browser for parameter testing

## Defense

Defensive measures and detection strategies:

- Enforce strict IP allowlists in production
- Log validation failures for anomaly detection

## Objectives

1. Verify blocking of private/reserved ranges
2. Establish control for bypass testing
3. Document filter behaviors

## Instructions

### Step 1: Test Alibaba Metadata

**Context**: Check private range detection.

Execute [[commands/throw-if-local-ip-validation]] with ?ip=100.100.100.200:

```bash
php test.php?ip=100.100.100.200
```

> Expected: Exception 'Local IP' due to IpUtils check.

### Step 2: Test AWS Metadata

**Context**: Confirm reserved range flags.

Execute [[commands/throw-if-local-ip-validation]] with ?ip=169.254.169.254:

```bash
php test.php?ip=169.254.169.254
```

> Expected: Exception from filter_var FILTER_FLAG_NO_RES_RANGE.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/throw-if-local-ip-validation]]

## Tools Used

- [[tools/PHP]]

## Tags

- ssrf
- payload-testing
