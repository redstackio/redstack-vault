---
tags:
  - json-analysis
  - data-disclosure
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
detection_risk: low
sub_techniques: []
id: ef74f94c-7d61-4b08-9615-dac0f4181c91
created_at: '2025-12-11T03:47:39.372Z'
updated_at: '2025-12-11T03:47:39.372Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Observe JSON Response for Disclosures

## Summary

This procedure focuses on analyzing the JSON response from the skills endpoint to identify exposed report titles from other users.

## Description

After accessing the endpoint, the JSON response includes arrays of endorsements with report IDs and titles. Due to the vulnerability, this data is visible to all users applying for the same skill, allowing observation of sensitive information in titles without authorization.

## Requirements

1. Access to the JSON response from /settings/skills
2. JSON parsing tool or manual inspection capability
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Sanitize responses to remove unauthorized data
- Log and alert on queries returning multi-user data

## Objectives

1. Identify disclosed report titles
2. Confirm vulnerability presence
3. Document exposed data

## Instructions

### Step 1: Inspect JSON Structure

**Context**: Parse and review the JSON for endorsement arrays.

Look for fields containing report IDs and titles from multiple users.

> Example structure: {"skills": {"Mobile Applications": {"endorsements": [{"report_id": "123", "title": "Exposed Title"}]}} }

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #json-analysis
- #data-disclosure
