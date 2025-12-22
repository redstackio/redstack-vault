---
id: ac-970157-twitter-rate-bypass
tags:
  - rate-limit-bypass
  - brute-force
  - account-takeover
  - credential-access
  - twitter
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Setup-and-Intercept-Twitter-Password-Change-Request]]'
  - '[[procedures/Brute-Force-Current-Password-with-Burp-Intruder]]'
step_count: 7
techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:43.176Z'
description: >-
  Exploits the absence of rate limiting on Twitter's password change endpoint to
  brute-force a victim's current password using a hijacked session, enabling
  full account takeover.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
  - '[[Valid Accounts]]'
---
# Twitter Password Change Rate Limit Bypass for Account Takeover

Multi-stage attack chain demonstrating exploitation of Twitter's password change endpoint due to missing rate limiting, allowing rapid brute-force attempts on the current password in a hijacked session to achieve account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~3.5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Hijack Session] --> B[Navigate to Password Settings]
    B --> C[Initiate and Intercept Request]
    C --> D[Configure Brute-Force in Burp Intruder]
    D --> E[Load Payload and Launch Attack]
    E --> F[Discover Password and Takeover Account]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform with access to Twitter (now X) account settings
- Hijacked user session (e.g., via XSS or session cookie theft)
- No rate limiting on /i/account/change_password.json endpoint

### Initial Access Requirements

- Valid session cookies for the target Twitter account
- Proxy setup (e.g., Burp Suite) to intercept traffic from a logged-in browser
- List of potential passwords for brute-forcing

## Detailed Attack Procedures

### Step 1: Navigate to Password Settings
procedure: [[procedures/Setup-and-Intercept-Twitter-Password-Change-Request]]

**Objective**: Access the password change interface in a hijacked session to prepare for request interception.

**Instructions**: Log in to the target Twitter account using the hijacked session cookies. Then, navigate to the password settings page.

**Expected Output**: Password change form loaded at https://twitter.com/settings/password.

**Success Indicators**:
- Settings page accessible without logout
- Session remains active

### Step 2: Initiate Password Change Request
procedure: [[procedures/Setup-and-Intercept-Twitter-Password-Change-Request]]

**Objective**: Trigger the password change POST request to capture it for modification.

**Instructions**: On the password change form, enter a random new password and confirmation, then click 'Next' to submit.

**Expected Output**: Form submission intercepted by proxy before reaching the server.

**Success Indicators**:
- POST request to /i/account/change_password.json captured
- Request includes current_password, password, and password_confirmation parameters

### Step 3: Intercept the Request
procedure: [[procedures/Setup-and-Intercept-Twitter-Password-Change-Request]]

**Objective**: Use a proxy to capture the HTTP POST request for analysis and modification.

**Instructions**: Configure your browser to route traffic through Burp Suite proxy. Intercept the request sent to https://api.twitter.com/i/account/change_password.json.

**Expected Output**: Raw HTTP request visible in Burp Proxy, showing headers like authorization: Bearer and Cookie with session tokens.

**Success Indicators**:
- Request body contains form-urlencoded parameters
- CSRF token and auth headers intact

### Step 4: Send Intercepted Request to Intruder
procedure: [[procedures/Brute-Force-Current-Password-with-Burp-Intruder]]

**Objective**: Prepare the captured request for automated payload testing in Burp Intruder.

**Instructions**: In Burp Suite, right-click the intercepted request and select 'Send to Intruder' to load it into the Intruder module.

**Expected Output**: Request loaded in Intruder with positions ready for payload insertion.

**Success Indicators**:
- Intruder tab opens with the request
- No errors in request parsing

### Step 5: Select Old Password Field for Brute-Forcing
procedure: [[procedures/Brute-Force-Current-Password-with-Burp-Intruder]]

**Objective**: Mark the current_password parameter as the target for brute-force payloads.

**Instructions**: In Burp Intruder, go to the Positions tab and highlight the value of the 'current_password' parameter in the request body, then click 'Add §' to set it as a payload position.

**Expected Output**: The current_password field marked with § for replacement.

**Success Indicators**:
- Only current_password is positioned for attack
- Other parameters (password, password_confirmation) remain static with dummy values

### Step 6: Load Password List as Payload
procedure: [[procedures/Brute-Force-Current-Password-with-Burp-Intruder]]

**Objective**: Configure a wordlist of potential passwords to test against the endpoint.

**Instructions**: In the Payloads tab, select 'Simple list' and load a file containing common passwords or a targeted list (e.g., from prior reconnaissance).

**Expected Output**: Payload set loaded, ready for attack launch.

**Success Indicators**:
- Wordlist imported without errors
- Payload count visible (e.g., 1000+ entries)

### Step 7: Start the Brute-Force Attack
procedure: [[procedures/Brute-Force-Current-Password-with-Burp-Intruder]]

**Objective**: Launch rapid requests to guess the current password and update it upon success.

**Instructions**: Click 'Start attack' in Burp Intruder. Monitor responses for success indicators like 200 OK with password update confirmation. Due to no rate limiting, send over 1000 requests in ~3.4 minutes.

**Expected Output**: Successful response when correct password is guessed, allowing new password set and account takeover.

**Success Indicators**:
- Response code 200 with JSON indicating success
- Account password changed; session now under attacker control

## Attack Chain Summary

### Key Achievements

1. Bypassed rate limiting to brute-force without blocks
2. Achieved full account takeover via password reset in hijacked session
3. Demonstrated severe impact of missing endpoint protections

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T12:00:00Z*
