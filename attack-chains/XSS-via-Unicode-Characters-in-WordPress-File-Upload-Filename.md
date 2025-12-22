---
tags:
  - xss
  - wordpress
  - file-upload
  - unicode
  - privilege-escalation
type: attack_chain
tools:
  - '[[tools/TamperData]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - PHP
  - Apache
complexity: medium
procedures:
  - '[[procedures/Bypass-File-Upload-Validation]]'
  - '[[procedures/Prepare-Malicious-XSS-File]]'
  - '[[procedures/Access-WordPress-Upload-Interface]]'
  - '[[procedures/Upload-File-with-Unicode-Filename]]'
  - '[[procedures/Trigger-XSS-via-File-Visit]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-stage attack exploiting improper Unicode handling in WordPress file
  uploads to achieve reflected XSS, leading to JavaScript execution and
  potential privilege escalation when an admin views the file.
skill_level: intermediate
impact_level: high
id: 1ec06c89-414b-48ad-a13b-bb235a8a8d6c
created_at: '2025-12-13T23:56:03.293Z'
updated_at: '2025-12-13T23:56:03.293Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# XSS via Unicode Characters in WordPress File Upload Filename

Multi-stage attack chain demonstrating a complete attack workflow exploiting a WordPress vulnerability in file upload sanitization.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious File] --> B[Bypass Validation]
    B --> C[Access Upload Interface]
    C --> D[Upload with Unicode]
    D --> E[Trigger XSS on Visit]
    E --> F[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#f39c12
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/TamperData]]

### Target Environment

- WordPress CMS on PHP with Apache web server
- File upload privileges (e.g., contributor or higher role)
- No specific ports beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Valid WordPress login credentials with media upload access
- Direct network access to the WordPress admin dashboard
- No prior persistent access needed, but admin interaction required for trigger

## Detailed Attack Procedures

### Step 1: Bypass File Upload Validation
procedure: [[procedures/Bypass-File-Upload-Validation]]

**Objective**: Intercept and modify the file upload POST request to bypass client-side JavaScript validation that prevents malicious content.

**Instructions**: Install and activate [[tools/TamperData]] in Firefox. Configure it to intercept POST requests to the WordPress upload endpoint. When uploading, modify the request to allow JavaScript in the file content, removing any client-side restrictions on file type or content.

**Expected Output**: Successful request modification without triggering browser validation errors.

**Success Indicators**:
- TamperData captures and alters the POST data
- No client-side rejection of the upload attempt

### Step 2: Prepare Malicious File
procedure: [[procedures/Prepare-Malicious-XSS-File]]

**Objective**: Create a disguised image file embedding a JavaScript payload that will execute when rendered as HTML.

**Instructions**: Use a text editor or image tool to create a blank PNG file. Embed XSS payload such as `<script>alert('XSS')</script>` within the file content (e.g., in metadata or as plain text). Save as `malicious.png` with a valid image extension to pass initial checks.

**Expected Output**: A file that appears as an image but contains executable JavaScript when served as text/HTML.

**Success Indicators**:
- File opens as image in viewers but source shows script tags
- Payload verifiable by viewing file in text editor

### Step 3: Access Upload Interface
procedure: [[procedures/Access-WordPress-Upload-Interface]]

**Objective**: Navigate to the WordPress media upload section to initiate the exploit process.

**Instructions**: Log in to the WordPress admin dashboard. Go to Media > Add New. Ensure [[tools/TamperData]] is active for intercepting the upcoming upload request.

**Expected Output**: Upload interface loaded, ready for file selection.

**Success Indicators**:
- Admin dashboard accessible
- Media library upload screen visible

### Step 4: Upload with Unicode Filename
procedure: [[procedures/Upload-File-with-Unicode-Filename]]

**Objective**: Upload the malicious file with a Unicode-prepended filename to trigger server-side sanitization flaws, resulting in a numeric filename like '-1.png'.

**Instructions**: Select the prepared file in the upload interface. Use [[tools/TamperData]] to modify the filename by prepending a special Unicode character (e.g., '±myfile.png'). Submit the upload; the `sanitize_file_name` and `wp_unique_filename` functions will fail, renaming to '-1' or similar.

**Expected Output**: File uploaded to `/wp-content/uploads/year/month/-1.png`, bypassing sanitization.

**Success Indicators**:
- Upload succeeds without errors
- File appears in media library with altered name

### Step 5: Trigger XSS
procedure: [[procedures/Trigger-XSS-via-File-Visit]]

**Objective**: Visit the uploaded file's URL to force Apache to serve it as text/HTML, executing the embedded JavaScript.

**Instructions**: Construct the URL (e.g., `/wp-content/uploads/2016/10/-1`) and visit it as an administrator. The numeric filename causes misinterpretation as HTML, running the payload for alerts or escalation (e.g., iframe to create user).

**Expected Output**: JavaScript execution, such as alert popup or new user creation.

**Success Indicators**:
- Payload executes on page load
- Admin session compromised or escalated

## Attack Chain Summary

### Key Achievements

1. Bypassed client-side upload restrictions using request tampering
2. Exploited Unicode sanitization flaw for XSS payload delivery
3. Achieved JavaScript execution leading to potential account creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01*
