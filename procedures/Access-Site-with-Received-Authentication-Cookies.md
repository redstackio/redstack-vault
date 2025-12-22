---
tags:
  - session-hijacking
  - access
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 1ed3c5f9-8078-4141-a27b-ba36283c530f
created_at: '2025-12-11T03:47:39.223Z'
updated_at: '2025-12-11T03:47:39.223Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---
# Access Site with Received Authentication Cookies

## Summary

This procedure uses the authentication cookies obtained from the exploit to access the WordPress site as a logged-in user, potentially with admin privileges.

## Description

Cookies are copied to a browser or tool to interact with the site, allowing admin dashboard access by guessing roles or usernames.

## Requirements

1. Authentication cookies from previous step
2. Web browser or HTTP client
3. Target site URL

## Defense

Defensive measures and detection strategies:

- Implement session monitoring for anomalies
- Use multi-factor authentication

## Objectives

1. Impersonate user
2. Access admin features
3. Escalate privileges

## Instructions

### Step 1: Import Cookies

**Context**: Load cookies into a browser to access the site.

Copy the Set-Cookie values and use them to log in, gaining admin privileges.

> Interact with the site to confirm access.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

## Commands Used

## Tools Used

## Tags

- #session-hijacking
- #access
