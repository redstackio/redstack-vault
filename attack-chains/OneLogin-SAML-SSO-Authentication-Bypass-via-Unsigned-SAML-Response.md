---
tags:
  - saml
  - auth-bypass
  - wordpress
  - onelogin
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-SAML-ACS-Endpoint]]'
  - '[[procedures/Craft-Unsigned-SAML-Response]]'
  - '[[procedures/Base64-Encode-SAML-Response]]'
  - '[[procedures/Send-Forged-SAML-Response]]'
  - '[[procedures/Extract-Authentication-Cookies]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:52.162Z'
description: >-
  Exploits a flaw in the OneLogin SAML-SSO WordPress plugin by submitting an
  unsigned SAML response to bypass authentication and gain administrator access.
id: e070d229-b9ac-4489-bb59-4d0decc9735a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# OneLogin SAML-SSO Authentication Bypass via Unsigned SAML Response

Multi-stage attack chain demonstrating authentication bypass in the OneLogin SAML-SSO WordPress plugin by crafting and submitting an unsigned SAML response, allowing unauthenticated attackers to impersonate administrators and gain full site control.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Endpoint] --> B[Craft Response]
    B --> C[Encode Response]
    C --> D[Send Forged Response]
    D --> E[Extract Cookies]
    E --> F[Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- WordPress site with OneLogin SAML-SSO plugin enabled
- Access to the SAML assertion consumer service (ACS) endpoint
- No authentication required for initial access

### Initial Access Requirements

- Public network access to the target WordPress site
- Knowledge of target domain (e.g., newsroom.uber.com)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Identify SAML ACS Endpoint
procedure: [[procedures/Identify-SAML-ACS-Endpoint]]

**Objective**: Locate the SAML assertion consumer service endpoint on the target WordPress site to prepare for response submission.

**Instructions**: Inspect the site's plugin directory or source code to confirm the OneLogin SAML-SSO plugin is in use. The standard ACS endpoint is at `/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs`.

**Expected Output**: Confirmation of the endpoint URL, such as `https://target.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs`.

**Success Indicators**:
- Endpoint responds to HTTP requests
- Plugin version indicates vulnerability to unsigned responses

### Step 2: Craft Unsigned SAML Response
procedure: [[procedures/Craft-Unsigned-SAML-Response]]

**Objective**: Create a forged SAML 2.0 response XML that claims successful authentication for an admin user without a digital signature to bypass validation.

**Instructions**: Manually construct an XML file (response.xml) with SAML structure: include `<samlp:Response>` with Success status, Assertion with Subject (NameID as email), Conditions, AuthnStatement, and AttributeStatement setting User.Username='admin', User.email='noreply@target.com', memberOf='Administrator'. Omit the `<ds:Signature>` tag.

**Expected Output**: Valid SAML XML file ready for encoding.

**Success Indicators**:
- XML parses without errors
- Contains admin attributes without signature

### Step 3: Base64 Encode SAML Response
procedure: [[procedures/Base64-Encode-SAML-Response]]

**Objective**: Encode the crafted SAML XML to prepare it for HTTP POST transmission as the SAMLResponse parameter.

**Instructions**: Use [[commands/base64-encode-saml]] to encode the response.xml file:

```bash
xml=`base64 response.xml`
```

**Expected Output**: Base64-encoded string stored in the 'xml' variable.

**Success Indicators**:
- Encoded string is generated without errors
- Decoding the string yields the original XML

### Step 4: Send Forged SAML Response
procedure: [[procedures/Send-Forged-SAML-Response]]

**Objective**: Submit the encoded unsigned SAML response to the ACS endpoint to trigger authentication bypass and session creation.

**Instructions**: Execute [[commands/curl-send-saml]] to POST the response:

```bash
curl -v 'https://target.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

**Expected Output**: HTTP 302 redirect with Set-Cookie headers for authentication.

**Success Indicators**:
- 302 response received
- Cookies set for wordpress_logged_in, wordpress_sec, saml_login

### Step 5: Extract Authentication Cookies
procedure: [[procedures/Extract-Authentication-Cookies]]

**Objective**: Capture the authentication cookies from the response and use them to access the site as an administrator.

**Instructions**: From the curl output, copy the Set-Cookie headers and import them into a browser or tool like curl for subsequent requests to the dashboard.

**Expected Output**: Valid session allowing access to /wp-admin.

**Success Indicators**:
- Successful login to WordPress dashboard as 'admin'
- Full site control achieved

## Attack Chain Summary

### Key Achievements

1. Bypassed SAML authentication without valid signatures
2. Impersonated administrator user
3. Gained full control of WordPress site including dashboard access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[External Remote Services]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2024-10-01T00:00:00Z*
