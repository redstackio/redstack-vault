---
id: proc-uuid-4
tags:
  - data-exfiltration
  - privacy
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:23.615Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Retrieve-and-Analyze-Unauthorized-Subscription-Data

## Summary

This procedure parses the API response from the IDOR exploit to extract and analyze sensitive treat subscription details of the target user, confirming the privacy violation.

## Description

Following the modified API request, this step focuses on collecting and reviewing the returned JSON data, which includes Subscription ID, Purchased Date, and Validity for the unauthorized user_id. In the Zomato attack scenario, this demonstrates the full impact of the IDOR by leaking personal purchase history. Target: API response data. Prerequisites: Successful exploitation response. Expected outcomes: Identification of leaked sensitive information for reporting or further abuse.

## Requirements

1. JSON response from the exploited API call
2. Tool for parsing JSON (e.g., jq or browser console)
3. Knowledge of expected data fields

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive data in API responses
- Implement data masking or access controls on subscription info
- Audit logs for data access patterns and alert on cross-user queries
- Regular vulnerability scanning for IDOR in APIs

## Objectives

1. Extract key subscription fields from response
2. Verify data belongs to target user (not own)
3. Document the leak for impact assessment

## Instructions

### Step 1: Capture Response

**Context**: Save the full JSON response from the modified request.

If using curl, redirect output: add `-o response.json` to the command.

**Expected Output**: File containing JSON like {"subscriptions": [{"id": 123, "purchased_date": "2023-01-01", "validity": "2023-12-31"}]}.

### Step 2: Parse and Analyze Data

**Context**: Inspect for sensitive details and confirm unauthorized access.

Use a JSON viewer or command-line tool to parse:

```bash
cat response.json | jq '.subscriptions[] | {id, purchased_date, validity}'
```

Compare with own data to ensure mismatch.

**Expected Output**: List of subscriptions with dates and validity periods.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- data-collection
- analysis
