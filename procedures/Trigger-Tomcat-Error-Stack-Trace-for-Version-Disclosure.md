---
tags:
  - info-disclosure
  - error-trigger
type: procedure
tools:
  - '[[tools/jexboss]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-path-manipulation]]'
  - '[[commands/curl-directory-traversal]]'
  - '[[commands/jexboss-exploit]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 643de5a6-7d99-40a9-9a67-58e233de3bf6
created_at: '2025-12-11T06:10:24.949Z'
updated_at: '2025-12-11T06:10:24.949Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1595]]'
---
# Trigger Tomcat Error Stack Trace for Version Disclosure

## Summary

This procedure manipulates URL paths to trigger server errors, revealing version information for targeted exploitation.

## Description

By requesting invalid paths on the Tomcat server, a stack trace is exposed, disclosing version 5.5.20, which is known to be vulnerable. This aids in selecting appropriate exploits.

## Requirements

1. HTTP access to the target
2. Ability to send crafted requests
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Configure servers to suppress detailed error messages
- Monitor for anomalous request patterns

## Objectives

1. Disclose server version
2. Confirm vulnerability presence
3. Guide exploit selection

## Instructions

### Step 1: Manipulate Paths to Trigger Error

**Context**: Send invalid path to cause stack trace.

**Command** ([[commands/curl-path-manipulation]]):
```bash
curl -i "http://subdomain.starbucks.com/invalid/path/to/cause/error"
```

> Parse response for Tomcat version.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques



## Commands Used

- [[commands/curl-path-manipulation]]

## Tools Used



## Tags

- [[info-disclosure]]
- [[error-trigger]]
