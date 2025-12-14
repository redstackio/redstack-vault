---
tags:
  - aws
  - cloudtrail
  - monitoring
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Discovery]]'
commands: []
techniques:
  - '[[T1087.004]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fc0129a3-a5a9-48cc-bf4d-580e7ac439f5
created_at: '2025-12-14T17:32:39.042Z'
updated_at: '2025-12-14T17:32:39.042Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1087.004]]'
---
# Monitor-CloudTrail-for-Standard-Call

## Summary

This procedure involves waiting and checking CloudTrail logs to verify that a production Datazone API call is recorded, confirming the logging mechanism works as expected.

## Description

CloudTrail logs API activity with a delay of 5-10 minutes. In this step, after executing a production call, monitor the trail via AWS console, CLI, or S3 to locate the event. This validates detection capabilities before exploiting unlogged paths. Target environment requires an active CloudTrail trail; outcomes include log confirmation or troubleshooting delivery issues.

## Requirements

1. CloudTrail trail configured and accessible.
2. Permissions to query CloudTrail events (e.g., cloudtrail:LookupEvents).
3. Timer or monitoring tool for 5-10 minute wait.

## Defense

Defensive measures and detection strategies:

- Enable real-time CloudTrail delivery to CloudWatch Logs for faster alerting.
- Set up alarms for Datazone API events.
- Regularly audit trail configurations for completeness.

## Objectives

1. Validate log generation for baseline calls.
2. Ensure no delivery delays or gaps.
3. Confirm event details match the API invocation.

## Instructions

### Step 1: Wait for Log Delivery

**Context**: Allow time for CloudTrail to process and deliver the event.

**Command** (No command; timing-based):

> Wait 5-10 minutes post-API call.

### Step 2: Query CloudTrail Logs

**Context**: Check for the specific event using AWS tools.

**Command** (AWS CLI example for lookup):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=datazone.amazonaws.com
```

> Filter for recent events with eventName: ListDomains. Expected output: JSON list including the call's timestamp, user ARN, and response elements.

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

- aws
- cloudtrail
- verification
