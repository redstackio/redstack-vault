---
tags:
  - ssti
  - smarty
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/smarty-version-check]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 95e2a728-9c9c-4272-9182-46257e8a0f08
created_at: '2025-12-13T09:01:17.035Z'
updated_at: '2025-12-13T09:01:17.035Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm Smarty Version

## Summary

This procedure confirms the version of the Smarty templating engine by injecting a version-retrieval payload into profile fields and checking the output in the invitation email.

## Description

After initial SSTI confirmation, this step verifies the Smarty version to assess exploitability for PHP code execution. The payload is injected similarly, and the email reveals the version string if successful.

## Requirements

1. Confirmed SSTI from prior testing
2. Profile editing and invitation access
3. Secondary email for receiving output

## Defense

Defensive measures and detection strategies:

- Disable or restrict Smarty's version exposure in templates
- Log and alert on template variable accesses

## Objectives

1. Retrieve Smarty version
2. Confirm engine for escalation
3. Proceed to code execution testing

## Instructions

### Step 1: Inject Version Payload

**Context**: Update profile fields and trigger email to reveal version.

**Command** ([[commands/smarty-version-check]]):
```bash
{$smarty.version}
```

> Set profile fields to this payload; invite user; observe Smarty version in email.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/smarty-version-check]]

## Tools Used



## Tags

- [[ssti]]
- [[smarty]]
