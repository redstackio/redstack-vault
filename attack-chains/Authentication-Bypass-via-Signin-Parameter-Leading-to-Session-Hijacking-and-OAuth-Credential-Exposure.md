---
id: ac-uuid-001
tags:
  - auth-bypass
  - session-hijacking
  - oauth-exposure
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Login-Endpoint]]'
  - '[[procedures/Bypass-Authentication-Using-Signin-Parameter]]'
  - '[[procedures/Perform-Session-Hijacking-via-Malicious-Link]]'
  - '[[procedures/Extract-Exposed-OAuth-Credentials]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:52.406Z'
description: >-
  A multi-stage attack exploiting improper authentication in a web application
  to bypass login as any user, hijack sessions via malicious links, and expose
  OAuth credentials from page source.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
---
# Authentication Bypass via Signin Parameter Leading to Session Hijacking and OAuth Credential Exposure

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper authentication in a web application's login endpoint.

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
    A[Access Login Endpoint] --> B[Exploit Auth Bypass]
    B --> C[Session Hijacking]
    C --> D[Extract OAuth Credentials]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome Developer Tools for inspection)
- No specialized tools required; manual URL crafting suffices.

### Target Environment

- Web application with SSO and OAuth integration
- Services: SSO (pool/sso/authenticate)
- Tech stack: OAuth, SSO
- Network access: Direct access to the login endpoint

### Initial Access Requirements

- No prior credentials needed
- Attacker must be able to craft and send GET requests or links
- Victim interaction required for session hijacking

## Detailed Attack Procedures

### Step 1: Access Login Endpoint
procedure: [[procedures/Access-Login-Endpoint]]

**Objective**: Locate and navigate to the vulnerable login endpoint to prepare for exploitation.

**Instructions**: Open a web browser and directly access the login URL, such as the redacted endpoint for the SSO authentication service.

**Expected Output**: The login page loads, revealing the endpoint structure for further manipulation.

**Success Indicators**:
- Login page accessible without errors
- Endpoint URL confirmed (e.g., contains /sso/authenticate)

### Step 2: Bypass Authentication Using Signin Parameter
procedure: [[procedures/Bypass-Authentication-Using-Signin-Parameter]]

**Objective**: Authenticate as any arbitrary user without credentials or registration by manipulating the signin parameter.

**Instructions**: Modify the login URL by appending the ?signin= parameter with an arbitrary user identifier, such as ?signin=targetuser. Access the crafted URL via GET request to bypass login and gain access to protected resources like /portal/index.php.

**Expected Output**: Successful authentication as the specified user, redirecting to protected areas without prompting for credentials.

**Success Indicators**:
- Access granted to /portal/index.php or similar
- No login form or error displayed

### Step 3: Perform Session Hijacking via Malicious Link
procedure: [[procedures/Perform-Session-Hijacking-via-Malicious-Link]]

**Objective**: Force a logged-in victim to switch sessions to the attacker's targeted user via a crafted malicious link.

**Instructions**: While the victim is logged in as user A, send them a malicious GET link containing the ?signin=targetuser parameter (e.g., via email or chat). Upon clicking, the victim's session logs out and authenticates as user B.

**Expected Output**: Victim's browser authenticates as the targeted user, granting access to their resources.

**Success Indicators**:
- Victim reports unexpected logout and login as another user
- Attacker observes session changes in application logs or behavior

### Step 4: Extract Exposed OAuth Credentials
procedure: [[procedures/Extract-Exposed-OAuth-Credentials]]

**Objective**: Inspect the page source to retrieve plaintext client ID and secret for potential further OAuth exploitation.

**Instructions**: After authentication, navigate to areas involving OAuth workflow and use browser developer tools to view the page source. Search for clientid and clientsecret values stored in plaintext.

**Expected Output**: Plaintext extraction of client ID and secret from JavaScript or HTML elements.

**Success Indicators**:
- Client ID and secret visible in source code
- No obfuscation or encryption present

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication for arbitrary users without credentials
2. Hijacked victim sessions through simple link sharing
3. Exposed sensitive OAuth credentials enabling further attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unsecured Credentials]] Unsecured Credentials

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---

*Last updated: 2023-10-01T00:00:00Z*
