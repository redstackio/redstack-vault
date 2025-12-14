---
tags:
  - information-disclosure
  - discovery
  - hash-weakness
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[System Information Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 763b590b-4552-4148-a23c-48dca463db19
created_at: '2025-12-14T17:27:42.366Z'
updated_at: '2025-12-14T17:27:42.366Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Verify-Email-Phone-Association-on-VK

## Summary

This procedure exploits a hash generation flaw in VK.com to check if an email and phone number are linked to the same user profile, disclosing private associations for targeted attacks.

## Description

VK.com's user profile features include a verification endpoint that confirms email-phone ownership, but weak hashing allows attackers to probe linkages without authentication. By submitting guessed or known email/phone pairs, responses reveal matches, aiding in social engineering or confirming takeover success.

## Requirements

1. Suspected email and phone for the target
2. Access to VK.com's association check feature
3. Browser or HTTP client for requests

## Defense

Defensive measures and detection strategies:

- Use strong, salted hashes for association checks
- Rate-limit and anonymize verification requests
- Log and monitor for enumeration patterns

## Objectives

1. Confirm email-phone linkage to a profile
2. Gather intel for further exploitation
3. Validate prior attack steps

## Instructions

### Step 1: Identify Test Inputs

**Context**: Collect potential email and phone to test against VK.com.

From public sources or prior recon, note email (e.g., victim@email.com) and phone (e.g., +1234567890).

**Expected Output**: Pair of identifiers ready for submission.

### Step 2: Submit Association Check

**Context**: Send request to the verification endpoint, observing for match indicators.

Use browser dev tools or an HTTP client to POST to the association endpoint with email, phone, and any required hash (exploiting weakness).

```bash
curl -X POST 'https://vk.com/profile_verify' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'email=victim@email.com&phone=+1234567890&action=verify_link'
```

**Expected Output**: Response like {"status": "linked"} or profile hint if matched.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[Discovery]]
