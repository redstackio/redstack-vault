---
id: proc-embed-homeactivity-intent
tags:
  - android
  - intent-embedding
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/embed-intent-in-homeactivity]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
updated_at: '2025-12-14T17:24:44.612Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
---
# Embed-Intent-into-HomeActivity-and-Launch

## Summary

This procedure embeds the crafted inner intent into an outer intent targeting the exported HomeActivity, preparing the full exploit chain for launch.

## Description

In the Android intent system, this wraps the malicious inner intent as 'extra_deep_link_intent' in an outer Intent for com.Slack.ui.HomeActivity. When launched, HomeActivity will process and start the embedded intent. Prerequisites: Inner intent from previous procedure. Expected outcomes: Outer intent that triggers the vulnerability upon startActivity.

## Requirements

1. Pre-crafted inner Intent object
2. Access to startActivity in malicious app
3. Slack app installed

## Defense

Defensive measures and detection strategies:

- Avoid exporting sensitive activities or use signature permissions
- Log and audit incoming intents for extras in HomeActivity
- Implement intent verification to prevent embedding

## Objectives

1. Create outer intent for exported HomeActivity
2. Embed inner intent securely for processing
3. Set up for seamless exploit execution

## Instructions

### Step 1: Create Outer Intent

**Context**: Initialize the outer intent targeting HomeActivity.

**Command** ([[commands/embed-intent-in-homeactivity]]):
```java
Intent start = new Intent(); start.setClassName("com.Slack","com.Slack.ui.HomeActivity"); start.putExtra("extra_deep_link_intent", next);
```

> This sets the class to the exported HomeActivity and embeds the inner intent (next) as the extra. Expected output: Outer Intent with payload ready for launch.

### Step 2: Prepare for Launch

**Context**: Ensure the outer intent is valid before starting.

No command; validate in code.

> Check that putExtra succeeded and class name is correct. Expected output: Confirmed embedding.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Sub-Techniques


## Commands Used

- [[commands/embed-intent-in-homeactivity]]

## Tools Used


## Tags

- [[android]]
- [[intent-embedding]]
