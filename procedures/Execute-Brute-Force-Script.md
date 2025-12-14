---
id: proc-execute-brute-script
tags:
  - brute-force
  - python-script
  - ip-rotation
type: procedure
tools:
  - '[[tools/hackeronebrute.py]]'
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/run-hackerone-brute-force-script]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Connection Proxy]]'
updated_at: '2025-12-14T17:31:52.779Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Connection Proxy]]'
---
# Execute-Brute-Force-Script

## Summary

This procedure runs a custom Python script to brute-force login credentials by rotating IPv6 addresses, evading IP rate limits and attempting passwords from a dictionary at high speed.

## Description

The script hackeronebrute.py uses 50 threads to cycle through 677 IPv6 addresses on venet0, sending POST requests to https://hackerone.com/sessions with the target username and passwords from 10k_most_common.txt. It spaces attempts to respect 4-second limits per IP, achieving ~30 passwords/second. In the PoC, it found 'Geniaal2!!' after 10,001 attempts in 335 seconds.

## Requirements

1. Configured VPS with IPv6 addresses
2. Prepared password dictionary
3. Python and script installed
4. Target username

## Defense

Defensive measures and detection strategies:

- Add CAPTCHA or 2FA after failures
- Implement account lockouts
- Monitor for multi-IP login attempts from same user
- Detect script-like request patterns (e.g., rapid common password tries)

## Objectives

1. Bypass rate limits via IP rotation
2. Attempt all dictionary passwords efficiently
3. Discover and output the correct password

## Instructions

### Step 1: Prepare Script Environment

**Context**: Ensure Python and script are ready on VPS.

```bash
python --version  # Confirm Python 2/3
# Assume script is uploaded
```

> Expected: Python available.

### Step 2: Run the Script

**Context**: Execute with parameters for username, file, interface, threads.

Execute [[commands/run-hackerone-brute-force-script]]:

```bash
python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50
```

> The script rotates IPs, sends requests, and monitors responses. Expected output: Progress at ~30 pw/s, [SUCCESS] Found the right password: Geniaal2!!, Total time: 335 seconds.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force
- [[Connection Proxy]] Proxy

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/run-hackerone-brute-force-script]]

## Tools Used

- [[tools/hackeronebrute.py]]
- [[tools/Python]]

## Tags

- [[brute-force]]
- [[python-script]]
- [[ip-rotation]]
