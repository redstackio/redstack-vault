---
id: ac-reverb-fb-token-bypass-001
tags:
  - authentication-bypass
  - account-takeover
  - facebook-oauth
  - api-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - iOS
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-Reverb-Facebook-Login-Request]]'
  - '[[procedures/Replace-fb_token-with-External-Token]]'
  - '[[procedures/Submit-Modified-Request-for-Account-Takeover]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.464Z'
description: >-
  Multi-stage attack exploiting lack of origin validation in Reverb's Facebook
  login API, allowing authentication with tokens from unrelated apps to achieve
  full account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Facebook Access Token Bypass for Full Account Takeover in Reverb App

Multi-stage attack chain demonstrating exploitation of the Reverb iOS app's Facebook login API vulnerability, where the server fails to validate the origin of the Facebook access_token. This allows an attacker to authenticate as any user using a token from a different Facebook app, such as Lyst, leading to complete account compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Intercept Login Request] --> B[Replace Token] --> C[Submit for Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Reverb iOS app or web equivalent
- Access to Facebook developer console for obtaining tokens from another app
- Network interception capability (e.g., proxy setup on mobile device)

### Initial Access Requirements

- Ability to initiate a Facebook login flow in the Reverb app
- Valid Facebook access token from a different app (e.g., Lyst app token)
- No prior credentials needed for the target account

## Detailed Attack Procedures

### Step 1: Intercept Login Request
procedure: [[procedures/Intercept-Reverb-Facebook-Login-Request]]

**Objective**: Capture the legitimate Facebook login request from the Reverb app to understand the payload structure.

**Instructions**: Configure Burp Suite as a proxy on the device running the Reverb iOS app. Initiate a Facebook login in the app to trigger the POST request to /api/auth/facebook. Use Burp Suite to intercept and view the JSON payload containing the original fb_token.

**Expected Output**: Intercepted POST request with JSON body including {"fb_token": "original_token_from_reverb"}.

**Success Indicators**:
- Request successfully captured in Burp Suite
- Payload structure confirmed, including fb_token field

### Step 2: Replace fb_token with External Token
procedure: [[procedures/Replace-fb_token-with-External-Token]]

**Objective**: Modify the intercepted request by substituting the fb_token with one obtained from another Facebook app, bypassing origin validation.

**Instructions**: In Burp Suite's Repeater, edit the JSON payload to replace the fb_token value with a token from a different app, such as the Lyst app (example token: EAAJ8Of8DF2IBAL5wChKjuRHSV2VEWpm7eCz2IMqqJy1lJJq8ooyQuKHcOXn6aZCZAIrCtClbrZBdUGhC3FbvncNYk1E0k7AOktEhDjUPwHPOh3x29JURSGIGPBlZCj5WlBHhHzI5KYAPbuXKiZBGTkKZABZATh9JjTqEDhRubYSEiTmhjeytx5moFH9naZB6XjZBRUMkmcbucFD9Vf8IoFZAD1LGngi6j5pXFGcTFPfBEudAZDZD). Ensure the request headers and other fields remain unchanged.

**Expected Output**: Modified JSON payload with new fb_token integrated into the request.

**Success Indicators**:
- Token replacement completed without syntax errors
- Request ready for forwarding in Burp Suite

### Step 3: Submit Modified Request for Account Takeover
procedure: [[procedures/Submit-Modified-Request-for-Account-Takeover]]

**Objective**: Forward the altered request to the server, achieving unauthorized authentication as the target user.

**Instructions**: From Burp Suite, forward the modified POST request to https://reverb.com/api/auth/facebook. Observe the server's response, which should indicate successful authentication without validating the token's app origin.

**Expected Output**: Server response with authentication success (e.g., 200 OK with user session tokens or redirect to logged-in state).

**Success Indicators**:
- Authentication succeeds as the target user
- Full access to the account granted, confirming takeover

## Attack Chain Summary

### Key Achievements

1. Bypassed Facebook token origin validation in Reverb's API
2. Achieved full account takeover without legitimate credentials
3. Demonstrated impact on all users via unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
