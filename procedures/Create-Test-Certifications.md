---
id: 12ae6c6b-9c27-4ee0-a4a4-938087d51939
name: Create Test Certifications
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.726Z'
updated_at: '2025-12-11T03:47:47.726Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - setup
  - web
  - hackerone
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Proxy]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Create Test Certifications

## Summary

This procedure creates licenses and certifications in HackerOne user accounts for testing deletion vulnerabilities.

## Description

Using the platform's interface, add certifications to each authenticated user's profile. This sets up testable assets for IDOR exploitation, targeting the GraphQL backend. Expected outcomes include visible certifications in profiles.

## Requirements

1. Authenticated HackerOne sessions.
2. Access to profile editing features.
3. Details for fictional or real certifications.

## Defense

Defensive measures and detection strategies:

- Rate limit profile edits to detect automated testing.
- Log certification creation for anomaly detection.

## Objectives

1. Populate profiles with deletable assets.
2. Prepare for exploitation testing.
3. Verify creation functionality.

## Instructions

### Step 1: Navigate to Profile Settings

**Context**: Access the certification management section.

In each browser, go to the user's profile and select the certifications tab.

> Ensure you are in edit mode.

### Step 2: Add Certifications

**Context**: Input certification details.

Fill in fields like name, organization, issue date, expiration date, ID, and URL, then save.

> Repeat for both accounts to create targetable items.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- setup
- web
- hackerone
