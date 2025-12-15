---
id: proc-trigger-graceful-restart
tags:
  - apache
  - graceful-restart
  - root-esc
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/apache2ctl-graceful]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:47.274Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger Graceful Restart to Execute Arbitrary Code as Root

## Summary

This procedure awaits or manually triggers Apache's graceful restart (via logrotate or apache2ctl), causing make_child() to perform an OOB read on the sprayed fake bucket, calling the controlled child_init() as root before dropping privileges.

## Description

During graceful restart, old workers receive SIGUSR1 and exit; new ones spawn via make_child() in prefork.c (L691), accessing all_buckets[process_score->bucket] without bounds check. This leads to apr_proc_mutex_child_init() on the fake mutex, executing the hijacked function as root. Triggered daily by logrotate at 6:25AM or manually.

## Requirements

1. Fake structures and sprayed buckets in place
2. Access to trigger apache2ctl (or wait for logrotate)
3. Controlled pDestructor string for payload (e.g., system('/bin/sh'))

## Defense

Defensive measures and detection strategies:

- Upgrade Apache to 2.4.39+ with bucket bounds checking
- Disable graceful restarts or monitor logrotate
- Use privilege separation (e.g., no root restarts)

## Objectives

1. Initiate restart to trigger OOB access
2. Execute arbitrary code via child_init chain
3. Achieve root shell from www-data

## Instructions

### Step 1: Await or Trigger Restart

**Context**: Wait for logrotate-induced restart or manual trigger.

**Command** ([[commands/apache2ctl-graceful]]):
```bash
apache2ctl graceful
```

> This kills old workers via SIGUSR1, spawns new via make_child(), leading to OOB read and root call.

### Step 2: Validate Escalation

**Context**: Post-restart, check for root execution (e.g., via controlled system() payload).

Monitor with `ps aux | grep apache` or execute id in payload.

> Expected: New processes as root briefly, payload executes (e.g., root shell).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

-

## Commands Used

- [[commands/apache2ctl-graceful]]

## Tools Used

-

## Tags

- restart-trigger
- oob-execution
