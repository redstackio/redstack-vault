---
id: ac-shopify-session-bypass-001
tags:
  - session-bypass
  - authentication
  - shopify
  - mobile
  - improper-session-management
type: attack_chain
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Test-Users-in-Shopify]]'
  - '[[procedures/Login-via-Shopify-iOS-App]]'
  - '[[procedures/Expire-Sessions-via-Admin-Interface]]'
  - '[[procedures/Verify-Session-Persistence-in-iOS-App]]'
  - '[[procedures/Test-Specific-User-Session-Expiration]]'
step_count: 5
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.641Z'
description: >-
  Demonstrates how the Shopify Admin 'Expire User Sessions' feature fails to
  invalidate active sessions in the iOS mobile app, allowing persistent
  unauthorized access.
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypassing Session Expiration in Shopify iOS App via Admin Web Interface

Multi-stage attack chain demonstrating improper session management in Shopify, where admin-initiated session expiration does not affect the iOS app, enabling continued unauthorized access to store functions like product addition even after revocation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Low |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Environment] --> B[Staff Login via iOS App]
    B --> C[Admin Expires All Sessions]
    C --> D[Verify iOS Session Persists]
    D --> E[Test Specific User Expiration]
    E --> F[Unauthorized Access Maintained]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#f39c12
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Shopify iOS app (latest version)
- Web browser for admin access
- Test Shopify store account with owner and staff permissions

### Target Environment

- Shopify platform (e.g., test store like whitehat-3.myshopify.com)
- Web admin interface
- iOS device (e.g., iPhone 6 Plus on iOS 8.3 or later)

### Initial Access Requirements

- Owner credentials for admin setup
- Staff credentials for testing
- Network access to Shopify admin and app

## Detailed Attack Procedures

### Step 1: Setup Test Environment
procedure: [[procedures/Setup-Test-Users-in-Shopify]]

**Objective**: Create owner and staff users with full permissions to simulate access control scenarios.

**Instructions**: Access the Shopify admin dashboard and create a new staff user with full access to store functions, such as adding products.

**Expected Output**: Staff user account (e.g., Alpha) created and confirmed with permissions.

**Success Indicators**:
- Owner user (e.g., Dimitris) can log in to admin.
- Staff user exists with full permissions.

### Step 2: Staff Login via iOS App
procedure: [[procedures/Login-via-Shopify-iOS-App]]

**Objective**: Establish an active session in the iOS app to test revocation.

**Instructions**: Open the Shopify iOS app, enter staff credentials, and perform an action like adding a product to confirm session validity.

**Expected Output**: Successful login and product addition in the app.

**Success Indicators**:
- App shows logged-in state.
- Store modifications (e.g., new product) are applied.

### Step 3: Admin Expires All Sessions
procedure: [[procedures/Expire-Sessions-via-Admin-Interface]]

**Objective**: Trigger session invalidation from the web admin to attempt revocation.

**Instructions**: As owner, navigate to the admin site, locate the 'Expire User Sessions' feature, and confirm the action, observing the success notification.

**Expected Output**: Notification stating all users are logged out.

**Success Indicators**:
- Admin interface shows confirmation message.
- Web session for owner may require re-login.

### Step 4: Verify Session Persistence in iOS App
procedure: [[procedures/Verify-Session-Persistence-in-iOS-App]]

**Objective**: Confirm that the iOS app session remains active despite admin action.

**Instructions**: Switch back to the iOS app (even after backgrounding it) and attempt to add another product using the staff account.

**Expected Output**: App remains logged in; product addition succeeds without re-authentication.

**Success Indicators**:
- No re-login prompt in app.
- Continued access to store functions.

### Step 5: Test Specific User Session Expiration
procedure: [[procedures/Test-Specific-User-Session-Expiration]]

**Objective**: Validate the bypass even for targeted user session revocation.

**Instructions**: In the admin, navigate to the specific staff user's profile, select 'Expire User's Session', confirm, then check the iOS app again.

**Expected Output**: iOS session still active; actions possible.

**Success Indicators**:
- Targeted expiration notification in admin.
- iOS app unaffected.

## Attack Chain Summary

### Key Achievements

1. Demonstrated failure of session synchronization between web admin and iOS app.
2. Enabled persistent unauthorized access post-revocation.
3. Highlighted risk of data modification (e.g., adding products) by compromised staff.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Persistence]]

---
*Last updated: 2023-10-01T00:00:00Z*
