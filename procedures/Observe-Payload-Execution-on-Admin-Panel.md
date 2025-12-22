---
tags:
  - xss
  - execution
  - collection
  - web
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5346f2ed-1e0c-4c2a-b2c5-c912a27eff44
created_at: '2025-12-13T23:52:50.052Z'
updated_at: '2025-12-13T23:52:50.052Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-Payload-Execution-on-Admin-Panel

## Summary

This procedure covers monitoring and confirming the execution of the stored XSS payload when an administrator views the affected deletion request on admin.acronis.com.

## Description

Following injection, the payload resides in admin-viewable logs. Execution occurs in the admin's browser context, allowing arbitrary JS like session theft. The target is the admin interface; outcomes include proof of compromise and potential data exfiltration.

## Requirements

1. Payload injected from previous step
2. Access to or simulation of admin panel (e.g., via report or controlled env)
3. Attacker server to receive callbacks from payload

## Defense

Defensive measures and detection strategies:

- Sanitize stored data before rendering in admin views
- Use strict CSP headers in admin interfaces
- Monitor for unexpected JS execution or outbound requests from admin sessions

## Objectives

1. Trigger payload via admin interaction
2. Verify JS execution and impact
3. Assess potential for further exploitation

## Instructions

### Step 1: Simulate or Await Admin View

**Context**: Ensure the deletion request appears in admin logs.

Notify or wait for admin to access admin.acronis.com and view pending deletions.

> Payload renders unsanitized, triggering execution.

### Step 2: Confirm Execution

**Context**: Observe effects like alerts or network requests.

Check attacker server logs for incoming data (e.g., stolen cookies) or use a simple alert payload.

> Success: JS runs in admin context, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[Collection]]
- [[web]]
