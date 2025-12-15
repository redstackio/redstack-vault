---
id: ac-maid-hackerone-1139535
tags:
  - maid
  - data-tampering
  - web
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Modify-Assumed-Immutable-Data-via-API-Manipulation]]'
step_count: 1
techniques:
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:24:48.193Z'
description: >-
  A vulnerability allowing modification of data assumed to be immutable on the
  HackerOne platform, potentially enabling unauthorized changes to report
  statuses or user data.
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Stored Data Manipulation]]'
---
# Modification of Assumed-Immutable Data Leading to Data Tampering on HackerOne

Multi-stage attack chain demonstrating a complete attack workflow targeting assumed-immutable data on the HackerOne bug bounty platform.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Data Modification]
    B --> C[Impact Assessment]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools
- [[Burp Suite]]

### Target Environment

- HackerOne web platform
- API endpoints for report management
- Authenticated session

### Initial Access Requirements

- Valid HackerOne account with access to reports
- Network access to hackerone.com
- No prior elevated privileges needed

## Detailed Attack Procedures

### Step 1: Identify and Modify Assumed-Immutable Data
procedure: [[procedures/Modify-Assumed-Immutable-Data-via-API-Manipulation]]

**Objective**: Locate an API endpoint that assumes data immutability and modify it to tamper with report details, such as changing a resolved status back to open.

**Instructions**: Authenticate to HackerOne and use browser tools or a proxy to intercept requests to report management endpoints. Identify fields marked as read-only in the UI but modifiable via direct API calls. Send a modified POST or PATCH request to alter the immutable field.

For example, intercept a report update request and modify the JSON payload to change a status field:

```bash
curl -X PATCH 'https://hackerone.com/reports/1139535' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"state": "open"}'
```

Validate the change by refreshing the report page or querying the API again.

**Expected Output**: The report status updates to the modified value, confirming successful tampering.

**Success Indicators**:
- API response returns 200 OK with updated data
- UI reflects the unauthorized change
- No immediate error or rollback occurs

## Attack Chain Summary

### Key Achievements

1. Successful modification of immutable report data
2. Potential disruption to platform integrity without detection
3. Demonstration of medium-impact vulnerability (CVSS 4.6)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Stored Data Manipulation]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
