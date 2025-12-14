---
tags:
  - auth-bypass
  - wordpress
  - jetpack
  - sso
  - account-takeover
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-and-Configure-JetPack-on-Target-WordPress-Site]]'
  - '[[procedures/Create-User-Account-on-WordPress-Site-with-Target-Email]]'
  - '[[procedures/Create-Confirmed-WordPress-com-Account-with-Personal-Email]]'
  - '[[procedures/Create-Unconfirmed-WordPress-com-Account-with-Victims-Email]]'
  - '[[procedures/Invite-Second-Account-from-Confirmed-Account]]'
  - '[[procedures/Accept-Invitation-on-Second-Account-to-Verify-Email]]'
  - '[[procedures/Access-WordPress-Admin-Panel-via-SSO]]'
step_count: 7
techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:31:42.777Z'
description: >-
  Multi-stage authentication bypass exploiting a flaw in WordPress.com's email
  verification process to gain unauthorized access to a JetPack-enabled
  WordPress site's admin panel without victim interaction.
skill_level: intermediate
impact_level: high
id: 1579cda2-a040-4c0d-8c0b-177d4850cdab
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[External Remote Services]]'
---
# JetPack SSO Authentication Bypass via WordPress.com Email Verification Flaw

Multi-stage attack chain demonstrating a complete authentication bypass workflow on JetPack-enabled WordPress sites.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Target Environment] --> B[Prepare Attacker Accounts]
    B --> C[Exploit Verification Flaw]
    C --> D[Gain Admin Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for manual testing
- Access to a self-hosted WordPress site (for simulation)

### Target Environment

- Self-hosted WordPress site with JetPack plugin installed
- WordPress.com account creation access
- No special ports required; operates over standard HTTPS (443)

### Initial Access Requirements

- No prior credentials needed
- Attacker must have internet access to WordPress.com and the target site
- Target site must have JetPack SSO enabled with 'Match accounts using email addresses' option activated

## Detailed Attack Procedures

### Step 1: Install and Configure JetPack
procedure: [[procedures/Install-and-Configure-JetPack-on-Target-WordPress-Site]]

**Objective**: Prepare the target WordPress site for the SSO vulnerability by enabling JetPack and the matching feature.

**Instructions**: Log into the WordPress admin dashboard, navigate to Plugins > Add New, search for and install the latest JetPack plugin, then activate it. Go to JetPack > Settings and enable the 'Match accounts using email addresses' option in the SSO section.

**Expected Output**: JetPack status shows as connected, and SSO settings confirm email matching is active.

**Success Indicators**:
- JetPack plugin listed as active in the plugins dashboard
- 'Match accounts using email addresses' toggle is enabled

### Step 2: Create User Account with Target Email
procedure: [[procedures/Create-User-Account-on-WordPress-Site-with-Target-Email]]

**Objective**: Establish a user on the target site using the victim's email to enable later matching.

**Instructions**: In the WordPress admin panel, go to Users > Add New, enter a username, set the email to the victim's address (e.g., victim@company.com), and assign an admin role if desired. Save the user without requiring immediate password setup.

**Expected Output**: New user appears in the Users list with the specified email.

**Success Indicators**:
- User profile shows the target email
- No email verification sent to the victim at this stage

### Step 3: Create Confirmed WordPress.com Account
procedure: [[procedures/Create-Confirmed-WordPress-com-Account-with-Personal-Email]]

**Objective**: Set up a controlled, verified account on WordPress.com to use for invitations.

**Instructions**: Visit wordpress.com, click Sign Up, provide the attacker's personal email, create a username and password, then check the personal email inbox to click the confirmation link sent by WordPress.com.

**Expected Output**: Account dashboard accessible, with email status marked as verified.

**Success Indicators**:
- Login successful without prompts for email verification
- Profile settings show confirmed email

### Step 4: Create Unconfirmed WordPress.com Account
procedure: [[procedures/Create-Unconfirmed-WordPress-com-Account-with-Victims-Email]]

**Objective**: Register an account using the victim's email without completing verification.

**Instructions**: On wordpress.com, sign up again using the victim's email (e.g., victim@company.com), choose a username and password, but do not click any confirmation link in the email (which won't arrive to the attacker anyway).

**Expected Output**: Account created but email remains unverified; login possible but limited.

**Success Indicators**:
- Account login works with the provided credentials
- Notifications or settings indicate email is unconfirmed

### Step 5: Invite Second Account from Confirmed Account
procedure: [[procedures/Invite-Second-Account-from-Confirmed-Account]]

**Objective**: Use the confirmed account to send an invitation that bypasses ownership checks.

**Instructions**: Log into the confirmed personal WordPress.com account, navigate to Settings > Users, enter the victim's email (victim@company.com) in the invite field, and send the invitation.

**Expected Output**: Invitation sent; notification appears in the target account's dashboard.

**Success Indicators**:
- Invite email or notification queued
- No errors about email ownership

### Step 6: Accept Invitation to Verify Email
procedure: [[procedures/Accept-Invitation-on-Second-Account-to-Verify-Email]]

**Objective**: Accept the invite to falsely verify the victim's email without actual ownership.

**Instructions**: Log into the unconfirmed WordPress.com account with the victim's email, check the notifications or account settings for the pending invitation, and click to accept it.

**Expected Output**: Email status updates to verified in the account settings.

**Success Indicators**:
- Profile shows email as confirmed
- No further verification prompts

### Step 7: Access Admin Panel via SSO
procedure: [[procedures/Access-WordPress-Admin-Panel-via-SSO]]

**Objective**: Use the verified fake account to log into the target site's admin via JetPack SSO.

**Instructions**: From the now-verified WordPress.com account, visit the target WordPress site (e.g., host.com/wp-admin), click 'Sign in with WordPress.com', and authenticate; the site matches the email and grants access.

**Expected Output**: Redirected to the WordPress admin dashboard as the matched user.

**Success Indicators**:
- Admin panel loads with elevated privileges
- No additional authentication required

## Attack Chain Summary

### Key Achievements

1. Bypassed email ownership verification on WordPress.com
2. Achieved account takeover on JetPack-enabled WordPress site
3. Gained admin access without victim interaction, enabling further exploits like RCE via plugin uploads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[External Remote Services]] External Remote Services

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
