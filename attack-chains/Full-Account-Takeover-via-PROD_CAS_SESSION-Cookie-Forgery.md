---
tags:
  - auth-bypass
  - cookie-forgery
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Navigate-to-Target-Application]]'
  - '[[procedures/Forge-PROD-CAS-SESSION-Cookie]]'
  - '[[procedures/Refresh-Page-to-Authenticate]]'
  - '[[procedures/Access-Victim-Profile]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.139Z'
description: >-
  A multi-stage attack exploiting insecure session cookie handling to
  impersonate any user by forging the PROD_CAS_SESSION cookie with a known
  6-digit User ID, leading to complete account takeover.
skill_level: beginner
impact_level: high
id: 3b8b723d-d020-4369-8b68-63507527d2c6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Full Account Takeover via PROD_CAS_SESSION Cookie Forgery

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of validation on the PROD_CAS_SESSION cookie in a U.S. Department of Defense application, allowing attackers to impersonate users by directly setting the cookie value to a 6-digit User ID.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Application] --> B[Forge Session Cookie]
    B --> C[Refresh to Authenticate]
    C --> D[Access Victim Profile]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools)

### Target Environment

- Web application at https://██████/MOS/ or similar entry points
- Knowledge of the victim's 6-digit User ID (e.g., obtained via enumeration or social engineering)

### Initial Access Requirements

- No credentials required
- Direct network access to the target website
- No prior access needed beyond public internet

## Detailed Attack Procedures

### Step 1: Navigate to Target Application
procedure: [[procedures/Navigate-to-Target-Application]]

**Objective**: Gain initial access to the application's entry point to prepare for cookie manipulation.

**Instructions**: Open a web browser and directly access one of the application's entry points.

**Expected Output**: The login or main page of the application loads without authentication.

**Success Indicators**:
- Page loads successfully at https://██████/MOS/
- No authentication prompts appear initially

### Step 2: Forge PROD_CAS_SESSION Cookie
procedure: [[procedures/Forge-PROD-CAS-SESSION-Cookie]]

**Objective**: Modify the session cookie to impersonate the victim by setting it to their 6-digit User ID.

**Instructions**: Use the browser's developer tools to inspect and edit cookies. Set the PROD_CAS_SESSION cookie for the domain **███** with the value as the victim's User ID (e.g., 195141).

**Expected Output**: Cookie is updated in the browser's storage without errors.

**Success Indicators**:
- Cookie value matches the victim's ID in dev tools
- No immediate errors or redirects

### Step 3: Refresh Page to Authenticate
procedure: [[procedures/Refresh-Page-to-Authenticate]]

**Objective**: Apply the forged cookie to establish a session as the victim.

**Instructions**: Reload the current page to trigger the application's session validation using the modified cookie.

**Expected Output**: The page refreshes, and the interface updates to show the victim as logged in (e.g., 'Welcome [Victim's Name]' in the top-right dropdown).

**Success Indicators**:
- User interface reflects victim's session
- Dropdown menu appears with victim's name

### Step 4: Access Victim Profile
procedure: [[procedures/Access-Victim-Profile]]

**Objective**: Confirm takeover by viewing and accessing the victim's personal information.

**Instructions**: Click the top-right dropdown showing the victim's name and select 'My Profile' to load the profile page.

**Expected Output**: Victim's profile loads, displaying personal details and any associated data.

**Success Indicators**:
- Profile page accessible with victim's information
- Full impersonation confirmed

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication without credentials
2. Impersonated any user with known ID
3. Accessed sensitive profile data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2024-01-01T00:00:00Z*
