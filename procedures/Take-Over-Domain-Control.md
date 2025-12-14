---
id: proc-004
tags:
  - dns-control
  - subdomain-takeover
  - aws
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T04:38:39.940Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Take Over Domain Control

## Summary

This procedure configures DNS records in the newly created hosted zone to fully control the subdomain, including adding arbitrary records for testing takeover.

## Description

With the hosted zone in place, add resource records like A, CNAME, or wildcards to redirect traffic, enabling control over the subdomain's resolution.

## Requirements

1. Hosted zone ID from creation step.
2. AWS CLI access.
3. Target IP or content for records.

## Defense

Defensive measures and detection strategies:

- Implement DNSSEC for delegation integrity.
- Regularly scan for subdomain takeovers using tools like Subjack.
- Alert on unexpected DNS changes via AWS SNS.

## Objectives

1. Add test records to verify control.
2. Confirm resolution to attacker resources.
3. Expand to wildcard for broad control.

## Instructions

### Step 1: Add Test A Record

**Context**: Create a subdomain record pointing to controlled server.

Prepare JSON and apply:

```bash
aws route53 change-resource-record-sets --hosted-zone-id Z1ABC123DEF --change-batch file://test-record.json
```

> JSON defines A record for test.api.... to 1.2.3.4.

### Step 2: Verify Takeover

**Context**: Test DNS resolution post-change.

```bash
dig test.api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io
```

> Should resolve to attacker's IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1583.001]] Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[DNS]]
- [[takeover]]
- [[aws]]
