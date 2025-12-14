---
tags:
  - path-traversal
  - csrf
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Developer-Tools]]'
  - '[[tools/Intercepting-Proxy]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Vulnerable-URL-for-User-Confirmation]]'
  - '[[procedures/Inspect-Network-Traffic-for-Unauthorized-Requests]]'
  - '[[procedures/Repeat-for-Password-Reset-Endpoint]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:27:50.506Z'
description: >-
  Demonstrates path traversal vulnerability in invitation_token parameter on
  user confirmation and password reset endpoints, enabling unauthorized GET
  requests and limited CSRF exploitation.
skill_level: intermediate
impact_level: medium
id: 55397fa7-0561-46c4-9254-d9a6c83973ee
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal in Invitation Token Leading to Limited CSRF on GET Requests

Multi-stage attack chain demonstrating path traversal in the invitation_token parameter on HackerOne's user confirmation and password reset endpoints, leading to unauthorized GET requests and potential limited CSRF exploitation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Craft Vulnerable URL] --> B[Inspect Network Traffic]
    B --> C[Repeat on Password Endpoint]
    C --> D[Observe Unauthorized GET]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Developer-Tools]]
- [[tools/Intercepting-Proxy]]

### Target Environment

- Web application (e.g., HackerOne platform)
- Browser with developer tools enabled
- Access to intercepting proxy for traffic monitoring

### Initial Access Requirements

- Valid target URL (e.g., https://hackerone.com)
- No authentication required for public endpoints
- Network access to the target domain

## Detailed Attack Procedures

### Step 1: Craft Vulnerable URL for User Confirmation
procedure: [[procedures/Craft-Vulnerable-URL-for-User-Confirmation]]

**Objective**: Construct a URL with path traversal in the invitation_token to trigger access to an arbitrary internal path.

**Instructions**: Open a browser and navigate to the crafted URL: https://hackerone.com/users/confirmation?confirmation_token=z2-aaa&invitation_token=/../../test. This uses '../' sequences to traverse to /test.json.

**Expected Output**: The page loads, but subsequent steps will reveal the unauthorized request.

**Success Indicators**:
- URL accessed without errors
- No immediate access denial

### Step 2: Inspect Network Traffic for Unauthorized Requests
procedure: [[procedures/Inspect-Network-Traffic-for-Unauthorized-Requests]]

**Objective**: Monitor and capture the unauthorized GET request triggered by the path traversal.

**Instructions**: With developer tools or an intercepting proxy active, reload the vulnerable URL and inspect the network tab or proxy logs for requests to unintended paths like https://hackerone.com/test.json.

**Expected Output**: Log entry showing a GET request to /test.json from the target domain.

**Success Indicators**:
- Unauthorized GET request observed in traffic
- Request originates from the legitimate domain but targets arbitrary path

### Step 3: Repeat for Password Reset Endpoint
procedure: [[procedures/Repeat-for-Password-Reset-Endpoint]]

**Objective**: Validate the vulnerability on the password reset endpoint to confirm consistency.

**Instructions**: Craft and access https://hackerone.com/users/password/new?invitation_token=/../../test, then inspect traffic as in Step 2 for the same unauthorized GET to /test.json.

**Expected Output**: Similar unauthorized request logged for the password endpoint.

**Success Indicators**:
- Path traversal confirmed on second endpoint
- Potential for CSRF chaining identified

## Attack Chain Summary

### Key Achievements

1. Successful path traversal in invitation_token parameter
2. Observation of unauthorized internal GET requests
3. Demonstration of limited CSRF potential on both endpoints

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
