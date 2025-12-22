---
tags:
  - salt-leakage
  - credential-exposure
  - coldfusion
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-retrieve-salt]]'
verified: false
platforms:
  - Web
  - Adobe ColdFusion
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:28:58.675Z'
sub_techniques: []
id: dd03a8a7-003c-4621-a726-77d31cf94b0f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
---
# Retrieve-Admin-Salt-via-Exposed-Method

## Summary

This procedure exploits an unprotected getSalt method in the ColdFusion administrator CFC to directly retrieve the salt value used for password hashing, enabling offline cracking attacks.

## Description

The vulnerability stems from the getSalt method being callable without authentication via a URL parameter in the administrator.cfc file. On the target DoD domain, accessing ?method=getSalt returns the salt (e.g., ████████), which can be used with leaked hashes to crack admin passwords using tools like Hashcat, bypassing login to the admin panel.

## Requirements

1. Access to the base admin endpoint from Step 1
2. Curl or browser for GET request
3. Knowledge of the method parameter syntax

## Defense

Defensive measures and detection strategies:

- Restrict CFC method access to authenticated sessions only
- Remove or disable debug/exposed API methods in production
- Log and alert on anomalous API calls to admin endpoints

## Objectives

1. Leak the administrator salt value
2. Enable hash cracking for auth bypass
3. Gain potential admin panel access

## Instructions

### Step 1: Invoke getSalt Method

**Context**: Append the method parameter to the CFC URL to trigger unauthenticated salt retrieval.

**Command** ([[commands/curl-retrieve-salt]]):
```bash
curl https://█████████/████████/adminapi/administrator.cfc?method=getSalt
```

> The response body contains the raw salt string. No headers or auth are needed; success is indicated by the salt appearing directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unsecured Credentials]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-salt]]

## Tools Used


## Tags

- [[salt-leakage]]
- [[credential-exposure]]
