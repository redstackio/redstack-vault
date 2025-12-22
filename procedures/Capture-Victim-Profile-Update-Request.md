---
tags:
  - idor
  - web
  - request-capture
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b6d105fe-d9f3-4658-ae55-5124dad74c24
created_at: '2025-12-14T17:25:47.553Z'
updated_at: '2025-12-14T17:25:47.553Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Victim-Profile-Update-Request

## Summary

This procedure logs into the victim's account in a separate browser and captures their profile update request to obtain target identifiers for IDOR exploitation.

## Description

Using Google Chrome with Burp proxy, authenticate as the victim, access the profile page, and intercept the POST /app/updateUser request. This reveals the victim's 'id' (e.g., '/redacted') and 'email' (e.g., 'redacted+victim@wearehackerone.com'). The process mirrors the attacker capture but in isolation, with outcomes including identifiers for payload modification.

## Requirements

1. Victim test credentials
2. [[tools/Burp-Suite]] proxied for Chrome (separate instance if needed)
3. [[tools/Google-Chrome]] browser

## Defense

Defensive measures and detection strategies:

- Cross-reference request IPs with authenticated user locations
- Detect multi-browser or proxy usage via headers
- Alert on rapid session switches between accounts

## Objectives

1. Isolate victim session for clean capture
2. Extract victim's 'id' and 'email' for targeting
3. Validate payload consistency across users

## Instructions

### Step 1: Login as Victim and Configure Proxy

**Context**: Authenticate and set up interception.

No specific command; UI actions.

> In [[tools/Google-Chrome]] (proxied to Burp), go to https://mtnmobad.mtnbusiness.com.ng/#/login1, enter victim credentials. Expected output: Successful login.

### Step 2: Access Profile and Intercept Request

**Context**: Trigger and capture the update request.

No specific command; navigate and intercept.

> Visit https://mtnmobad.mtnbusiness.com.ng/#/userProfile, enable intercept in Burp. Expected output: POST request captured with victim's JSON payload.

### Step 3: Record and Logout

**Context**: Document identifiers and end session.

No specific command; manual.

> Note 'id' and 'email' from payload, then logout. Expected output: Identifiers recorded, session closed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Google-Chrome]]

## Tags

- [[idor]]
- [[web]]
- [[request-capture]]
