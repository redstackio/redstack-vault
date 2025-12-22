---
id: ac-uuid-placeholder
tags:
  - xss
  - persistent-xss
  - owncloud
  - javascript-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-XSS-Payload-into-ownCloud-Profile-Name]]'
step_count: 1
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.977Z'
description: >-
  A persistent XSS attack exploiting unsanitized quotation marks in ownCloud
  profile names to inject JavaScript that executes when other users view the
  affected profile, enabling session theft or further browser compromise.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Persistent XSS in ownCloud Account Profile via Unsanitized Name Fields

Multi-stage attack chain demonstrating a complete attack workflow exploiting a persistent XSS vulnerability in ownCloud's account profile feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Inject Payload into Profile] --> B[Profile View Triggers Execution]
    B --> C[JavaScript Executes in Victim Browser]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- ownCloud web application
- Authenticated user account
- No special services or ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Valid ownCloud user credentials
- Direct access to the ownCloud web interface
- No prior network compromise needed

## Detailed Attack Procedures

### Step 1: Inject XSS Payload
procedure: [[procedures/Inject-XSS-Payload-into-ownCloud-Profile-Name]]

**Objective**: Inject a malicious JavaScript payload into the account profile's first or last name field to break out of an embedded <iframe> tag and enable persistent XSS execution when other users view the profile.

**Instructions**: Log in to the ownCloud instance, navigate to the account profile settings, and enter a payload like "><script>alert('XSS')</script> into the first name field. Save the changes. When another user views the affected profile, the payload executes in their browser context.

**Expected Output**: Successful save without errors; alert() or other JS triggers on profile view by victims.

**Success Indicators**:
- Profile updates successfully
- JavaScript executes (e.g., alert box appears) when viewing the profile from another account
- Potential for cookie theft or BeEF hooking confirmed via network inspection

## Attack Chain Summary

### Key Achievements

1. Persistent storage of malicious JavaScript in user profile
2. Arbitrary code execution in the browser of any user viewing the profile
3. Potential for session hijacking or advanced browser exploitation (e.g., via BeEF)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
