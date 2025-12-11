---
tags:
  - idor
  - api
  - discovery
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-uber-api]]'
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e8ddfd66-204c-4409-838c-0cfb86182e29
created_at: '2025-12-11T06:10:28.617Z'
updated_at: '2025-12-11T06:10:28.617Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---
# Identify Vulnerable Uber API Endpoint

## Summary

This procedure involves discovering and confirming the vulnerability of the Uber marketplace API endpoint that accepts userUuid parameters, enabling potential IDOR attacks by testing accessibility without authorization checks.

## Description

The target endpoint is https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails, which processes POST requests. Without proper validation, it allows querying for any user's data. This is typically identified through API exploration or reverse engineering of Uber's web applications.

## Requirements

1. Internet access to the Uber API
2. A tool for sending HTTP requests, such as [[tools/curl]]
3. Knowledge of at least one valid user UUID for initial testing

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks on API parameters
- Monitor API logs for anomalous UUID queries from single IP addresses

## Objectives

1. Confirm endpoint accessibility
2. Verify lack of authorization enforcement
3. Prepare for targeted exploitation

## Instructions

### Step 1: Locate the Endpoint

**Context**: Use network inspection or public API references to identify the endpoint URL.

**Command** ([[commands/curl-post-uber-api]]):
```bash
curl -X POST 'https://bonjour.uber.com/marketplace/_rpc?rpc=getConsentScreenDetails' -H 'Content-Type: application/json' -d '{"userUuid": "test_uuid"}'
```

> This sends a basic POST request to test if the endpoint responds without authentication.

### Step 2: Analyze Response

**Context**: Examine the output for signs of data disclosure or error handling.

> Look for JSON fields containing user information; absence of access denied errors indicates vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques

## Commands Used

- [[commands/curl-post-uber-api]]

## Tools Used

- [[tools/curl]]

## Tags

- [[idor]]
- [[commands/curl-post-uber-api]]
