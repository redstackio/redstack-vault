---
tags:
  - aws
  - non-production
  - silent-call
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-bedrock-agent-list-agents-nonprod]]'
  - '[[commands/aws-bedrock-agent-list-knowledge-bases-nonprod]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.792Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4e029dfc-80a3-4b19-9459-92d8a68cf7e5
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Test-Non-Production-Endpoint-Silent-Calls

## Summary

This procedure tests API calls to non-production Bedrock-Agent endpoints, confirming they enforce IAM permissions but fail to log to CloudTrail, allowing undetected interactions.

## Description

Non-production endpoints for Bedrock-Agent (discovered via endpoint enumeration) accept standard IAM credentials and respond normally but lack CloudTrail integration, likely due to isolated development stacks. This enables adversaries to probe services invisibly. Target environment requires AWS CLI and knowledge of non-production URLs (e.g., via --endpoint-url flag). Outcomes include successful/failed responses without logs, contrasting production behavior.

## Requirements

1. AWS CLI with IAM credentials
2. Knowledge of non-production endpoint URLs (e.g., [redacted])
3. CloudTrail configured for comparison

## Defense

Defensive measures and detection strategies:

- Disable or restrict access to non-production endpoints via IAM policies
- Implement endpoint-specific logging or WAF rules for anomalous URLs
- Use AWS Config to monitor service configurations

## Objectives

1. Validate silent API execution on non-production endpoints
2. Confirm no CloudTrail events for calls
3. Test functionality post any partial fixes (e.g., errors on knowledge-bases)

## Instructions

### Step 1: Call Non-Production Endpoint

**Context**: Override the default endpoint to target non-production URL and execute list-agents.

**Command** ([[commands/aws-bedrock-agent-list-agents-nonprod]]):
```bash
aws bedrock-agent list-agents --region us-west-2 --endpoint-url [redacted]
```

> Expected output: JSON with empty agentSummaries or error; no CloudTrail log after 5-10 minutes.

### Step 2: Test Additional Operation and Verify No Logging

**Context**: Use another operation to confirm persistence and check for logs.

**Command** ([[commands/aws-bedrock-agent-list-knowledge-bases-nonprod]]):
```bash
aws bedrock-agent list-knowledge-bases --endpoint-url [redacted] --region us-west-2
```

> Expected output: InternalServerErrorException (e.g., max retries); verify CloudTrail absence.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/aws-bedrock-agent-list-agents-nonprod]]
- [[commands/aws-bedrock-agent-list-knowledge-bases-nonprod]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- bedrock-agent
- cloudtrail
