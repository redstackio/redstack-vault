---
tags:
  - xss
  - stored-xss
  - javascript
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Group-with-XSS-Payload]]'
  - '[[procedures/Obtain-Sharing-URL-for-Malicious-Group]]'
  - '[[procedures/Trigger-XSS-via-Sharing-Page-Visit]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.485Z'
description: >-
  A multi-step attack exploiting stored XSS in the wis.pr application by
  injecting malicious JavaScript into group names, which executes on sharing
  pages for any visitor.
skill_level: low
impact_level: high
id: d13f5980-b4cf-4f30-9e23-37d9415456a6
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS via Unsanitized Group Names in wis.pr Sharing Pages

Multi-stage attack chain demonstrating a complete stored XSS exploit in the wis.pr application, where user-controlled group names are injected into meta tags without sanitization, leading to arbitrary JavaScript execution on public sharing pages.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Low |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Group] --> B[Obtain Sharing URL]
    B --> C[Visit Sharing Page and Execute Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- wis.pr web application
- Access to group creation feature (authenticated user account)
- Public sharing pages enabled

### Initial Access Requirements

- Valid user credentials for wis.pr
- Network access to the wis.pr domain
- No prior access needed beyond registration

## Detailed Attack Procedures

### Step 1: Create Malicious Group
procedure: [[procedures/Create-Group-with-XSS-Payload]]

**Objective**: Inject a malicious JavaScript payload into a group name to store the XSS vulnerability.

**Instructions**: Log in to wis.pr, navigate to the group creation page, and enter a payload like `Test>"<script>alert('test');</script>` as the group name. Submit the form to create the group.

**Expected Output**: Group created successfully with the malicious name stored in the backend.

**Success Indicators**:
- Group appears in the user's list with the exact payload in the name
- No errors during creation

### Step 2: Obtain Sharing URL
procedure: [[procedures/Obtain-Sharing-URL-for-Malicious-Group]]

**Objective**: Generate a public sharing URL for the malicious group to enable payload delivery to victims.

**Instructions**: After creating the group, locate the sharing option (e.g., 'Share' button) and copy the generated URL, which includes the group ID (format: http://wis.pr/*****).

**Expected Output**: A shareable URL pointing to the group's public page.

**Success Indicators**:
- URL copied without errors
- URL format matches expected pattern with group ID

### Step 3: Trigger XSS Execution
procedure: [[procedures/Trigger-XSS-via-Sharing-Page-Visit]]

**Objective**: Visit the sharing URL to execute the stored JavaScript payload in the victim's browser.

**Instructions**: Open the sharing URL in a web browser. The payload from the group name will be reflected in the twitter:description meta tag, causing the script to execute.

**Expected Output**: JavaScript alert('test') pops up, confirming execution.

**Success Indicators**:
- Alert dialog appears
- Browser console shows no blocking errors (e.g., CSP violations)

## Attack Chain Summary

### Key Achievements

1. Successful storage of XSS payload in group metadata
2. Generation of a public URL that delivers the payload to any visitor
3. Arbitrary JavaScript execution, enabling session hijacking or data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
