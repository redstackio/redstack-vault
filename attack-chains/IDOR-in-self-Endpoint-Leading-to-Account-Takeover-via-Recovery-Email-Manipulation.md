---
tags:
  - idor
  - account-takeover
  - information-disclosure
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Firefox-Multi-Account-Containers]]'
tactics:
  - '[[Persistence]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-and-Identify-IDOR-in-Self-Endpoint]]'
  - '[[procedures/Retrieve-Victim-Username-via-Friends-API]]'
  - '[[procedures/Modify-Self-Request-to-Add-Attacker-Recovery-Email]]'
  - '[[procedures/Request-Password-Reset-Using-Added-Recovery-Email]]'
  - '[[procedures/Validate-Recovery-Email-and-Reset-Password]]'
step_count: 5
techniques:
  - '[[Account Manipulation]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.477Z'
description: >-
  Multi-stage attack exploiting IDOR in a DoD social network to takeover user
  accounts by manipulating recovery emails and disclosing usernames.
skill_level: intermediate
impact_level: high
id: 62b4bb79-fcef-43f6-9b39-6b0cfa730e3e
validated: true
mitre_tactics:
  - '[[Persistence]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Account Discovery]]'
---
# IDOR in /self Endpoint Leading to Account Takeover via Recovery Email Manipulation

Multi-stage attack chain demonstrating a complete account takeover workflow on a U.S. Department of Defense social network via IDOR and information disclosure.

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
    A[Intercept 2FA Request] --> B[Disclose Username]
    B --> C[Modify Recovery Email]
    C --> D[Reset Password]
    D --> E[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox-Multi-Account-Containers]]
- Browser or proxy tool (e.g., Burp Suite) for request interception and modification

### Target Environment

- Web platform (ASP.NET-based social network)
- Valid user session cookies and __RequestVerificationToken
- Target users without pre-verified recovery emails

### Initial Access Requirements

- Authenticated session on the target site
- Knowledge of victim's user ID
- No special network position required (public-facing web app)

## Detailed Attack Procedures

### Step 1: Intercept and Identify IDOR
procedure: [[procedures/Intercept-and-Identify-IDOR-in-Self-Endpoint]]

**Objective**: Capture the 2FA toggle request to uncover the vulnerable /self endpoint and IDOR parameters.

**Instructions**: Use a browser with session isolation or a proxy to monitor network traffic during the 2FA authentication switch process. Intercept the POST request to /self and inspect parameters like userName, originalEmail, Email, and RecoveryEmail, which lack authorization checks.

**Expected Output**: Captured POST request revealing modifiable parameters without ownership verification.

**Success Indicators**:
- Request intercepted successfully
- Parameters identified as vulnerable to IDOR

### Step 2: Retrieve Victim Username
procedure: [[procedures/Retrieve-Victim-Username-via-Friends-API]]

**Objective**: Use the friends API to disclose the victim's username from their user ID for targeted attacks.

**Instructions**: Send a POST request to /api.ashx/v2/users/{userId}/friends.json with RequesteeId set to the victim's ID using a valid session. Parse the response's ProfileUrl to extract the username.

**Expected Output**: JSON response containing ProfileUrl with the victim's username.

**Success Indicators**:
- Username successfully retrieved
- No access controls blocking the request

### Step 3: Modify Recovery Email
procedure: [[procedures/Modify-Self-Request-to-Add-Attacker-Recovery-Email]]

**Objective**: Exploit IDOR to add the attacker's email as a recovery option to the victim's account.

**Instructions**: Modify the intercepted /self POST request, setting userName to victim's username, originalEmail and Email to victim's email, and RecoveryEmail to attacker's email. Replay the request with valid cookies and __RequestVerificationToken. This works only if the victim has no verified recovery email.

**Expected Output**: Server response confirming the recovery email addition (e.g., 200 OK without errors).

**Success Indicators**:
- Recovery email added to victim's account
- No authorization errors

### Step 4: Request Password Reset
procedure: [[procedures/Request-Password-Reset-Using-Added-Recovery-Email]]

**Objective**: Trigger a password reset to send the link to the attacker's controlled recovery email.

**Instructions**: Initiate a password reset for the victim's account through the site's reset functionality, ensuring the link is routed to the newly added recovery email.

**Expected Output**: Password reset link received in attacker's email inbox.

**Success Indicators**:
- Reset link delivered to attacker
- Victim unaware of the change

### Step 5: Validate and Takeover Account
procedure: [[procedures/Validate-Recovery-Email-and-Reset-Password]]

**Objective**: Confirm the recovery email and use the reset link to gain full control of the victim's account.

**Instructions**: Access the recovery email confirmation link (e.g., /self?guid=...) using any valid session, validate it, set a new password, and log in as the victim.

**Expected Output**: Successful login with the new password, granting full account access.

**Success Indicators**:
- Account login successful
- Control over victim's profile and data

## Attack Chain Summary

### Key Achievements

1. Unauthorized addition of recovery email via IDOR
2. Username disclosure for targeting
3. Complete account takeover affecting potentially thousands of users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Persistence]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
