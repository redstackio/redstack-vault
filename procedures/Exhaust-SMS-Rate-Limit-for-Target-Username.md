---
tags:
  - rate-limit
  - exhaustion
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
  - '[[Gather Victim Identity Information]]'
updated_at: '2025-12-14T17:24:42.867Z'
sub_techniques: []
id: eb2fa7b6-679f-4ee8-8147-2054be919665
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Exhaust-SMS-Rate-Limit-for-Target-Username

## Summary

This procedure repeatedly requests SMS codes during Twitter's password reset to exhaust the rate limit for the associated phone number, creating a blocked state that can be detected in subsequent brute force attempts.

## Description

By initiating multiple password reset requests for a target username, the SMS delivery to the linked phone number becomes rate-limited. Twitter's system responds with a distinct 'exceeded attempts' message once the limit is hit, which leaks the block status specific to that phone number. This is performed on the web platform and requires no special access, but relies on the known partial digits from prior reconnaissance.

## Requirements

1. Known target username and partial phone digits.
2. Ability to make repeated HTTP requests (manual or automated).
3. Same IP/session to trigger per-account limits.

## Defense

Defensive measures and detection strategies:

- Enforce stricter per-IP and per-username rate limits on reset requests.
- Use CAPTCHA or secondary verification after a few attempts.
- Log and analyze patterns of repeated resets for potential enumeration attacks.

## Objectives

1. Block SMS delivery to the target phone number.
2. Establish a detectable state for brute force identification.
3. Prepare for cross-IP enumeration without alerting the user.

## Instructions

### Step 1: Repeated Reset Requests

**Context**: Trigger multiple SMS sends to exhaust the quota.

Navigate to the password reset URL and enter the target username repeatedly (5-10 times).

> Each request attempts to send an SMS; after exhaustion, the message changes to 'You've exceeded the number of attempts. Please try again later.'

### Step 2: Verify Exhaustion

**Context**: Confirm the rate limit is active for the phone.

Attempt one more reset to observe the block message.

> Successful output: Block confirmation tied to the phone ending in known digits.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rate-limit]]
- [[exhaustion]]
- [[twitter]]
