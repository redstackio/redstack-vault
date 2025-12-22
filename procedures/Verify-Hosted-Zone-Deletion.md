---
id: proc-002
tags:
  - dns
  - verification
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:38:39.943Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify Hosted Zone Deletion

## Summary

This procedure confirms that an AWS Route 53 hosted zone referenced by dangling NS records has been deleted, leaving the subdomain delegation vulnerable to takeover.

## Description

After identifying potential dangling NS records, verify the hosted zone's status by attempting resolutions against the name servers. Failed resolutions indicate deletion. This step is crucial before attempting to claim the zone.

## Requirements

1. NS records from previous discovery step.
2. Access to DNS query tools.
3. Optional: AWS account to check zone existence via API (if permitted).

## Defense

Defensive measures and detection strategies:

- Implement automated checks for dangling delegations in CI/CD pipelines.
- Use AWS Config rules to monitor hosted zone deletions and NS updates.
- Log and alert on DNS query failures for internal domains.

## Objectives

1. Test resolution against dangling NS servers.
2. Confirm SERVFAIL or NXDOMAIN responses.
3. Document the vulnerability for reporting.

## Instructions

### Step 1: Direct NS Query

**Context**: Query one of the dangling NS servers directly for the subdomain.

Use dig with @ns-server:

```bash
dig @ns-123.awsdns-45.com api.e2e-kops-aws-canary.test-cncf-aws.canary.k8s.io A
```

> Expect SERVFAIL if zone deleted.

### Step 2: Check Zone Existence

**Context**: If AWS access available, query the hosted zone list (informational only).

```bash
aws route53 list-hosted-zones --max-items 100
```

> Absence of the zone confirms deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[DNS]]
- [[verification]]
- [[aws]]
