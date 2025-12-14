---
id: proc-enumerate-userid-001
tags:
  - enumeration
  - user-discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Foxy-Proxy]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-profile-update-victim-enum]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:06.652Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-Victims-User-ID

## Summary

This procedure logs in as the victim (or test account) and intercepts a profile update request to extract the victim's userId, which is needed to target their profile in the IDOR exploit.

## Description

By performing a benign profile update while authenticated as the victim, the request reveals the associated userId (e.g., 123465). This ID is sequential or predictable in many apps, enabling targeting without prior knowledge.

## Requirements

1. Victim account credentials
2. Proxy tools (Burp Suite via Foxy Proxy) configured
3. Access to profile edit page

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize user IDs
- Log cross-account access attempts
- Implement ID binding to sessions

## Objectives

1. Authenticate as victim and access profile
2. Capture userId from intercepted request
3. Store ID for use in exploitation

## Instructions

### Step 1: Login as Victim

**Context**: Authenticate to the victim's session.

Login at https://target.com/login with victim@gmail.com and password.

> Successful authentication to dashboard.

### Step 2: Update Profile and Intercept

**Context**: Perform a profile change to trigger the POST and capture userId.

Go to My Account > Edit, update a field like PhoneNumber, enable proxy, submit, and intercept.

**Command** ([[commands/curl-profile-update-victim-enum]]):
```bash
curl -X POST https://target.com/EditUserProfile/Save \
  -H "Cookie: .AspNetCore.Antiforgery.w=..." \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Email=test@gmail.com&userId=123465&__RequestVerificationToken=...&PhoneNumber=13333333333333339&Title=Pentester&FirstName=attacking&LastName=wearehackerone&passChange=true&CitizenshipId=101&PositionTitleIds=10&PersonProfileId=0"
```

> Request reveals userId=123465; update succeeds.

### Step 3: Note and Verify ID

**Context**: Confirm the ID is distinct from attacker's.

Compare with attacker's userId (123464); note for modification step.

> Victim's ID ready for targeting.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/curl-profile-update-victim-enum]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Foxy-Proxy]]

## Tags

- enumeration
- user-discovery
