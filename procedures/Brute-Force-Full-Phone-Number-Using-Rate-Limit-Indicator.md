---
tags:
  - brute-force
  - phone-enumeration
  - twitter
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Gather Victim Identity Information]]'
updated_at: '2025-12-14T17:24:42.858Z'
sub_techniques:
  - '[[Password Guessing]]'
id: 31ab8951-7fb6-4461-a446-51b48758fc3e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Gather Victim Identity Information]]'
---
# Brute-Force-Full-Phone-Number-Using-Rate-Limit-Indicator

## Summary

This procedure brute-forces the full phone number by testing variations ending in the known digits, identifying the exact match through the unique 'exceeded attempts' response from the prior rate limit exhaustion.

## Description

Using the new IP, attackers input phone number candidates into the password reset form. Non-matching numbers receive standard responses, while the correct one triggers the block message due to exhaustion. Narrowing to common prefixes (e.g., 10,000 possibilities) makes it feasible. This web-based technique compromises user privacy by revealing sensitive identifiers.

## Requirements

1. Known last two digits and country format (e.g., 8-digit prefix for some regions).
2. List of possible prefixes (e.g., operator ranges like 26-27).
3. New IP from prior step.

## Defense

Defensive measures and detection strategies:

- Uniform error messages for all phone inputs (no distinction for rate limits).
- Rate limit phone reset attempts globally, not just per account.
- Anomaly detection on bulk phone inputs matching partial patterns.

## Objectives

1. Identify the exact full phone number.
2. Exploit response differences for enumeration.
3. Achieve complete user identity disclosure.

## Instructions

### Step 1: Prepare Number List

**Context**: Generate candidates ending in known digits.

Create a list of phone numbers like '12345615', focusing on valid prefixes (e.g., 26xxxx15 to 27yyyy15).

> Use a script or manual list; aim for ~10,000 to keep feasible.

### Step 2: Test Each Number

**Context**: Submit resets and observe responses.

For each number, access begin_password_reset (e.g., https://twitter.com/i/flow/password_reset) and enter the phone.

> Matching number outputs 'You've exceeded the number of attempts.'; others 'We'll send a code...' or 'not associated'.

### Step 3: Identify Match

**Context**: Confirm the hit.

Record the number triggering the block as the target's.

> Successful output: Full number enumerated, e.g., '+1-XXX-XXX-1515'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Brute Force]] Brute Force
- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used


## Tags

- [[brute-force]]
- [[phone-enumeration]]
- [[twitter]]
