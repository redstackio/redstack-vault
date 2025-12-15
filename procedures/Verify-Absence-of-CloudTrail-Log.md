---
tags:
  - aws
  - cloudtrail
  - verification
type: procedure
tools:
  - '[[tools/AWS-CLI]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
techniques:
  - '[[Disable Cloud Logs]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1ef095d2-442b-4eac-b064-d4b7314f07e8
created_at: '2025-12-14T17:32:39.035Z'
updated_at: '2025-12-14T17:32:39.035Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable Cloud Logs]]'
---
# Verify-Absence-of-CloudTrail-Log

## Summary

This procedure confirms that non-production Datazone API calls do not generate CloudTrail entries, validating the logging bypass.

## Description

After invoking a non-prod endpoint, wait and query CloudTrail to ensure no event appears. This step proves evasion success in an AWS setup with Datazone; outcomes include log absence confirmation, highlighting the vulnerability for silent operations.

## Requirements

1. Recent non-prod API call executed.
2. CloudTrail access for querying.
3. 5-10 minute monitoring period.

## Defense

Defensive measures and detection strategies:

- Extend CloudTrail to cover all endpoints via custom trails.
- Alert on missing logs for high-risk services like Datazone.
- Conduct periodic endpoint audits.

## Objectives

1. Confirm logging evasion.
2. Rule out delayed log delivery.
3. Document gap for remediation.

## Instructions

### Step 1: Wait Post-Call

**Context**: Allow processing time.

**Command** (Timing):

> Wait 5-10 minutes.

### Step 2: Check for Events

**Context**: Query without finding the call.

**Command** (AWS CLI lookup):
```bash
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventSource,AttributeValue=datazone.amazonaws.com --start-time $(date -u -d '10 minutes ago' +%Y-%m-%dT%H:%M:%SZ)
```

> Expected output: No matching events for the non-prod call.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable Cloud Logs]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/AWS-CLI]]

## Tags

- aws
- log-absence
- evasion
