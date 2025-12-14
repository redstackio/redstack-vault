---
id: proc-uuid-delete
tags:
  - broken-access-control
  - data-manipulation
  - unauthorized-deletion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/delete-access-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:28:59.063Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Data Manipulation]]'
---
# Delete-Access-Request-via-Broken-Endpoint

## Summary

This procedure exploits a broken access control vulnerability in the DoD system's delete endpoint to remove any user access request by providing its sequential ID via POST, without requiring authentication or authorization, resulting in data loss for legitimate users.

## Description

The delete endpoint at https://██████/███████████████ lacks proper checks, allowing unauthenticated attackers to delete requests by specifying the ID in the '███████' parameter alongside an encoded 'url' path. Request IDs are sequential, enabling enumeration and mass deletion. This targets web-based systems; prerequisites include a known ID from prior steps. The outcome is permanent removal of the request from the database, disrupting operations and causing integrity violations.

## Requirements

1. Known sequential request ID from creation or enumeration
2. Network access to the delete endpoint
3. curl or similar tool for HTTP POST requests
4. Caution: Target only test/own requests to avoid impacting production data

## Defense

Defensive measures and detection strategies:

- Enforce authentication and authorization on all delete endpoints (e.g., JWT validation, role-based access)
- Implement ID obfuscation or non-sequential generation to hinder enumeration
- Monitor delete API calls for unauthenticated sources and log anomalous IP patterns

## Objectives

1. Perform unauthorized deletion of a target access request
2. Demonstrate lack of access controls leading to data loss
3. Disrupt system operations by removing legitimate requests

## Instructions

### Step 1: Prepare the Request

**Context**: Encode the required parameters for the delete endpoint, using the extracted ID.

Replace '███████' with the target ID (e.g., 12345) in the data payload.

### Step 2: Execute Deletion

**Context**: Send a POST request to the vulnerable endpoint to trigger the deletion.

**Command** ([[commands/delete-access-request]]):
```bash
curl https://██████/███████████████ -X POST -data="url=%2F███████&███████=██████" -k
```

> This command posts to the delete endpoint with the encoded URL path and ID parameter. The -k flag ignores SSL certificate validation. Expected output is a success response (e.g., 200 OK) with no body, but the request is removed from the database.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Data Manipulation]] Data Manipulation

### Sub-Techniques


## Commands Used

- [[commands/delete-access-request]]

## Tools Used


## Tags

- [[broken-access-control]]
- [[data-manipulation]]
- [[unauthorized-deletion]]
