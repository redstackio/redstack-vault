---
tags:
  - burp-suite
  - json-conversion
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 917f412f-cfdd-4575-bd08-ccdbb69b99ca
created_at: '2025-12-11T06:10:31.102Z'
updated_at: '2025-12-11T06:10:31.102Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Convert Request to JSON Format

## Summary

This procedure converts the intercepted HTTP request to JSON format using a Burp Suite extension, facilitating payload manipulation for the GitLab exploit.

## Description

With the request intercepted, right-click in the HTTP Editor and use the Content-Type Converter extension to change the content type to JSON. This allows treating parameters like 'email' as arrays. Applicable to web vulnerability testing in GitLab environments.

## Requirements

1. Burp Suite with Content-Type Converter extension installed
2. Intercepted request in Burp
3. Extension accessible via menu

## Defense

Defensive measures and detection strategies:

- Validate content types on server-side
- Log unusual request formats

## Objectives

1. Change request format to JSON
2. Enable array injection
3. Advance exploitation

## Instructions

### Step 1: Use Extension

**Context**: In the intercepted request, right-click and select Extensions > Content-Type Converter > Convert to JSON.

> Confirm the payload is now in JSON format.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Content-Type-Converter]]

## Tags

- burp-suite
- json-conversion
