---
tags:
  - unrestricted-upload
  - xss
  - rce
  - file-upload
  - php-shell
  - stored-xss
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-and-Complete-Request-Form]]'
  - '[[procedures/Upload-Malicious-HTML-File]]'
  - '[[procedures/Submit-Request-and-Retrieve-Document-ID]]'
  - '[[procedures/Access-Uploaded-File-to-Trigger-Payload]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:32.414Z'
description: >-
  A multi-stage attack exploiting an unrestricted file upload in a web
  application's request form to upload HTML files containing malicious
  JavaScript and PHP code, resulting in stored XSS for session hijacking and
  potential remote code execution via a PHP shell.
skill_level: intermediate
impact_level: high
id: 2e28a325-0b3b-4d20-9857-a9ba6aa39ee5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
  - '[[Command-Line Interface]]'
---
# Unrestricted File Upload Leading to Stored XSS and Potential RCE

Multi-stage attack chain demonstrating exploitation of an unrestricted file upload vulnerability in a DoD web application to achieve stored XSS and potential RCE.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Request Form] --> B[Upload Malicious File]
    B --> C[Submit and Retrieve Document]
    C --> D[Access File and Trigger Payload]
    D --> E[Execute XSS and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome with developer tools)
- Text editor to craft the malicious HTML payload

### Target Environment

- Web application running on PHP
- Access to the /request?openform endpoint
- Authenticated user session (if required by the application)

### Initial Access Requirements

- Valid network access to the target web server
- No special credentials beyond basic user access to the request form
- Prior reconnaissance to identify the upload feature

## Detailed Attack Procedures

### Step 1: Access and Complete Request Form
procedure: [[procedures/Access-and-Complete-Request-Form]]

**Objective**: Initiate the file upload process by navigating to the request form and filling in required details to reach the upload stage.

**Instructions**: Open a web browser and navigate to the target application's request form endpoint at `https://target.com/request?openform`. Fill in the necessary fields on the initial form, such as requester name, email, and description. Submit the form to proceed to the next page, where additional details like request type and attachments are entered.

**Expected Output**: Redirection to the attachment upload page with fields for file selection.

**Success Indicators**:
- Form loads successfully without errors
- User is able to proceed to the file upload section

### Step 2: Upload Malicious HTML File
procedure: [[procedures/Upload-Malicious-HTML-File]]

**Objective**: Select and upload an HTML file containing malicious JavaScript for XSS and embedded PHP code for a shell.

**Instructions**: On the upload page, click the 'browse' button to select a pre-crafted HTML file (e.g., `unsure1.html`) that includes a script tag with XSS payload like `<script>alert('XSS');</script>` and PHP code like `<?php system($_GET['cmd']); ?>`. Ensure the file is named innocuously to avoid suspicion. The upload occurs without type validation.

**Expected Output**: File selection dialog opens, and the file is queued for upload.

**Success Indicators**:
- File is selected without rejection
- No error messages about file type or content

### Step 3: Submit Request and Retrieve Document ID
procedure: [[procedures/Submit-Request-and-Retrieve-Document-ID]]

**Objective**: Submit the form to store the uploaded file and obtain the 14-digit Document Number for later access.

**Instructions**: Click 'submit request' to process the upload. After submission, navigate to the `ModifyRequest.xsp` page and enter the generated 14-digit Document Number (visible in the confirmation or URL) to view the request details.

**Expected Output**: Request submitted successfully, and the modification page loads with the document details.

**Success Indicators**:
- Confirmation message or redirect after submission
- Document Number is obtainable and valid for access

### Step 4: Access Uploaded File to Trigger Payload
procedure: [[procedures/Access-Uploaded-File-to-Trigger-Payload]]

**Objective**: View the uploaded file to execute the XSS and access the PHP shell for RCE.

**Instructions**: On the request modification page, scroll to the bottom where attachments are listed. Click on the uploaded HTML file (e.g., `unsure1.html`). The browser will render the file, triggering the JavaScript for stored XSS. For RCE, construct a direct URL like `https://target.com/{DocumentID}/$FILE/unsure1.html?cmd=whoami` to execute PHP commands via the shell.

**Expected Output**: Alert or XSS effects visible in the browser; command output (e.g., server username) displayed for RCE.

**Success Indicators**:
- JavaScript executes, showing XSS payload effects
- PHP shell responds to commands, indicating RCE capability

## Attack Chain Summary

### Key Achievements

1. Successful upload of malicious HTML without file type restrictions
2. Stored XSS execution leading to potential session hijacking
3. Potential RCE via embedded PHP shell for arbitrary command execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
