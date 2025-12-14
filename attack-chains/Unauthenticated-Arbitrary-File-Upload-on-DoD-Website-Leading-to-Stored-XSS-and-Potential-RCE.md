---
id: ac-unauth-file-upload-dod
tags:
  - arbitrary-file-upload
  - unauthenticated
  - xss
  - rce
  - php
  - web
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-and-Access-Upload-Endpoint]]'
  - '[[procedures/Exploit-Unauthenticated-File-Upload]]'
  - '[[procedures/Retrieve-and-Verify-Uploaded-File]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.336Z'
description: >-
  Exploits an unauthenticated file upload vulnerability on a U.S. Department of
  Defense website to upload arbitrary files, enabling stored XSS, hosting
  malicious content, and potential server-side code execution via public access
  to uploaded files.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthenticated Arbitrary File Upload on DoD Website Leading to Stored XSS and Potential RCE

Multi-stage attack chain demonstrating exploitation of an unauthenticated arbitrary file upload vulnerability on a U.S. Department of Defense website. The attack allows attackers to upload malicious files without authentication, store them in a publicly accessible directory, and retrieve them, enabling stored cross-site scripting (XSS), hosting of attacker-controlled content, and potential remote code execution (RCE) if executable files like PHP shells are uploaded.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Upload Endpoint] --> B[Upload Arbitrary File]
    B --> C[Retrieve Uploaded File]
    C --> D[Exploit for XSS or RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome)
- Optional: [[tools/curl]] for automated testing

### Target Environment

- Web platform with PHP backend
- Publicly accessible upload endpoint (e.g., /upload.php)
- No authentication required

### Initial Access Requirements

- Internet access to the target domain (e.g., *.mil domain)
- No credentials needed due to unauthenticated nature
- Basic knowledge of HTTP requests and file uploads

## Detailed Attack Procedures

### Step 1: Discover and Access Upload Endpoint
procedure: [[procedures/Discover-and-Access-Upload-Endpoint]]

**Objective**: Identify and navigate to the vulnerable upload endpoint to confirm its existence and lack of authentication.

**Instructions**: Open a web browser and directly access the suspected upload endpoint URL, such as https://██████/upload.php. Observe if the page loads without prompting for login, indicating no authentication is required.

**Expected Output**: The upload form or page loads successfully, allowing file selection without credentials.

**Success Indicators**:
- Page accessible without login
- Upload interface visible

### Step 2: Exploit Unauthenticated File Upload
procedure: [[procedures/Exploit-Unauthenticated-File-Upload]]

**Objective**: Upload an arbitrary test file to the endpoint, leveraging the lack of validation to store it on the server and observe any path leakage in the response.

**Instructions**: On the /upload.php form, select and submit a benign test file (e.g., a simple text or image file named 'delete.me'). Monitor the response for success messages that may leak internal server paths, confirming the file is stored publicly.

**Expected Output**: Success message like "File uploaded successfully to /path/to/delete.me", revealing the predictable storage location.

**Success Indicators**:
- File upload succeeds without errors
- Internal path information leaked in response

### Step 3: Retrieve and Verify Uploaded File
procedure: [[procedures/Retrieve-and-Verify-Uploaded-File]]

**Objective**: Access the uploaded file via its predictable public path to confirm storage and retrieval, demonstrating potential for malicious exploitation.

**Instructions**: Navigate to the leaked or predictable path, such as https://██████████/delete.me, to view or download the uploaded file. Verify the content matches the original upload.

**Expected Output**: The uploaded file is displayed or downloadable directly in the browser.

**Success Indicators**:
- File accessible publicly
- Content verifiable as attacker-controlled

## Attack Chain Summary

### Key Achievements

1. Confirmed unauthenticated access to upload functionality on a sensitive DoD website.
2. Successfully uploaded and stored arbitrary files in a public directory.
3. Demonstrated retrieval of files, paving the way for stored XSS via HTML/JS uploads or RCE via PHP shells.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
