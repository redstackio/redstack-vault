---
id: proc-17512-enumerate-emails
tags:
  - user-enumeration
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:06.455Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate Valid User Emails

## Summary

This procedure identifies valid registered email addresses on a target platform like HackerOne, using prior enumeration vulnerabilities to find emails such as michiel@hackerone.com, setting the stage for targeted password resets.

## Description

In the context of web authentication systems, user enumeration often reveals valid emails through subtle response differences or public data. This step exploits such weaknesses to obtain a target email, enabling subsequent password reset attacks. Expected outcomes include a confirmed valid email, requiring no authentication but relying on external recon.

## Requirements

1. Access to user enumeration endpoint or public profiles
2. Knowledge of target domain (e.g., hackerone.com)
3. Basic web browsing or scripting tools for queries

## Defense

Defensive measures and detection strategies:

- Implement consistent error messages for enumeration attempts
- Rate limit user lookup requests
- Monitor for anomalous query patterns to external directories

## Objectives

1. Discover at least one valid registered email
2. Confirm email validity without alerting the system
3. Prepare for password reset targeting

## Instructions

### Step 1: Query Public or Enumeration Endpoints

**Context**: Use known enumeration vulnerabilities to test emails.

No specific command; manually or via browser/script, test formats like first.last@domain.com against login or profile endpoints.

> Observe response differences (e.g., 'user not found' vs generic error) to confirm validity.

### Step 2: Compile Target List

**Context**: Gather confirmed emails for reset targeting.

Document emails like jobert@hackerone.com.

> Success: List of 1+ valid emails ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-enumeration]]
- [[Reconnaissance]]
