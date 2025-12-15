---
id: proc-837328-collaboration-setup
tags:
  - collaboration
  - websocket
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.012Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Establish-Quantopian-Collaboration-Session

## Summary

This procedure sets up a shared collaboration session on Quantopian's algorithm building feature, establishing a WebSocket connection that allows synchronized updates across participants, prerequisite for manipulating shared HTML elements.

## Description

Quantopian's collaboration feature uses WebSockets for real-time editing of algorithm code and forms. By joining the same session as the victim, the attacker gains the ability to broadcast events that affect all clients' DOM, exploiting the lack of validation. This targets web-based environments with active user sessions and requires social engineering to lure the victim into collaborating.

## Requirements

1. Valid Quantopian account with access to algorithm creation
2. Target victim account that can be invited to collaborate
3. Browser supporting WebSockets (e.g., Chrome, Firefox)

## Defense

Defensive measures and detection strategies:

- Implement WebSocket message validation and sender authentication in collaboration libraries
- Monitor for anomalous DOM updates in shared sessions
- Educate users on risks of collaborating with untrusted parties

## Objectives

1. Secure shared WebSocket room access with victim
2. Verify synchronization of interface elements
3. Prepare for payload injection without alerting victim

## Instructions

### Step 1: Create or Join Algorithm Session

**Context**: Initiate a collaboration room to establish the shared WebSocket connection.

Log in to https://quantopian.com, navigate to algorithm creation, and enable collaboration. Invite the target user via email or link.

**Expected Output**: Room ID generated (e.g., 5ce6e50b298f7c6e0acb68c6), visible in URL or network tab.

### Step 2: Verify Connection

**Context**: Confirm both parties are connected and elements sync.

Send a benign update (e.g., edit algorithm code) and observe if it appears in the victim's view.

**Expected Output**: Real-time sync confirmed; WebSocket frames visible in DevTools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[collaboration]]
- [[websocket]]
- [[initial-access]]
