---
id: proc-uuid-003
tags:
  - aws
  - ssm
  - ops-summary
  - list-commands
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-ssm-get-ops-summary-nonprod]]'
  - '[[commands/aws-ssm-list-ops-item-events-nonprod]]'
  - '[[commands/aws-ssm-list-commands-nonprod]]'
  - '[[commands/export-aws-profile-noperm]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1087.004]]'
updated_at: '2025-12-14T17:32:20.866Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Test Additional SSM Actions for Silent Enumeration

## Summary

This procedure tests various SSM actions (e.g., GetOpsSummary, ListOpsItemEvents, ListCommands) on non-production endpoints to enumerate IAM permissions silently, comparing responses for privileged vs. unprivileged roles.

## Description

Extending the initial test, call multiple SSM operations using redacted non-production endpoints like ███ or https://████. Responses differ: empty arrays (e.g., {"Entities": []}) for allowed, AccessDeniedException for denied. Affects 18 endpoints; no CloudTrail logs enable stealthy reconnaissance on compromised credentials. Test across accounts to isolate effects.

## Requirements

1. Multiple AWS profiles (admin, noperm, extended-management).
2. List of non-production endpoint URLs.
3. Ability to switch AWS accounts for validation.
4. SSM service permissions for baseline.

## Defense

Defensive measures and detection strategies:

- Apply allowlists for SSM endpoints in network policies.
- Monitor anomalous SSM call patterns via CloudWatch.
- Rotate IAM credentials regularly.

## Objectives

1. Map SSM-specific permissions.
2. Validate across privilege levels and accounts.
3. Confirm consistent logging evasion.

## Instructions

### Step 1: Set Unprivileged Profile

**Context**: Prepare for denied permission test.

**Command** ([[commands/export-aws-profile-noperm]]):
```bash
export AWS_PROFILE=noperm
```

> Switches to no-permissions profile. Expected output: Silent.

### Step 2: Test GetOpsSummary

**Context**: Probe for OpsSummary permission.

**Command** ([[commands/aws-ssm-get-ops-summary-nonprod]]):
```bash
aws ssm get-ops-summary --endpoint-url ███
```

> For noperm: AccessDeniedException; for admin: {"Entities": []}. No log.

### Step 3: Test List Actions

**Context**: Enumerate events and commands.

**Command** ([[commands/aws-ssm-list-ops-item-events-nonprod]]):
```bash
aws ssm list-ops-item-events --endpoint-url https://████
```

> Varies: {"Summaries": []} or AccessDenied; no log.

**Command** ([[commands/aws-ssm-list-commands-nonprod]]):
```bash
aws ssm list-commands --endpoint-url https://███████
```

> Post-mitigation: ValidationException for both.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1087.004]] Cloud Account

### Sub-Techniques


## Commands Used

- [[commands/export-aws-profile-noperm]]
- [[commands/aws-ssm-get-ops-summary-nonprod]]
- [[commands/aws-ssm-list-ops-item-events-nonprod]]
- [[commands/aws-ssm-list-commands-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- multi-action
- enumeration
