---
tags:
  - saml
  - auth-bypass
  - xml-manipulation
  - rocket-chat
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/samlbypasspoc.py]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/samlbypasspoc-modify-response]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Configure-SAML-Authentication-in-Rocket.Chat]]'
  - '[[procedures/Intercept-SAML-Login-Request-with-Burp-Suite]]'
  - '[[procedures/Modify-SAML-Response-Using-Bypass-POC-Script]]'
  - '[[procedures/Forward-Modified-SAML-Response-to-Bypass-Authentication]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
description: >-
  A multi-stage attack exploiting improper SAML response validation in
  Rocket.Chat to bypass authentication and gain unauthorized access as any user,
  including administrators.
skill_level: intermediate
impact_level: high
id: 2cb73b06-6198-43c0-b62a-c5e30901efbe
created_at: '2025-12-14T17:31:19.347Z'
updated_at: '2025-12-14T17:31:19.347Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Rocket.Chat SAML Authentication Bypass via Malicious Response Prepending

## Overview

This attack chain exploits a vulnerability in Rocket.Chat's SAML response processing, where the signature is verified on the first Signature element, but assertions are pulled from the first Response element without cross-verification. By prepending a malicious unsigned Response element to a valid signed response, an attacker can bypass authentication and log in as any user, including administrators, by altering attributes like NameID, Email, and OrganizationName. The attack requires SAML configuration and uses proxy interception to modify the response in transit.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Configure SAML] --> B[Intercept Login]
    B --> C[Modify Response]
    C --> D[Forward and Bypass]
    D --> E[Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/samlbypasspoc.py]]

### Target Environment

- Rocket.Chat instance with SAML authentication enabled
- Access to configure IdP details
- Web browser for login initiation

### Initial Access Requirements

- Administrative access to Rocket.Chat for SAML setup (or pre-configured SAML)
- Network access to the Rocket.Chat login endpoint
- No prior credentials needed beyond initial setup

## Detailed Attack Procedures

### Step 1: Configure SAML Authentication
procedure: [[procedures/Configure-SAML-Authentication-in-Rocket.Chat]]

**Objective**: Set up SAML as the authentication provider to enable the vulnerable login flow.

**Instructions**: Access the Rocket.Chat administration panel and configure SAML settings with IdP details, such as entity ID, SSO URL, and certificate. Enable SAML login and save the configuration.

**Expected Output**: SAML authentication is active, and login redirects to the IdP.

**Success Indicators**:
- SAML option appears on the login page
- Test login initiates SAML flow without errors

### Step 2: Initiate Login and Intercept Request
procedure: [[procedures/Intercept-SAML-Login-Request-with-Burp-Suite]]

**Objective**: Capture the legitimate SAMLResponse during the login process for later modification.

**Instructions**: Start the SAML login flow in a browser proxied through Burp Suite. Intercept the POST request to the login endpoint containing the SAMLResponse parameter.

**Expected Output**: Intercepted request with base64 URL-encoded SAMLResponse.

**Success Indicators**:
- Request captured showing SAMLResponse in the body
- Original response decodes to valid XML with signed Response and assertions

### Step 3: Modify SAML Response
procedure: [[procedures/Modify-SAML-Response-Using-Bypass-POC-Script]]

**Objective**: Craft a malicious SAMLResponse by prepending an unsigned Response with altered assertions while preserving the original signature.

**Instructions**: Decode the intercepted SAMLResponse if needed, then execute [[commands/samlbypasspoc-modify-response]] with the URL-encoded value:

```bash
python3 samlbypasspoc.py <URL_encoded_SAMLResponse>
```

Edit the script to set malicious values (e.g., NameID to admin@domain.com). The script injects the malicious element at the XML start.

**Expected Output**: New URL-encoded SAMLResponse with prepended malicious Response.

**Success Indicators**:
- Output decodes to XML with unsigned malicious Response first, followed by signed original
- Assertions in first Response reflect admin values

### Step 4: Replace and Forward Request
procedure: [[procedures/Forward-Modified-SAML-Response-to-Bypass-Authentication]]

**Objective**: Submit the modified response to complete the bypass and gain unauthorized access.

**Instructions**: In Burp Suite, replace the SAMLResponse parameter with the script output and forward the POST request to the server.

**Expected Output**: Successful login redirect to Rocket.Chat dashboard as the targeted user.

**Success Indicators**:
- Authentication succeeds without IdP validation errors
- User session active with admin privileges (e.g., access to admin panel)

## Attack Chain Summary

### Key Achievements

1. SAML authentication fully bypassed via XML structure manipulation
2. Unauthorized login as any user, including administrators
3. No need for valid IdP credentials or signature forgery

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
