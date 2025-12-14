---
id: proc-slack-dos-dm-exhaust
name: Trigger Resource Exhaustion in Slack DMs
tags:
  - dos
  - resource-exhaustion
  - slack
  - direct-messages
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.738Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Trigger Resource Exhaustion in Slack DMs

## Summary

This procedure exploits uncontrolled resource consumption in Slack's Direct Messages feature to cause a denial of service for a targeted user by overwhelming the system's handling of incoming messages or attachments, preventing access to DMs as reported in a November 2019 vulnerability.

## Description

The vulnerability stems from insufficient controls on resource usage within Slack's direct messaging functionality, allowing an attacker with messaging access to flood the target with resource-intensive payloads. This leads to server-side exhaustion, impacting the target's ability to view or interact with DMs. Discovered and reported via HackerOne, Slack patched this within weeks without user intervention. The attack requires only basic access to the target's workspace and exploits the absence of robust rate limiting or payload size restrictions at the time.

## Requirements

1. Valid Slack account in the same workspace as the target
2. Ability to initiate or participate in a Direct Message with the target
3. Access to Slack Web or Mobile client (no elevated privileges needed)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on message sending in DMs
- Monitor for unusual spikes in message volume or attachment sizes per user/session
- Enforce payload size limits for uploads in messaging features
- Use anomaly detection to flag rapid messaging patterns indicative of DoS attempts

## Objectives

1. Cause denial of service by exhausting resources allocated to the target's DM session
2. Disrupt target user's access to direct communications
3. Demonstrate impact of poor resource controls in real-time collaboration tools

## Instructions

### Step 1: Establish DM Channel

**Context**: Begin by ensuring a Direct Message channel exists with the target to enable message delivery.

Open the Slack client (Web or Mobile), search for the target user, and start a new DM conversation if none exists. Confirm the channel is active by sending a test message.

> Expected output: Message delivers successfully, and target receives notification (if online).

### Step 2: Initiate Resource Exhaustion

**Context**: Flood the DM channel with high-volume or large-payload messages to trigger uncontrolled resource consumption on Slack's backend.

Using the Slack interface, rapidly send multiple messages in quick succession. To amplify impact, attach large files (e.g., images or documents up to Slack's then-limit of 1GB per file) repeatedly. Aim for 100+ messages or several large attachments within a short period (e.g., 1-2 minutes) to overwhelm processing.

> Expected output: Messages appear to send without error on the attacker's side, but the target's client begins to lag, fail to load new messages, or display errors like "Something went wrong" when accessing the DM.

### Step 3: Verify DoS Impact

**Context**: Confirm the attack's success by observing or querying the target's access to DMs.

Monitor the target's response or use a secondary account to check if the DM thread is responsive. Success is indicated if the target cannot retrieve or send messages in the thread for an extended period.

> Expected output: Target reports inaccessibility; Slack may temporarily throttle but not prevent the exhaustion in vulnerable versions.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] Application or System Exploitation

## Commands Used


## Tools Used


## Tags

- dos
- resource-exhaustion
- slack
- direct-messages
