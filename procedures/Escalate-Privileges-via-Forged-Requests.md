---
tags:
  - privilege-escalation
  - request-forgery
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 22c8c1a2-927e-4752-b0c1-17f6f0155430
created_at: '2025-12-11T03:47:39.286Z'
updated_at: '2025-12-11T03:47:39.286Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---
# Escalate Privileges via Forged Requests

## Summary

This procedure uses bypassed CSRF protections to forge requests on behalf of a logged-in user, leading to privilege escalation in the GitHub Enterprise Server management console.

## Description

Once CSRF is bypassed via path traversal, attackers can submit forged requests to elevate privileges, such as granting admin access. This exploits the vulnerability in versions prior to 3.5 and requires an active session. The result is unauthorized control over the server.

## Requirements

1. Successful CSRF bypass
2. Crafted privilege escalation payloads
3. Access to management console endpoints

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous privilege changes
- Use role-based access controls and logging

## Objectives

1. Forge requests for escalation
2. Achieve higher privileges
3. Gain control over the server

## Instructions

### Step 1: Identify Escalation Endpoints

**Context**: Locate management console endpoints that handle privilege modifications.

Review API or console paths for admin functions.

### Step 2: Forge and Submit Request

**Context**: Craft and send a request to escalate privileges using the bypassed session.

Use HTTP methods to modify user roles or permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[Privilege Escalation]]
- #request-forgery
