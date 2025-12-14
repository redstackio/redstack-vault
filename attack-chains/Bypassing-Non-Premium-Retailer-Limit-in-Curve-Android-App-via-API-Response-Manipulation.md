---
tags:
  - business-logic
  - api-manipulation
  - android
  - mobile
  - privilege-escalation
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Android
  - Web API
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]'
step_count: 7
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:28.382Z'
description: >-
  A business logic flaw allowing non-premium users to manipulate API responses
  and select unlimited retailers for cashback rewards, effectively gaining
  premium privileges.
skill_level: intermediate
impact_level: high
id: 36fd138c-e73a-4f6b-aff1-1d25249dd5d9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypassing Non-Premium Retailer Limit in Curve Android App via API Response Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting a business logic flaw in the Curve Android application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login as Non-Premium User] --> B[Select Initial Retailers]
    B --> C[Intercept API Response]
    C --> D[Modify Response to Empty Merchants List]
    D --> E[Select New Retailers]
    E --> F[Confirm and Repeat]
    F --> G[Gain Access to All Retailers]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#f39c12
    style F fill:#f39c12
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Android mobile app (Curve version 2.9.0 or similar)
- Access to API endpoint: api.imaginecurve.com
- No specific ports required; uses HTTPS

### Initial Access Requirements

- Valid non-premium Curve user account credentials
- Network access to proxy traffic (e.g., rooted device or emulator like Genymotion for Android)
- Prior app installation and basic navigation knowledge

## Detailed Attack Procedures

### Step 1: Login to Non-Premium Account
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Authenticate into the Curve app as a non-premium user to establish a session.

**Instructions**: Open the Curve Android app and log in using non-premium credentials. Ensure the app recognizes the account as non-premium (no premium features available).

**Expected Output**: Successful login with access to basic features, including the 'Earn Curve Cash' section limited to 3 retailers.

**Success Indicators**:
- App dashboard loads without premium badges
- Rewards section shows limit of 3 retailers

### Step 2: Navigate to Earn Curve Cash and Select 3 Retailers
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Access the rewards functionality and make an initial selection to trigger the API.

**Instructions**: Navigate to the 'Earn Curve Cash' section in the app and select exactly 3 retailers (e.g., Waitrose, Whole Foods, Tesco) as per non-premium limits.

**Expected Output**: Retailers displayed in the selection interface with a limit warning.

**Success Indicators**:
- 3 retailers selected without errors
- App UI enforces the limit

### Step 3: Confirm Initial Retailer Selection
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Submit the initial selection to populate the merchants list on the server.

**Instructions**: Click 'Confirm' to add the 3 retailers to the account. Note that the app provides no in-app edit option post-confirmation.

**Expected Output**: Confirmation message; retailers added to account.

**Success Indicators**:
- Success toast or message in app
- Account reflects 3 selected retailers

### Step 4: Intercept API Request/Response with Proxy
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Capture the API call that fetches the current merchants list for manipulation.

**Instructions**: Configure the Android device/emulator to route traffic through [[tools/Burp-Suite]] proxy. Go back to 'Earn Curve Cash' and trigger a refresh or navigation that issues a GET request to `/v1/rewards/users/programs/e329e463-7f5d-4358-9109-4f97c9f86abd/merchants`. Intercept the response using Burp Suite.

**Expected Output**: Captured HTTP GET request and JSON response with `{"success":true,"data":{"merchants":[list of 3 retailers]}}`.

**Success Indicators**:
- Request intercepted in Burp
- Response shows current merchants array

### Step 5: Modify Response to Empty Merchants List
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Alter the API response to trick the client into believing no retailers are selected, resetting the limit.

**Instructions**: In Burp Suite, edit the response body to `{"success":true,"data":{"merchants":[]}}` and forward it to the app.

**Expected Output**: App receives modified response; UI now shows empty or resettable list.

**Success Indicators**:
- Modified response forwarded without errors
- App treats list as empty on next interaction

### Step 6: Select 3 New Retailers After Modification
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Exploit the reset state to add another set of retailers.

**Instructions**: Turn off interception in Burp Suite. Navigate back to 'Earn Curve Cash' and select 3 new retailers, as the app now perceives the list as empty.

**Expected Output**: New selection allowed without limit enforcement.

**Success Indicators**:
- UI permits new selection
- No limit error displayed

### Step 7: Confirm Update and Repeat Process
procedure: [[procedures/Bypass-Curve-Retailer-Limit-via-API-Manipulation]]

**Objective**: Accumulate retailers beyond the limit by repeating the manipulation.

**Instructions**: Click 'Confirm' to add the new retailers. Repeat steps 4-7 to add more sets until all desired retailers are selected, gaining cashback on unlimited options.

**Expected Output**: Account updated with additional retailers; cashback applicable to all selected.

**Success Indicators**:
- Multiple confirmations succeed
- App/account shows more than 3 retailers
- Cashback rewards active on extras

## Attack Chain Summary

### Key Achievements

1. Bypassed client-side retailer limit using API response tampering
2. Gained unauthorized premium-like cashback access for non-premium users
3. Demonstrated lack of server-side validation in rewards program

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
