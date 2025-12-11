---
tags:
  - information-disclosure
  - endpoint-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 29548f80-0d61-4cb1-ac21-2a2e290a4897
created_at: '2025-12-11T03:47:39.507Z'
updated_at: '2025-12-11T03:47:39.507Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Direct Access to Export Endpoint

## Summary

This procedure directly accesses the HackerOne export endpoint to retrieve raw data, including hidden comments from partially disclosed reports.

## Description

By querying the export/raw endpoint, an attacker can bypass UI restrictions and obtain sensitive comment data. This exploits the failure to enforce visibility rules in the export process on the HackerOne platform.

## Requirements

1. Knowledge of the report ID
2. HTTP client like curl
3. Authenticated access (cookies or tokens if required)

## Defense

Defensive measures and detection strategies:

- Restrict endpoint access to authorized users only
- Implement rate limiting and monitoring on export endpoints

## Objectives

1. Query the export endpoint directly
2. Retrieve raw data with hidden comments
3. Validate the information disclosure

## Instructions

### Step 1: Access Export URL

**Context**: Fetch the raw export data.

Execute [[commands/curl-hackerone-export]] to retrieve the data:

```bash
curl "https://hackerone.com/reports/█████████/export/raw?include_internal_activities=false"
```

> The response includes the hidden comments in raw format.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques

None

## Commands Used

- [[commands/curl-hackerone-export]]

## Tools Used

None

## Tags

- information-disclosure
- endpoint-access
