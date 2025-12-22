---
tags:
  - dos
  - file-upload
  - resource-exhaustion
  - php
type: attack_chain
tools:
  - '[[tools/isup.me]]'
  - '[[tools/check-host.net]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Lack-of-Size-Validation-in-File-Upload-Feature]]'
  - '[[procedures/Test-Upload-Limits-with-Large-File]]'
  - '[[procedures/Confirm-Bypass-of-PHP-Upload-Limits-with-Smaller-File]]'
  - '[[procedures/Execute-DoS-Attack-with-Multiple-Simultaneous-Uploads]]'
  - '[[procedures/Verify-Site-Downtime-Using-External-Services]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T05:32:10.130Z'
description: >-
  Multi-stage attack exploiting missing file size validation in a PHP-based web
  application's user profile picture upload feature, leading to server resource
  exhaustion and temporary denial of service.
skill_level: intermediate
impact_level: high
id: 16b2e9bd-0e37-4128-93b2-bbd329cfa8a9
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# DoS via Unrestricted Large File Uploads in User Profile Picture Feature

Multi-stage attack chain demonstrating a complete workflow to exploit missing file size checks in a web application's user profile picture upload, resulting in denial of service through resource exhaustion.

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
    A[Reconnaissance: Identify Upload Feature] --> B[Testing: Attempt Large Upload]
    B --> C[Validation: Confirm Bypass]
    C --> D[Exploitation: Multiple Uploads for DoS]
    D --> E[Verification: Check Downtime]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/isup.me]]
- [[tools/check-host.net]]
- Web browser (multiple instances)

### Target Environment

- PHP-based web application with file upload functionality
- Access to user profile edit page (e.g., /user/{id}/edit)
- No authentication bypass required if logged in as user

### Initial Access Requirements

- Valid user account to access profile edit
- Network access to the staging/production server
- No prior elevated access needed

## Detailed Attack Procedures

### Step 1: Identify Lack of Size Validation in File Upload Feature
procedure: [[procedures/Identify-Lack-of-Size-Validation-in-File-Upload-Feature]]

**Objective**: Discover the file upload feature and observe absence of size restrictions.

**Instructions**: Navigate to the user profile edit page, such as https://staging.uzbey.com/user/406/edit, and inspect the 'upload picture' option for any client-side size warnings or limits.

**Expected Output**: Upload interface without size indicators or validation messages.

**Success Indicators**:
- No size warnings displayed
- Upload form allows file selection without restrictions

### Step 2: Test Upload Limits with Large File
procedure: [[procedures/Test-Upload-Limits-with-Large-File]]

**Objective**: Attempt to upload an excessively large file to probe server response.

**Instructions**: Select and upload a 2.52 GB .7z file via the web interface on the profile edit page. Monitor for error messages or upload progress.

**Expected Output**: Upload proceeds without 413 error or size warning, leading to page load failure and connection slowdown.

**Success Indicators**:
- File upload initiates without rejection
- Server experiences slowdown or timeout

### Step 3: Confirm Bypass of PHP Upload Limits with Smaller File
procedure: [[procedures/Confirm-Bypass-of-PHP-Upload-Limits-with-Smaller-File]]

**Objective**: Verify that PHP configuration limits are not enforced using a moderately sized file.

**Instructions**: Upload an 8.20 MB JPEG image through the same interface and check for enforcement of php.ini settings like upload_max_filesize=2M.

**Expected Output**: Upload succeeds without errors, confirming bypass of PHP limits.

**Success Indicators**:
- No error messages for file exceeding 2M limit
- File processes successfully

### Step 4: Execute DoS Attack with Multiple Simultaneous Uploads
procedure: [[procedures/Execute-DoS-Attack-with-Multiple-Simultaneous-Uploads]]

**Objective**: Overload server resources by initiating multiple large file uploads concurrently.

**Instructions**: Open 6 browser instances to the upload page and simultaneously start uploading 2.52 GB files in each. Monitor server responsiveness.

**Expected Output**: Site becomes unresponsive after a few minutes due to resource exhaustion.

**Success Indicators**:
- Server slowdown and connection issues
- Site offline for several minutes

### Step 5: Verify Site Downtime Using External Services
procedure: [[procedures/Verify-Site-Downtime-Using-External-Services]]

**Objective**: Confirm the DoS impact using third-party uptime checkers.

**Instructions**: During the attack, query [[tools/isup.me]] and [[tools/check-host.net]] with the target URL (e.g., https://staging.uzbey.com) to validate downtime.

**Expected Output**: Services report the site as down or unreachable.

**Success Indicators**:
- External checkers indicate downtime
- Connectivity failures confirmed

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable upload feature without size checks
2. Demonstrated bypass of PHP upload limits
3. Achieved temporary DoS rendering the site offline
4. Verified impact with external monitoring

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
