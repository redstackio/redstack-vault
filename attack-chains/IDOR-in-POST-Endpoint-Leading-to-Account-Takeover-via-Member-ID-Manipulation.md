---
tags:
  - idor
  - account-takeover
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-05T12:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-POST-Endpoint-for-IDOR]]'
  - '[[procedures/Manipulate-Member-ID-Parameter-in-Request]]'
  - '[[procedures/Submit-Tampered-Request-for-Account-Takeover]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.291Z'
description: >-
  A multi-step attack exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in a POST endpoint by manipulating the member_id parameter to
  achieve unauthorized access and full control over another user's account.
skill_level: intermediate
impact_level: high
id: 07fd97f0-0eff-4664-a29c-6d17f20627e4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# IDOR in POST Endpoint Leading to Account Takeover via Member ID Manipulation

Multi-stage attack chain demonstrating a complete workflow for exploiting an IDOR vulnerability to take over user accounts via parameter manipulation in a web application.

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
    A[Identify Endpoint] --> B[Manipulate Parameter]
    B --> C[Submit Request]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- Browser developer tools or [[commands/curl-post-request]]

### Target Environment

- Web application with POST endpoints handling user data
- Access to the application's API or web interface
- Knowledge of the target's user ID structure (e.g., numeric IDs)

### Initial Access Requirements

- Valid session or authentication to the application (e.g., logged-in user account)
- Network access to the web application
- No prior elevated privileges needed, but authenticated access enables testing

## Detailed Attack Procedures

### Step 1: Identify Vulnerable POST Endpoint
procedure: [[procedures/Identify-Vulnerable-POST-Endpoint-for-IDOR]]

**Objective**: Locate the POST endpoint that processes the member_id parameter without proper authorization checks, setting the stage for IDOR exploitation.

**Instructions**: Use browser developer tools or a proxy like Burp Suite to inspect network traffic while interacting with account-related features. Look for POST requests containing a member_id parameter. Test the endpoint by sending a legitimate request with your own member_id.

Execute a sample POST request using [[commands/curl-identify-post-endpoint]] to confirm the endpoint's behavior:

```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "YOUR_ID"}'
```

**Expected Output**: A successful response (e.g., 200 OK) confirming the endpoint processes the member_id without errors for the authenticated user.

**Success Indicators**:
- Endpoint identified and responds to legitimate requests
- member_id parameter observed in request body

### Step 2: Manipulate Member ID Parameter
procedure: [[procedures/Manipulate-Member-ID-Parameter-in-Request]]

**Objective**: Tamper with the member_id to reference a target victim's account, bypassing authorization to access or modify their data.

**Instructions**: Intercept the legitimate POST request using a tool like Burp Suite. Replace the member_id value with the victim's ID (e.g., obtained from enumeration or known values). Ensure the request retains your authentication headers to simulate an authorized but misdirected action.

Modify and test using [[commands/curl-manipulate-member-id]]:

```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID"}'
```

**Expected Output**: The server processes the request for the victim's account without rejecting it, indicating IDOR success (e.g., returns or modifies victim data).

**Success Indicators**:
- Request accepted with altered member_id
- Response contains or affects victim's account data

### Step 3: Submit Tampered Request for Account Takeover
procedure: [[procedures/Submit-Tampered-Request-for-Account-Takeover]]

**Objective**: Execute the tampered request to gain full control over the victim's account, such as changing credentials or accessing sensitive information.

**Instructions**: With the manipulated member_id, submit actions that alter account details (e.g., update password, email, or enable features). Repeat if needed for persistent access. Verify takeover by attempting login or data access with victim credentials if obtained.

Perform the takeover using [[commands/curl-submit-takeover-request]]:

```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID", "new_password": "ATTACKER_PASSWORD"}'
```

**Expected Output**: Confirmation of update (e.g., 200 OK with success message), allowing subsequent login as the victim.

**Success Indicators**:
- Victim's account modified (e.g., password changed)
- Attacker gains login access to victim's account

## Attack Chain Summary

### Key Achievements

1. Identified and confirmed the IDOR-vulnerable endpoint
2. Successfully manipulated the member_id to target arbitrary accounts
3. Achieved complete account takeover, enabling data access and modification

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Persistence]]

---
*Last updated: 2023-10-05T12:00:00Z*
