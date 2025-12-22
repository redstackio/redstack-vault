---
tags:
  - exploitation
  - takeover
  - third-party
type: procedure
tools: []
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
updated_at: '2025-12-14T04:51:26.718Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 987c035e-f981-4a8b-bb3d-ab0bc5bfe89a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Claim Inactive Third-Party Resource

## Summary

This procedure claims an inactive resource on a third-party service to gain control over a dangling subdomain DNS record.

## Description

With a confirmed inactive resource, attackers create or register it on the service, hijacking the subdomain. This enables serving malicious content. Targets are services like S3 or GitHub; requires account on the service.

## Requirements

1. Account on the third-party service
2. Knowledge of the exact resource name from DNS
3. No prior access to target needed

## Defense

Defensive measures and detection strategies:

- Clean up unused resources immediately after deletion
- Use service-specific monitoring for new claims on old names
- Rotate DNS records and monitor for unauthorized content

## Objectives

1. Secure control of the resource
2. Propagate DNS changes
3. Enable content serving on subdomain

## Instructions

### Step 1: Access Third-Party Service

**Context**: Log in and search for the inactive resource name.

No command; web-based: Go to thirdparty.com, sign up/log in, and create a new resource (e.g., bucket) with the dangling name.

### Step 2: Confirm Claim

**Context**: Verify ownership in the service dashboard.

Expected: Dashboard shows the resource as active under your account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[exploitation]]
- [[takeover]]
- [[third-party]]
