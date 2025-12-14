---
id: ac-slack-dos-dm-2019
name: >-
  Denial of Service via Uncontrolled Resource Consumption in Slack Direct
  Messages
tags:
  - dos
  - resource-exhaustion
  - slack
  - direct-messages
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Resource-Exhaustion-in-Slack-DMs]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.741Z'
description: >-
  An attack chain exploiting uncontrolled resource consumption in Slack's Direct
  Messages feature to cause denial of service for targeted users by overwhelming
  the messaging system.
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Denial of Service via Uncontrolled Resource Consumption in Slack Direct Messages

Multi-stage attack chain demonstrating a complete attack workflow targeting Slack's Direct Messages feature to induce denial of service through resource exhaustion.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Target Selection] --> B[Resource Exhaustion]
    B --> C[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses native Slack client functionality)

### Target Environment

- Slack Web or Mobile application
- Active Slack workspace with Direct Messages enabled
- Attacker must have access to send messages in the target's DM channel

### Initial Access Requirements

- Valid Slack account with messaging permissions to the target user
- Network access to Slack services
- No prior elevated access needed, but shared workspace membership required

## Detailed Attack Procedures

### Step 1: Trigger Resource Exhaustion
procedure: [[procedures/Trigger-Resource-Exhaustion-in-Slack-DMs]]

**Objective**: Overload the Direct Messages feature by consuming excessive resources, leading to denial of service for the target user.

**Instructions**: Identify a target user in your Slack workspace and initiate a Direct Message conversation. Then, rapidly send a high volume of messages or large payloads (such as attachments) to exhaust server-side resources allocated to the DM session. This leverages the lack of rate limiting or resource caps in the DM functionality as it existed in November 2019.

**Expected Output**: The target user experiences degraded performance or complete inaccessibility to their Direct Messages, with messages failing to load or the interface freezing.

**Success Indicators**:
- Target reports inability to access DMs
- Slack client shows errors or timeouts in the DM thread
- No immediate feedback from Slack on message sending limits

## Attack Chain Summary

### Key Achievements

1. Successfully induced DoS on target user's Direct Messages without specialized tools
2. Exploited a flaw in resource management that affected user experience
3. Demonstrated impact on productivity in collaborative environments like Slack workspaces

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] Application or System Exploitation

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
