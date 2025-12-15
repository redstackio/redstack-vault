---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: IDOR in Lark AutoReply to Steal Private Files
tags:
  - idor
  - lark
  - autoreply
  - file-theft
  - unauthorized-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Lark-AutoReply]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:28.508Z'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in Lark's AutoReply feature to access and steal other users'
  private files by manipulating file IDs without authorization checks.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in Lark AutoReply to Steal Private Files

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in Lark's AutoReply functions to steal private files.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify AutoReply Feature] --> B[Manipulate File ID for Unauthorized Access]
    B --> C[Exfiltrate Private Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or [[tools/Burp-Suite]] for request manipulation

### Target Environment

- Lark web application (platform: Web)
- Access to a Lark account
- Knowledge of target user's file ID (alphanumeric)

### Initial Access Requirements

- Valid Lark user credentials for initial login
- Network access to Lark's web services
- No prior elevated access needed, but authenticated session required

## Detailed Attack Procedures

### Step 1: Identify AutoReply Function
procedure: [[procedures/Explore-Lark-AutoReply-Feature]]

**Objective**: Explore the AutoReply features to understand file referencing via alphanumeric IDs and identify potential manipulation points.

**Instructions**: Log in to your Lark account and navigate to the AutoReply settings. Use browser developer tools to inspect how files are attached or referenced in AutoReply configurations. Note the structure of requests involving file IDs, which are alphanumeric strings without session-bound checks.

**Expected Output**: Identification of API endpoints or response fields that directly reference file IDs, such as in JSON payloads for AutoReply setup.

**Success Indicators**:
- AutoReply interface accessed successfully
- File ID format observed (e.g., 'abc123def456')

### Step 2: Manipulate Response to Access Private Files
procedure: [[procedures/Exploit-IDOR-in-Lark-AutoReply]]

**Objective**: Exploit the lack of authorization checks by injecting a known target file ID into AutoReply requests or responses to retrieve unauthorized private files.

**Instructions**: With a known file ID from another user (obtained via enumeration or prior knowledge), modify the AutoReply request payload to reference that ID. Use a tool like Burp Suite to intercept and alter the request, or craft a direct API call. For example, send a POST request to the AutoReply endpoint with the manipulated file ID in the body.

**Expected Output**: Server response containing the private file content or download link, confirming unauthorized access.

**Success Indicators**:
- Private file retrieved without ownership errors
- File content exfiltrated (e.g., downloaded to local system)

## Attack Chain Summary

### Key Achievements

1. Discovered IDOR in AutoReply by exploring file ID handling
2. Successfully manipulated requests to access other users' private files
3. Demonstrated high-impact data theft, leading to vulnerability disclosure and bounty

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T12:00:00Z*
