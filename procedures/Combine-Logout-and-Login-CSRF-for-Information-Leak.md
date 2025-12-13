---
tags:
  - csrf
  - xss
  - information-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 38e8ac67-a508-41c1-afb6-66284a82b397
created_at: '2025-12-13T09:01:26.491Z'
updated_at: '2025-12-13T09:01:26.491Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Combine Logout and Login CSRF for Information Leak

## Summary

This procedure chains Logout CSRF with Login CSRF to steal sessions or trigger Self-XSS.

## Description

By logging out the user and forcing a new login, attackers can leak confidential data or execute stored XSS.

## Requirements

1. Prior CSRF setup
2. Stored Self-XSS in target

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to prevent XSS
- Monitor session changes

## Objectives

1. Leak session information
2. Execute malicious scripts
3. Achieve data exfiltration

## Instructions

### Step 1: Chain CSRF Attacks

**Context**: Perform logout then login CSRF.

> Use previously crafted pages to sequence the attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[csrf]]
- [[xss]]
