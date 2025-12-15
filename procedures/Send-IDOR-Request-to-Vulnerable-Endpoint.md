---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
tags:
  - idor
  - api-request
  - parameter-manipulation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-publitas-idor-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:18.342Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Send-IDOR-Request-to-Vulnerable-Endpoint

## Summary

This procedure exploits the IDOR vulnerability by sending a request to the Publitas API endpoint with an arbitrary SOURCE_ID, bypassing ownership checks to access unauthorized content.

## Description

The vulnerable endpoint in Publitas fails to validate if the SOURCE_DOCUMENT_ID (or SOURCE_ID) belongs to the requesting user, allowing direct object access. Using an authenticated session, craft a request with a target ID (e.g., observed from other users via public leaks or enumeration). This leads to disclosure of offline publication metadata, including cover page URLs with embedded sensitive IDs.

## Requirements

1. Authenticated API token from Publitas account
2. Target SOURCE_ID (e.g., from enumeration)
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership verification for all ID-based requests
- Rate-limit API calls and log anomalous ID usage

## Objectives

1. Submit manipulated request to vulnerable endpoint
2. Retrieve unauthorized publication data
3. Confirm IDOR exploitation

## Instructions

### Step 1: Prepare Authentication

**Context**: Obtain and include your session token.

Log in to Publitas and extract the Bearer token from browser storage or headers.

### Step 2: Craft and Send Request

**Context**: Use curl to target the endpoint with arbitrary ID.

Execute [[commands/curl-publitas-idor-request]] to verify:

```bash
curl -X GET "https://api.publitas.com/vulnerable-endpoint?SOURCE_ID=TARGET_SOURCE_ID" -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json"
```

> This command sends a GET request; replace TARGET_SOURCE_ID with a non-owned value. Expected output: JSON with cover URL if successful.

### Step 3: Validate Response

**Context**: Check for unauthorized data.

Inspect the response for errors; success indicates IDOR working.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-publitas-idor-request]]

## Tools Used


## Tags

- [[idor]]
- [[api-request]]
- [[parameter-manipulation]]
