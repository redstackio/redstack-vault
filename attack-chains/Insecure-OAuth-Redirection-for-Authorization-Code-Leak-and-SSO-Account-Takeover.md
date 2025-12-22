---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - oauth-misconfig
  - redirect-uri
  - auth-code-leak
  - sso-takeover
  - phishing
type: attack_chain
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Initiate-OAuth-Flow-for-Admin-Account-Addition]]'
  - '[[procedures/Manipulate-OAuth-successRedirectUrl]]'
  - '[[procedures/Phish-Victim-for-OAuth-Authentication]]'
  - '[[procedures/Intercept-and-Exchange-OAuth-Authorization-Code]]'
step_count: 4
techniques:
  - '[[Steal Application Access Token]]'
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.643Z'
description: >-
  Multi-stage attack exploiting insufficient validation of OAuth redirect URIs
  in the 8x8 admin application to leak authorization codes and achieve SSO
  account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Insecure OAuth Redirection for Authorization Code Leak and SSO Account Takeover

Multi-stage attack chain demonstrating exploitation of OAuth misconfiguration in the admin.8x8.vc application, allowing arbitrary redirect URIs to intercept authorization codes and takeover victim SSO accounts.

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
    A[Initiate OAuth Flow] --> B[Manipulate Redirect URI]
    B --> C[Trick Victim Authentication]
    C --> D[Intercept Code and Exchange for Token]
    D --> E[SSO Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#2ecc71
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for URL manipulation
- Attacker-controlled domain and server to capture redirects

### Target Environment

- Web platform
- Gmail OAuth integration
- SSO-enabled admin application (admin.8x8.vc)

### Initial Access Requirements

- Access to the admin.8x8.vc application
- Victim with Gmail account for authentication
- No prior credentials needed, but social engineering for victim interaction

## Detailed Attack Procedures

### Step 1: Initiate the Admin Account Addition Process
procedure: [[procedures/Initiate-OAuth-Flow-for-Admin-Account-Addition]]

**Objective**: Trigger the OAuth authentication flow by starting the admin account addition process in the target application.

**Instructions**: Navigate to the admin.8x8.vc application in a web browser. Locate the admin account addition feature and initiate it, which redirects to Gmail for authentication. Observe the generated OAuth URL containing the successRedirectUrl parameter.

**Expected Output**: OAuth authorization URL pointing to Gmail with embedded redirect parameters.

**Success Indicators**:
- Successful redirection to Gmail login page
- Presence of successRedirectUrl in the URL

### Step 2: Manipulate the successRedirectUrl Parameter
procedure: [[procedures/Manipulate-OAuth-successRedirectUrl]]

**Objective**: Alter the OAuth redirect URI to point to an attacker-controlled domain, bypassing validation.

**Instructions**: Using browser developer tools or a proxy like Burp Suite, intercept the OAuth request during the account addition process. Modify the successRedirectUrl parameter to https://attacker-controlled-domain.com/callback. Proceed with the flow to generate the manipulated URL.

**Expected Output**: Modified OAuth URL with arbitrary redirect domain.

**Success Indicators**:
- Parameter successfully changed without error
- Flow continues to Gmail authentication

### Step 3: Trick Victim into Authenticating
procedure: [[procedures/Phish-Victim-for-OAuth-Authentication]]

**Objective**: Socially engineer the victim to authenticate via the manipulated OAuth URL, causing redirect to attacker's domain with the code.

**Instructions**: Send the manipulated OAuth URL to the victim via email, chat, or other means, disguising it as a legitimate admin setup link. Instruct the victim to authenticate with their Gmail credentials. Upon success, the redirect will append the authorization code to the attacker's URL.

**Expected Output**: Victim completes authentication, browser redirects to attacker's domain with ?code=AUTH_CODE in the query string.

**Success Indicators**:
- Victim reports successful login
- Authorization code visible in redirect URL

### Step 4: Intercept and Use the Leaked Authorization Code
procedure: [[procedures/Intercept-and-Exchange-OAuth-Authorization-Code]]

**Objective**: Capture the leaked code and exchange it for an access token to takeover the victim's SSO account.

**Instructions**: On the attacker-controlled server, log the incoming redirect request and extract the authorization code from the query parameters. Use the code to make a POST request to the OAuth token endpoint (typically https://accounts.google.com/o/oauth2/token) with client_id, client_secret (if known or bypassed), redirect_uri, grant_type=authorization_code, and code. Receive the access token and use it to authenticate to admin.8x8.vc SSO.

**Expected Output**: Access token issued; successful login to victim's admin account.

**Success Indicators**:
- Token exchange succeeds
- Attacker gains access to victim's SSO session on admin.8x8.vc

## Attack Chain Summary

### Key Achievements

1. Bypassed OAuth redirect validation to control code destination
2. Leaked victim authorization code via social engineering
3. Exchanged code for access token enabling full SSO takeover

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2024-01-01T00:00:00Z*
