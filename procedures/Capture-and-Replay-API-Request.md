---
id: proc-3371448-request-replay
tags:
  - request-interception
  - api-replay
  - authorization-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/analyze-api-request]]'
  - '[[commands/modify-jwt-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.417Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Capture-and-Replay-API-Request

## Summary

This procedure involves intercepting an API request from a privileged user, modifying it with lower-privilege credentials, and replaying it to test for authorization flaws, specifically in the context of the Lovable AI API.

## Description

By using a proxy to capture HTTP requests during an admin action, this procedure allows analysis and alteration of requests (e.g., swapping JWT tokens) before replay. In the Lovable AI case, it reveals the lack of server-side validation on the AI toggle endpoint, enabling Editors to perform admin actions. This is effective against APIs using JWT without proper RBAC enforcement, leading to privilege escalation.

## Requirements

1. Proxy tool configured between browser and API (e.g., Burp Suite)
2. Access to both Admin and Editor sessions
3. Knowledge of the target endpoint and payload structure
4. HTTPS interception capabilities (CA certificate installed)

## Defense

Defensive measures and detection strategies:

- Validate JWT claims (roles) on every sensitive endpoint server-side
- Implement request signing or CSRF tokens for state-changing actions
- Monitor for request patterns indicating replay attacks (e.g., via SIEM)
- Use WAF rules to block unauthorized endpoint access

## Objectives

1. Identify and extract API request details for exploitation
2. Modify requests to simulate privilege abuse
3. Confirm successful replay without authentication failure

## Instructions

### Step 1: Set Up Interception

**Context**: Configure a proxy to capture traffic from the web interface.

Install and run Burp Suite, configure browser proxy to 127.0.0.1:8080, and ensure HTTPS interception is enabled.

No command; use tool UI to start proxy.

### Step 2: Capture and Analyze Request

**Context**: Perform the action to trigger and intercept the request.

**Command** ([[commands/analyze-api-request]]):
```bash
echo 'POST https://lovable-api.com/workspaces/<WORKSPACE_ID>/tool-preferences/ai_gateway/enable' \
  'Headers: Authorization: Bearer <ADMIN_JWT>, Content-Type: application/json' \
  'Body: {"approval_preference":"disable"}'
```

> Outputs request for review; copy from Burp's Proxy history. Expected output: Formatted request details for modification.

### Step 3: Modify and Prepare Replay

**Context**: Alter the Authorization header in the intercepted request.

**Command** ([[commands/modify-jwt-request]]):
```bash
# Manual modification simulation (use Burp Repeater tab in practice)
sed 's/Bearer <ADMIN_JWT>/Bearer <EDITOR_JWT>/g' captured_request.txt > modified_request.txt
```

> Replaces token; expected output: Updated request file ready for curl replay.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/analyze-api-request]]
- [[commands/modify-jwt-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-interception]]
- [[api-replay]]
- [[jwt-modification]]
