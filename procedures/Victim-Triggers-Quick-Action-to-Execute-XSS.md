---
tags:
  - xss
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands//add_contacts]]'
  - '[[commands//remove_contacts]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e78e5392-1826-49a9-8ad1-1674a2ff1b65
created_at: '2025-12-11T03:47:49.348Z'
updated_at: '2025-12-11T03:47:49.348Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Victim Triggers Quick Action to Execute XSS

## Summary

This procedure triggers the stored XSS by using quick actions in an issue description, loading malicious contact names.

## Description

Typing /add_contacts or /remove_contacts loads the popup with unescaped names, executing the script.

## Requirements

1. Malicious contact created
2. Victim in issue creation mode

## Defense

Defensive measures and detection strategies:

- Escape HTML in rendered fields
- Browser XSS protection

## Objectives

1. Execute arbitrary JavaScript
2. Achieve session hijacking potential

## Instructions

### Step 1: Type Quick Action

**Context**: In description, type [[commands//add_contacts]] or [[commands//remove_contacts]].

> Press enter to trigger popup.

### Step 2: Load Contact List

**Context**: Popup loads contacts, executing payload.

> Observe script execution (e.g., alert).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands//add_contacts]]
- [[commands//remove_contacts]]

## Tools Used



## Tags

- #xss
- #trigger
