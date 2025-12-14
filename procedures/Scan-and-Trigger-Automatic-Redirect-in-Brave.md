---
id: proc-brave-scan-redirect-001
tags:
  - open-redirect
  - qr-code
  - phishing
type: procedure
tools:
  - '[[tools/Brave-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:34.857Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Drive-by Compromise]]'
---
# Scan-and-Trigger-Automatic-Redirect-in-Brave

## Summary

This procedure details scanning a malicious QR code using Brave's scanner to exploit the open redirect vulnerability, resulting in immediate navigation to a harmful site.

## Description

The Brave QR scanner decodes and opens URLs automatically, without validation or prompts. Pointing at a QR with a malicious URL (e.g., http://www.evil.com/) triggers the redirect. Tested on Android/iOS; client-side only. Impacts include phishing success and potential malware execution, eroding user trust.

## Requirements

1. Malicious QR code image available
2. Brave scanner accessed and camera active
3. Good lighting for accurate scanning

## Defense

Defensive measures and detection strategies:

- Patch Brave to include QR URL previews and confirmations
- Use third-party scanners that require explicit approval
- Browser telemetry for detecting rapid QR-to-redirect sequences
- User training on QR risks

## Objectives

1. Decode and execute the embedded URL payload
2. Achieve stealthy site redirection
3. Compromise user via phishing or malware

## Instructions

### Step 1: Position QR Code

**Context**: Align the scanner with the target image.

Hold the device camera steady over the QR code.

> Expected: Scanner detects and highlights the code.

### Step 2: Initiate Scan

**Context**: Trigger decoding and redirect.

The scan happens automatically upon detection; no button press needed in Brave.

> Expected: Browser loads the malicious URL instantly, e.g., redirect to http://www.evil.com/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Brave-Browser]]

## Tags

- open-redirect
- qr-code
- phishing
