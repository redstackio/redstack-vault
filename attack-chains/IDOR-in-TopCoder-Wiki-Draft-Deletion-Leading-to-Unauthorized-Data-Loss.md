---
id: ac-idor-topcoder-draft-deletion
tags:
  - idor
  - web-vulnerability
  - unauthorized-deletion
  - data-loss
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-TopCoder-Drafts-Viewing-Page]]'
  - '[[procedures/Test-Own-Draft-Deletion]]'
  - '[[procedures/Exploit-IDOR-to-Delete-Foreign-Draft]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.587Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  the TopCoder wiki application's draft management to delete other users' drafts
  without ownership verification.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR in TopCoder Wiki Draft Deletion Leading to Unauthorized Data Loss

Multi-stage attack chain demonstrating a complete attack workflow exploiting IDOR in the TopCoder wiki draft management feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Drafts Page] --> B[Test Own Deletion]
    B --> C[Exploit IDOR for Foreign Deletion]
    C --> D[Data Loss Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or proxy tool like Burp Suite for request manipulation

### Target Environment

- Web platform
- TopCoder wiki application at https://apps.topcoder.com/wiki
- Authenticated access to the application

### Initial Access Requirements

- Valid user credentials for the TopCoder wiki
- Knowledge of target user's draft ID (e.g., via social engineering or enumeration)
- Network access to the wiki endpoint

## Detailed Attack Procedures

### Step 1: Access Drafts Viewing Page
procedure: [[procedures/Access-TopCoder-Drafts-Viewing-Page]]

**Objective**: Understand the draft management functionality and observe the deletion mechanism.

**Instructions**: Navigate to the personal drafts page using a browser or curl to inspect the interface and identify draft IDs.

**Expected Output**: List of personal drafts displayed, with visible deletion options.

**Success Indicators**:
- Drafts page loads successfully
- Draft IDs are visible in the page source or network requests

### Step 2: Test Own Draft Deletion
procedure: [[procedures/Test-Own-Draft-Deletion]]

**Objective**: Verify that the deletion endpoint functions correctly for owned drafts.

**Instructions**: Submit a deletion request using your own draft ID to confirm the mechanism works as expected.

**Expected Output**: The targeted draft is removed from your drafts list.

**Success Indicators**:
- Own draft is deleted without errors
- No authentication issues encountered

### Step 3: Exploit IDOR to Delete Foreign Draft
procedure: [[procedures/Exploit-IDOR-to-Delete-Foreign-Draft]]

**Objective**: Modify the request to target another user's draft ID, bypassing ownership checks.

**Instructions**: Intercept and alter the discardDraftId parameter in the deletion request to a foreign draft ID.

**Expected Output**: The foreign draft is deleted, confirmed by checking the target's drafts or error messages.

**Success Indicators**:
- Foreign draft no longer accessible
- No ownership error returned by the server

## Attack Chain Summary

### Key Achievements

1. Gained understanding of draft management without triggering alerts
2. Validated deletion functionality on controlled data
3. Achieved unauthorized deletion of other users' data via IDOR

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---

*Last updated: 2023-10-01T00:00:00Z*
