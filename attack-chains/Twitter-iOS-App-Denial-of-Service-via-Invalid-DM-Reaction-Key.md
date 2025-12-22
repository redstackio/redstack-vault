---
tags:
  - dos
  - twitter
  - ios
  - api
  - input-validation
type: attack_chain
tools:
  - '[[tools/Chrome-DevTools]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - iOS
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Twitter-DM-Reaction-Vulnerability-for-iOS-DoS]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:24:42.424Z'
description: >-
  A multi-stage attack exploiting Twitter's DM reaction API by injecting an
  empty reaction_key, leading to repeated crashes in the iOS app and effective
  denial-of-service until manual cleanup via web.
skill_level: intermediate
impact_level: high
id: 39301242-3443-4c3c-9d66-9e828eb30cc5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Twitter iOS App Denial of Service via Invalid DM Reaction Key

Multi-stage attack chain demonstrating exploitation of Twitter's DM reaction API vulnerability to cause denial-of-service on the iOS app by injecting an invalid empty reaction_key, rendering the app unusable until the affected conversation is deleted via web interface.

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
    A[Initiate DM Conversation] --> B[Capture Legitimate Reaction Request]
    B --> C[Modify and Send Invalid Reaction]
    C --> D[Trigger iOS App Crash]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Chrome-DevTools]]
- [[tools/curl]]

### Target Environment

- Twitter web platform (twitter.com)
- Twitter iOS app
- Required services: Twitter API (https://api.twitter.com/1.1/dm/reaction/new.json)
- Network access: Authenticated Twitter account with DM capabilities

### Initial Access Requirements

- Valid Twitter credentials (auth_token, CSRF token)
- Access to a DM conversation (can be with self)
- Browser with developer tools and bash shell for curl

## Detailed Attack Procedures

### Step 1: Initiate DM Conversation
procedure: [[procedures/Exploit-Twitter-DM-Reaction-Vulnerability-for-iOS-DoS]]

**Objective**: Establish a direct message conversation to obtain necessary IDs for targeting.

**Instructions**: Log in to twitter.com and start a new DM conversation with the target user (or yourself for testing). Note the conversation_id and dm_id from the URL or network requests.

**Expected Output**: Active DM thread with visible conversation_id (e.g., from URL: twitter.com/messages/[CONV_ID]) and dm_id for specific messages.

**Success Indicators**:
- DM conversation opened successfully
- IDs extracted for use in subsequent steps

### Step 2: Capture Legitimate Reaction Request
procedure: [[procedures/Exploit-Twitter-DM-Reaction-Vulnerability-for-iOS-DoS]]

**Objective**: Intercept a valid DM reaction API call to obtain the base request structure, including tokens.

**Instructions**: Open Chrome DevTools (F12 > Network tab), navigate to the DM, add a legitimate reaction (e.g., heart emoji) to a message, right-click the POST request to /dm/reaction/new.json, and copy as cURL. Extract CSRF token, auth_token, and bearer from the request.

**Expected Output**: cURL command with full headers and parameters for a valid reaction.

**Success Indicators**:
- Network request captured
- All authentication tokens obtained without errors

### Step 3: Modify and Send Invalid Reaction
procedure: [[procedures/Exploit-Twitter-DM-Reaction-Vulnerability-for-iOS-DoS]]

**Objective**: Craft and execute a modified API request with an empty reaction_key to inject the invalid reaction.

**Instructions**: Modify the captured cURL by setting reaction_key to empty (&reaction_key=). Replace placeholders with actual IDs and tokens, then execute using [[commands/curl-twitter-dm-invalid-reaction]]:

```bash
curl -i 'https://api.twitter.com/1.1/dm/reaction/new.json?reaction_key=&conversation_id=[CONV_ID]&dm_id=[DM_ID]' -X POST -H 'x-csrf-token: [CSRF_TOKEN]' -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' -H 'cookie: auth_token=[AUTH_TOKEN]; ct0=[CSRF_TOKEN]'
```

**Expected Output**: HTTP 200 response from API indicating successful reaction addition, but the empty key causes client-side instability.

**Success Indicators**:
- API request succeeds without authentication errors
- Invalid reaction applied to the DM

### Step 4: Trigger iOS App Crash
procedure: [[procedures/Exploit-Twitter-DM-Reaction-Vulnerability-for-iOS-DoS]]

**Objective**: View the affected DM in the iOS app to induce repeated crashes, achieving DoS.

**Instructions**: Open the Twitter iOS app, navigate to the DM list or the specific conversation. The app will crash upon rendering the malformed reaction, especially if it's the latest message.

**Expected Output**: App crashes immediately or on interaction with the DM list; restarts but crashes again on retry.

**Success Indicators**:
- iOS app crashes when accessing DMs
- Victim unable to use DM functionality until web deletion

## Attack Chain Summary

### Key Achievements

1. Successful injection of invalid reaction via API without server-side rejection
2. Targeted DoS on iOS client, bypassing web functionality
3. Requirement for manual web intervention to mitigate, highlighting client-server desync

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---

*Last updated: 2024-01-01T00:00:00Z*
