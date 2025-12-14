---
tags:
  - replay
  - bypass
  - apns-registration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:29:09.562Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a334fd11-2a7b-4054-b280-87666cfc55a1
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Cloud Instance Metadata API]]'
---
# Replay-Registration-Request-with-Unprivileged-Account

## Summary

This procedure resends the captured POST request to `/admin/mobile_devices.json` using a downgraded account, exploiting the missing permission check to register the device and gain unauthorized notifications.

## Description

With permissions revoked, the UI blocks registration, but the API does not validate 'Settings' access. Replaying the request (with original APNS token and session) succeeds, allowing the unprivileged user to receive order details via push notifications, exposing sensitive customer data.

## Requirements

1. Captured request from interception
2. Active session with unprivileged account
3. Proxy tool for replay

## Defense

Defensive measures and detection strategies:

- Add server-side permission checks to all API endpoints
- Monitor for anomalous request replays or permission mismatches in logs
- Rate-limit device registration attempts

## Objectives

1. Successfully register device without 'Settings' permission
2. Confirm bypass via notification receipt
3. Expose sensitive order data

## Instructions

### Step 1: Prepare Replay Environment

**Context**: Ensure unprivileged session is active.

Log in with the downgraded account in the app or web, confirming UI access denial for settings.

### Step 2: Execute Replay

**Context**: Send the modified request.

In Burp Suite Repeater, paste the intercepted POST request, update any session cookies to match the unprivileged account, and send to `/admin/mobile_devices.json`.

**Expected Output**: 200 OK response with registered device confirmation; notifications start arriving on the device.

Verify by creating a test order and checking for push alert with details.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Cloud Instance Metadata API]] Credentials from Password Stores (reusing API session/token)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- replay
- authorization-bypass
- shopify-api
