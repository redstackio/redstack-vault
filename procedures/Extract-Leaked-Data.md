---
tags:
  - credential-leak
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Cloud (GitLab.com)
techniques:
  - '[[Data from Local System]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c7ef7ec4-9b58-4844-bb68-0f711ba1bbd3
created_at: '2025-12-11T03:47:56.778Z'
updated_at: '2025-12-11T03:47:56.778Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1005]]'
---
# Extract Leaked Data

## Summary

This procedure involves observing and extracting leaked sensitive data from the API response.

## Description

The response contains leaked bytes from files like database configs, enabling further attacks.

## Requirements

1. API response from previous step

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive files
- Audit file access

## Objectives

1. Collect leaked credentials
2. Use for escalation

## Instructions

### Step 1: Review Response

**Context**: Parse the output for leaks.

Examine the API response for sensitive information like database connection details.

> Look for ~250 bytes of data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #credential-leak
