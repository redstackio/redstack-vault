---
tags:
  - brute-force
  - credential-access
  - crashplan
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
id: 76b8d7e2-f5e9-492f-b59a-73b416f12f9d
created_at: '2025-12-14T17:26:30.454Z'
updated_at: '2025-12-14T17:26:30.454Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-CrashPlan-Friend-Code

## Summary

This procedure brute-forces the 6-digit alphanumeric friend code for a CrashPlan server like backup.uber.com:443 by systematically trying all combinations until the valid code is found, granting unauthorized backup access.

## Description

With no rate limiting, a scripted attack can iterate through the 2.17 billion possibilities via HTTP POST requests to the validation endpoint. Use parallelization (e.g., multiple threads) to speed up the process. Target environment is a web-based CrashPlan instance. Prerequisites: Validated endpoint from prior recon. Expected outcome: Acquisition of the exact code, enabling further actions like data upload.

## Requirements

1. Scripting language (e.g., Python) for request automation
2. Proxy rotation to avoid potential IP blocks
3. Stable connection to port 443

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting and temporary bans on suspicious IPs
- Rotate or strengthen friend codes periodically
- Implement anomaly detection on validation request volumes

## Objectives

1. Discover the valid friend code
2. Gain authorization for inbound backups
3. Minimize detection during iteration

## Instructions

### Step 1: Setup Brute-Force Script

**Context**: Prepare a tool to generate and test codes systematically.

Write a Python script using itertools.product to generate codes (e.g., chars='0123456789abcdefghijklmnopqrstuvwxyz') and requests library to POST each to the endpoint.

> Expected output: Script ready, testing first batch of codes.

### Step 2: Execute Brute-Force

**Context**: Run the iteration, monitoring for valid responses.

Launch the script with threading (e.g., 10-50 concurrent requests). Parse responses for success (e.g., HTTP 200 with 'valid' message).

> Expected output: Valid code identified after X attempts; log the code for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used


## Tags

- [[brute-force]]
- [[credential-access]]
