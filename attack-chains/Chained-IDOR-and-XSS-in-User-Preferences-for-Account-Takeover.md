---
tags:
  - idor
  - xss
  - account-takeover
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Browser-DevTools]]'
  - '[[tools/Local-Proxy]]'
  - '[[tools/Email-Client]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Team-and-Users]]'
  - '[[procedures/Discover-Target-User-UUID]]'
  - '[[procedures/Exploit-IDOR-to-Update-Preferences-with-XSS]]'
  - '[[procedures/Trigger-XSS-in-Victim-Preferences]]'
  - '[[procedures/Perform-Account-Takeover-via-Password-Reset]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:25:29.263Z'
description: >-
  A multi-stage attack exploiting Insecure Direct Object Reference (IDOR) in the
  user preferences API to inject XSS payloads and change emails, enabling cookie
  theft and account takeover via password reset.
skill_level: intermediate
impact_level: high
id: 6ed45073-f870-452d-be83-b0dfeeabaf0f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Chained IDOR and XSS in User Preferences for Account Takeover

Multi-stage attack chain demonstrating exploitation of an IDOR vulnerability in the /api/v1/user/preferences/{uuid} endpoint, allowing low-privilege users to modify any team member's data. This leads to injecting XSS payloads into the signature field for cookie theft and changing the email for password reset hijacking, resulting in full account takeover.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Team] --> B[Discover UUID]
    B --> C[Exploit IDOR with XSS]
    C --> D[Trigger XSS]
    D --> E[Account Takeover]
    E --> F[Objective Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-DevTools]]
- [[tools/Local-Proxy]]
- [[tools/Email-Client]]

### Target Environment

- Web application platform (e.g., Outpost.co-like SaaS)
- Required services: API endpoints over HTTPS, email service for resets
- Network access: Direct browser access to app.outpost.co and api.outpost.co

### Initial Access Requirements

- Valid user credentials for low-privilege 'USER' role
- Ability to invite team members (admin access for setup)
- Control over an email address for receiving resets

## Detailed Attack Procedures

### Step 1: Setup Team and Users
procedure: [[procedures/Setup-Team-and-Users]]

**Objective**: Create a team environment with an admin (victim) and low-privilege user (attacker) to enable team-based UUID exposure.

**Instructions**: Log in as an admin user (user1) and invite a new user (user2) with 'USER' role using the application's invitation features.

**Expected Output**: user2 account created and joined to the team.

**Success Indicators**:
- Invitation email sent and accepted
- user2 visible in team roster

### Step 2: Discover Target User UUID
procedure: [[procedures/Discover-Target-User-UUID]]

**Objective**: Extract the victim's (user1) UUID from network traffic during legitimate app interactions.

**Instructions**: Log in as user2, navigate to the Mail tab, and select user1 from the Conversation assignment dropdown. Use [[tools/Browser-DevTools]] or [[tools/Local-Proxy]] to monitor the GET request to https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid={uuid}.

Execute [[commands/get-conversation-assigned]] to capture the UUID:

```bash
# Monitored via DevTools or Proxy
GET https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid=da4f313f-e21e-4b5f-b2da-42d9864716f6
```

**Expected Output**: Network response revealing the full UUID of user1.

**Success Indicators**:
- UUID copied (e.g., da4f313f-e21e-4b5f-b2da-42d9864716f6)
- No authentication errors

### Step 3: Exploit IDOR to Update Preferences with XSS
procedure: [[procedures/Exploit-IDOR-to-Update-Preferences-with-XSS]]

**Objective**: Use the discovered UUID to update user1's preferences, changing email to attacker's and injecting XSS in signature.

**Instructions**: Craft a PUT request to /api/v1/user/preferences/{user1-uuid} using user2's auth cookie. Set email to {attacker-email} and signature to XSS payload.

Execute [[commands/put-update-preferences]] via proxy or curl:

```bash
curl -X PUT \
  https://api.outpost.co/api/v1/user/preferences/da4f313f-e21e-4b5f-b2da-42d9864716f6 \
  -H "Cookie: auth={user2-cookie}" \
  -H "Content-Type: application/json" \
  -d '{"firstName":"user1-changed-by-user2","lastName":"null","email":"{attacker-email}","role":"USER","defaultMailboxUuid":"","mailboxUuids":["e4a63ae3-bb10-46f8-be28-a2660a2344ec"],"signature":"<p style=\"margin:0;\">User Signature2<img src=x onerror=alert(document.cookie) ></p>","timezone":"Europe/Moscow","defaultSendAndResolve":false,"selectFirstConversation":true}'
```

**Expected Output**: HTTP 200 response confirming update.

**Success Indicators**:
- Preferences updated without permission errors
- Email and signature modified

### Step 4: Trigger XSS in Victim Preferences
procedure: [[procedures/Trigger-XSS-in-Victim-Preferences]]

**Objective**: Cause the victim to execute the injected XSS by viewing their preferences page.

**Instructions**: Have user1 log in and navigate to https://app.outpost.co/settings/preferences, where the signature field renders the XSS payload.

**Expected Output**: Alert box displaying user1's cookies (e.g., document.cookie contents).

**Success Indicators**:
- XSS payload executes (alert fires)
- Cookies visible for theft

### Step 5: Perform Account Takeover via Password Reset
procedure: [[procedures/Perform-Account-Takeover-via-Password-Reset]]

**Objective**: Use the changed email to hijack user1's account via password reset.

**Instructions**: As attacker, go to https://app.outpost.co/sign-in/help, enter {attacker-email}, receive reset link in [[tools/Email-Client]], follow it to set new password, then log in with user1's original email and new password.

**Expected Output**: Successful login as user1 with full access.

**Success Indicators**:
- Reset email received
- New password sets without issues
- Admin access gained

## Attack Chain Summary

### Key Achievements

1. Bypassed authorization to modify any team member's data via IDOR
2. Injected and triggered reflected XSS for session hijacking
3. Achieved full account takeover by redirecting password resets

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
