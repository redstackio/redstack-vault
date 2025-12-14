---
tags:
  - jwt
  - recon
  - jitsi-meet
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: dbb410e5-f57a-4204-9953-c1bc701c5822
created_at: '2025-12-14T17:31:42.670Z'
updated_at: '2025-12-14T17:31:42.670Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Obtain-Jitsi-Meet-JWT-Public-Key

## Summary

This procedure retrieves the public key configured for JWT authentication in Jitsi Meet, which is often exposed in configuration files or accessible via network inspection, enabling subsequent token forgery.

## Description

In Jitsi Meet with Prosody, asymmetric JWT validation uses public keys (e.g., RS256) that are typically stored in config files like /etc/prosody/conf.d/jitsi-meet.cfg.lua or exposed in API responses. Attackers can obtain this key without authentication, as it's public by design for verification. This step is prerequisite for exploiting the validation flaw where symmetric algorithms are not blocked.

## Requirements

1. Network access to the Jitsi Meet server
2. Ability to inspect configuration or traffic (e.g., via browser dev tools or direct file access if internal)
3. Basic understanding of PEM key formats

## Defense

Defensive measures and detection strategies:

- Restrict config file access and avoid exposing keys in public endpoints
- Monitor for anomalous key retrieval attempts in logs
- Use key rotation and validate only asymmetric algorithms strictly

## Objectives

1. Acquire the public key for HMAC misuse
2. Confirm key format for forgery compatibility
3. Prepare for JWT manipulation

## Instructions

### Step 1: Inspect Configuration Files

**Context**: If you have server access or can enumerate configs, locate the public key in Prosody settings.

Search for the JWT configuration in files like prosody.cfg.lua, where the public key is defined under authentication_modules.

> Look for lines like: public_key = "/path/to/public.pem"; Extract the key content.

### Step 2: Network Inspection for Exposed Keys

**Context**: Many deployments expose the key via API or static files; use browser tools or curl to fetch.

Intercept requests to Jitsi Meet's authentication endpoints (e.g., /auth) and check for key exposure in responses or headers.

> If the key is in a downloadable config, download and parse it manually.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[jwt]]
- [[recon]]
- [[jitsi-meet]]
