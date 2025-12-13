---
tags:
  - nextcloud
  - id4me
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 00443b40-ca72-4895-888a-f1b06417ed90
created_at: '2025-12-13T09:01:26.585Z'
updated_at: '2025-12-13T09:01:26.585Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Select Custom ID4me Domain

## Summary

This procedure selects a custom domain for ID4me authentication, pointing to a dummy server to simulate the process.

## Description

Using a domain like 'id4me.cloud.wtf' redirects to a test server that fakes authentication, enabling unauthorized registration.

## Requirements

1. Access to ID4me endpoint
2. Dummy ID4me server setup
3. Browser access

## Defense

Defensive measures and detection strategies:

- Restrict allowed ID4me domains
- Log and alert on unusual authentication attempts

## Objectives

1. Simulate authentication provider
2. Proceed to registration
3. Bypass standard login

## Instructions

### Step 1: Choose Domain

**Context**: In the ID4me interface, input the custom domain.

Select 'id4me.cloud.wtf' and submit.

> This triggers redirect to the dummy server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[id4me]]
- [[authentication]]
