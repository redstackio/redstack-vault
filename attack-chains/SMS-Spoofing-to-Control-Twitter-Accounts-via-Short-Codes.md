---
tags:
  - sms-spoofing
  - account-takeover
  - unauthenticated-access
  - twitter
  - business-logic
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Mobile (SMS)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Spoof-SMS-to-Execute-Twitter-Commands]]'
step_count: 1
techniques:
  - '[[T1566.004]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.165Z'
description: >-
  Exploit Twitter's SMS command system by spoofing the victim's phone number to
  send unauthenticated commands to short codes, enabling full account control
  including tweeting, DMing, and 2FA removal.
skill_level: intermediate
impact_level: high
id: 00bc87e3-b084-48ab-84c2-98db3756148d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[T1566.004]]'
  - '[[Exploit Public-Facing Application]]'
---
# SMS Spoofing to Control Twitter Accounts via Short Codes

Multi-stage attack chain demonstrating a complete attack workflow exploiting Twitter's SMS command system.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Spoof SMS] --> B[Execution: Send Commands to Short Code]
    B --> C[Objective: Account Control]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- SMS spoofing service or tool (e.g., online SMS spoofing platforms)

### Target Environment

- Twitter account with SMS enabled
- Access to geographical short codes (e.g., UK, India, Australia carriers)
- Knowledge of Twitter SMS commands from help pages

### Initial Access Requirements

- No credentials needed; relies on spoofing
- Network access to SMS gateways
- No prior access to target account

## Detailed Attack Procedures

### Step 1: Spoof SMS and Send Commands
procedure: [[procedures/Spoof-SMS-to-Execute-Twitter-Commands]]

**Objective**: Impersonate the target's phone number to send SMS commands to Twitter's short codes, executing actions like tweeting, DMing, or removing 2FA without authentication.

**Instructions**: Use an SMS spoofing service to craft and send messages appearing from the target's phone number to Twitter's geographical short code (e.g., for UK carriers). Reference Twitter's documented SMS commands (e.g., 'TWEET message' to post a tweet). No specific bash commands are required; the action is performed via SMS interface.

**Expected Output**: Successful execution of the command on the target account, such as a new tweet posted or 2FA disabled, verifiable via the Twitter web interface.

**Success Indicators**:
- Action performed on target account (e.g., tweet appears)
- No authentication prompts or errors from Twitter's SMS system

## Attack Chain Summary

### Key Achievements

1. Unauthenticated control over SMS-enabled Twitter accounts
2. Ability to perform critical actions like 2FA removal and DMing
3. Potential for mass abuse affecting millions in regions like UK, India, Australia

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1566.004]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
