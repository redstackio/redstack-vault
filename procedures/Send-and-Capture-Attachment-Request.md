---
tags:
  - attachment-upload
  - traffic-capture
  - android
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.775Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7080c7ce-3cbf-466a-bed5-0ff2623ed7c1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-and-Capture-Attachment-Request

## Summary

This procedure involves sending an attachment via the BCM Messenger app while capturing the resulting HTTP requests to identify generated attachment IDs for further exploitation.

## Description

Using two app accounts, send a test attachment (e.g., photo) from victim to attacker, proxying traffic through Burp Suite. The upload generates a POST request and a numeric ID (e.g., 938540538), which is predictable and used in the download endpoint. This step confirms the app's attachment flow and captures baseline requests for modification.

## Requirements

1. Two BCM Messenger accounts (attacker and victim)
2. Proxy setup from previous procedure active
3. Android device with app permissions for media access
4. Stable network connection to the server (ameim.bs2dl.yy.com)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on attachment uploads to detect anomalous patterns
- Log and monitor upload requests for unusual IP or device fingerprints
- Use non-predictable UUIDs instead of sequential numeric IDs

## Objectives

1. Generate a valid attachment ID through normal app usage
2. Capture the full request/response cycle in Burp
3. Verify ID format for predictability (numeric, possibly epoch-based)

## Instructions

### Step 1: Prepare Accounts

**Context**: Ensure accounts are set up for interaction.

Log in to victim and attacker accounts on separate devices or sessions.

> No command; app login. Expected: Both accounts active.

### Step 2: Send Attachment

**Context**: Trigger the upload to generate traffic.

In the app, select and send an attachment from victim to attacker chat.

> App action. Expected: POST request to upload endpoint in Burp, response with ID 938540538.

### Step 3: Review Capture

**Context**: Confirm ID extraction.

In Burp Proxy, inspect the response for the attachment ID.

> GUI review. Expected: Numeric ID noted for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[attachment-upload]]
- [[traffic-capture]]
