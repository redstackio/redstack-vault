---
id: proc-uuid-004
tags:
  - aws
  - mitigation
  - validation
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-probe-invalid-endpoint]]'
  - '[[commands/curl-post-with-header]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:32:20.864Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Verify Post-Mitigation Endpoint Validation

## Summary

This procedure uses curl to probe SSM endpoints post-mitigation, checking for validation errors that block unauthorized access or enumeration.

## Description

After applying fixes like endpoint validation, test redacted URLs with curl to elicit ValidationException or UnknownOperationException. This confirms mitigations prevent silent calls, though some actions like ListOpsItemEvents may remain partially vulnerable. No data access possible; focuses on ingress layer changes.

## Requirements

1. curl installed on a system with AWS network access.
2. Knowledge of redacted endpoint URLs.
3. Headers for operation testing (e.g., custom AWS headers).
4. Comparison to pre-mitigation behavior.

## Defense

Defensive measures and detection strategies:

- Enforce strict endpoint allowlisting in SSM service.
- Log all HTTP probes to non-standard AWS URLs.
- Use WAF rules to block anomalous requests.

## Objectives

1. Confirm mitigation blocks invalid endpoints.
2. Identify residual vulnerabilities.
3. Validate exception responses.

## Instructions

### Step 1: Probe Invalid Endpoint

**Context**: Test basic access to redacted endpoint.

**Command** ([[commands/curl-probe-invalid-endpoint]]):
```bash
curl █████
```

> Expected output: <ValidationException><Message>400 ERROR: Invalid Endpoint</Message></ValidationException>.

### Step 2: Test with Header and POST

**Context**: Simulate API call with authentication header.

**Command** ([[commands/curl-post-with-header]]):
```bash
curl -X POST https://███ -H "████"
```

> Expected output: <UnknownOperationException/> indicating operation rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques


## Commands Used

- [[commands/curl-probe-invalid-endpoint]]
- [[commands/curl-post-with-header]]

## Tools Used

- [[tools/curl]]

## Tags

- mitigation
- validation
- post-exploit
