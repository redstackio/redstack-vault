---
tags:
  - aws
  - cloudtrail
  - logging
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/aws-bedrock-agent-list-agents-production]]'
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.795Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: ffb5b0e8-ee1d-48db-84cf-3952c2dea9b9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify-Production-Endpoint-Logging

## Summary

This procedure verifies that production API calls to the AWS Bedrock-Agent service generate logs in CloudTrail, providing a baseline to contrast with unlogged non-production endpoints.

## Description

In an AWS environment with Bedrock-Agent enabled and CloudTrail configured, execute a standard API operation to confirm logging behavior. This step is crucial for identifying logging discrepancies in non-production setups, where adversaries can exploit the absence of logs for stealthy reconnaissance. Prerequisites include AWS CLI setup with valid credentials and CloudTrail trail active in the target region (e.g., us-west-2). Expected outcomes include a logged event after a short delay, highlighting normal detection mechanisms.

## Requirements

1. AWS CLI installed and configured with IAM credentials
2. CloudTrail enabled for the AWS account and region
3. Access to Bedrock-Agent service (any permission level)

## Defense

Defensive measures and detection strategies:

- Ensure comprehensive CloudTrail logging across all regions and services
- Monitor for anomalous API call patterns via AWS GuardDuty or custom alerts
- Regularly audit IAM policies to limit credential exposure

## Objectives

1. Establish baseline logging for production endpoints
2. Confirm CloudTrail event generation timing (5-10 minutes)
3. Identify reliance on logs for permission monitoring

## Instructions

### Step 1: Execute Production API Call

**Context**: Call the Bedrock-Agent list-agents operation on the default production endpoint to trigger logging.

**Command** ([[commands/aws-bedrock-agent-list-agents-production]]):
```bash
aws bedrock-agent list-agents --region us-west-2
```

> This command lists agents in the us-west-2 region using the production endpoint. Expected output is a JSON response with agentSummaries array; the call generates a CloudTrail event logged under the RunInstances or similar event name variant for Bedrock.

### Step 2: Monitor CloudTrail Logs

**Context**: Wait and verify the log entry to confirm detection baseline.

**Command** (No direct command; use AWS Console or CLI to query):
```bash
# Optional: Use AWS CLI to describe trails or events if scripted
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=bedrock-agent.amazonaws.com
```

> Check after 5-10 minutes. Expected output includes the event details if logged successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/aws-bedrock-agent-list-agents-production]]

## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- cloudtrail
- bedrock-agent
