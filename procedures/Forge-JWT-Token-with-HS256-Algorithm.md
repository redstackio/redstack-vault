---
tags:
  - jwt
  - forgery
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Application Access Token]]'
id: e21d6327-2154-4c78-82bc-767ddf53afa8
created_at: '2025-12-14T17:31:42.661Z'
updated_at: '2025-12-14T17:31:42.661Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
  - '[[Valid Accounts]]'
---
# Forge-JWT-Token-with-HS256-Algorithm

## Summary

This procedure forges a JWT token for Jitsi Meet by modifying the header to use HS256 (symmetric) instead of the configured RS256, signing with the public key as the secret to bypass Prosody's validation.

## Description

The Prosody module in Jitsi Meet does not restrict symmetric algorithms during validation, allowing an attacker to craft a token with {'alg': 'HS256'} in the header, encode a payload with conference claims (e.g., {"context":{"user":{"name":"attacker","id":1}},"aud":"jitsi","iss":"myapp","sub":"meet.jitsi","room":"*","exp":timestamp}), and sign using HMAC-SHA256 with the public key's raw bytes as the secret. This exploits the improper handling, making the token appear valid.

## Requirements

1. Obtained public key from prior step
2. JWT encoding/decoding capability (e.g., Python PyJWT library or jwt.io)
3. Knowledge of target claims for Jitsi Meet (e.g., room access)

## Defense

Defensive measures and detection strategies:

- Enforce algorithm whitelisting in Prosody to block HS256
- Validate JWT headers strictly for asymmetric only
- Log and alert on mismatched algorithm usage

## Objectives

1. Create a valid-looking forged JWT
2. Ensure token passes Prosody validation
3. Enable unauthorized claims like moderator access

## Instructions

### Step 1: Prepare JWT Components

**Context**: Define header, payload, and secret using the public key.

Set header: {"typ":"JWT","alg":"HS256"}. Payload example: {"aud":"jitsi","iss":"auth","sub":"jitsi","room":"protected-room","context":{"group":"focus"},"exp":(time.time() + 3600)}. Secret: public_key_bytes (decode PEM to raw).

> Base64-encode header and payload separately without padding.

### Step 2: Sign and Assemble Token

**Context**: Compute HMAC signature and combine into JWT.

Use HMAC-SHA256 to sign the concatenated header.payload with the secret, then base64-encode the signature. Final token: header.payload.signature.

> Test decode on jwt.io (set alg to HS256) to verify structure; the exploit relies on Prosody using the same secret for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Use Alternate Authentication Material]]
- [[Valid Accounts]]

### Sub-Techniques

- [[Application Access Token]]

## Commands Used


## Tools Used


## Tags

- [[jwt]]
- [[forgery]]
- [[auth-bypass]]
