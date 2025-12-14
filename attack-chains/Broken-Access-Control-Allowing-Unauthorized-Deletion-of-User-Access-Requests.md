---
id: ac-uuid-1493007
tags:
  - broken-access-control
  - idor
  - data-manipulation
  - data-loss
  - dod
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Create-and-Extract-Access-Request-ID]]'
  - '[[procedures/Delete-Access-Request-via-Broken-Endpoint]]'
  - '[[procedures/Verify-Access-Request-Existence]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Manipulation]]'
updated_at: '2025-12-14T17:28:59.073Z'
description: >-
  Multi-stage attack exploiting broken access control in a DoD user access
  request system to delete any user's request by ID without authentication,
  causing data loss and operational disruption.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data Manipulation]]'
---
# Broken Access Control Allowing Unauthorized Deletion of User Access Requests

Multi-stage attack chain demonstrating exploitation of a broken access control vulnerability in a U.S. Department of Defense information system's user access request functionality. An attacker can delete any user's access request by supplying the sequential request ID to the delete endpoint without any authentication or authorization checks. This leads to unauthorized data loss, disruption of legitimate user access processes, and potential denial of service for the system. The attack relies on intercepting traffic to obtain IDs and exploiting related endpoints for verification.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit and Intercept Request] --> B[Extract Request ID]
    B --> C[Verify Existence Optional]
    C --> D[Delete Request]
    D --> E[Verify Deletion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web-based DoD information system with user access request functionality
- Access to https://█████████/████████ or https://█████████/██████ endpoints
- Network access to the target system (no authentication required for exploitation)

### Initial Access Requirements

- No credentials needed; attacker requires only network connectivity to the public-facing endpoints
- Burp Suite configured as a proxy for traffic interception

## Detailed Attack Procedures

### Step 1: Submit and Intercept Access Request
procedure: [[procedures/Create-and-Extract-Access-Request-ID]]

**Objective**: Create a test user access request and intercept the server response to obtain the sequential request ID.

**Instructions**: Configure Burp Suite as a proxy and navigate to the request form at https://█████████/████████ or https://█████████/██████. Fill out and submit the form while intercepting the traffic.

**Expected Output**: Server response containing the new request ID (a sequential number).

**Success Indicators**:
- Form submission intercepted in Burp
- Request ID visible in the response body

### Step 2: Verify Request Existence (Optional)
procedure: [[procedures/Verify-Access-Request-Existence]]

**Objective**: Confirm the request was created and exists in the database using a related vulnerability for exfiltration.

**Instructions**: Use the extracted ID in the verification command to exfiltrate the request details.

Execute [[commands/exfiltrate-access-request]]:

```bash
curl https://██████/██████████ -X POST -data="url=%2F████&██████████=████████" -k
```

**Expected Output**: Exfiltrated request data if the request exists.

**Success Indicators**:
- Response contains request details
- Confirms ID is valid and request is present

### Step 3: Delete Access Request
procedure: [[procedures/Delete-Access-Request-via-Broken-Endpoint]]

**Objective**: Exploit the broken access control to delete the target request without authorization.

**Instructions**: Supply the request ID to the delete endpoint via POST request.

Execute [[commands/delete-access-request]]:

```bash
curl https://██████/███████████████ -X POST -data="url=%2F███████&███████=██████" -k
```

**Expected Output**: Successful deletion (typically no body or success status; request removed from database).

**Success Indicators**:
- No error response indicating permission denied
- Subsequent verification shows empty response

### Step 4: Verify Deletion (Optional)
procedure: [[procedures/Verify-Access-Request-Existence]]

**Objective**: Confirm the deletion by attempting to exfiltrate the request again.

**Instructions**: Re-run the verification command with the same ID.

Execute [[commands/exfiltrate-access-request]]:

```bash
curl https://██████/██████████ -X POST -data="url=%2F████&██████████=████████" -k
```

**Expected Output**: Empty response body, indicating the request is no longer in the database.

**Success Indicators**:
- Empty or error response on exfiltration
- Request confirmed deleted

## Attack Chain Summary

### Key Achievements

1. Unauthorized creation and ID extraction of access requests via intercepted traffic
2. Exploitation of unauthenticated delete endpoint to remove any request by sequential ID
3. Verification of impact through related exfiltration vulnerability, demonstrating data loss

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data Manipulation]] Data Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2024-01-01T00:00:00Z*
