---
tags:
  - data-exfiltration
  - info-leak
  - client-fetch
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile (iOS)
  - Mobile (Android)
  - iPad
  - Smart TV
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:25:18.062Z'
sub_techniques: []
id: a0c05617-f50c-4af2-b274-8d10ad9fa88d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Send-Modified-Message-and-Capture-Victim-Data

## Summary

This procedure finalizes the attack by sending the tampered message and monitoring the attacker's server for leaked victim information when the client fetches the embedded URL.

## Description

Upon sending, the message appears as a normal GIF in LinkedIn. When the victim opens the conversation, their client automatically fetches the URL to render the 'media', sending a request to the attacker's Burp Collaborator. This leaks headers with IP, User-Agent (revealing OS, browser, device), device ID, phone model (more on iOS), and time zone. Impact varies by platform, with iOS leaking the most.

## Requirements

1. Modified message successfully sent from previous step
2. Burp Collaborator poll or web interface active
3. Victim interaction (opening message)

## Defense

Defensive measures and detection strategies:

- Block or proxy external media fetches in client apps
- Warn users about unknown senders or unusual media
- Analyze client logs for unexpected external requests

## Objectives

1. Trigger victim client to make request to malicious URL
2. Collect and analyze leaked personal and device data
3. Assess platform-specific disclosure levels

## Instructions

### Step 1: Deliver Message

**Context**: Ensure the tampered message reaches the victim.

In LinkedIn:

1. Confirm the message is sent and visible in the conversation
2. Optionally, use social engineering to prompt victim to open

> Expected output: Message queued or delivered in LinkedIn UI.

### Step 2: Monitor for Leak

**Context**: Watch Collaborator for incoming data.

In Burp Collaborator:

1. Access the Collaborator server dashboard
2. Wait for victim to open message (may take seconds to minutes)
3. Review HTTP request details: IP from source, User-Agent header, custom headers for device info

> Expected output: Request log showing leaked data; e.g., User-Agent: "LinkedIn-iOS/10.0 (iPhone14,5; iOS 16.0)" revealing model and OS.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Client Configurations]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[data-exfiltration]]
- [[info-leak]]
- [[client-fetch]]
