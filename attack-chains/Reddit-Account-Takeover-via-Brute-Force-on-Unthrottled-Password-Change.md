---
id: ac-reddit-bruteforce-pwchange-001
tags:
  - brute-force
  - rate-limit-bypass
  - account-takeover
  - credential-access
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Test-Reddit-Account]]'
  - '[[procedures/Intercept-Reddit-Password-Change-Request]]'
  - '[[procedures/Brute-Force-Old-Password-with-Burp-Intruder]]'
step_count: 4
techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.357Z'
description: >-
  Demonstrates account takeover on Reddit by brute-forcing the old password
  during password change due to absent rate limiting, using session hijacking as
  a prerequisite.
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
# Reddit Account Takeover via Brute-Force on Unthrottled Password Change

Multi-stage attack chain demonstrating a complete attack workflow exploiting the lack of rate limiting on Reddit's password change endpoint, allowing unlimited brute-force attempts on the old password field.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Test Account] --> B[Intercept Password Change Request]
    B --> C[Brute-Force Old Password]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform (Reddit old interface at https://old.reddit.com)
- No specific ports or services beyond standard HTTPS (443)
- Attacker requires initial session access (e.g., via stolen cookies from XSS)

### Initial Access Requirements

- Valid session cookies for the target account (e.g., obtained via XSS or other session hijacking)
- Network access to Reddit's web interface
- Burp Suite configured as a proxy for traffic interception

## Detailed Attack Procedures

### Step 1: Create Test Account
procedure: [[procedures/Create-Test-Reddit-Account]]

**Objective**: Establish a controlled test environment on Reddit to simulate the target account for vulnerability verification.

**Instructions**: Register a new account on the old Reddit interface and set an initial password known to the attacker.

**Expected Output**: Successful account creation with the specified password.

**Success Indicators**:
- Account login successful with initial password
- Access to user preferences page confirmed

### Step 2: Initiate Password Change and Intercept Request
procedure: [[procedures/Intercept-Reddit-Password-Change-Request]]

**Objective**: Trigger a password change attempt to capture the HTTP request structure for subsequent brute-forcing.

**Instructions**: Navigate to the password update page, enter an incorrect old password along with new credentials, and intercept the submission using Burp Suite proxy.

**Expected Output**: Captured POST request to the password update endpoint with parameters for old_password, new_password, and confirm_new_password.

**Success Indicators**:
- Request intercepted in Burp Suite
- Response indicates failed verification due to wrong old password (no rate limit error)

### Step 3: Brute-Force Old Password Field
procedure: [[procedures/Brute-Force-Old-Password-with-Burp-Intruder]]

**Objective**: Automate guessing of the old password using a wordlist to identify the correct one and change the account password.

**Instructions**: Send the intercepted request to Burp Intruder, configure the old_password parameter as the payload position, load a wordlist of 8890 entries including common passwords, and launch the attack. Monitor for a successful response indicating password change.

**Expected Output**: After ~8000 requests, a successful response (e.g., 200 OK with password updated confirmation) when the correct password is guessed.

**Success Indicators**:
- No throttling or CAPTCHA observed across requests
- Password change succeeds, allowing login with new credentials
- Account fully controlled by attacker

### Step 4: Validate Account Takeover

**Objective**: Confirm control over the account post-brute-force to demonstrate full takeover.

**Instructions**: Log in to the account using the new password set during the successful brute-force attempt. Verify access to account settings, posts, and other features.

**Expected Output**: Unrestricted access to the account dashboard and functionalities.

**Success Indicators**:
- Login successful with new password
- Ability to perform actions like posting or changing settings

## Attack Chain Summary

### Key Achievements

1. Exposed lack of rate limiting on password verification, enabling efficient brute-force attacks.
2. Demonstrated how session hijacking (e.g., via XSS) combines with this flaw for complete account takeover.
3. Highlighted the risk of unlimited attempts (~8000+ requests) without detection or blocking.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
