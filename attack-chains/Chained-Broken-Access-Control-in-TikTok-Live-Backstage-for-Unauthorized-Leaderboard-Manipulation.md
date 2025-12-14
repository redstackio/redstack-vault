---
id: ac-tiktok-leaderboard-bac-001
tags:
  - broken-access-control
  - tiktok
  - leaderboard
  - access-bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Broken-Access-Control-in-TikTok-Live-Backstage]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.275Z'
description: >-
  A chained broken access control vulnerability allowing low-privilege users to
  gain full unauthorized control over public leaderboard activities of other
  organizations in TikTok Live Backstage.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Chained Broken Access Control in TikTok Live Backstage for Unauthorized Leaderboard Manipulation

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient access controls in TikTok's Live Backstage to manipulate public leaderboards of unrelated organizations.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access as Low-Priv User] --> B[Exploit Access Control Bypass]
    B --> C[Manipulate Leaderboard Activities]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)

### Target Environment

- TikTok Live Backstage web application
- Access to a low-privilege account (group member or leader)

### Initial Access Requirements

- Valid low-privilege credentials for TikTok account
- Network access to TikTok web platform
- No prior admin access needed

## Detailed Attack Procedures

### Step 1: Exploit Broken Access Control
procedure: [[procedures/Exploit-Broken-Access-Control-in-TikTok-Live-Backstage]]

**Objective**: Gain unauthorized control over public leaderboard activities of other organizations by bypassing access controls with low-privilege credentials.

**Instructions**: Log in to TikTok Live Backstage with a low-privilege account. Navigate to the public leaderboard management interface intended for the attacker's organization. Modify the URL or use developer tools to alter parameters targeting another organization's leaderboard ID (e.g., change org_id in the request). Submit actions to manipulate rankings, such as adding/removing entries or altering scores.

**Expected Output**: Successful manipulation of the target organization's leaderboard without error, visible changes in live event rankings.

**Success Indicators**:
- Leaderboard updates applied to unrelated organization
- No access denied errors during manipulation
- Real-time reflection of changes in public view

## Attack Chain Summary

### Key Achievements

1. Bypassed organization-specific access controls using low-privilege account
2. Achieved full control over public leaderboard features of other organizations
3. Enabled disruption of live events and rankings without detection

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
