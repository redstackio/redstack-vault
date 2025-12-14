---
tags:
  - nextcloud
  - api-bypass
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/nextcloud-delete-workflow-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.937Z'
sub_techniques: []
id: 4ceed787-e79c-4ce0-8bd6-d0cac0f2d32e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Deletion-via-OCS-API

## Summary

This procedure exploits the lack of password confirmation in Nextcloud's OCS API to delete a user workflow directly, bypassing the UI security control and enabling unauthorized destructive actions.

## Description

The vulnerability stems from the OCS API endpoint `/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/{id}` not enforcing the same contextual checks as the web UI. Using an authenticated session (via cookies or tokens), a DELETE request deletes the workflow without verification. This targets Nextcloud with workflowengine on PHP, leading to potential data loss or privilege escalation in configurations.

## Requirements

1. Authenticated session cookie or OCS API token
2. Known workflow ID from prior creation
3. Network access to Nextcloud OCS endpoint
4. Tool like curl for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement uniform access controls across UI and API endpoints
- Log all API deletion requests with user context and audit for anomalies
- Require additional MFA for destructive API actions

## Objectives

1. Delete workflow without password prompt
2. Demonstrate broken context-dependent access control
3. Highlight risk of API direct access

## Instructions

### Step 1: Prepare Authenticated Request

**Context**: Ensure the request includes authentication to access the user-owned workflow.

**Command** (Session Setup):

Extract session cookie from browser or use API token.

> Use in subsequent curl headers. Expected output: Valid auth for API.

### Step 2: Send DELETE Request

**Context**: Target the specific workflow ID via the OCS API to bypass UI.

**Command** ([[commands/nextcloud-delete-workflow-api]]):
```bash
curl -X DELETE "https://nextcloud.example.com/ocs/v2.php/apps/workflowengine/api/v1/workflows/user/3?format=json" -H "OCS-APIRequest: true" -b "cookie_session=your_session_cookie"
```

> Executes the deletion. Expected output: HTTP 200 OK with JSON like {"ocs":{"meta":{"status":"ok","statuscode":200,"message":"OK"},"data":[]}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/nextcloud-delete-workflow-api]]

## Tools Used


## Tags

- [[nextcloud]]
- [[api-bypass]]
- [[access-control]]
