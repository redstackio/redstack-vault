---
id: proc-003
tags:
  - aws-route53
  - dns-setup
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.001]]'
updated_at: '2025-12-14T04:38:39.942Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[T1583.001]]'
---
# Create Matching Hosted Zone

## Summary

This procedure registers a new public hosted zone in AWS Route 53 for the parent domain, ensuring its NS records match the dangling delegation to hijack control.

## Description

By creating a hosted zone with the exact name of the deleted one, AWS assigns NS records that can be made to match the dangling pointers, allowing delegation takeover without changing parent DNS.

## Requirements

1. AWS account with Route 53 permissions.
2. Dangling NS records identified.
3. AWS CLI installed and configured.

## Defense

Defensive measures and detection strategies:

- Lock down hosted zone creation with IAM policies requiring approval.
- Monitor AWS CloudTrail for new hosted zone creations matching sensitive domains.
- Use domain registrars with anti-hijacking features.

## Objectives

1. Create the hosted zone successfully.
2. Verify NS records match dangling ones.
3. Prepare for record configuration.

## Instructions

### Step 1: Create Public Hosted Zone

**Context**: Initiate hosted zone creation for the target domain.

Use AWS CLI:

```bash
aws route53 create-hosted-zone --name test-cncf-aws.canary.k8s.io --caller-reference $(date +%s) --hosted-zone-config Comment="Research Zone"
```

> Returns zone ID and NS records.

### Step 2: Retrieve and Compare NS

**Context**: Get the new NS records and ensure they align with dangling.

```bash
aws route53 get-hosted-zone --id /hostedzone/Z1ABC123DEF
```

> Compare NS values manually.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Resource Development

### Techniques

- [[T1583.001]] Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[aws-route53]]
- [[DNS]]
- [[infrastructure]]
