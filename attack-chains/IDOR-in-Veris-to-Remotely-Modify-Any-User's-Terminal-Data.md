---
tags:
  - idor
  - web
  - authorization-bypass
  - data-modification
  - veris
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-to-Modify-User-Terminal-Data-in-Veris]]'
step_count: 3
techniques:
  - '[[Unused-Unsupported Cloud Regions]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.312Z'
description: >-
  An authenticated user exploits an Insecure Direct Object Reference (IDOR)
  vulnerability in the Veris application to modify any other user's sensitive
  terminal data via manipulated PUT requests, leading to potential privilege
  escalation or data tampering.
skill_level: intermediate
impact_level: high
id: abd2ae0e-9563-49d0-b2a0-a5a75bdb644d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unused-Unsupported Cloud Regions]]'
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in Veris to Remotely Modify Any User's Terminal Data

Multi-stage attack chain demonstrating exploitation of a critical IDOR vulnerability in the Veris web application. An authenticated user can inspect HTTP requests to identify the terminal update endpoint, manipulate the terminal/gatekeeper ID to target another user's data, and perform unauthorized modifications via PUT requests. This bypasses authorization checks, allowing tampering with sensitive terminal configurations that could enable privilege escalation, such as altering access controls or injecting malicious data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify PUT Endpoint] --> B[Manipulate ID for Target User] --> C[Verify Unauthorized Modification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (Veris platform)
- Authenticated session required
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid authenticated user credentials for Veris
- Network access to the Veris application
- Proxy tool like Burp Suite for request interception and modification

## Detailed Attack Procedures

### Step 1: Identify the PUT Endpoint
procedure: [[procedures/Exploit-IDOR-to-Modify-User-Terminal-Data-in-Veris]]

**Objective**: Locate the HTTP PUT endpoint used for updating terminal data by inspecting legitimate requests from an authenticated session.

**Instructions**: Log in to the Veris application and perform a normal terminal data update action. Use [[tools/Burp-Suite]] to intercept the request and note the endpoint structure, including the terminal/gatekeeper ID parameter specific to your own user.

**Expected Output**: Captured PUT request showing the endpoint (e.g., `/api/terminal/update`) and the ID parameter (e.g., `{"terminal_id": "your_user_id", "data": {...}}`).

**Success Indicators**:
- PUT request intercepted with identifiable ID parameter
- Endpoint confirmed for terminal/gatekeeper data updates

### Step 2: Manipulate Request to Target Another User
procedure: [[procedures/Exploit-IDOR-to-Modify-User-Terminal-Data-in-Veris]]

**Objective**: Alter the terminal/gatekeeper ID in the PUT request to reference another user's resource and send the modified request to perform unauthorized data changes.

**Instructions**: In [[tools/Burp-Suite]], edit the intercepted PUT request by replacing the ID with a target user's ID (obtained via enumeration or known value). Update the payload with arbitrary terminal data, such as changing configurations or injecting values. Forward the request to the server.

Use [[commands/curl-put-modify-terminal]] as an alternative for scripted testing:

```bash
curl -X PUT -H "Authorization: Bearer your_token" -H "Content-Type: application/json" -d '{"terminal_id": "target_user_id", "gatekeeper_data": {"key": "malicious_value"}}' https://veris.example.com/api/terminal/update
```

**Expected Output**: HTTP 200 OK response indicating successful update without authorization errors.

**Success Indicators**:
- Request accepted and processed
- No 403 Forbidden or authorization denial

### Step 3: Verify the Exploitation
procedure: [[procedures/Exploit-IDOR-to-Modify-User-Terminal-Data-in-Veris]]

**Objective**: Confirm that the targeted user's terminal data has been modified as intended, validating the IDOR impact.

**Instructions**: Access the Veris application as the target user or use an administrative view to inspect the terminal/gatekeeper data. Alternatively, send a GET request to retrieve the updated data using [[tools/Burp-Suite]] or [[commands/curl-get-terminal-data]]:

```bash
curl -H "Authorization: Bearer target_token" https://veris.example.com/api/terminal/target_user_id
```

Check for the injected or modified values in the response.

**Expected Output**: Retrieved data reflects the unauthorized changes made in Step 2.

**Success Indicators**:
- Modified data visible in target user's terminal configuration
- Evidence of tampering, such as altered settings or injected payloads

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to access and modify arbitrary user terminal data
2. Demonstrated potential for privilege escalation by altering sensitive configurations
3. Highlighted critical IDOR flaw leading to rapid resolution by the Veris team

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unused-Unsupported Cloud Regions]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
