---
tags:
  - insecure-storage
  - sensitive-data-exposure
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-data-retrieve]]'
  - '[[commands/curl-data-validate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:32:10.789Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7d3d4962-93fa-4d79-9185-d9df8c3c621c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Access Unencrypted Sensitive Data Storage

## Summary

This procedure exploits the lack of encryption in sensitive data storage within the Stripo Inc application, allowing direct retrieval and exposure of plaintext information once access is gained via API.

## Description

The application's storage mechanism failed to encrypt sensitive data, such as user details, making it vulnerable to exposure upon unauthorized access. Combined with permissive API keys, attackers can query storage endpoints to retrieve data without decryption. This was identified in a HackerOne report with medium severity, targeting web storage backends, and outcomes include full data leaks.

## Requirements

1. Valid API access (from prior exploitation)
2. Knowledge of storage endpoints
3. HTTP client for data retrieval

## Defense

Defensive measures and detection strategies:

- Enforce encryption at rest for all sensitive data
- Audit storage access via API logs
- Implement data loss prevention (DLP) tools

## Objectives

1. Retrieve unencrypted sensitive data
2. Validate exposure of plaintext information
3. Exfiltrate data for analysis

## Instructions

### Step 1: Retrieve Sensitive Data

**Context**: Use API access to pull data from unencrypted storage.

**Command** ([[commands/curl-data-retrieve]]):
```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/storage/sensitive-data
```

> Expected output: Raw JSON with plaintext sensitive fields, confirming no encryption.

### Step 2: Validate Data Exposure

**Context**: Parse and inspect the retrieved data for sensitive content.

**Command** ([[commands/curl-data-validate]]):
```bash
curl -H "Authorization: Bearer overly_permissive_key" https://api.stripo.com/v1/storage/user-info | jq '.data'
```

> This filters the response. Success shows unmasked user info like emails or tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/curl-data-retrieve]]
- [[commands/curl-data-validate]]

## Tools Used

- [[tools/curl]]

## Tags

- [[insecure-storage]]
- [[sensitive-data-exposure]]
