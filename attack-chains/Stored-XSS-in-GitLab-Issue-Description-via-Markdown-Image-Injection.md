---
tags:
  - xss
  - stored-xss
  - gitlab
  - markdown-injection
  - javascript-execution
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-and-Create-GitLab-Project]]'
  - '[[procedures/Create-Malicious-Issue-with-XSS-Payload]]'
  - '[[procedures/Trigger-Stored-XSS-by-Viewing-Issue]]'
  - '[[procedures/Exploit-XSS-via-Issue-Editing]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.323Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in GitLab's issue
  description field using Markdown image syntax to inject malicious JavaScript
  attributes, leading to arbitrary code execution in viewers' browsers.
skill_level: intermediate
impact_level: high
id: 3e261fc6-427a-4b11-9ebb-64b76e477236
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in GitLab Issue Description via Markdown Image Injection

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in GitLab's issue details page. An attacker injects a malicious payload into the issue description using Markdown image syntax, which evades sanitization and executes JavaScript when any user views the issue, potentially leading to session hijacking, data theft, or phishing attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticate and Create Project] --> B[Create Malicious Issue]
    B --> C[View Issue to Trigger XSS]
    C --> D[Optional: Edit for Persistence]
    D --> E[Execute Arbitrary JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Chrome]]

### Target Environment

- GitLab instance (self-hosted or SaaS)
- Web browser with JavaScript enabled
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid user credentials for GitLab (attacker must be authenticated)
- Network access to the GitLab web interface
- No prior elevated access needed, but project creation permissions required

## Detailed Attack Procedures

### Step 1: Authenticate and Create Project
procedure: [[procedures/Authenticate-and-Create-GitLab-Project]]

**Objective**: Gain access to GitLab and set up a project to host the vulnerable issue.

**Instructions**: Sign in using valid credentials, navigate to create a new public project named 'PoC' via the UI.

**Expected Output**: A new public project is created and accessible.

**Success Indicators**:
- Successful login to GitLab dashboard
- Project 'PoC' listed in user's projects

### Step 2: Create Malicious Issue
procedure: [[procedures/Create-Malicious-Issue-with-XSS-Payload]]

**Objective**: Inject the XSS payload into a new issue's description field using Markdown syntax.

**Instructions**: Navigate to the Issues section, create a new issue titled 'PoC' with the payload `![xss\" onload=alert(1);//](a)` in the description, then submit.

**Expected Output**: Issue is saved without errors, payload stored in description.

**Success Indicators**:
- Issue appears in the project’s issue list
- Description field contains the injected Markdown

### Step 3: Trigger Stored XSS
procedure: [[procedures/Trigger-Stored-XSS-by-Viewing-Issue]]

**Objective**: View the issue details page to execute the stored JavaScript payload.

**Instructions**: Open the created issue's details page in Firefox or Chrome; the onload attribute in the rendered image tag triggers the alert.

**Expected Output**: JavaScript alert(1) pops up in the browser.

**Success Indicators**:
- Alert dialog appears confirming XSS execution
- No errors in browser console related to sanitization

### Step 4: Exploit via Editing
procedure: [[procedures/Exploit-XSS-via-Issue-Editing]]

**Objective**: Demonstrate persistence by editing an existing issue to inject the payload.

**Instructions**: Edit any existing issue, add the same payload to the description, save, and view to trigger.

**Expected Output**: Updated issue renders the payload and executes JavaScript on view.

**Success Indicators**:
- Edit saves successfully
- XSS triggers on subsequent views by any user

## Attack Chain Summary

### Key Achievements

1. Successful injection of stored XSS payload via Markdown image attributes in GitLab issues
2. Arbitrary JavaScript execution in victims' browsers upon viewing affected issues
3. Reproduction across issue creation and editing workflows
4. Potential for session hijacking or data exfiltration in multi-user environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
