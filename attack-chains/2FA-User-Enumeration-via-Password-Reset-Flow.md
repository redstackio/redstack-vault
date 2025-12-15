---
tags:
  - user-enumeration
  - 2fa-enumeration
  - business-logic
  - password-reset
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enumerate-2FA-Status-via-Password-Reset]]'
step_count: 2
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.406Z'
description: >-
  A business logic flaw in the password reset process that leaks whether users
  have 2FA enabled by differing response prompts.
skill_level: beginner
impact_level: medium
id: da21812a-2d67-4ec3-b9be-0f942d51342d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# 2FA User Enumeration via Password Reset Flow

Multi-stage attack chain demonstrating a business logic vulnerability in the password reset workflow that allows enumeration of 2FA-enabled users.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate Password Reset] --> B[Observe Response Differences]
    B --> C[Infer 2FA Status]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[tools/curl]]

### Target Environment

- Web application with password reset functionality
- No special services or ports required beyond standard HTTPS (443)
- Network access to the login/reset endpoint

### Initial Access Requirements

- Public access to the password reset page
- No credentials needed
- Ability to submit reset requests for arbitrary email addresses

## Detailed Attack Procedures

### Step 1: Initiate Password Reset
procedure: [[procedures/Enumerate-2FA-Status-via-Password-Reset]]

**Objective**: Trigger the password reset flow for target user accounts to observe initial responses.

**Instructions**: Navigate to the password reset page and enter a target user's email address. Submit the request to start the reset process. This can be done manually via the web form or using a tool like curl to simulate the request.

For example, using a browser:
- Go to `/forgot-password` or similar endpoint.
- Input email: `target@example.com`.
- Submit.

Or via curl:
```bash
curl -X POST https://target.com/api/forgot-password -d 'email=target@example.com'
```

**Expected Output**: A response indicating the reset initiation, such as a success message or redirect to verification.

**Success Indicators**:
- Reset request accepted without errors
- Flow proceeds to next stage (e.g., code entry or 2FA prompt)

### Step 2: Observe 2FA Prompt Differences
procedure: [[procedures/Enumerate-2FA-Status-via-Password-Reset]]

**Objective**: Analyze the reset flow's response to determine if 2FA is enabled for the user.

**Instructions**: After initiating the reset, monitor the subsequent prompts. If 2FA is enabled, the system will prompt for a second factor (e.g., TOTP code). If not, it will proceed directly to password entry or email code verification without mentioning 2FA. Repeat for multiple users to enumerate status.

In a browser, follow the flow after submission. For automated testing, inspect responses:
```bash
curl -X POST https://target.com/api/reset-verify -d 'token=reset_token&code=123456'
```
Observe if the response includes a 2FA challenge field or error.

**Expected Output**: Differentiated UI/API responses: 2FA prompt for enabled users, direct password set for disabled.

**Success Indicators**:
- Clear distinction in flow based on 2FA status
- Ability to infer enablement for tested users

## Attack Chain Summary

### Key Achievements

1. Successful enumeration of 2FA status for arbitrary users
2. Identification of business logic flaw in reset flow
3. Potential complication of targeted attacks due to exposed security configs, though rate-limiting mitigates abuse

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]] Account Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
