---
tags:
  - verification
  - caching
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - AWS
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 967437d0-a3b7-4f71-bd01-64b3d75b8de5
created_at: '2025-12-13T09:01:26.275Z'
updated_at: '2025-12-13T09:01:26.275Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify Cached Token Access

## Summary

This procedure verifies that access persists due to token caching in AWS Cognito after provider-side revocation, and observes when the cache expires.

## Description

Post-login, test application functionality to confirm access. Monitor the time until the cache expires (up to 1 hour), after which reauthorization is required, demonstrating the vulnerability's impact.

## Requirements

1. Successful login from previous steps
2. Timer or clock to track cache duration
3. Access to application features

## Defense

Defensive measures and detection strategies:

- Reduce cache TTL in Cognito configurations
- Implement session monitoring for anomalies

## Objectives

1. Confirm continued access
2. Measure revocation delay
3. Validate vulnerability exploitation

## Instructions

### Step 1: Test Application Access

**Context**: Interact with the application to ensure full access.

Navigate through Courier features, such as dashboard or settings.

> Access should be unrestricted.

### Step 2: Monitor Cache Expiration

**Context**: Wait and retest login after potential expiration.

Wait approximately 1 hour, then log out and attempt relogin.

> After expiration, login should fail and prompt reauthorization.

### Step 3: Document Findings

**Context**: Record the exact duration of cached access.

Note the time from revocation to denial.

> This quantifies the vulnerability window.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[caching]]
- [[verification]]
