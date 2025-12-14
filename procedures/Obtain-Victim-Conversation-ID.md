---
id: proc-dust-id-obtain-001
tags:
  - enumeration
  - conversation-discovery
  - dust-tt
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:26.901Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain-Victim-Conversation-ID

## Summary

This procedure involves acquiring or enumerating the conversation ID of another user's private thread in a Dust.tt workspace, setting up targets for unauthorized access exploitation.

## Description

Conversation IDs in Dust.tt are string identifiers (e.g., conv_abc123) tied to workspaces. Attackers can obtain them via social engineering, URL leakage, or API enumeration by monitoring network traffic during workspace interactions. No direct enumeration endpoint exists, but IDs are guessable or observable in shared contexts.

## Requirements

1. Authenticated session in the target workspace
2. Access to browser developer tools or proxy for traffic inspection
3. Knowledge of potential victims (e.g., admin users)

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize conversation IDs to hinder guessing
- Log and alert on unusual API access patterns to non-owned resources
- Restrict visibility of IDs in client-side code

## Objectives

1. Identify a valid conversation ID owned by another user
2. Confirm the ID belongs to the same workspace
3. Prepare for exploitation without triggering client-side errors

## Instructions

### Step 1: Monitor Network Traffic

**Context**: Observe API calls during normal workspace usage to capture IDs.

While authenticated, interact with conversations (e.g., create or view your own) and use browser dev tools (Network tab) to filter for /conversations/ requests.

> Expected output: Requests revealing sId fields like "conv_abc123" in responses.

### Step 2: Enumerate or Guess IDs

**Context**: If direct observation fails, attempt sequential guessing or use prior knowledge.

Test potential IDs in API calls (e.g., via curl) or infer from timestamps/user patterns. For example, admin conversations may follow predictable naming.

> Expected output: Valid ID that returns data in a read attempt (tested in subsequent procedures).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[enumeration]]
- [[dust-tt]]
