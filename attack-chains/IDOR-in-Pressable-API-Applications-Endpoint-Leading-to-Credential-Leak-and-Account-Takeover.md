---
id: ac-pressable-idor-1695454
tags:
  - idor
  - api
  - credential-leak
  - account-takeover
  - pressable
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Pressable-API-Application]]'
  - '[[procedures/Intercept-API-Application-View-with-Proxy]]'
  - '[[procedures/Trigger-API-Application-Update-Request]]'
  - '[[procedures/Modify-Request-to-Exploit-IDOR]]'
  - '[[procedures/Receive-Error-Response-Leaking-Credentials]]'
  - '[[procedures/Use-Leaked-Credentials-for-Exploitation]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:24.404Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  the Pressable API to leak API credentials and achieve account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
---
# IDOR in Pressable API Applications Endpoint Leading to Credential Leak and Account Takeover

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the Pressable API applications endpoint, allowing unauthorized access to other users' API credentials and subsequent account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create API App] --> B[Intercept View]
    B --> C[Trigger Update]
    C --> D[Modify Request for IDOR]
    D --> E[Leak Credentials]
    E --> F[Exploit with Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Pressable API service (https://my.pressable.com/api/applications)
- Ruby on Rails backend (inferred from authenticity_token)
- No specific ports required; standard HTTPS

### Initial Access Requirements

- Valid Pressable account credentials for initial API app creation
- Network access to https://my.pressable.com
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Create API Application
procedure: [[procedures/Create-Pressable-API-Application]]

**Objective**: Establish a legitimate API application to use as a base for intercepting and modifying requests.

**Instructions**: Navigate to the Pressable API applications page and create a new application.

**Expected Output**: New API application created with its own ID.

**Success Indicators**:
- Application listed in the dashboard
- Application ID visible

### Step 2: Intercept Application Details View with Proxy
procedure: [[procedures/Intercept-API-Application-View-with-Proxy]]

**Objective**: Set up monitoring to capture the update request for the created application.

**Instructions**: Click on the created application and configure the proxy to intercept traffic.

**Expected Output**: Proxy captures the GET request to view application details.

**Success Indicators**:
- Traffic visible in proxy interface
- No errors in proxy setup

### Step 3: Trigger Update Request
procedure: [[procedures/Trigger-API-Application-Update-Request]]

**Objective**: Initiate the POST request to the update endpoint to enable modification.

**Instructions**: Click the 'Update' button to send the POST request with application parameters.

**Expected Output**: Intercepted POST request containing application[id] and authenticity_token.

**Success Indicators**:
- Request body includes required parameters
- Proxy successfully intercepts the request

### Step 4: Modify Request to Exploit IDOR
procedure: [[procedures/Modify-Request-to-Exploit-IDOR]]

**Objective**: Alter the application ID to target a victim's application and strip unnecessary parameters to trigger the leak.

**Instructions**: In the proxy, change application%5Bid%5D to the target's ID and remove all other parameters except authenticity_token.

**Expected Output**: Modified POST request ready for forwarding.

**Success Indicators**:
- Parameter application[id] updated to victim ID
- Only essential parameters remain

### Step 5: Receive Error Response Leaking Credentials
procedure: [[procedures/Receive-Error-Response-Leaking-Credentials]]

**Objective**: Send the modified request to provoke an error that exposes the victim's Client ID and Secret.

**Instructions**: Forward the modified request to the server.

**Expected Output**: Error message ('Name must be provided') but the response renders the victim's application page with credentials.

**Success Indicators**:
- Credentials visible in the response
- Victim's application details displayed

### Step 6: Use Leaked Credentials for Further Exploitation
procedure: [[procedures/Use-Leaked-Credentials-for-Exploitation]]

**Objective**: Authenticate with the leaked credentials to perform unauthorized actions, such as adding collaborators for takeover.

**Instructions**: Use the Client ID and Secret to make API calls to endpoints like collaborator bulk create.

**Expected Output**: Successful API actions on the victim's account.

**Success Indicators**:
- API authentication succeeds
- Unauthorized changes applied to victim account

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to any API application's credentials via IDOR manipulation
2. Leak of Client ID and Client Secret through error handling
3. Full account takeover by adding collaborators using leaked tokens

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

---
*Last updated: 2023-10-01T00:00:00Z*
