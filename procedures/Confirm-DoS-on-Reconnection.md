---
id: p6f7g8h9-i0j1-2345-fghi-6789012345
tags:
  - dos-verification
  - api-failure
  - web
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:28:28.743Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Confirm-DoS-on-Reconnection

## Summary

This procedure attempts to reconnect to the OAuth app after session refresh to confirm the denial of service caused by malformed cookies.

## Description

Final verification step where the injected cookies prevent successful API authorization. Targets the Explore API flow. Prerequisites: Refreshed session with persistent cookies. Expected: Failure in connection, requiring manual cookie deletion.

## Requirements

1. Refreshed session.
2. Created OAuth app.
3. Persistent malicious cookies.

## Defense

Defensive measures and detection strategies:

- Auto-detect and reset anomalous cookies.
- User notifications for auth failures.
- Support for easy cookie management.

## Objectives

1. Attempt API reconnection.
2. Observe authorization failure.
3. Validate DoS impact.

## Instructions

### Step 1: Navigate to Apps

**Context**: Access the dashboard post-refresh.

Go to https://www.tumblr.com/oauth/apps.

> Apps list loads.

### Step 2: Attempt Connection

**Context**: Trigger the vulnerable flow again.

Click 'Explore API' on the app.

> Fails due to malformed cookies; error in authorization.

### Step 3: Validate Recovery

**Context**: Test mitigation.

Manually delete oa-consumer_key and oa_consumer_secret in dev tools, then retry.

> Connection succeeds after deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos-verification
- api-failure
- web

