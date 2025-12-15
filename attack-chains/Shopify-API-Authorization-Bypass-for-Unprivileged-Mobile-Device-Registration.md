---
tags:
  - shopify
  - api
  - authorization-bypass
  - mobile
  - apns
  - notifications
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Web
  - Mobile
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-Shopify-with-Privileged-Account]]'
  - '[[procedures/Intercept-Mobile-Device-Registration-Request]]'
  - '[[procedures/Revoke-Account-Permissions]]'
  - '[[procedures/Remove-Existing-Mobile-Device-Registration]]'
  - '[[procedures/Replay-Registration-Request-with-Unprivileged-Account]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:29:09.584Z'
description: >-
  A multi-step attack exploiting improper authorization in Shopify's mobile
  device registration API, allowing unprivileged administrators to register
  devices and receive sensitive order notifications via APNS.
skill_level: intermediate
impact_level: high
id: 3eba0a62-3edb-4321-8013-1de1c2c96f7e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Cloud Instance Metadata API]]'
---
# Shopify API Authorization Bypass for Unprivileged Mobile Device Registration

Multi-stage attack chain demonstrating exploitation of improper authorization in Shopify's `/admin/mobile_devices.json` API endpoint. An administrator without 'Settings' permission can register their mobile device to receive sensitive order notifications, bypassing UI restrictions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login with Privileged Account] --> B[Intercept Registration Request]
    B --> C[Revoke Permissions]
    C --> D[Remove Existing Device]
    D --> E[Replay Request as Unprivileged]
    E --> F[Receive Sensitive Notifications]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#e67e22
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Shopify admin platform (Web and Mobile app)
- Required services: APNS for push notifications
- Network access: Valid Shopify admin credentials with initial full access

### Initial Access Requirements

- Privileged Shopify admin account (full permissions initially)
- Mobile device with Shopify app installed
- Proxy tool configured to intercept app traffic (e.g., Burp Suite)

## Detailed Attack Procedures

### Step 1: Login with Privileged Account
procedure: [[procedures/Login-to-Shopify-with-Privileged-Account]]

**Objective**: Authenticate to trigger the initial mobile device registration process using a full-access account.

**Instructions**: Open the Shopify mobile app and log in with an account that has full administrative permissions, including 'Settings'. This will initiate the device registration request to the API.

**Expected Output**: Successful login and automatic sending of a POST request to `/admin/mobile_devices.json` with the APNS token.

**Success Indicators**:
- App login succeeds
- Device registration request is observable in the proxy

### Step 2: Intercept Registration Request
procedure: [[procedures/Intercept-Mobile-Device-Registration-Request]]

**Objective**: Capture the HTTP POST request used for mobile device registration, including the APNS token.

**Instructions**: Configure a proxy tool like Burp Suite to intercept traffic from the Shopify mobile app. Perform the login action to trigger the request, and capture the full POST to `/admin/mobile_devices.json`.

**Expected Output**: Intercepted request body containing the APNS token and device details.

**Success Indicators**:
- Request intercepted successfully
- APNS token extracted and noted for replay

### Step 3: Revoke Account Permissions
procedure: [[procedures/Revoke-Account-Permissions]]

**Objective**: Downgrade the account to unprivileged status by removing the 'Settings' permission, simulating an unauthorized user.

**Instructions**: In the Shopify admin web interface, navigate to user settings and revoke the 'Settings' permission from the account used in Step 1. Save the changes to apply the downgrade.

**Expected Output**: Account permissions updated; 'Settings' access denied.

**Success Indicators**:
- Permission revocation confirmed in admin panel
- Attempting UI-based device registration now fails due to lack of permissions

### Step 4: Remove Existing Mobile Device Registration
procedure: [[procedures/Remove-Existing-Mobile-Device-Registration]]

**Objective**: Clean up any prior device registrations to ensure a fresh state for the replay.

**Instructions**: Using the Shopify admin web interface (while permissions are still sufficient or via API if needed), delete the mobile device entry associated with the account's APNS token.

**Expected Output**: Mobile device record removed from the system.

**Success Indicators**:
- No active device registrations for the account
- API query to `/admin/mobile_devices.json` returns empty or no matching entry

### Step 5: Replay Registration Request
procedure: [[procedures/Replay-Registration-Request-with-Unprivileged-Account]]

**Objective**: Resend the captured request using the now-unprivileged account to bypass authorization and register the device.

**Instructions**: Using the proxy tool, replay the intercepted POST request to `/admin/mobile_devices.json` with the original APNS token, ensuring the session is from the downgraded account.

**Expected Output**: API responds with success (e.g., 200 OK), and the device is registered.

**Success Indicators**:
- Registration succeeds despite missing 'Settings' permission
- Unprivileged account begins receiving order notifications via APNS, exposing sensitive data

## Attack Chain Summary

### Key Achievements

1. Bypassed UI-enforced permissions via API exploitation
2. Registered unprivileged device for sensitive notifications
3. Demonstrated improper authorization leading to data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Cloud Instance Metadata API]] Credentials from Password Stores (API token reuse)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---
*Last updated: 2024-10-01T00:00:00Z*
