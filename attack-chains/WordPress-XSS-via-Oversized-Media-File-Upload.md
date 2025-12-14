---
tags:
  - xss
  - wordpress
  - media-upload
  - file-upload
  - javascript-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-WordPress-Media-Upload-XSS]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.361Z'
description: >-
  A multi-stage attack exploiting cross-site scripting vulnerabilities in
  WordPress 4.7.2 media upload error handling for oversized files, leading to
  arbitrary JavaScript execution in the admin panel.
id: 82395162-eda8-4d00-894d-7562cf803730
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# WordPress XSS via Oversized Media File Upload

Multi-stage attack chain demonstrating exploitation of XSS in WordPress 4.7.2 during media file uploads exceeding size limits, allowing arbitrary JavaScript execution in the administrator's context.

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
    A[Prepare Malicious File] --> B[Access Upload Interface]
    B --> C[Attempt Oversized Upload]
    C --> D[Trigger and Execute XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools for inspection)

### Target Environment

- WordPress 4.7.2 installation
- Authenticated administrator access
- Web platform with PHP backend

### Initial Access Requirements

- Valid admin credentials for the WordPress site
- Direct network access to the target WordPress instance (e.g., http://target.com/wp-admin)
- No prior compromise needed, but admin privileges required to access media upload

## Detailed Attack Procedures

### Step 1: Prepare Malicious Oversized File
procedure: [[procedures/Trigger-WordPress-Media-Upload-XSS]]

**Objective**: Create a large file with an embedded XSS payload in the filename to bypass sanitization during error message rendering.

**Instructions**: Generate a file larger than the upload limit (e.g., 20MB) using any text editor or script, naming it with a malicious payload like 'Dinosaurs secret life<img src=x onerror=alert(1)>.png'. Fill the file with dummy data to exceed size limits.

**Expected Output**: A 20MB+ file ready for upload, with the filename containing the unescaped JavaScript payload.

**Success Indicators**:
- File created successfully and exceeds server upload size limit (default 2MB in WordPress)
- Filename includes payload verifiable by opening in a text editor

### Step 2: Access WordPress Media Upload Interface
procedure: [[procedures/Trigger-WordPress-Media-Upload-XSS]]

**Objective**: Navigate to the admin media upload page to prepare for file submission.

**Instructions**: Log in as an administrator and visit the media upload interface at http://target.com/wp-admin/media-new.php. Ensure the Plupload interface is loaded, which handles uploads via JavaScript.

**Expected Output**: The media library upload page loads, showing drag-and-drop or 'Select Files' options.

**Success Indicators**:
- Page loads without errors
- Admin authentication confirmed via session

### Step 3: Attempt to Upload the Oversized File
procedure: [[procedures/Trigger-WordPress-Media-Upload-XSS]]

**Objective**: Submit the malicious file to trigger size limit errors that interpolate the filename unsafely.

**Instructions**: Use the 'Select Files' button, drag-and-drop, or file manager to attempt uploading the prepared oversized file. The upload will fail due to size constraints, invoking error handlers in script-loader.php and handlers.min.js.

**Expected Output**: Upload failure with error messages displayed, such as those from pluploadL10n.file_exceeds_size_limit or big_upload_failed.

**Success Indicators**:
- Error message appears in the interface
- No successful upload occurs, but DOM updates with filename

### Step 4: Observe XSS Execution
procedure: [[procedures/Trigger-WordPress-Media-Upload-XSS]]

**Objective**: Confirm arbitrary JavaScript execution in the admin context from the unsafe error rendering two XSS vectors.

**Instructions**: Monitor the page for the alert(1) popup or inspect the DOM where jQuery('#media-items').append() inserts the error HTML. The payload executes due to unescaped filename in replace operations.

**Expected Output**: JavaScript alert or console execution, demonstrating code injection; inspect network/dev tools for confirmation.

**Success Indicators**:
- Alert box pops up or custom JS runs
- DOM inspection shows injected <img> tag with onerror handler

## Attack Chain Summary

### Key Achievements

1. Successful creation and preparation of a malicious oversized file with XSS payload in filename
2. Triggering of upload errors that expose two XSS vectors in WordPress admin interface
3. Achievement of arbitrary JavaScript execution, enabling potential session hijacking or further admin compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2024-10-01T00:00:00Z*
