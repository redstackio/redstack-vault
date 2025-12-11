---
tags:
  - gitlab
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[TA0009]]'
commands:
  - '[[gitlab-move-quick-action]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[T1213]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 88fc4ee1-ab9d-4468-8af0-f1fc4f3db4ab
created_at: '2025-12-06T06:57:46.333Z'
updated_at: '2025-12-06T06:57:46.333Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Observe Exposed Project Data

## Summary

This procedure explains how to inspect the JSON response from the Quick Action to extract exposed sensitive data like runner tokens.

## Description

After submitting the /move command, the API response includes the full serialized Project model, revealing attributes such as runners_token and runners_token_encrypted, even for unauthorized projects.

## Requirements

1. Browser developer tools enabled
2. Prior execution of Quick Action
3. Network monitoring capability

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive tokens properly
- Add access checks to serialization processes

## Objectives

1. Extract runner tokens from response
2. Identify other sensitive attributes
3. Assess potential for further exploitation

## Instructions

### Step 1: Open Developer Tools

**Context**: Monitor network traffic.

In your browser, open DevTools and go to the Network tab.

> Filter for the POST request to /notes.

### Step 2: Inspect Response

**Context**: View the JSON payload.

Locate the response and examine the JSON for sensitive fields.

> Look for runners_token and related data.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0009]]

### Techniques

- [[T1213]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[gitlab-move-quick-action]]
- [[data-exfiltration]]
