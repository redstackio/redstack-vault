---
id: proc-uuid-003
name: Brute-Force-Verification-Code-with-Burp-Intruder
tags:
  - brute-force
  - credential-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:33:06.514Z'
sub_techniques:
  - '[[Password Spraying]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Verification-Code-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder module to automate guessing of the verification code by sending multiple modified POST requests, exploiting the lack of rate limiting to identify the correct code quickly.

## Description

With the intercepted request, the 'code' parameter is marked for payload injection. A payload list of common 4-6 digit codes (e.g., 0000-9999) is loaded, and Intruder launches parallel or sequential attacks. Success is detected by response differences (e.g., redirect on valid code). This leads to account takeover in unprotected systems.

## Requirements

1. Intercepted POST request saved in Burp Repeater/Intruder
2. Payload list prepared (e.g., numbers.txt with 0000 to 9999)
3. Burp Suite Professional for faster attacks

## Defense

Defensive measures and detection strategies:

- Rate limit code submissions (e.g., 3 attempts per code generation)
- Implement exponential backoff and IP blocking after failures
- Analyze web logs for high-volume POSTs to verification endpoints

## Objectives

1. Guess the correct verification code
2. Bypass authentication without limits
3. Enable password reset access

## Instructions

### Step 1: Send to Intruder

**Context**: Load the captured request into Burp Intruder for payload configuration.

Right-click the request in Proxy/History > Send to Intruder; in Positions, highlight the code value (e.g., §0000§).

> Clear other positions; set payload type to Simple list and load numbers.txt.

### Step 2: Launch Attack

**Context**: Start the brute-force and monitor responses.

Click Start attack; sort results by response length or status (valid code often has longer body or 302 redirect).

> Expected Output: Table showing requests; identify the code with differing response (e.g., code=1234 succeeds).

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Spraying]] Password Spraying (adapted for codes)

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[credential-access]]
