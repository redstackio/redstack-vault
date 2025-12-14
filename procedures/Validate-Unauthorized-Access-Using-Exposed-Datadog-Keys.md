---
tags:
  - api-key-exposure
  - unauthorized-access
  - datadog
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-datadog-api-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:29.266Z'
skill_level: intermediate
impact_level: critical
detection_risk: medium
sub_techniques:
  - '[[Cloud Instance Metadata API]]'
id: 83566fdd-3fd2-4f17-acf1-e47b1da348a1
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Validate-Unauthorized-Access-Using-Exposed-Datadog-Keys

## Summary

This procedure demonstrates the use of extracted Datadog API and application keys to gain unauthorized read and write access to the Datadog instance, confirming the vulnerability's impact without performing destructive actions.

## Description

Using the keys discovered in client-side JS, this procedure tests API endpoints to verify permissions. The scenario targets a Datadog-integrated web app, where keys allow full instance control. Outcomes include successful queries for metrics or sites, rated critical (CVSS 9.6). Prerequisites: Extracted keys and API knowledge; perform responsibly to avoid exploitation.

## Requirements

1. Extracted API and application keys from JS file
2. curl or Postman for API testing
3. Knowledge of Datadog API endpoints (e.g., https://api.datadoghq.com)

## Defense

Defensive measures and detection strategies:

- Rotate exposed keys immediately and monitor API logs for anomalous access
- Enforce least-privilege for API keys (e.g., read-only where possible)
- Use API gateways to validate and log all requests

## Objectives

1. Confirm read access to Datadog data
2. Test write capabilities if applicable
3. Document impact for responsible disclosure

## Instructions

### Step 1: Prepare API Request

**Context**: Set up the authentication using the exposed keys.

Use the API key for authentication and application key for app-specific access.

### Step 2: Test Read Access

**Context**: Send a request to a Datadog endpoint to validate access.

Execute [[commands/curl-datadog-api-test]] to query sites:

```bash
curl -X GET "https://api.datadoghq.com/api/v1/sites" \
     -H "DD-API-KEY: <extracted_api_key>" \
     -H "DD-APPLICATION-KEY: <extracted_app_key>"
```

> This command authenticates with the exposed keys and retrieves site data. Expected output: JSON response with site details if access is granted.

**Expected Output**: Successful HTTP 200 response with Datadog instance data, demonstrating unauthorized read access.

### Step 3: Assess Write Access (Responsible Testing)

**Context**: Optionally test non-destructive write operations, such as creating a test metric.

Similar to Step 2, but use a POST endpoint; avoid in production without permission.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques

- [[Cloud Instance Metadata API]]

## Commands Used

- [[commands/curl-datadog-api-test]]

## Tools Used


## Tags

- [[api-key-exposure]]
- [[unauthorized-access]]
- [[datadog]]
- [[credential-access]]
