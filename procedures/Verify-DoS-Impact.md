---
tags:
  - dos
  - verification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-send-invalid-transfer-encoding]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: b90d5d4f-d5f9-441e-9718-c4129c0a7ed2
created_at: '2025-12-11T06:10:40.119Z'
updated_at: '2025-12-11T06:10:40.119Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Verify DoS Impact

## Summary

This procedure verifies the success of cache poisoning by checking if poisoned resources cause denial of service on the target's core functionality.

## Description

After poisoning, legitimate requests to affected JavaScript files should return errors, breaking website functionality for users and confirming DoS.

## Requirements

1. Access to the poisoned resources
2. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Regularly purge caches
- Monitor for DoS patterns in access logs

## Objectives

1. Confirm cache serves poisoned content
2. Assess impact on core services

## Instructions

### Step 1: Request Poisoned Resource

**Context**: Fetch the potentially poisoned JavaScript file.

**Command** ([[commands/curl-send-invalid-transfer-encoding]]):

```bash
curl https://www.paypalobjects.com/path/to/poisoned/js/file
```

> Expect a '501 Not Implemented' error if successful.

### Step 2: Test Functionality

**Context**: Attempt to use affected website features.

> Manually browse paypal.com and note any broken JavaScript-dependent features.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-invalid-transfer-encoding]]

## Tools Used

- [[tools/curl]]

## Tags

- [[dos]]
- [[verification]]
