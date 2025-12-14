---
id: proc-access-multistream-1070510
tags:
  - multistreaming
  - stream-key-exposure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.341Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Multistreaming-Settings

## Summary

This procedure accesses the Streamlabs multistreaming settings page using the API bypass to reveal Prime-only RTMP URLs and stream keys, which are hidden for non-subscribers.

## Description

The multistreaming feature at https://streamlabs.com/dashboard#/multistream/settings provides URLs and keys for broadcasting to multiple platforms, restricted to Prime users. Tampering with the subscription API unlocks this, exposing sensitive configuration data that could enable unauthorized streaming or further attacks.

## Requirements

1. Active Burp proxy with rules applied
2. Logged-in session
3. Basic understanding of RTMP for validation

## Defense

Defensive measures and detection strategies:

- Regenerate stream keys on access and log usage
- Require server-side auth tokens for RTMP endpoints
- Detect proxy tampering via response time anomalies or TLS fingerprinting

## Objectives

1. Expose hidden multistreaming UI
2. Retrieve RTMP URL and stream key
3. Demonstrate privilege escalation to premium tools

## Instructions

### Step 1: Navigate to Settings

**Context**: Load the page dependent on Prime status.

In the proxied browser, go to https://streamlabs.com/dashboard#/multistream/settings.

**Expected Output**: Page loads fully, showing configuration options.

### Step 2: View RTMP Details

**Context**: Inspect the now-visible stream parameters.

Look for fields displaying RTMP URL (e.g., rtmp://example.com/live) and stream key.

**Expected Output**: Sensitive credentials displayed, normally redacted.

### Step 3: Validate Access

**Context**: Confirm usability by testing the key (optional, for PoC).

Copy the key and attempt a basic RTMP connection using a tool like ffmpeg.

**Expected Output**: Successful stream setup, proving bypass efficacy.

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

- [[multistreaming]]
- [[stream-key-exposure]]
