---
tags:
  - 2fa-bypass
  - information-disclosure
  - account-takeover
  - totp-leak
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Google-Authenticator]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Establish-Session-and-Intercept-Renew-Request]]'
  - '[[procedures/Extract-2FA-Secret-from-API-Response]]'
  - '[[procedures/Import-Secret-into-TOTP-App]]'
  - '[[procedures/Generate-and-Use-TOTP-Codes-for-Bypass]]'
step_count: 6
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:18.054Z'
description: >-
  Multi-stage attack exploiting an information disclosure vulnerability in
  Algolia's support access renewal API to leak the Google Authenticator 2FA
  secret, enabling TOTP code generation and full account compromise.
skill_level: intermediate
impact_level: high
id: b1c32e33-440e-4821-9ffb-ad7655f1ed40
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Information Disclosure of 2FA Secret Leading to Account Takeover in Algolia

Multi-stage attack chain demonstrating a complete attack workflow exploiting an API vulnerability in Algolia.com to disclose the Google Authenticator 2FA secret, generate valid TOTP codes, and achieve full account compromise.

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
    A[Establish Session] --> B[Intercept Renew Request]
    B --> C[Extract 2FA Secret]
    C --> D[Import Secret to TOTP App]
    D --> E[Generate TOTP Codes]
    E --> F[Perform Account Takeover Actions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Google-Authenticator]]

### Target Environment

- Web platform (Algolia.com)
- Required services: HTTPS API endpoints for account support
- Network access: Direct internet access to https://www.algolia.com

### Initial Access Requirements

- Valid credentials for target account (or stolen session cookies)
- Network position: Attacker with ability to proxy traffic
- Prior access: None beyond session establishment

## Detailed Attack Procedures

### Step 1: Login to Algolia.com
procedure: [[procedures/Establish-Session-and-Intercept-Renew-Request]]

**Objective**: Authenticate to obtain a valid session for the target account.

**Instructions**: Use a web browser to navigate to https://www.algolia.com and log in with valid credentials. Ensure session cookies are captured if using a proxy like Burp Suite.

**Expected Output**: Successful login redirect to the dashboard, with active session.

**Success Indicators**:
- Dashboard access granted
- Session cookies present in proxy logs

### Step 2: Navigate to the Support Page
procedure: [[procedures/Establish-Session-and-Intercept-Renew-Request]]

**Objective**: Access the account support section to prepare for the renew action.

**Instructions**: From the dashboard, click on the account settings and navigate to the support page at https://www.algolia.com/account/support.

**Expected Output**: Support page loads, displaying options including the 'Renew' button for support access.

**Success Indicators**:
- URL matches https://www.algolia.com/account/support
- Renew button visible

### Step 3: Intercept the Renew Request
procedure: [[procedures/Establish-Session-and-Intercept-Renew-Request]]

**Objective**: Capture the HTTP request triggered by renewing support access using a proxy tool.

**Instructions**: Configure Burp Suite Proxy to intercept traffic from the browser. Click the 'Renew' button on the support page to trigger the API request. In Burp Suite, intercept the outgoing POST request to the renew endpoint.

**Expected Output**: Intercepted HTTP request visible in Burp Suite Proxy tab.

**Success Indicators**:
- Request body contains renew parameters
- No errors in request forwarding

### Step 4: Replay and Inspect the Response
procedure: [[procedures/Extract-2FA-Secret-from-API-Response]]

**Objective**: Forward the request, capture the response, and locate the leaked 2FA secret.

**Instructions**: Send the intercepted request to Burp Suite Repeater. Forward or replay the request to receive the server response. Inspect the JSON response body for the 'gauth_secret' key and copy its value.

**Expected Output**: JSON response containing {"gauth_secret": "leaked_secret_value"}.

**Success Indicators**:
- gauth_secret field present and non-empty
- Secret value extracted (e.g., a base32-encoded string)

### Step 5: Import the Secret into Google Authenticator
procedure: [[procedures/Import-Secret-into-TOTP-App]]

**Objective**: Add the leaked secret to a TOTP app to generate valid 2FA codes.

**Instructions**: Open the Google Authenticator app on a mobile device. Select 'Add account' manually, enter the account name (e.g., 'Algolia'), and input the extracted gauth_secret as the key. Save to start generating codes.

**Expected Output**: New entry in app displaying a 6-digit TOTP code that refreshes every 30 seconds.

**Success Indicators**:
- App accepts the secret without errors
- Codes generate successfully

### Step 6: Use TOTP Codes to Bypass 2FA and Compromise Account
procedure: [[procedures/Generate-and-Use-TOTP-Codes-for-Bypass]]

**Objective**: Leverage generated codes to perform high-privilege actions like email changes or account deletion.

**Instructions**: Navigate to sensitive areas such as email update, recovery code download, or account deletion pages. When prompted for 2FA, enter the current TOTP code from the app. Confirm actions succeed without additional verification.

**Expected Output**: Successful execution of actions, e.g., email updated or account deleted.

**Success Indicators**:
- 2FA prompts accepted with app-generated codes
- Critical actions complete without blocks

## Attack Chain Summary

### Key Achievements

1. Leaked the 2FA secret via API response disclosure
2. Bypassed TOTP-based protections using imported secret
3. Achieved full account takeover through unauthorized high-privilege operations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unsecured Credentials]] Unprotected Service
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
