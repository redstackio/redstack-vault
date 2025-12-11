---
tags:
  - auth-bypass
  - cve-2007-1036
type: procedure
tools:
  - '[[tools/jexboss]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-path-manipulation]]'
  - '[[commands/curl-directory-traversal]]'
  - '[[commands/jexboss-exploit]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 556e411c-70dd-45d3-b653-d42895fb7af3
created_at: '2025-12-11T06:10:24.891Z'
updated_at: '2025-12-11T06:10:24.891Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Access Unprotected JBoss Web Console

## Summary

This procedure accesses an unprotected JBoss console (CVE-2007-1036) for unauthenticated admin privileges.

## Description

After bypassing the proxy, the /web-console is reached without auth, allowing admin requests and setting up for RCE.

## Requirements

1. Prior proxy bypass
2. Direct access to /web-console
3. Vulnerable JBoss setup

## Defense

Defensive measures and detection strategies:

- Enable authentication on admin consoles
- Restrict internal access

## Objectives

1. Gain admin access without creds
2. Prepare for exploitation
3. Confirm improper access control

## Instructions

### Step 1: Request Console Path

**Context**: Use traversed path to access console.

**Command** ([[commands/curl-directory-traversal]]):
```bash
curl -i "http://subdomain.starbucks.com/josso/%5C../web-console"
```

> Verify no auth required.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/curl-directory-traversal]]

## Tools Used



## Tags

- [[auth-bypass]]
- [[cve-2007-1036]]
