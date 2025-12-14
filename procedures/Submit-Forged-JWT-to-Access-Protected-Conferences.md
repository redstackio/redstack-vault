---
tags:
  - jwt
  - access
  - jitsi-meet
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 888c71ae-1df3-47ef-b044-2f4221901f72
created_at: '2025-12-14T17:31:42.658Z'
updated_at: '2025-12-14T17:31:42.658Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Forged-JWT-to-Access-Protected-Conferences

## Summary

This procedure submits the forged JWT to Jitsi Meet endpoints to bypass authentication and gain access to protected rooms or start new conferences.

## Description

With the forged token, include it in the Authorization: Bearer <token> header when requesting access via the Jitsi Meet web interface or API endpoints like /join or conference creation. Prosody validates it as legitimate due to the algorithm confusion, granting unauthorized entry. This can lead to eavesdropping, disruption, or control of meetings.

## Requirements

1. Forged JWT from prior step
2. URL of the target Jitsi Meet instance
3. Browser or HTTP client for submission

## Defense

Defensive measures and detection strategies:

- Patch to Jitsi Meet 2.0.5963 or later
- Implement strict JWT algorithm enforcement in Prosody
- Monitor access logs for anomalous token patterns or unauthorized room joins

## Objectives

1. Authenticate with forged token
2. Enter or create protected conferences
3. Achieve unauthorized access

## Instructions

### Step 1: Prepare Authentication Request

**Context**: Set up the request with the forged JWT.

Use a browser to navigate to https://target-jitsi-meet/room-name, or craft an HTTP request with Authorization header.

> Ensure claims in token match the target room (e.g., "room":"*" for any).

### Step 2: Submit and Verify Access

**Context**: Send the request and confirm bypass.

Submit via web form or API; if successful, the interface loads without login prompts, allowing participation.

> Check for errors in Prosody logs; success means no rejection on signature or algorithm.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[jwt]]
- [[access]]
- [[jitsi-meet]]
