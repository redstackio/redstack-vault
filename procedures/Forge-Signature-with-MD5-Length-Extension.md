---
id: proc-forge-md5-length-extension-signature
tags:
  - length-extension
  - signature-forgery
  - auth-bypass
  - md5
  - api
type: procedure
tools:
  - '[[tools/Hashpump]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/hashpump-extend]]'
  - '[[commands/curl-api-request]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:31:11.134Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
# Forge-Signature-with-MD5-Length-Extension

## Summary

This procedure exploits the MD5 length-extension vulnerability in WP API Key-Auth by forging authentication signatures to append malicious data, allowing unauthorized access to protected WordPress API endpoints without knowing the secret key.

## Description

The WP API Key-Auth plugin generates signatures using MD5 on a JSON message followed by the secret, enabling length-extension attacks. An attacker observes a valid request to get the original signature and message length, then uses a tool like Hashpump to compute an extended message and signature. This forged signature can be used in API requests to inject payloads, bypassing validation. Target environment is a WordPress site with the plugin active. Prerequisites include capturing a legitimate request (e.g., via proxy) and having the API key. Expected outcomes include successful unauthorized API calls, such as creating or reading protected posts.

## Requirements

1. Valid API key from observation (public or intercepted)
2. Original signature and message length from a legitimate request
3. Hashpump tool installed
4. Network access to the target WordPress API

## Defense

Defensive measures and detection strategies:

- Replace MD5 with HMAC-SHA256 for signatures
- Validate message integrity beyond hashing (e.g., length checks, timestamps)
- Log and monitor API requests for signature anomalies or unusual payloads

## Objectives

1. Generate forged signature for extended message
2. Bypass authentication on API endpoints
3. Access or modify protected resources

## Instructions

### Step 1: Capture Original Request

**Context**: Intercept a legitimate API request to obtain the message, signature, and length for extension.

Use a proxy like Burp Suite or browser tools to capture, e.g., a POST to /wp-json/wp/v2/posts with headers X-WP-Key-Auth-Signature and X-WP-Key-Auth-Key.

Note the JSON body length in bytes and the hex signature.

### Step 2: Perform Length-Extension

**Context**: Use Hashpump to append payload to the original message and compute new signature.

**Command** ([[commands/hashpump-extend]]):
```bash
./hashpump -s 9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d -k 50 -p '}{"admin":true,"payload":"malicious"}' --digest md5
```

> Replace -s with original hex signature, -k with message byte length (e.g., 50), -p with JSON-closing and new payload. Expected output: new message and signature hex.

### Step 3: Submit Forged Request

**Context**: Send the extended message with forged signature to the API.

**Command** ([[commands/curl-api-request]]):
```bash
curl -X POST https://target.com/wp-json/wp/v2/posts -H "X-WP-Key-Auth-Signature: NEW_SIGNATURE" -H "X-WP-Key-Auth-Key: API_KEY" -d 'ORIGINAL_JSON_EXTENDED'
```

> Use the output from Step 2. Expected output: 200 OK response with API data, no auth error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Credentials In Files]] Meshed Editing

### Sub-Techniques


## Commands Used

- [[commands/hashpump-extend]]
- [[commands/curl-api-request]]

## Tools Used

- [[tools/Hashpump]]

## Tags

- exploitation
- cryptographic-attack
- auth-bypass
