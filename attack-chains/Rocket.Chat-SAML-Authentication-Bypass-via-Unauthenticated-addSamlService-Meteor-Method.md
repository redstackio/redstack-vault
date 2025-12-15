---
tags:
  - saml
  - auth-bypass
  - rocket-chat
  - meteor
  - javascript
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Rocket.Chat-Login-Page-with-SAML-Enabled]]'
  - '[[procedures/Disable-SAML-Signature-Verification-via-addSamlService]]'
  - '[[procedures/Submit-Faked-SAML-Response-for-User-Impersonation]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.244Z'
description: >-
  Unauthenticated exploitation of the addSamlService Meteor method in
  Rocket.Chat to disable SAML signature verification, enabling impersonation of
  arbitrary users including administrators via faked SAML responses.
skill_level: intermediate
impact_level: high
id: 3a0c41ab-4fa0-4c1d-9560-f2234e87f97c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Rocket.Chat SAML Authentication Bypass via Unauthenticated addSamlService Meteor Method

Multi-stage attack chain exploiting an unauthenticated Meteor method in Rocket.Chat to bypass SAML authentication, allowing attackers to log in as any user, including administrators, by disabling signature verification and submitting forged responses.

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
    A[Access Login Page] --> B[Disable SAML Verification]
    B --> C[Submit Faked SAML Response]
    C --> D[Impersonate Admin User]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer console (e.g., Chrome DevTools)
- SAML response crafting tool (e.g., browser extensions or scripts for forging XML)

### Target Environment

- Rocket.Chat instance with SAML authentication enabled using the default 'Default' provider
- Web platform accessible via browser
- No specific ports beyond standard HTTPS (443)

### Initial Access Requirements

- Public network access to the Rocket.Chat login page
- No credentials required (unauthenticated)
- SAML provider configured with certificate settings

## Detailed Attack Procedures

### Step 1: Access Login Page
procedure: [[procedures/Access-Rocket.Chat-Login-Page-with-SAML-Enabled]]

**Objective**: Navigate to the Rocket.Chat login interface where SAML is enabled to prepare for exploitation.

**Instructions**: Open a web browser and navigate to the target's login page, ensuring SAML is configured with the 'Default' provider. Verify SAML buttons or options are visible on the page.

**Expected Output**: Login page loads with SAML authentication options displayed.

**Success Indicators**:
- SAML provider 'Default' is active
- No authentication barriers encountered

### Step 2: Disable SAML Signature Verification
procedure: [[procedures/Disable-SAML-Signature-Verification-via-addSamlService]]

**Objective**: Use the unauthenticated Meteor method to set the certificate flag to false, bypassing signature checks.

**Instructions**: Open the browser console on the login page and execute the following command using [[commands/meteor-call-addSamlService]]:

```javascript
Meteor.call("addSamlService", "Default_cert");
```

This creates a falsy certificate setting (SAML_Custom_Default_cert = false), causing the verifySignatures method to skip validation.

**Expected Output**: No errors in console; setting updated silently in the backend.

**Success Indicators**:
- Console shows successful method call without rejection
- Backend settings reflect falsy certificate value (verifiable via admin panel if accessible)

### Step 3: Submit Faked SAML Response
procedure: [[procedures/Submit-Faked-SAML-Response-for-User-Impersonation]]

**Objective**: Craft and submit a forged SAML response to authenticate as an arbitrary user.

**Instructions**: Initiate the SAML login flow (e.g., click SAML button), intercept the request (using browser tools or proxy), and replace the response XML with a faked one impersonating a target user (e.g., admin). Submit the modified response through the login form.

**Expected Output**: Successful login redirect to the dashboard as the impersonated user.

**Success Indicators**:
- Authentication succeeds without signature errors
- Access granted to administrative functions

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to disable SAML protections
2. Bypass of signature verification for forged responses
3. Full account takeover including admin privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
