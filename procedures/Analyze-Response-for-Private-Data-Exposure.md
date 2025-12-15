---
id: proc-analyze-graphql-response
tags:
  - graphql
  - data-analysis
  - information-disclosure
  - hackerone
type: procedure
tools:
  - '[[tools/GraphQL-Client]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:53.562Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Analyze Response for Private Data Exposure

## Summary

This procedure examines the GraphQL response from aggregation queries to identify exposed private information, such as handles of private programs and asset details.

## Description

After executing the aggregation query, the response contains unfiltered buckets that aggregate data across private and public programs. Analysis involves parsing JSON to spot sensitive keys (e.g., 'private') and doc_counts, confirming the bypass of access controls. This reveals potential for further enumeration of private assets.

## Requirements

1. JSON response from prior aggregation query.
2. JSON parsing tool (e.g., jq) or manual inspection.
3. Knowledge of HackerOne program structures.

## Defense

Defensive measures and detection strategies:

- Sanitize aggregation outputs to exclude private data.
- Implement anomaly detection for response sizes or unusual bucket keys.
- Regular audits of GraphQL query responses for leakage.

## Objectives

1. Parse and identify private handles in buckets.
2. Quantify exposure (e.g., doc_counts for private entries).
3. Validate impact by cross-checking against accessible programs.

## Instructions

### Step 1: Parse the Response JSON

**Context**: Use a tool like jq to extract 'aggs' section and list buckets.

**Command**:
```bash
cat response.json | jq '.data.opportunities_search.aggs.results.buckets[] | {key, doc_count}'
```

> This filters buckets showing key-value pairs. Look for 'private' or unknown handles. Expected: Array of objects like {"key": "private", "doc_count": 1}.

### Step 2: Cross-Reference for Confirmation

**Context**: Compare exposed handles against what the user can see in the HackerOne UI.

**Instructions**: Manually query public opportunities or use the UI to list accessible programs. Any handle in buckets not visible indicates exposure.

**Expected Output**: Confirmation of private data like sum_other_doc_count: 37, with multiple private entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/GraphQL-Client]]

## Tags

- data-analysis
- graphql
- exposure-validation
