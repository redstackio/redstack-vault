---
id: proc-uuid-3
tags:
  - dos
  - client-side
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.441Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe-Client-Side-DoS-Effects

## Summary

This procedure tests and verifies the denial of service impacts on client-side components after setting a long username, including app crashes and interface hangs.

## Description

Once the long name is set, accessing account features like contacts or sending messages causes UI rendering to fail due to memory overload from processing the oversized string. This affects the Android app (crashes) and web interfaces (slowdowns up to 40 minutes). The procedure involves targeted interactions to observe effects on self and other users.

## Requirements

1. hey.com account with long name set
2. Android device with hey.com app installed
3. Another test account for recipient effects

## Defense

Defensive measures and detection strategies:

- Client-side truncation of long names in rendering
- Crash reporting and anomaly detection in app logs

## Objectives

1. Confirm app and interface disruptions
2. Measure impact duration and severity
3. Validate DoS on multiple clients

## Instructions

### Step 1: Test Android App

**Context**: Load the account in the mobile app to trigger crash.

Open hey.com app and navigate to contacts or messages.

> App crashes on name render; restart required.

### Step 2: Test Web and Recipient Effects

**Context**: Send message and observe slowdowns.

Send a message to another user; check inbox, trash, contacts in web/app.

> Interfaces hang for extended periods (e.g., 40 minutes) when displaying the name.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- client-side
