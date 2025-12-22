---
id: proc-vk-generate-hash-316078
tags:
  - auth-bypass
  - hash-generation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-grant-access-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:47.575Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate Reusable Grant Access Hash

## Summary

This procedure exploits the VK.com grant_access endpoint to generate authentication hashes that do not expire and are not bound to critical account parameters like 2FA status or recent session resets, enabling their reuse for unauthorized access.

## Description

In the VK.com login flow, after initial access to a victim's account, the grant_access endpoint (https://login.vk.com/?act=grant_access) produces hashes lacking proper security bindings. This allows an attacker who has previously visited or accessed the account to capture and reuse these hashes for subsequent logins without 2FA. The attack scenario targets web-based authentication, assuming the attacker can intercept or simulate login requests. Expected outcomes include obtaining persistent auth tokens leading to account compromise.

## Requirements

1. Prior access to the victim's VK.com account (e.g., via phishing or session hijacking)
2. Ability to intercept HTTP requests (browser dev tools or proxy)
3. Network access to VK.com over HTTPS

## Defense

Defensive measures and detection strategies:

- Implement hash expiration (e.g., short TTL) and binding to 2FA status/session resets
- Monitor for anomalous login attempts using reused hashes
- Enforce strict session management and rate limiting on auth endpoints

## Objectives

1. Generate an unbound hash from the grant_access endpoint
2. Capture the hash for reuse in future requests
3. Enable 2FA bypass in subsequent authentications

## Instructions

### Step 1: Trigger Grant Access Request

**Context**: Simulate or intercept a login flow that hits the grant_access endpoint after initial account access.

**Command** ([[commands/curl-grant-access-request]]):
```bash
curl -X GET "https://login.vk.com/?act=grant_access&ip_h=example_ip&hash=initial_session_hash" -H "Cookie: session_id=victim_session" -v
```

> This command sends a request to the endpoint using a captured session cookie from prior access. Expected output includes a response with a generated hash lacking expiration metadata. Extract the hash from the JSON or form response.

### Step 2: Validate Hash Properties

**Context**: Inspect the hash to confirm it is unbound and reusable.

**Command** ([[commands/curl-grant-access-request]]):
```bash
curl -X POST "https://login.vk.com/?act=login" -d "grant_hash=captured_hash&continue=1" -H "User-Agent: Mozilla/5.0" -v
```

> Reuse the hash in a login POST. If unbound, it should proceed without 2FA prompts. Expected output: Redirect to dashboard or auth token in response headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-grant-access-request]]

## Tools Used


## Tags

- [[2fa-bypass]]
- [[auth-bypass]]
