---
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands//add_contacts]]'
  - '[[commands//remove_contacts]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e0ed1465-7564-4879-aaa3-da6c459c1ac8
created_at: '2025-12-11T03:47:49.489Z'
updated_at: '2025-12-11T03:47:49.489Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Create Malicious Contact with XSS Payload

## Summary

This procedure injects an XSS payload into GitLab Customer Relations contact fields for later execution.

## Description

The first and last name fields are not properly escaped, allowing stored XSS. Payload like '<script>alert(document.domain)</script>' is used.

## Requirements

1. Customer Relations enabled in group
2. Permissions to create contacts

## Defense

Defensive measures and detection strategies:

- Sanitize input in contact fields
- Monitor for script tags in database entries

## Objectives

1. Store malicious script
2. Set up for trigger via quick actions

## Instructions

### Step 1: Create Contact

**Context**: Navigate to Customer Relations and add new contact.

> Set First name and Last name to '<script>alert(document.domain)</script>'.

### Step 2: Save Contact

**Context**: Provide email and save.

> Verify contact is listed with payload intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #xss
- #payload-injection
