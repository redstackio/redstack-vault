---
tags:
  - auth-bypass
  - account-takeover
  - response-manipulation
  - twitter
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]
step_count: 17
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:31:52.957Z'
description: >-
  An attack chain exploiting improper authentication in Twitter's contact update
  flows, allowing session hijackers to bypass password prompts by manipulating
  server responses, leading to account takeover through contact changes and
  password resets.
skill_level: intermediate
impact_level: high
id: f7754164-0d4f-48c3-ae63-3686d02c414c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
---
# Twitter Account Takeover via Password Bypass in Email and Phone Update Flows

Multi-stage attack chain demonstrating a complete attack workflow for bypassing password authentication in Twitter's (now X) account settings to update email and phone numbers, enabling full account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 17 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Hijack Session and Navigate to Settings] --> B[Initiate Email Update]
    B --> C[Intercept Request and Copy Flow Token]
    C --> D[Modify Response to Fake Success]
    D --> E[Update Email and Verify]
    E --> F[Initiate Phone Update]
    F --> G[Intercept Request and Copy Flow Token for Phone]
    G --> H[Modify Response for Phone]
    H --> I[Update Phone and Verify]
    I --> J[Reset Password via New Contacts for Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#27ae60
    style F fill:#f39c12
    style G fill:#f39c12
    style H fill:#f39c12
    style I fill:#27ae60
    style J fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (Twitter web application)
- Required services: Twitter account management, email verification, phone/SMS verification
- Tech stack: JavaScript (client-side), Twitter web app
- No specific ports; browser-based over HTTPS

### Initial Access Requirements

- Hijacked user session (valid cookies for the target account)
- Network position: Local proxy setup (e.g., browser traffic routed through proxy)
- Prior access needed: Active session in a proxied browser

## Detailed Attack Procedures

### Step 1: Navigate to the account settings
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Access the vulnerable update flows in Twitter settings.

**Instructions**: Log in with the hijacked session and go to Settings and Privacy -> Accounts.

**Expected Output**: Account settings page loaded.

**Success Indicators**:
- Settings page accessible without logout
- Accounts section visible

### Step 2: Initiate email update
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Trigger the email update flow to generate the authentication request.

**Instructions**: Click on Email -> Update email address.

**Expected Output**: Password prompt for email change appears.

**Success Indicators**:
- Update email interface loads
- Password input field displayed

### Step 3: Enter random password and submit
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Generate a flow token by submitting invalid credentials.

**Instructions**: Enter any random password and click 'Next'.

**Expected Output**: Request sent to server with flow token.

**Success Indicators**:
- Flow token present in intercepted request
- Server error response expected but intercepted

### Step 4: Intercept the request
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Capture the authentication request using a proxy.

**Instructions**: Use [[tools/Burp-Suite]] to intercept the request to the server.

**Expected Output**: Request paused in proxy.

**Success Indicators**:
- Request details visible, including flow token

### Step 5: Copy the flow token
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Extract the flow token for response crafting.

**Instructions**: Copy the flow token from the request (up to the colon).

**Expected Output**: Flow token string copied (e.g., "flow_token:abc123").

**Success Indicators**:
- Token valid and unique to the flow

### Step 6: Forward request and intercept response
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Allow the request to reach the server and capture the failure response.

**Instructions**: Forward the request in the proxy and intercept the returning response.

**Expected Output**: Server response with authentication failure.

**Success Indicators**:
- Response status 200 or error, JSON payload visible

### Step 7: Modify the server response
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Craft a fake success response to bypass the password check.

**Instructions**: Replace the response with a crafted HTTP 200 OK containing JSON: {"flow_token": "pasted_token", "status": "success", "subtasks": [email update subtasks]}.

**Expected Output**: Modified response with success status.

**Success Indicators**:
- JSON validates as success for email flow

### Step 8: Forward modified response to client
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Deliver the faked success to the client-side app.

**Instructions**: Forward the modified response to the browser.

**Expected Output**: Client proceeds to email entry without password re-prompt.

**Success Indicators**:
- Password screen bypassed

### Step 9: Bypass achieved and update email
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Complete the email update to enable takeover.

**Instructions**: Enter and verify the new email address.

**Expected Output**: New email added to account.

**Success Indicators**:
- Confirmation of email update
- Ability to receive reset emails

### Step 10: Initiate phone update (for phone vulnerability)
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Trigger the phone update flow.

**Instructions**: Click on Phone -> Add/Update phone number.

**Expected Output**: Password prompt for phone change.

**Success Indicators**:
- Phone update interface loads

### Step 11: Enter random password and submit for phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Generate flow token for phone flow.

**Instructions**: Enter random password and click 'Next'.

**Expected Output**: Request with new flow token.

**Success Indicators**:
- Flow token generated

### Step 12: Intercept request for phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Capture phone authentication request.

**Instructions**: Intercept using proxy.

**Expected Output**: Request paused.

**Success Indicators**:
- Request contains phone flow details

### Step 13: Copy flow token for phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Extract token for phone response.

**Instructions**: Copy flow token from request.

**Expected Output**: Phone flow token copied.

**Success Indicators**:
- Token ready for crafting

### Step 14: Forward request and intercept response for phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Get server response for phone.

**Instructions**: Forward and intercept response.

**Expected Output**: Failure response captured.

**Success Indicators**:
- Response available for modification

### Step 15: Modify server response for phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Fake success for phone flow.

**Instructions**: Craft HTTP 200 OK with JSON: {"flow_token": "pasted_token", "status": "success", "subtasks": [phone update subtasks including country codes list]}.

**Expected Output**: Modified success response.

**Success Indicators**:
- JSON includes phone-specific subtasks

### Step 16: Forward modified response for phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Bypass phone password check.

**Instructions**: Forward to client.

**Expected Output**: Client advances to phone entry.

**Success Indicators**:
- No password re-prompt

### Step 17: Bypass achieved and update phone
procedure: [[procedures/Response-Manipulation-to-Bypass-Authentication-in-Twitter-Settings]]

**Objective**: Add new phone for takeover completion.

**Instructions**: Enter and verify the new mobile number.

**Expected Output**: Phone added to account.

**Success Indicators**:
- SMS verification successful
- Account contacts updated for reset abuse

## Attack Chain Summary

### Key Achievements

1. Bypassed password authentication for sensitive account changes without valid credentials.
2. Updated email and phone to attacker-controlled contacts.
3. Enabled password reset to lock out the legitimate user and achieve full takeover.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

---

*Last updated: 2023-10-01T00:00:00Z*
