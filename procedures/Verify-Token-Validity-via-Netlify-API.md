---
id: proc-003
tags:
  - api-testing
  - valid-accounts
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/jq]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-verify-netlify-token]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.734Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Token-Validity-via-Netlify-API

## Summary

This procedure tests a leaked Netlify token by querying the API for account details, confirming permissions like Owner and Developer roles.

## Description

Using the extracted token, send an authenticated request to Netlify's /accounts endpoint. A successful response reveals account scope, roles, and associated sites, validating the token for further exploitation such as deployments or billing changes.

## Requirements

1. Extracted Netlify Bearer token
2. curl and jq installed
3. Internet access to api.netlify.com

## Defense

Defensive measures and detection strategies:

- Rotate tokens immediately upon leak detection
- Enable API logging and anomaly detection on Netlify
- Use short-lived tokens and role-based access control

## Objectives

1. Authenticate with the token
2. Retrieve account metadata
3. Confirm high-privilege access

## Instructions

### Step 1: Query Accounts Endpoint

**Context**: Use the token to fetch account information, verifying validity.

**Command** ([[commands/curl-verify-netlify-token]]):
```bash
curl -X GET https://api.netlify.com/api/v1/accounts -H "Authorization: Bearer ████" -s | jq
```

> This command sends a GET request with the Bearer token. The -s flag suppresses curl's progress bar, and jq formats the JSON response. Replace ████ with the actual token.

**Expected Output**: JSON array with account objects, including "name": "Mozilla IT Web SRE", "slug": "mozilla-it", and "roles": ["Owner", "Developer", "Billing Admin").

### Step 2: Analyze Response

**Context**: Parse the output to identify accessible resources.

Use jq to filter, e.g., jq '.[] | {name, roles}'.

> Look for sites, billing info, and SAML configs indicating full control.

**Expected Output**: Filtered JSON showing privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used

- [[commands/curl-verify-netlify-token]]

## Tools Used

- [[tools/curl]]
- [[tools/jq]]

## Tags

- [[api-testing]]
- [[valid-accounts]]
