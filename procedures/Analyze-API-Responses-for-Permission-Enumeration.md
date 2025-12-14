---
tags:
  - iam
  - permission-enumeration
  - discovery
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - AWS
techniques:
  - '[[T1087.004]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: f0446cba-8e24-4f8d-a507-9a861f7ed157
created_at: '2025-12-14T17:32:29.152Z'
updated_at: '2025-12-14T17:32:29.152Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Analyze-API-Responses-for-Permission-Enumeration

## Summary

This procedure involves testing multiple DocumentDB Elastic API actions on non-production endpoints and analyzing responses to silently map IAM permissions without CloudTrail detection.

## Description

With unlogged endpoints, adversaries can iterate through API operations (e.g., list, create, delete) to determine granted permissions based on success/failure responses. This reconnaissance reveals the IAM principal's scope, facilitating targeted escalation or lateral movement in AWS, all while evading log-based monitoring.

## Requirements

1. Valid non-production endpoint URL
2. AWS CLI configured
3. List of target API actions (e.g., docdb-elastic:ListClusterSnapshots, ListClusters)
4. Scripting or manual logging for response analysis

## Defense

Defensive measures and detection strategies:

- Implement least-privilege IAM policies limiting action scopes
- Use AWS GuardDuty for anomalous API behavior detection
- Enable VPC Flow Logs to capture endpoint traffic patterns

## Objectives

1. Identify permitted IAM actions for the credential
2. Build a permission profile for exploitation planning
3. Maintain operational stealth throughout testing

## Instructions

### Step 1: Test Multiple API Actions

**Context**: Systematically invoke variations on the non-production endpoint.

**Command** (Example for list-clusters):
```bash
aws docdb-elastic list-clusters --endpoint-url ██████
```

> Run similar commands for other actions. Note HTTP 200 for permitted vs. 403/AccessDenied for denied.

### Step 2: Analyze and Document Responses

**Context**: Compile results to enumerate permissions.

No specific command; manually or script (e.g., Python with boto3) to parse JSON outputs and log permissions.

> Success indicates permission granted (e.g., full list returned); failure reveals boundaries. Repeat for 10-20 actions to map comprehensively.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1087.004]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CLI]]

## Tags

- iam
- enumeration
- discovery
