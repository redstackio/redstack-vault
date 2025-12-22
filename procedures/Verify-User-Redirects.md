---
tags:
  - verification
  - redirect
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 47aa7cf9-f6bc-4d46-8a04-b874391e28ad
created_at: '2025-12-13T09:01:17.562Z'
updated_at: '2025-12-13T09:01:17.562Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify User Redirects

## Summary

This procedure verifies that users are successfully redirected to the attacker's domain by checking server connections.

## Description

After exploitation, incoming connections on the attacker's server confirm the redirect chain, demonstrating potential for mass user compromise in a production scenario.

## Requirements

1. Redirect server running on attacker domain
2. Prior steps completed
3. Logging enabled on port 8443

## Defense

Defensive measures and detection strategies:

- Validate all redirect locations
- Use secure coding to prevent header manipulation

## Objectives

1. Confirm incoming redirected connections
2. Validate end-to-end exploitation
3. Assess impact potential

## Instructions

### Step 1: Check Server Logs

**Context**: Review logs for connections on port 8443.

> Monitor the attacker's server at pqp.mx:8443 for incoming connections from the target redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[verification]]
- [[redirect]]
