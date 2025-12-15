---
id: proc-analyze-dashlane-response
tags:
  - data-exfiltration
  - analysis
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
updated_at: '2025-12-14T17:29:36.688Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Analyze-Linked-Accounts-Response

## Summary

This procedure parses the JSON response from the getLinkedAccounts endpoint to extract and interpret disclosed linked email addresses, confirming the IDOR exploitation.

## Description

Post-exploitation analysis focuses on the response content to identify leaked data, such as associated emails across accounts. In Dashlane, the "logins" array reveals unauthorized linkages, highlighting privacy risks. Expected outcomes include documentation of leaked associations for reporting.

## Requirements

1. JSON response from API call
2. Text editor or JSON parser
3. Knowledge of the target email queried

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive response data and audit API outputs
- Implement data loss prevention (DLP) rules for email patterns
- Log response contents for anomaly detection

## Objectives

1. Extract linked emails from response
2. Verify unauthorized disclosure
3. Assess impact on user privacy

## Instructions

### Step 1: Parse JSON Response

**Context**: Review the HTTP response body for the content section.

Look for {"code":200,"message":"OK","content":{"logins":[...]} }.

### Step 2: Identify Leaked Data

**Context**: Compare returned emails against the authenticated user's known accounts.

Document emails like ["pentester.owasp@gmail.com","arbaz.owasp@gmail.com","hacker.arbaz@gmail.com"], noting cross-account linkages.

> Success confirms IDOR if unrelated emails appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- data-exfiltration
- analysis
