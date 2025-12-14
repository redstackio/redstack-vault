---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - clickjacking
  - account-takeover
  - wordpress
  - csrf-bypass
  - privilege-escalation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-WordPress-User-Accounts]]'
  - '[[procedures/Embed-Malicious-Iframe-in-WordPress-Post]]'
  - '[[procedures/Publish-Malicious-WordPress-Post]]'
  - '[[procedures/Log-In-as-Victim-User]]'
  - '[[procedures/Induce-Victim-to-Visit-Malicious-Post]]'
  - '[[procedures/Verify-Account-Takeover-and-Escalation]]'
step_count: 6
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.329Z'
description: >-
  Multi-stage attack enabling WordPress editors to takeover lower-privileged
  user accounts through clickjacking with malicious HTML iframes in posts,
  bypassing CSRF and leading to privilege escalation and potential RCE.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
  - '[[Valid Accounts]]'
---
# WordPress Account Takeover via Clickjacking by Editor Users

Multi-stage attack chain demonstrating a complete attack workflow for account takeover in WordPress using clickjacking.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Accounts] --> B[Create Malicious Post]
    B --> C[Publish Post]
    C --> D[Victim Logs In]
    D --> E[Victim Visits Post]
    E --> F[Verify Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser-based actions)

### Target Environment

- WordPress 4.9.7 or similar vulnerable version
- PHP backend
- Port 9080 (or standard 80/443) for web access

### Initial Access Requirements

- Attacker has editor role credentials
- Victim has author/subscriber role
- Network access to WordPress site

## Detailed Attack Procedures

### Step 1: Create User Accounts
procedure: [[procedures/Create-WordPress-User-Accounts]]

**Objective**: Establish attacker (editor) and victim (author/subscriber) accounts to simulate the privilege differential.

**Instructions**: Access the WordPress admin dashboard and create the necessary user roles via the Users > Add New section. Assign editor role to attacker account and author/subscriber to victim.

**Expected Output**: Two active user accounts with specified roles.

**Success Indicators**:
- Editor account login successful
- Lower-privileged account created and verifiable

### Step 2: Create Malicious Post as Editor
procedure: [[procedures/Embed-Malicious-Iframe-in-WordPress-Post]]

**Objective**: Embed hidden iframe and JavaScript in a post to load and manipulate the victim's profile page.

**Instructions**: Log in as editor, go to Posts > Add New, and insert custom HTML with a hidden iframe pointing to the profile page (e.g., replace with attacker's IP if proxied: http://159.65.157.23:9080/wp-admin/profile.php). Include JavaScript to alter fields like first_name.value = 'hacked by rewanthcool' and trigger submit.

**Expected Output**: Draft post with embedded malicious HTML.

**Success Indicators**:
- HTML embeds without filtering errors
- Iframe src loads correctly in preview

### Step 3: Publish the Malicious Post
procedure: [[procedures/Publish-Malicious-WordPress-Post]]

**Objective**: Make the post publicly accessible to lure the victim.

**Instructions**: In the post editor, click Publish to go live, then copy the generated post URL for sharing.

**Expected Output**: Live post URL accessible via browser.

**Success Indicators**:
- Post visible on frontend
- URL copied for distribution

### Step 4: Log In as Victim
procedure: [[procedures/Log-In-as-Victim-User]]

**Objective**: Ensure victim session is active for iframe context exploitation.

**Instructions**: In a separate incognito browser or session, log in to the WordPress site using the victim account credentials.

**Expected Output**: Victim dashboard accessible.

**Success Indicators**:
- Victim session authenticated
- No logout or errors

### Step 5: Victim Visits Malicious Post
procedure: [[procedures/Induce-Victim-to-Visit-Malicious-Post]]

**Objective**: Trigger the clickjacking payload by having the victim load the post.

**Instructions**: Direct the victim to paste and visit the malicious post URL; the hidden iframe loads in the victim's session, generating a fresh CSRF nonce and executing JS to submit profile changes.

**Expected Output**: Automatic form submission in background.

**Success Indicators**:
- No visible changes to victim
- Iframe executes without errors (check browser console if needed)

### Step 6: Verify Account Takeover
procedure: [[procedures/Verify-Account-Takeover-and-Escalation]]

**Objective**: Confirm profile alterations and escalate if targeting admin accounts.

**Instructions**: As victim, revisit /wp-admin/profile.php to check changes (e.g., name updated). For full takeover, modify payload for email change, reset password, logout sessions, then use new credentials to install vulnerable plugins for RCE.

**Expected Output**: Altered profile data; potential admin access.

**Success Indicators**:
- Profile fields modified
- Password reset email to attacker
- Privilege escalation to admin

## Attack Chain Summary

### Key Achievements

1. Bypassed CSRF via session-context iframe nonce
2. Achieved account takeover without direct interaction
3. Enabled privilege escalation to RCE via plugin installation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
