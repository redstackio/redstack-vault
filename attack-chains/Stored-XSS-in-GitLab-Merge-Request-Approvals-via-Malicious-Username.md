---
tags:
  - xss
  - stored-xss
  - gitlab
  - javascript-execution
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-GitLab-Project-Settings]]'
  - '[[procedures/Insert-Malicious-XSS-Username]]'
  - '[[procedures/Trigger-XSS-via-Selection]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:37.838Z'
description: >-
  A stored XSS attack exploiting insufficient username sanitization in GitLab's
  merge request approval feature, allowing arbitrary JavaScript execution when
  selecting the malicious username.
skill_level: intermediate
impact_level: high
id: e8b0b92a-d1b1-43bb-8b68-119550646ef9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS in GitLab Merge Request Approvals via Malicious Username

Multi-stage attack chain demonstrating a complete stored XSS workflow in GitLab's merge request approval feature.

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
    A[Access Project Settings] --> B[Insert Malicious Username]
    B --> C[Trigger XSS Execution]
    C --> D[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser interaction)

### Target Environment

- GitLab EE instance (web-based)
- Access to project settings with merge request approval configuration
- No specific services/ports beyond standard HTTPS (443)
- Network access to the GitLab web interface

### Initial Access Requirements

- Valid GitLab account with permissions to modify usernames and access project settings
- Ability to set a username containing JavaScript payload
- Victim access to the project settings page

## Detailed Attack Procedures

### Step 1: Access Project Settings
procedure: [[procedures/Access-GitLab-Project-Settings]]

**Objective**: Navigate to the merge request approval configuration to prepare for payload insertion.

**Instructions**: Log in to the GitLab instance and open the target project's settings page. Locate the merge request approvals section.

**Expected Output**: Project settings interface loaded, with approval fields visible.

**Success Indicators**:
- Settings page accessible
- Merge request approval configuration displayed

### Step 2: Insert Malicious XSS Username
procedure: [[procedures/Insert-Malicious-XSS-Username]]

**Objective**: Set a username with an embedded XSS payload that will be stored and rendered unsanitized.

**Instructions**: Create or edit a user account with a username containing a JavaScript payload, such as `<script>alert('XSS')</script>`. Then, in the approval requester field, paste or select this username.

**Expected Output**: Username saved and visible in the approval field dropdown.

**Success Indicators**:
- Malicious username stored without sanitization
- Payload appears in the interface as entered

### Step 3: Trigger XSS via Selection
procedure: [[procedures/Trigger-XSS-via-Selection]]

**Objective**: Interact with the malicious username to execute the stored JavaScript in the victim's browser context.

**Instructions**: In the project settings approval field, click on or select the dropdown result containing the malicious username, triggering the payload execution.

**Expected Output**: JavaScript alert or arbitrary code runs in the browser.

**Success Indicators**:
- Script executes (e.g., alert pops up)
- Potential for session hijacking or data theft confirmed

## Attack Chain Summary

### Key Achievements

1. Successful storage of XSS payload in username
2. Execution of arbitrary JavaScript upon selection
3. Demonstration of high-impact risks like session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
