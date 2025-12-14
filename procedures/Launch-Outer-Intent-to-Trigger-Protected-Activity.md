---
id: proc-launch-outer-intent
tags:
  - android
  - intent-launch
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/start-activity-exploit]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:44.608Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Launch-Outer-Intent-to-Trigger-Protected-Activity

## Summary

This procedure launches the outer intent from a malicious app, causing HomeActivity to resume and execute the embedded deeplinkIntent, thereby accessing the protected activity.

## Description

The attack executes in a malicious Android app context, calling startActivity on the outer intent. HomeActivity's onResume triggers handleIntentExtras, starting the inner intent without validation. Prerequisites: Prepared outer intent. Expected outcomes: Protected activity launches with attacker-controlled parameters, e.g., WebView loading malicious URL.

## Requirements

1. Malicious app with startActivity permission
2. Outer intent from embedding procedure
3. Device with Slack

## Defense

Defensive measures and detection strategies:

- Use PendingIntent or explicit intents only
- Monitor app switches and intent logs for anomalies
- Employ app sandboxing and inter-app communication restrictions

## Objectives

1. Trigger the intent chain execution
2. Bypass protections to reach protected components
3. Achieve unauthorized actions like content loading

## Instructions

### Step 1: Execute Start Activity

**Context**: Launch the outer intent to initiate the exploit.

**Command** ([[commands/start-activity-exploit]]):
```java
startActivity(start);
```

> This calls startActivity on the outer intent, resuming HomeActivity and processing the extra to start the embedded intent. Expected output: Protected activity opens, e.g., WebView with arbitrary URL.

### Step 2: Validate Execution

**Context**: Confirm the protected activity triggered.

No command; observe app behavior.

> Watch for WebView or other activity launch without user intent. Expected output: Successful bypass and action execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/start-activity-exploit]]

## Tools Used


## Tags

- [[android]]
- [[intent-launch]]
- [[exploitation]]
