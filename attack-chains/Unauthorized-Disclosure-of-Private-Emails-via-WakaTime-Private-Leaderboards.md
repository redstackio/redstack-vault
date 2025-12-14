---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - information-disclosure
  - privacy-misconfiguration
  - email-harvesting
  - pii-exposure
  - wakatime
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Create-WakaTime-Private-Leaderboard]]'
  - '[[procedures/Invite-User-to-WakaTime-Leaderboard]]'
  - '[[procedures/User-Joins-WakaTime-Leaderboard]]'
  - '[[procedures/Observe-Private-Email-Disclosure-on-WakaTime-Leaderboard]]'
step_count: 4
techniques:
  - '[[Employee Names]]'
updated_at: '2025-12-14T17:30:35.755Z'
description: >-
  A privacy misconfiguration in WakaTime's private leaderboards that exposes
  users' private email addresses to leaderboard members, bypassing privacy
  settings and enabling unauthorized PII collection.
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Employee Names]]'
---
# Unauthorized Disclosure of Private Emails via WakaTime Private Leaderboards

Multi-stage attack chain demonstrating a complete attack workflow exploiting a privacy misconfiguration in WakaTime's private leaderboards feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Private Leaderboard] --> B[Invite Target User]
    B --> C[Target User Joins]
    C --> D[Observe Email Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- WakaTime web platform (wakatime.com)
- Active WakaTime accounts for attacker and target user

### Initial Access Requirements

- Attacker must have a WakaTime account with leaderboard creation privileges
- Target user must have a WakaTime account with private email settings enabled
- No special network access beyond internet connectivity

## Detailed Attack Procedures

### Step 1: Create Private Leaderboard
procedure: [[procedures/Create-WakaTime-Private-Leaderboard]]

**Objective**: Set up a controlled environment to invite the target and trigger the disclosure.

**Instructions**: Log in to your WakaTime account, navigate to the dashboard, and use the leaderboard creation interface to generate a new private leaderboard. Specify it as private during setup to restrict visibility.

**Expected Output**: A new private leaderboard is created, with a unique URL and management page accessible only to the creator.

**Success Indicators**:
- Leaderboard appears in your dashboard
- Invitation functionality is available on the management page

### Step 2: Invite Target User
procedure: [[procedures/Invite-User-to-WakaTime-Leaderboard]]

**Objective**: Send an invitation to the target user to join the private leaderboard, setting the stage for membership-based disclosure.

**Instructions**: From the leaderboard management page, enter the target user's WakaTime username or public profile link to generate and send the invite. Confirm the invitation is dispatched via WakaTime's notification system.

**Expected Output**: Invitation email or notification sent to the target user.

**Success Indicators**:
- Invite status shows as pending in the leaderboard management
- Target user receives the invitation in their WakaTime account

### Step 3: Target User Joins Leaderboard
procedure: [[procedures/User-Joins-WakaTime-Leaderboard]]

**Objective**: Ensure the target becomes a member, activating the vulnerability trigger.

**Instructions**: Coordinate with or wait for the target user to log in to their WakaTime account, view the invitation, and accept it to join the private leaderboard.

**Expected Output**: Target user appears as a member on the leaderboard roster.

**Success Indicators**:
- Member list updates to include the target
- Leaderboard page reflects the new joiner

### Step 4: Observe Email Disclosure
procedure: [[procedures/Observe-Private-Email-Disclosure-on-WakaTime-Leaderboard]]

**Objective**: Access and capture the exposed private email address, demonstrating the privacy bypass.

**Instructions**: Refresh or navigate to the private leaderboard page in your browser. Inspect the member details or UI elements where user information is displayed to view the target's private email.

**Expected Output**: The target's private email address is visible in the leaderboard interface, despite their privacy settings.

**Success Indicators**:
- Email address appears in plain text on the page
- No consent or opt-in prompt was required for exposure

## Attack Chain Summary

### Key Achievements

1. Bypassed user privacy settings to access private PII
2. Enabled potential email harvesting for phishing or spam campaigns
3. Highlighted compliance risks under GDPR/CCPA due to unconsented data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Employee Names]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T12:00:00Z*
