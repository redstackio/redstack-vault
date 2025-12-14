---
tags:
  - cloudinary
  - api
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/cloudinary-usage-api-call]]'
platforms:
  - Cloud
techniques:
  - '[[Cloud Instance Metadata API]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3795a928-0440-4cf6-b8e9-b71f93aca0b5
created_at: '2025-12-14T17:32:48.323Z'
updated_at: '2025-12-14T17:32:48.323Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
---
# Retrieve-Cloudinary-Account-Usage-Statistics

## Summary

This procedure queries the Cloudinary API to fetch account usage metrics, such as request counts and resource totals, using authenticated credentials to demonstrate data access capabilities.

## Description

The usage endpoint provides insights into account activity, which can reveal operational details. In the Reverb.com vulnerability, this confirms control over the 'reverb' account. Use basic auth with extracted creds. Prerequisites: Valid session. Outcomes: JSON data on usage, aiding in assessing impact.

## Requirements

1. Authenticated API access.
2. curl or similar HTTP client.
3. cloud_name ('reverb').

## Defense

Defensive measures and detection strategies:

- Restrict usage endpoint access via API keys with limited scopes.
- Log all usage queries and alert on unusual patterns.
- Regularly review account metrics for discrepancies.

## Objectives

1. Obtain quantitative account data.
2. Validate full access level.
3. Exfiltrate non-sensitive but revealing statistics.

## Instructions

### Step 1: Execute Usage Query

**Context**: Call the dedicated usage endpoint with auth.

Execute [[commands/cloudinary-usage-api-call]]:

```bash
curl -u '434762629765715:█████' https://api.cloudinary.com/v1_1/reverb/usage
```

> Retrieves JSON with keys like 'requests', 'resources', 'derived_resources'.

**Expected Output**: {"requests":1894689201,"resources":36029794,"derived_resources":256178843}

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Cloud Instance Metadata API]]

### Sub-Techniques


## Commands Used

- [[commands/cloudinary-usage-api-call]]

## Tools Used


## Tags

- [[cloudinary]]
- [[api]]
- [[Exfiltration]]
