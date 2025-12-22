---
tags:
  - xss
  - reflected-xss
  - nextcloud
  - file-upload
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-05T12:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Filename-in-Nextcloud]]'
  - '[[procedures/Trigger-Rename-Error-to-Reflect-Payload]]'
  - '[[procedures/Bypass-CSP-for-XSS-Execution]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.547Z'
description: >-
  A multi-stage attack exploiting a reflected XSS vulnerability in Nextcloud's
  file renaming feature by using a malicious filename that triggers unsanitized
  error messages.
skill_level: intermediate
impact_level: high
id: 73e7ab03-94e6-44e9-99df-b318936c757a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Reflected XSS in Nextcloud File Renaming via Malicious Filename

Multi-stage attack chain demonstrating a complete attack workflow exploiting a reflected XSS in Nextcloud's file renaming error handling.

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
    A[Create Malicious File] --> B[Trigger Rename Error]
    B --> C[Execute XSS via CSP Bypass]
    C --> D[Data Theft or Session Hijack]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools)

### Target Environment

- Nextcloud instance (web-based file sharing platform)
- Access to create and rename files in a shared folder

### Initial Access Requirements

- Authenticated user account in Nextcloud
- Ability to upload files (attacker account)
- Victim user with rename permissions on the same file
- Network access to the Nextcloud web interface

## Detailed Attack Procedures

### Step 1: Create Malicious Filename
procedure: [[procedures/Create-Malicious-Filename-in-Nextcloud]]

**Objective**: Upload a file with a filename containing a JavaScript XSS payload to set up the reflected attack vector.

**Instructions**: Log in to the Nextcloud web interface as an authenticated user. Navigate to the file upload section and create or upload a file, renaming it to include the malicious payload such as `<img src=x onerror=prompt(1)>.jpg`. Ensure the file is in a shared folder accessible by the victim.

**Expected Output**: File successfully created with the malicious name visible in the file list.

**Success Indicators**:
- File appears in the directory with the exact malicious filename
- No immediate errors during upload or rename to malicious name

### Step 2: Trigger Rename Error to Reflect Payload
procedure: [[procedures/Trigger-Rename-Error-to-Reflect-Payload]]

**Objective**: Induce an error during file rename as the victim, causing the original malicious filename to be reflected unsanitized in the error message, triggering XSS.

**Instructions**: As the victim user, attempt to rename the malicious file by entering an invalid filename, such as appending a backslash `\` (e.g., `malicious.jpg\`). Submit the rename action to generate the error.

**Expected Output**: Error message displayed in the browser, reflecting the original payload like `<img src=x onerror=prompt(1)>.jpg` without escaping, leading to potential script execution.

**Success Indicators**:
- Error popup or message shows the unsanitized filename
- Browser console logs JavaScript errors or execution attempts

### Step 3: Bypass CSP for XSS Execution
procedure: [[procedures/Bypass-CSP-for-XSS-Execution]]

**Objective**: Circumvent Nextcloud's Content Security Policy to allow the reflected JavaScript payload to execute fully, enabling actions like prompting or data exfiltration.

**Instructions**: If CSP blocks inline scripts, modify the payload to use allowed vectors (e.g., leverage existing scripts or use a different onerror handler compatible with the policy). Refresh or re-trigger the error to execute `prompt(1)` or steal session data via AJAX to an attacker-controlled server.

**Expected Output**: JavaScript alert box with `1` or successful data exfiltration to attacker's endpoint.

**Success Indicators**:
- Alert or prompt executes in the victim's browser
- Network requests sent to attacker server with stolen data (e.g., cookies)

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload via filename
2. Reflection and execution of arbitrary JavaScript in victim context
3. Potential for session hijacking or phishing despite CSP challenges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-05T12:00:00Z*
