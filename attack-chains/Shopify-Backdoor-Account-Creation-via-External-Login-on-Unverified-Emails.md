---
tags:
  - authentication-bypass
  - account-takeover
  - oauth
  - shopify
  - external-login
type: attack_chain
tools:
  - '[[tools/Browser-Developer-Console]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Unverified-Shopify-Account]]'
  - '[[procedures/Inject-HTML-for-External-Login-Linking]]'
  - '[[procedures/Authenticate-with-External-Provider]]'
  - '[[procedures/Verify-and-Test-Backdoor-Access]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:45.010Z'
description: >-
  Attack chain exploiting Shopify's improper authentication checks to link
  external logins like Google to unverified email accounts, enabling backdoor
  access and potential account takeover.
skill_level: intermediate
impact_level: high
id: 44095724-b5be-4955-aa2e-c14e1d81fb24
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
  - '[[Exploit Public-Facing Application]]'
---
# Shopify Backdoor Account Creation via External Login on Unverified Emails

Multi-stage attack chain demonstrating how to bypass Shopify's email verification by linking an external login service (e.g., Google) to an unverified account, creating a persistent backdoor for unauthorized access to the victim's profile, organizations, and shops.

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
    A[Create Unverified Account] --> B[Inject HTML for External Link]
    B --> C[Authenticate with Google]
    C --> D[Verify Backdoor Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-Developer-Console]]

### Target Environment

- Web platform
- Access to Shopify Partners portal (partners.shopify.com)
- Valid Google account for authentication
- No special ports or services beyond standard HTTPS

### Initial Access Requirements

- No prior credentials needed
- Internet access to Shopify and Google services
- Victim's email address (e.g., for testing: saltymermaid+victim@wearehackerone.com)

## Detailed Attack Procedures

### Step 1: Create Unverified Account
procedure: [[procedures/Create-Unverified-Shopify-Account]]

**Objective**: Register a new Shopify account using the victim's unverified email to establish a base for the backdoor.

**Instructions**: Navigate to the Shopify Partners registration page and create an account with the victim's email. The account will remain unverified by design.

**Expected Output**: Account creation confirmation with an account ID in the URL upon profile access.

**Success Indicators**:
- Account registered successfully
- Email not verified (no verification prompt completed)

### Step 2: Access Profile and Inject External Login
procedure: [[procedures/Inject-HTML-for-External-Login-Linking]]

**Objective**: Use browser tools to inject a link that allows connecting an external login without UI restrictions or verification checks.

**Instructions**: Access the account profile page and open the browser developer console. Inject the HTML snippet to create a 'Connect to Google' link, then click it to initiate the OAuth flow.

**Expected Output**: POST request to the external login endpoint, redirecting to Google's OAuth page.

**Success Indicators**:
- Injected link appears and functions
- Redirect to Google authentication without email verification

### Step 3: Authenticate with External Provider
procedure: [[procedures/Authenticate-with-External-Provider]]

**Objective**: Complete the external authentication to link the Google account to the unverified Shopify account.

**Instructions**: On the Google OAuth page, log in with a controlled Google account. Upon success, it redirects back to the Shopify profile with the external login now linked.

**Expected Output**: Successful redirect to Shopify account profile showing the linked Google login.

**Success Indicators**:
- Google account linked in profile
- No email verification required for the link

### Step 4: Verify and Test Backdoor Access
procedure: [[procedures/Verify-and-Test-Backdoor-Access]]

**Objective**: Confirm the backdoor by accessing the account via the external login from a different session, simulating victim compromise.

**Instructions**: In a new browser or incognito session, attempt login via the external provider using the victim's email. Verify access to organizations and shops.

**Expected Output**: Successful login and access to victim's organizations without password or verification.

**Success Indicators**:
- 'Log in with Google' option available
- Full access to profile and associated resources

## Attack Chain Summary

### Key Achievements

1. Bypassed email verification for external login linking
2. Created a persistent backdoor account tied to victim's email
3. Enabled unauthorized access to Shopify organizations and shops
4. Potential for information disclosure or full takeover upon victim interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[External Remote Services]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
