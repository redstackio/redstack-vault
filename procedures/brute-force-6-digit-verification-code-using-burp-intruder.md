---
tags:
  - brute-force
  - intruder
  - burp-suite
type: procedure
tools:
  - '[[tools/burp-suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0ca2ef4a-a3a2-4826-a765-1cecc64506f2
created_at: '2025-12-14T17:24:47.708Z'
updated_at: '2025-12-14T17:24:47.708Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force 6-Digit Verification Code Using Burp Intruder

## Summary

This procedure uses Burp Suite's Intruder to systematically test all 1,000,000 possible 6-digit combinations for the email verification code, exploiting the absence of rate limits to find the correct one quickly.

## Description

The Evernote verification endpoint accepts unlimited attempts without delays, allowing an attacker to fuzz the confirmationCode parameter. Using Burp Intruder, the request is automated with numeric payloads from 000000 to 999999. This low-entropy code (20 bits) can be cracked in minutes on a standard connection. Prerequisites include the intercepted request from the initial setup. The outcome is identification of the valid code, enabling further account hijacking.

## Requirements

1. Intercepted verification request from prior step
2. Burp Suite Professional (Intruder feature)
3. Stable internet connection to handle ~1M requests

## Defense

Defensive measures and detection strategies:

- Enforce rate limiting (e.g., 10 attempts/minute per IP)
- Increase code length/entropy (e.g., 8+ digits or alphanumeric)
- Log and alert on high-volume requests to verification endpoints
- Implement exponential backoff or temporary IP bans

## Objectives

1. Automate exhaustive testing of confirmationCode values
2. Exploit lack of protections to verify without legitimate code access
3. Generate responses for analysis to pinpoint success

## Instructions

### Step 1: Configure Intruder Attack

**Context**: Prepare the fuzzing payload on the confirmationCode parameter.

Right-click the intercepted request in Burp Repeater and send to Intruder.

> In Intruder, clear default positions and mark §confirmationCode§ as the payload position. Set attack type to Sniper.

### Step 2: Set Payload Options

**Context**: Define the brute-force range for 6-digit codes.

Configure payload set 1 as Numbers, from 000000 to 999999, step 1, with leading zeros.

> Optionally, add payload processing to pad numbers to 6 digits. Start the attack; monitor progress in the results table.

### Step 3: Monitor and Throttle if Needed

**Context**: Ensure the attack runs without interruption.

Adjust throttle if responses slow down.

> The attack should complete in 2-5 minutes; review HTTP status and lengths in real-time.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/burp-suite]]

## Tags

- [[brute-force]]
- [[intruder]]
