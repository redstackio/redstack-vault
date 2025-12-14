---
tags:
  - rce
  - php
  - drupal
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.656Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[JavaScript]]'
id: e32b681b-9e33-4192-abe4-e7ef0205c3a8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
---
# Achieve RCE via Admin Session

## Summary

This procedure exploits the admin session to execute arbitrary PHP code using Drupal's callback features, such as module hooks or form submissions, achieving remote code execution.

## Description

With admin privileges, Drupal's flexibility allows triggering PHP callbacks, e.g., via serialized objects in forms or uploaded files. This leads to full server compromise, with cleanup to evade detection.

## Requirements

1. Valid admin session from prior step
2. Knowledge of Drupal admin interfaces (e.g., module configuration)
3. PHP payload for execution (e.g., system commands)

## Defense

Defensive measures and detection strategies:

- Disable unsafe PHP callbacks in Drupal config
- File integrity monitoring on web root
- Audit logs for admin actions and code execution

## Objectives

1. Trigger PHP code execution via admin features
2. Run server commands for persistence or exfil
3. Clean up session to avoid traces

## Instructions

### Step 1: Trigger Callback

**Context**: Use admin access to invoke a vulnerable callback.

Navigate to a form or module page (e.g., /admin/config/development/performance) and submit serialized data like O:8:"stdClass":1:{s:7:"_GET";a:1:{s:3:"cmd";s:2:"id";}} to deserialize and execute.

> Expected: Command output (e.g., uid=33) in response or log.

### Step 2: Cleanup

**Context**: Delete the forged session.

Inject DELETE FROM sessions WHERE sid='fakesid'; via another request or admin interface.

> Expected: Session removed; no evidence left.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[php-execution]]
- [[drupal]]
