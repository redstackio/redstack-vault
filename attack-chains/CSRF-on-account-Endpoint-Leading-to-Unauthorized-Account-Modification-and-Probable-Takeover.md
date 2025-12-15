---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - csrf
  - account-takeover
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Broken-CSRF-Protection-on-account-Endpoint]]'
  - '[[procedures/Exploit-CSRF-to-Modify-Account-Information]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:12.230Z'
description: >-
  A multi-stage attack exploiting broken CSRF protection on the /account
  endpoint of https://www.niche.co to modify user account details, such as
  email, potentially enabling account takeover limited by Twitter integration.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# CSRF on /account Endpoint Leading to Unauthorized Account Modification and Probable Takeover

Multi-stage attack chain demonstrating a complete attack workflow exploiting broken CSRF protection on https://www.niche.co to enable unauthorized changes to user account information, such as email addresses, leading to probable account takeover despite limitations from Twitter credential handling.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Broken CSRF] --> B[Exploitation for Account Modification]
    B --> C[Probable Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for inspecting requests
- Proxy tool like Burp Suite for request manipulation (optional but recommended)

### Target Environment

- Web platform
- Services: Twitter integration for authentication
- Network access: Direct access to https://www.niche.co as a logged-in user

### Initial Access Requirements

- Valid user session on https://www.niche.co (logged in via Twitter)
- Ability to trick the victim into interacting with a malicious page or link
- No prior privileged access needed

## Detailed Attack Procedures

### Step 1: Discovery of Broken CSRF Protection
procedure: [[procedures/Discover-Broken-CSRF-Protection-on-account-Endpoint]]

**Objective**: Identify the absence of CSRF protection on the /account endpoint to confirm vulnerability to unauthorized requests.

**Instructions**: Log in to https://www.niche.co using Twitter credentials. Use browser developer tools to inspect the /account endpoint. Attempt to submit a test request without a CSRF token to verify if the server accepts it without validation. For example, craft a simple POST request to /account to change a non-sensitive field and observe if it succeeds without the expected CSRF header or token.

**Expected Output**: Successful modification without CSRF token, confirming broken protection.

**Success Indicators**:
- Request accepted without CSRF token
- Account details altered successfully in testing

### Step 2: Exploitation for Account Modification
procedure: [[procedures/Exploit-CSRF-to-Modify-Account-Information]]

**Objective**: Trick a logged-in user into submitting a malicious request to the /account endpoint, altering sensitive information like the email address to facilitate takeover.

**Instructions**: Create a malicious HTML page hosting a form that submits a POST request to https://www.niche.co/account with parameters to change the email (e.g., new_email=attacker@example.com). Host this page on a controlled domain and lure the victim (logged-in user) to visit it via phishing or social engineering. The form auto-submits using JavaScript to exploit the valid session cookie.

**Expected Output**: Victim's account email updated to attacker's control, confirmed by checking the account details post-exploitation.

**Success Indicators**:
- Email address changed without victim interaction on the legitimate site
- Potential for password reset or takeover via the new email, limited by Twitter auth

## Attack Chain Summary

### Key Achievements

1. Confirmed broken CSRF on /account endpoint allowing unauthorized modifications
2. Demonstrated exploitation leading to email changes for probable account takeover
3. Highlighted limitations due to Twitter integration preventing full credential compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
