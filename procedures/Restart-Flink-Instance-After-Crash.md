---
id: proc-restart-flink
tags:
  - persistence
  - restart
  - flink-recovery
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Implant Internal Image]]'
updated_at: '2025-12-14T17:32:48.419Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Implant Internal Image]]'
---
# Restart-Flink-Instance-After-Crash

## Summary

This procedure recovers the crashed Apache Flink instance by re-running a SQL job in Aiven to restart the service and recreate the exploitable jar file.

## Description

The RCE exploitation crashes the Flink instance due to the gadget's impact. Re-execution of the initial SQL job restarts it and regenerates the jar ID, allowing repeated attacks. This is UI-based in Aiven console. Prerequisites: Access to Aiven after crash confirmation.

## Requirements

1. Aiven console access post-crash
2. Original SQL job details for re-execution
3. Tolerance for brief downtime

## Defense

Defensive measures and detection strategies:

- Alert on Flink crashes and frequent restarts
- Limit job re-execution rates via Aiven policies
- Investigate crash logs for RCE indicators (e.g., JS execution traces)

## Objectives

1. Restore Flink instance functionality
2. Recreate jar for further exploitation
3. Maintain access persistence

## Instructions

### Step 1: Confirm Crash and Access Console

**Context**: Verify downtime and return to Aiven.

No command; check Flink UI for unavailability, then log back into Aiven console.

> Dashboard shows service status as down.

### Step 2: Re-run SQL Job

**Context**: Restart Flink and deploy new jar.

No command; in Aiven interface, re-execute the SQL job to restart instance and create new jar.

> Confirmation of restart; new jar ID generated (e.g., similar to original).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Implant Internal Image]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- persistence
- restart
- flink-recovery
