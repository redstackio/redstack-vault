---
tags:
  - information-disclosure
  - filename-leak
  - web-vulnerability
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
  - '[[procedures/Trigger-Error-to-Disclose-Unowned-Attachment-Filenames]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:25:12.573Z'
description: >-
  A single-step attack exploiting an information disclosure vulnerability in
  Mavenlink's mobile site, where attempting to delete unowned expense
  attachments reveals filenames in error messages, enabling unauthorized
  discovery of sensitive file information.
skill_level: beginner
impact_level: medium
id: 79ab3792-dd68-4e4d-9dc3-3ea6d9f9bc9f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
---

# Information Disclosure of Unowned Attachment Filenames via Error Message on Mavenlink Mobile Site

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Discovery]
    B --> C[Objective]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual web interaction)

### Target Environment

- Target Platform: Web (mobile site m.mavenlink.com)
- Required services/ports: HTTPS on port 443
- Network access requirements: Internet access to Mavenlink's mobile site

### Initial Access Requirements

- Credential requirements: Valid user account with access to expenses
- Network position: External
- Prior access needed: Authenticated session on m.mavenlink.com

## Detailed Attack Procedures

### Step 1: Trigger Disclosure
procedure: [[procedures/Trigger-Error-to-Disclose-Unowned-Attachment-Filenames]]

**Objective**: Attempt to delete an unowned attachment to trigger an error message that discloses the filename.

**Instructions**: Navigate to the mobile site m.mavenlink.com and log in with a valid account. Locate an expense with attachments, then attempt to delete an attachment that is not owned by your user account. The delete action will fail and display an error message containing the filename of the unowned attachment.

**Expected Output**: An error message like "Failed to delete attachment: filename.ext" revealing the target filename.

**Success Indicators**:
- Error message appears with embedded filename
- Filename of unowned attachment is visible, confirming disclosure

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of unowned attachment filenames
2. Identification of potential sensitive files without ownership
3. Medium-impact information leak via error handling flaw

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
