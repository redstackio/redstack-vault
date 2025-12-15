---
tags:
  - account-takeover
  - auth-bypass
  - access-control
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Intercept-Login-Request]]'
  - '[[procedures/Modify-Login-Response]]'
  - '[[procedures/Set-Target-User-Cookie]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
description: >-
  A multi-step attack exploiting improper access control in the login endpoint
  to achieve unauthorized account takeover by intercepting and modifying HTTP
  responses.
skill_level: intermediate
impact_level: high
id: 2467e93d-8880-4755-bba2-80cc731d9b6a
created_at: '2025-12-14T17:33:11.955Z'
updated_at: '2025-12-14T17:33:11.955Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Full Account Takeover via Login Response Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper access control in the Mars website's login functionality.

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
    A[Intercept Login Request] --> B[Modify Response]
    B --> C[Set Target Cookie]
    C --> D[Account Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application (e.g., Mars website)
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Ability to intercept traffic (e.g., via proxy)

### Initial Access Requirements

- No credentials required
- Network position: Man-in-the-middle capable (e.g., same network or configured proxy)
- Prior access needed: None, but victim must attempt login

## Detailed Attack Procedures

### Step 1: Intercept Login Request
procedure: [[procedures/Intercept-Login-Request]]

**Objective**: Capture the HTTP request to the login endpoint during an attempted login to prepare for response modification.

**Instructions**: Configure a proxy tool like Burp Suite to intercept traffic to the target website. Trigger a login attempt on the Mars website to capture the request.

**Expected Output**: Raw HTTP request details, including POST data to the login endpoint.

**Success Indicators**:
- HTTP request to login endpoint captured
- Request body visible with form parameters (e.g., username, password)

### Step 2: Modify Response
procedure: [[procedures/Modify-Login-Response]]

**Objective**: Alter the server's response to simulate a successful authentication, bypassing server-side checks.

**Instructions**: In the proxy tool, edit the response from the login endpoint to change status codes and body to indicate success (e.g., set status to 200 and include auth tokens).

**Expected Output**: Modified response forwarded to the client, resulting in a successful login state.

**Success Indicators**:
- Client receives faked success response
- No further auth challenges triggered

### Step 3: Set Target User Cookie
procedure: [[procedures/Set-Target-User-Cookie]]

**Objective**: Inject a cookie with the target user's ID to assume their session and gain full account access.

**Instructions**: Modify the response headers to include a Set-Cookie directive with the desired user's ID, then release the response to the client.

**Expected Output**: Browser sets the cookie, granting access to the target account.

**Success Indicators**:
- Cookie set in browser for target user
- Unauthorized access to target account confirmed (e.g., view private data)

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication without credentials
2. Achieved full account takeover for any user
3. Demonstrated impact of missing server-side response validation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01*
