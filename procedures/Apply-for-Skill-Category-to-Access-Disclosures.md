---
tags:
  - skill-application
  - access-trigger
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 57affb66-e62b-479e-88c0-7b860c18ab2d
created_at: '2025-12-11T03:47:39.370Z'
updated_at: '2025-12-11T03:47:39.370Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
---
# Apply for Skill Category to Access Disclosures

## Summary

This procedure triggers access to category-specific disclosures by applying for a skill endorsement on HackerOne.

## Description

To view disclosures for a specific skill category, such as Mobile, the user must submit an application. This action exposes the report titles submitted as proof by other users in that category, exploiting the query flaw.

## Requirements

1. HackerOne account with eligibility to apply for skills
2. Access to the skills interface
3. Target skill category identified

## Defense

Defensive measures and detection strategies:

- Restrict visibility of endorsements to submitters only
- Audit skill application logs for anomalous behavior

## Objectives

1. Gain access to category disclosures
2. Expose additional report titles
3. Validate full scope of vulnerability

## Instructions

### Step 1: Submit Skill Application

**Context**: Use the HackerOne interface to apply for the desired skill category.

Navigate to the skills page and submit a report as proof for the category.

> Upon submission, refresh the endpoint to view exposed titles.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #skill-application
- #access-trigger
