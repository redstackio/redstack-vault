---
id: proc-observe-graphql-response
tags:
  - data-retrieval
  - graphql
  - response-analysis
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:20.454Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Financial-Data-Response

## Summary

This procedure captures and analyzes the GraphQL response from the modified query, confirming unauthorized access to financial data like total earnings in Shopify's partner dashboard.

## Description

After forwarding the altered payload, the server returns JSON with serviceMetrics data, exposing amounts such as "0.0" for totalEarnings despite the user's lack of permissions. This validates the improper authorization vulnerability.

## Requirements

1. Modified request forwarded from previous step
2. Tools to view response (dev tools or proxy)
3. Knowledge of expected JSON structure

## Defense

Defensive measures and detection strategies:

- Implement data leakage prevention (DLP) on API responses
- Correlate API access logs with user permissions
- Anonymize or restrict financial data in responses

## Objectives

1. Receive and parse the GraphQL response
2. Extract sensitive financial information
3. Confirm bypass success

## Instructions

### Step 1: Capture Response

**Context**: View the server's reply to the modified query.

In dev tools Network tab or proxy, inspect the response to the GraphQL POST.

> JSON body contains the data object.

### Step 2: Analyze Data

**Context**: Verify exposure of unauthorized fields.

Look for { "data":{ "serviceMetrics":{ "totalEarnings":{ "amount":"0.0" } } } } in the response.

> The amount field reveals financial details.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-retrieval]]
- [[response-observation]]
- [[financial-exposure]]
