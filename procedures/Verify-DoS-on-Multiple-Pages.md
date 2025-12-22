---
id: proc-713407-verify-dos
tags:
  - verify
  - dos
  - impact
  - pages
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.285Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify-DoS-on-Multiple-Pages

## Summary

This procedure tests the scope of the DoS by accessing various HackerOne pages that render the affected profile picture, confirming application-wide impact.

## Description

Post-upload, pages like /hacktivity, /thanks, and directory listings attempt to display the malicious image, triggering the same ActiveStorage exception. This verifies the vulnerability affects multiple user-facing sections, denying service to all viewers. Targets web endpoints on https://hackerone.com.

## Requirements

1. Successful malicious upload completed
2. Access to affected user's profile pages
3. Browser session active

## Defense

Defensive measures and detection strategies:

- Isolate faulty attachments and prevent rendering
- Alert on repeated exceptions from image processing

## Objectives

1. Identify impacted pages
2. Demonstrate broad DoS effect
3. Quantify application disruption

## Instructions

### Step 1: Navigate to Hacktivity Page

**Context**: Test a key user section.

No command required; visit https://hackerone.com/hacktivity or similar.

> Page fails to load with 500 error due to profile image render.

### Step 2: Check Thanks and Directory

**Context**: Verify propagation to other areas.

No command required; browse to /thanks or directory listings.

> Consistent errors confirm wide impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verify
- dos
- impact
- pages
